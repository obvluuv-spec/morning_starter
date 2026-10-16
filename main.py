import os 
import subprocess
import time
import webbrowser

browser_path = r"" # here comes the path
webbrowser.register("mybrowser", None, webbrowser.BackgroundBrowser(browser_path))

app = []
websites = []

with open("application.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if line.startswith("app:"):
             pfad = line[len("app:"):].strip().strip('"')
             app.append(pfad)
             
             
             
             
             
        elif line.startswith("website:"):
            url = line[len("website:"):].strip().strip('"')
            websites.append(url)

for url in websites:
    if not url.startswith(("https://", "http://")):
        url = "https://" + url
    webbrowser.get("mybrowser").open(url)
    time.sleep(3)

for app_path in app:
    if os.path.exists(app_path):
        subprocess.Popen(app_path)
        time.sleep(10)
    else:
        continue