import subprocess
import sys

def abrir_chrome(url="https://www.google.com"):
    if sys.platform == "win32":
        caminho = r"C:\\Program Files\\Google\\Chrome\Application\\chrome.exe"
    elif sys.platform == "darwin":  # macOS
        caminho = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    else:  # Linux
        caminho = "google-chrome"

    subprocess.Popen([caminho, url])


