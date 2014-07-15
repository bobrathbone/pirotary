#!/usr/bin/env python
#
# Raspberry Pi Rotary Test Encoder Class
#
# Author : Bob Rathbone
# Site   : http://www.bobrathbone.com
#
# This class uses a standard rotary encoder with push switch
#

import sys
import time
from rotary_class import RotaryEncoder

# Define GPIO inputs
PIN_A = 14 	# Pin 8 
PIN_B = 15	# Pin 10
BUTTON = 4	# Pin 7

# This is the event callback routine to handle events
def switch_event(event):
	if event == RotaryEncoder.CLOCKWISE:
		print "Clockwise"
	elif event == RotaryEncoder.ANTICLOCKWISE:
		print "Anticlockwise"
	elif event == RotaryEncoder.BUTTONDOWN:
		print "Button down"
	elif event == RotaryEncoder.BUTTONUP:
		print "Button up"
	return

# Define the switch
rswitch = RotaryEncoder(PIN_A,PIN_B,BUTTON,switch_event)

while True:
	time.sleep(0.5)


