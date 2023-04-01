import sys, os, platform, socket, psutil, time, ctypes, subprocess, GPUtil
information = []
if sys.platform == "win32": information.append("Windows 10")
elif sys.platform == "linux": information.append("Linux")
elif sys.platform == "darwin": information.append("Mac OS X")
information.append(sys.version)
string = "\n".join(information)
user = os.getlogin()
os.system("")
lines = []
for i in range(len(user) + len(socket.gethostname()) + 1):
    lines.append("-")
bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"
secs = time.time() - psutil.boot_time()
temp = secs
days = secs // 86400
secs %= 86400
hours = secs // 3600
secs %= 3600
mins = secs // 60
secs %= 60

days = str(days).split(".")[0]
hours = str(hours).split(".")[0]
mins = str(mins).split(".")[0]
secs = str(secs).split(".")[0]
days = int(days)
hours = int(hours)
mins = int(mins)
secs = int(secs)

dhms = ""
if days > 0:
    if days != 1:
        dhms = f"{days} Days"
    else:
        dhms = f"{days} Day"
if hours > 0:
    if hours != 1:
        dhms = f"{dhms} {hours} Hours"
    else:
        dhms = f"{dhms} {hours} Hour"
if mins > 0:
    if mins != 1:
        dhms = f"{dhms} {mins} Minutes"
    else:
        dhms = f"{dhms} {mins} Minute"
if secs > 0:
    if secs != 1:
        dhms = f"{dhms} {secs} Seconds"
    else:
        dhms = f"{dhms} {secs} Second"
screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
res = str(screensize).replace("(", "").replace(")", "").replace(", ", "x")
colors = []
for i in range(8):
    colors.append(bg("   ", i))
colors2 = []
for i in range(8):
    colors2.append(bg("   ", i+8))
colors2 = "".join(colors2)
colors = "".join(colors)
disk = psutil.disk_usage("C:")
total = round(disk.total/1000000000)
used = round(disk.used/1000000000)
perc = disk.percent
mem = psutil.virtual_memory()
mem = mem.percent
n = subprocess.check_output(["wmic", "path", "win32_VideoController", "get", "name"]).decode()
n = n.replace("Name                       ", "")
n = n.replace("\n", "")
n = n.replace("\r", "")
GPUs = GPUtil.getGPUs()
uuid = GPUs[0].uuid
###################################
ver = "1.0.0"
logo = [
f'\x1b[94m                     ....,,:;+ccllll \x1b[93m{user}@{socket.gethostname()}\n',
f'       ...,,+:;  cllllllllllllllllll \x1b[37m{"".join(lines)}\n',
f' ,cclllllllllll  lllllllllllllllllll \x1b[93mOS\x1b[37m: {platform.platform()} ({sys.platform}) \n',
f' llllllllllllll  lllllllllllllllllll \x1b[93mHost\x1b[37m: {socket.gethostname()}\n',
f' llllllllllllll  lllllllllllllllllll \x1b[93mProcessor\x1b[37m: {platform.uname().processor}\n',
f' llllllllllllll  lllllllllllllllllll \x1b[93mWFETCH Version\x1b[37m: {ver}\n',
f' llllllllllllll  lllllllllllllllllll \x1b[93mUptime\x1b[37m:{dhms}\n',
f' llllllllllllll  lllllllllllllllllll \x1b[93mGPU\x1b[37m: {n}\n',
f'\n',
f' llllllllllllll  lllllllllllllllllll \x1b[93mGPU UUID\x1b[37m: {uuid}\n',
f' llllllllllllll  lllllllllllllllllll \x1b[93mResolution\x1b[37m: {res}\n',
f' llllllllllllll  lllllllllllllllllll \x1b[93mCPU Cores\x1b[37m: {psutil.cpu_count()}\n',
f' llllllllllllll  lllllllllllllllllll \x1b[93mCPU Usage\x1b[37m: {psutil.cpu_percent()}%\n',
f' llllllllllllll  lllllllllllllllllll \x1b[93mMemory Usage\x1b[37m: {mem}%\n',
f" `'ccllllllllll  lllllllllllllllllll \x1b[93mDisk (C:)\x1b[37m: {used} GB / {total} GB ({perc}%)\n",
"       `' \\\\*::  :ccllllllllllllllll \n",
f"                        ````''*::cll {colors}\n",
f'                                  `` {colors2}']
print("\x1b[94m".join(logo))
print("\x1b[0m")
