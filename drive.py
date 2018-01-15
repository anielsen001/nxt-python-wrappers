import numpy as np
import nxt, thread, time

class Drive(object):

    # define two motor objects on the left and right side of carriage
    leftMotor = None
    rightMotor = None

    # define objects to drive in different ways
    #
    # synchonized motors that drive the same
    synchroMotor = None
    
    def __init__(self,left_motor,right_motor):

        self.leftMotor = left_motor
        self.rightMotor = right_motor

        turnRatio = 1.0
        self.synchroMotor = nxt.motor.SynchronizedMotors(left_motor,
                                                         right_motor,
                                                         turnRatio)
        
    def straight(self,delta_time,power=100):
        """
        drive the motors together

        delta_time is how long to drive
        power > 0 goes forward
        power < 0 goes reverse
        """

        self.synchroMotor.run(power=power)
        time.sleep(delta_time)
        #self.synchroMotor.idle()
        self.synchroMotor.brake()
        
    def forward(self,delta_time,power=100):
        """
        drive the motors forward
        """

        self.straight(delta_time,power=np.abs(power))

    def reverse(self,delta_time,power=100):
        """
        drive the motors reverse
        """

        self.straight(delta_time,power=-np.abs(power))
    
