# script to control donna's "I love you" bot
#
# orginally based on examples from nxt-python/examples

import nxt, thread, time

import numpy as np

import drive

# this find_one_brick method is unreliable
#b = nxt.find_one_brick(host=ID)

from nxt.bluesock import BlueSock

# connection to first brick "JAWS"
ID1 = '00:16:53:17:52:EE' # MAC address
sock1 = BlueSock(ID1)
b1 = sock1.connect()

# connection to 2nd brick "pie" 
ID2 = '00:16:53:0A:4B:2B' # MAC address
sock2 = BlueSock(ID2)
b2 = sock2.connect()

mx = nxt.Motor(b1, nxt.PORT_A) # left-side
my = nxt.Motor(b1, nxt.PORT_B) # right-side

d = drive.Drive(mx,my)

marm = nxt.Motor(b2, nxt.PORT_C) # arm motor

touch = nxt.Touch(b1,nxt.PORT_1)
ultrasonic = nxt.Ultrasonic(b1,nxt.PORT_2)

b1.close()
b2.close()
