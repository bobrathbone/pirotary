#!/usr/bin/env python
# $Id: test_rotary.py,v 1.2 2013/12/30 08:22:48 bob Exp $

import RPi.GPIO as GPIO
import time

# Switch definitions
MENU_SWITCH = 25
LEFT_SWITCH = 14
RIGHT_SWITCH = 15
UP_SWITCH = 17
DOWN_SWITCH = 18
CLOCKWISE=1
ANTICLOCKWISE=2


GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setwarnings(False)

rotary_a = 0
rotary_b = 0
rotary_c = 0
last_state = 0
direction = 0

# Call back routine called by switch events
def switch_event(switch):
	global rotary_a,rotary_b,rotary_c
	global direction
	global last_state

	if GPIO.input(LEFT_SWITCH):
		rotary_a = 1
	else:
		rotary_a = 0

	if GPIO.input(RIGHT_SWITCH):
		rotary_b = 1
	else:
		rotary_b = 0

	rotary_c = rotary_a ^ rotary_b
	new_state = rotary_a * 4 + rotary_b * 2 + rotary_c * 1
	delta = (new_state - last_state) % 4
	last_state = new_state

	if delta == 1:
		if direction == CLOCKWISE:
			print "Clockwise"
		else:
			direction = CLOCKWISE
	elif delta == 3:
		if direction == ANTICLOCKWISE:
			print "Anticlockwise"
		else:
			direction = ANTICLOCKWISE
        return

# For rev 2 boards with inbuilt pull-up/down resistors 
GPIO.setup(MENU_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(UP_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOWN_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LEFT_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RIGHT_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up switch event processing
GPIO.add_event_detect(MENU_SWITCH, GPIO.FALLING, callback=switch_event)
GPIO.add_event_detect(LEFT_SWITCH, GPIO.FALLING, callback=switch_event)
GPIO.add_event_detect(RIGHT_SWITCH, GPIO.FALLING, callback=switch_event)
GPIO.add_event_detect(UP_SWITCH, GPIO.FALLING, callback=switch_event)
GPIO.add_event_detect(DOWN_SWITCH, GPIO.FALLING, callback=switch_event)

while True:
	time.sleep(0.5)


