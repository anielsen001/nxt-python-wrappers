# script to control donna's "I love you" bot
#
# orginally based on examples from nxt-python/examples

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

b.close()

class Drive(object):
    """
    This class is designed to drive a carriage with wheels driven by motors on the 
    left and right side. 

    We wish to drive the carriage by specifying distance. 
    """
    
    left_motor = None
    right_motor = None
    
    def __init__(self,left_motor,right_motor):
        """
        input motors on left and right side. These are of type nxt.Motor
        """
        self.left_motor = left_motor
        self.right_motor = right_motor
        
    def forward(self,delta_time):

       	self.left_motor.run(regulated=True)
        self.right_motor.run(regulated=True)
        time.sleep(delta_time)
        self.left_motor.idle()
        self.right_motor.idle()


