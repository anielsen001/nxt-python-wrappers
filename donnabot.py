# script to control donna's "I love you" bot
#
# orginally based on examples from nxt-python/examples

ID1 = '00:16:53:17:52:EE'
ID2 = '00:16:53:0A:4B:2B'

import nxt, thread, time

import numpy as np

import drive

# this find_one_brick method is unreliable
#b = nxt.find_one_brick(host=ID)

from nxt.bluesock import BlueSock
sock = BlueSock(ID1)
b=sock.connect()

mx = nxt.Motor(b, nxt.PORT_A) # left-side
my = nxt.Motor(b, nxt.PORT_B) # right-side

d = drive.Drive(mx,my)

marm = nxt.Motor(b, nxt.PORT_C) # arm motor

touch = nxt.Touch(b,nxt.PORT_1)
ultrasonic = nxt.Ultrasonic(b,nxt.PORT_2)

b.close()
