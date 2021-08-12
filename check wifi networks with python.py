# import module
import subprocess

# "devices" is a variable.
# Store data in it.
devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
# decode ascii
devices = devices.decode('ascii')
# replace it
devices = devices.replace('\r', "")
# Now print "devices" for the output.
print(devices)

# Programmer / Developer - Mohit Pandey.
# GitHub - @mohit377

# YouTube Channel link - https://youtube.com/c/mohitpandey10
# GitHub Profile Link - https://github.com/mohit377

# Press "ctrl" and click on the link to open it.

# Thanks!!!