# script to control donna's "I love you" bot

ID = '00:16:53:17:52:EE'

import nxt, thread, time

# this find_one_brick method is unreliable
#b = nxt.find_one_brick(host=ID)

from nxt.bluesock import BlueSock
sock = BlueSock(ID)
b=sock.connect()

mx = nxt.Motor(b, nxt.PORT_A) # left-side
my = nxt.Motor(b, nxt.PORT_B) # right-side

touch = nxt.Touch(b,nxt.PORT_1)
ultrasonic = nxt.Ultrasonic(b,nxt.PORT_2)

class Drive(object):

    left_motor = None
    right_motor = None
    
    def __init__(self,left_motor,right_motor):

        self.left_motor = left_motor
        self.right_motor = right_motor
        
    def straight(self,delta_time):

       	self.left_motor.run(regulated=True)
        self.right_motor.run(regulated=True)
        time.sleep(delta_time)
        self.left_motor.idle()
        self.right_motor.idle()

b.close()
