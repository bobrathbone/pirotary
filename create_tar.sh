#!/bin/bash
# $Id: create_tar.sh,v 1.1 2014/01/31 14:31:21 bob Exp $

FILELIST="rotary_class.py test_rotary_class.py test_rotary_switches.py"

# Cleanup 
rm -f *.pyc
chown -R  pi:pi /home/pi/develop/rotary/${FILELIST}

# Create radio software tar file
tar -cvzf  pi_rotary.tar.gz ${FILELIST}


