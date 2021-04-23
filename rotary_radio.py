#!/usr/bin/env python
# $Id: rotary_radio.py,v 1.3 2021/04/23 08:31:35 bob Exp $
# Simple radio using four buttons

import os
import atexit
from time import sleep
from rotary_class import RotaryEncoder

# Register exit routine
def finish():
	exec_command("service mpd stop")
        print("Radio stopped")

atexit.register(finish)

# Switch definitions
VOLUME_UP = 8
VOLUME_DOWN = 10
CHANNEL_UP = 15
CHANNEL_DOWN = 16
MENU = 7

# Amend  playlist to point to a valid playlist in /var/lib/mpd/playlist 
# without the .m3u ot .pls extension
playlist = "_Radio"

# Execute system command sub-routine
def exec_command(cmd):
	result = ""
	p = os.popen(cmd)
	for line in p.readline().split('\n'):
		result = result + line
	return result

# This is the event callback routine to handle events
def callback(event):
        if event == RotaryEncoder.CLOCKWISE:
		exec_command("mpc volume +5")
        elif event == RotaryEncoder.ANTICLOCKWISE:
		exec_command("mpc volume -5")
        elif event == RotaryEncoder.BUTTONDOWN:
		exec_command("mpc next")
		if len(exec_command("mpc current")) < 1:
			exec_command("mpc play 1")
        elif event == RotaryEncoder.BUTTONUP:
		print exec_command("mpc current")
        return


### Main routine ###
if __name__ == "__main__":
	exec_command("service mpd start")
	exec_command("mpc clear")
	exec_command("mpc load " + playlist) # Amend to load a valid playlist into MPD
	exec_command("mpc play")
	exec_command("mpc volume 70")
	print exec_command("mpc current")
	vol_switch = RotaryEncoder(VOLUME_DOWN,VOLUME_UP,MENU,callback)

	while True:
		sleep(0.2)

# End of radio


