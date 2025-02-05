# Rocore Group Finder X

**Rocore Group Finder X** is an advanced, multithreaded **Roblox group finder** that scans for **unowned, joinable groups** using optimized API calls. It includes webhook support, logging, and full configuration through `configuration.json`.

## Features 🚀
- 🔥 **Fully Configurable** via `configuration.json`
- ⚡ **Multithreaded Scanning** for fast results
- 📡 **Discord Webhook Integration** (toggle on/off)
- 📜 **Hit Logging** (logs found groups to a file)
- 🛡️ **Auto-retries on rate limits**
- 🏹 **Customizable Group ID Range**

---
## Installation 📥
### **1. Clone the Repository**
```sh
git clone https://github.com/9sp6/Rocore-Group-Finder.git
cd Rocore-Group-Finder
```

### **2. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3. Configure `config.json`**
Edit `configuration.json` to customize settings:
```json
{
    "enable_webhook": true,
    "webhook_url": "YOUR_DISCORD_WEBHOOK_URL",
    "threads": 10,
    "group_id_range": [1000000, 1150000],
    "retry_delay": 5,
    "log_hits": true
}
```

### **4. Run the Finder**
Run using the batch file:
```sh
runme.bat
```
Or manually:
```sh
python rocore_group_finder.py
```

---
## Usage ⚙️
- **Finds unclaimed Roblox groups** in the specified range.
- **Sends hits to Discord webhook** (if enabled).
- **Saves found groups to `hits.log`**.

---
## Notes 📝
- Higher thread count = Faster scans but **higher rate limit risks**.
- Ensure `configuration.json` is properly set up before running.
- Use a **VPN or proxy** to avoid IP bans if scanning aggressively.

---
## License 📜
This project is for **educational purposes only**. Use responsibly.

---
### Created by **Spooky** 👻

