import os, platform, sys

colors = True
os_name = platform.platform()

if os_name.lower().startswith(("win", "darwin", "ios")):
	colors = False
if os_name.startswith("Windows-10") and int(platform.version().split(".")[2]) > 10586:
	colors = True 
	os.system('')

if not colors:
	pink = reset = ''
else:
	pink = "\033[38;5;205m"
	reset = "\033[0m"
