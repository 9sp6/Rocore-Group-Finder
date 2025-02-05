import os
import threading
import requests
import random
import json
import time
from dhooks import Webhook
import ctypes

# Load configuration
with open("configuration.json", "r") as config_file:
    config = json.load(config_file)

enable_webhook = config["enable_webhook"]
webhook_url = config["webhook_url"]
threads = config["threads"]
group_id_range = config["group_id_range"]
retry_delay = config["retry_delay"]
log_hits = config["log_hits"]

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

set_console_title("Rocore Group Finder X")

# Webhook setup
hook = Webhook(webhook_url) if enable_webhook else None

def log_message(message):
    print(message)
    if log_hits:
        with open("hits.log", "a") as log_file:
            log_file.write(message + "\n")

def groupfinder():
    while True:
        try:
            group_id = random.randint(group_id_range[0], group_id_range[1])
            response = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={group_id}", timeout=30)
            
            if 'owned' not in response.text:
                api_response = requests.get(f"https://groups.roblox.com/v1/groups/{group_id}", timeout=30)
                if api_response.status_code != 429:
                    group_data = api_response.json()
                    if 'errors' not in group_data:
                        if 'isLocked' not in api_response.text and 'owner' in api_response.text:
                            if group_data['publicEntryAllowed'] and group_data['owner'] is None:
                                message = f'[✔] Hit: https://www.roblox.com/groups/group.aspx?gid={group_id} '
                                log_message(message)
                                if enable_webhook:
                                    hook.send(message)
                            else:
                                log_message(f"[-] No Entry Is Allowed: {group_id}")
                        else:
                            log_message(f"[-] Group Is Locked: {group_id}")
                else:
                    log_message("[!] You've been Rate Limited, Retrying...")
                    time.sleep(retry_delay)
            else:
                log_message(f"[-] Group Is Already Owned: {group_id}")
        except Exception as e:
            log_message(f"[!] Error: {str(e)}")

print("""

            ───────────────────────────────────────────────────────────────────────────────────────────────────
            ─████████████████───██████████████─██████████████─██████████████─████████████████───██████████████─
            ─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
            ─██░░████████░░██───██░░██████░░██─██░░██████████─██░░██████░░██─██░░████████░░██───██░░██████████─
            ─██░░██────██░░██───██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░██────██░░██───██░░██─────────
            ─██░░████████░░██───██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░████████░░██───██░░██████████─
            ─██░░░░░░░░░░░░██───██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
            ─██░░██████░░████───██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░██████░░████───██░░██████████─
            ─██░░██──██░░██─────██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░██──██░░██─────██░░██─────────
            ─██░░██──██░░██████─██░░██████░░██─██░░██████████─██░░██████░░██─██░░██──██░░██████─██░░██████████─
            ─█░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██─
            ─██████──██████████─██████████████─██████████████─██████████████─██████──██████████─██████████████─
            ───────────────────────────────────────────────────────────────────────────────────────────────────
                                                                 
""")

def start_threads():
    while threading.active_count() <= threads:
        threading.Thread(target=groupfinder).start()

if __name__ == "__main__":
    start_threads()
