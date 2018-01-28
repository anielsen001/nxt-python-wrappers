import numpy as np
import nxt, thread, time

# these are the potential states of the drive system
IDLE = -1
BRAKE = 0
FORWARD = 1
REVERSE = 2
TURN_IN_LEFT = 3
TURN_IN_RIGHT = 4
TURN_OUT_LEFT = 5
TURN_OUT_RIGHT = 6
TURN_PLACE_LEFT = 7
TURN_PLACE_RIGHT = 8

# there is some minimum power below which the motors don't turn
# this is determined empirically
# these values are described in the nxt.motor.BaseMotor class comments.
# MAX_POWER should really be -127 or 128 to keep things simple, the
# 127 value is use here.
MIN_POWER = 64
MAX_POWER = 127

class DriveError(Exception):
    """
    Errors associated with the drive system
    """
    pass

class Drive(object):

    # the methods currently run for a specified period of time and
    # power. They cannot be easily calibrated for distance or angle
    # the Motor.turn() methods can help with that, with constructs like:
    # d.synchroMotor.turn(power=-100,tacho_units=360)
    # or
    # d.rightMotor.turn(power=100,tacho_units = 180)
    # for these motors, tacho_units are degrees

    # define two motor objects on the left and right side of carriage
    leftMotor = None
    rightMotor = None

    # define objects to drive in different ways
    #
    # synchonized motors that drive the same
    synchroMotor = None

    # state of the drive system
    _state = None
    
    def __init__(self,left_motor,right_motor):

        self.leftMotor = left_motor
        self.rightMotor = right_motor

        turnRatio = 1.0
        self.synchroMotor = nxt.motor.SynchronizedMotors(left_motor,
                                                         right_motor,
                                                         turnRatio)

        # on init, idle all the drive motors
        self.idle()

    def setState(self,state):
        """ set the state of the drive system. returns the state """
        self._state = state
        return self._state

    def getState(self,state):
        """ return the state of the drive system """
        return self._state

    def idle(self):
        """ no power to motors, no brake to motors """
        self.synchroMotor.idle()
        self.setState( IDLE )

    def brakeAll(self):
        """
        brake all motors
        """
        self.synchroMotor.brake()
        self.setState( STOP )
    
    def straight(self,delta_time=None,power=100):
        """
        drive the motors together

        delta_time is how long to drive None runs continuously
        power > 0 goes forward
        power < 0 goes reverse

        if abs(power) <= MIN_POWER then motors won't turn
        """

        if np.abs(power) > MAX_POWER :
            # error condition
            raise DriveError('power must be <= ' + str(MAX_POWER) )
        
        if ( np.abs(power) <= MIN_POWER ) and \
           ( not power == 0 ) :
            self.brakeAll()
        elif power > 0 :
            self.synchroMotor.run(power=power)
            self.setState( FORWARD )
        elif power < 0 :
            self.synchroMotor.run(power=power)
            self.setState( REVERSE )
        else:
            # power = 0
            # equivalent to IDLE
            self.idle()
            
        if delta_time is not None:
            time.sleep(delta_time)
            # use of brake vice idle causes hardstop instead of glide to stop
            #self.synchroMotor.idle()
            self.brakeAll()
        
    def forward(self,delta_time=None,power=100):
        """
        drive the motors forward
        """
        
        self.straight(delta_time=delta_time,power=np.abs(power))

    def reverse(self,delta_time=None,power=100):
        """
        drive the motors reverse
        """

        self.straight(delta_time=delta_time,power=-np.abs(power))
    

    def turnInPlace(self,delta_time=None,turnLeft=True,power=100):
        """
        rotate the carriage by turning each motor in opposite 
        directions at the same rate
        """
        if turnLeft:
            # left turn - counter-clockwise as seen from above

            self.leftMotor.run(power = -power)
            self.rightMotor.run(power = power)
            self.setState( TURN_IN_LEFT )
                       
        else:
            # right turn - clockwise as seen from above
            self.leftMotor.run(power = power)
            self.rightMotor.run(power = -power)
            self.setState( TURN_IN_RIGHT )

        if delta_time is not None:
            time.sleep(delta_time)
            self.leftMotor.brake()
            self.rightMotor.brake()
            self.setState( STOP )

    def turnOut(self,delta_time=None,turnLeft=True,power=100):
        """
        rotate the carriage by braking one wheel and turning
        the opposite so that the carriage turns out from its 
        track
        """
        if turnLeft:
            self.rightMotor.run( power = power )
            self.leftMotor.brake()
            self.setState( TURN_OUT_LEFT )
        else:
            self.rightMotor.brake()
            self.leftMotor.run( power = power )
            self.setState( TURN_OUT_RIGHT )

        if delta_time is not None:
            time.sleep(delta_time)
            self.leftMotor.brake()
            self.rightMotor.brake()
            self.setState( STOP )
        
    def turnIn(self,delta_time=None,turnLeft=True,power=100):
        """
        rotate the carriage by braking one wheel and turning
        the opposite so that the carriage turns into its track
        """
        if turnLeft:
            self.rightMotor.brake()
            self.leftMotor.run( power = -power )
            self.setState( TURN_IN_LEFT )
        else:
            self.rightMotor.run( power = -power )
            self.leftMotor.brake()
            self.setState( TURN_IN_RIGHT )

        if delta_time is not None:
            time.sleep(delta_time)
            self.leftMotor.brake()
            self.rightMotor.brake()
            self.setState( STOP )

        
            
