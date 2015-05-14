#!/usr/bin/env python

import serial                                 # imports serial library
import time                                    # imports time library
ser = serial.Serial("/dev/ttyAMA0", 50)            # init serial coms
                              

ser.write ("x")                                 # send void byte to reset arduino
time.sleep (2)                                 # wait for arduino reset cycle

ser.write ("10101010101010101A")                                 # send byte to turn on led   
