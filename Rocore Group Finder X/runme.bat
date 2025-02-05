@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Running Rocore Group Finder X...
python finder.py

pause
