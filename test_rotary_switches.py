#!/usr/bin/env python
#
# Raspberry Pi Rotary Test Encoder Class
# $Id: test_rotary_switches.py,v 1.4 2014/01/31 14:06:26 bob Exp $
#
# Author : Bob Rathbone
# Site   : http://www.bobrathbone.com
#
# This class uses standard rotary encoder with push switch
#

import sys
import time
from rotary_class import RotaryEncoder

# Switch definitions
RIGHT_BUTTON = 25
LEFT_A = 14
LEFT_B = 15
RIGHT_A = 17
RIGHT_B = 18
LEFT_BUTTON = 4 


# This is the event callback routine to handle left knob events
def left_knob_event(event):
	handle_event(event,"Left knob")	
	return

# This is the event callback routine to handle right knob events
def right_knob_event(event):
	handle_event(event,"Right knob")	
	return

# This is the event callback routine to handle events
def handle_event(event, name):
	if event == RotaryEncoder.CLOCKWISE:
		print name, "Clockwise event =", RotaryEncoder.CLOCKWISE
	elif event == RotaryEncoder.ANTICLOCKWISE:
		print name, "Anticlockwise event =", RotaryEncoder.BUTTONDOWN
	elif event == RotaryEncoder.BUTTONDOWN:
		print name, "Button down event =", RotaryEncoder.BUTTONDOWN
	elif event == RotaryEncoder.BUTTONUP:
		print name, "Button up event =", RotaryEncoder.BUTTONUP
	return

# Define the left and right knobs
leftknob = RotaryEncoder(LEFT_A,LEFT_B,LEFT_BUTTON,left_knob_event)
rightknob = RotaryEncoder(RIGHT_A,RIGHT_B,RIGHT_BUTTON,right_knob_event)

# Wait for events
while True:
	time.sleep(0.5)

# End of program

