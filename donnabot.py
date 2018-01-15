# script to control donna's "I love you" bot
#
# orginally based on examples from nxt-python/examples

ID = '00:16:53:17:52:EE'

import nxt, thread, time

import numpy as np

import donnabot

# this find_one_brick method is unreliable
#b = nxt.find_one_brick(host=ID)

from nxt.bluesock import BlueSock
sock = BlueSock(ID)
b=sock.connect()

mx = nxt.Motor(b, nxt.PORT_A) # left-side
my = nxt.Motor(b, nxt.PORT_B) # right-side

d = donnabot.Drive(mx,my)

touch = nxt.Touch(b,nxt.PORT_1)
ultrasonic = nxt.Ultrasonic(b,nxt.PORT_2)

b.close()
