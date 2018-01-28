"""
arm.py

arm control for robot
"""

from __future__ import print_function

import nxt, thread, time
from nxt.motor import BlockedException
import numpy as np

class ArmError(Exception):
    pass

class Arm(object):

    # the motor associated with the arm
    m = None

    # define points where the motor must stop due to mechanical
    # stops, the two values in the list should be max and min counts
    stops = list()
    
    def __init__(self,motor):
        self.m = motor

        self.findStops()

    def findStops(self,power=20):
        # find at most two stops in the forward and back direction
        # of the arm

        # if we already have stops set, clear them and then find the
        # stops
        if len(self.stops) >= 2:
            self.clearStops()
        
        # power should be as small as possible to avoid damaging anything
        self.findStop(direction = 1, power = power)
        self.findStop(direction = -1, power = power)
        
    def findStop(self,direction = 1, power = 20):
        # find a single stop 
        try:
            # try to turn slightly more than 360 degrees around
            # if we do that without an exeption then the full motion
            # is clear
            self.m.turn(power=power*direction,tacho_units = 370)
        except BlockedException:
            # the motor hit a stop - idle the motor, add the stop to the
            # stop list and return the stop value
            self.m.idle()
            stopCount = self.getArmTacho()
            self.stops.append( stopCount )
            return stopCount
        else:
            # no stop found
            return None
        
    def clearStops(self):
        """ clear all stops """
        self.stops = list()

    def getArmTacho(self):
        """ find the current tacho count of the arm """
        tc = tc = self.m.get_tacho()
        return tc.tacho_count

    def moveArm(self,tacho,direction=1,power=100):
        """
        move the arm by the tacho in the given direction
        """

        # get the current arm motor location
        currentTacho = self.getArmTacho()
        
        # determine the desired location to move the arm to
        desiredTacho = tacho*np.sign( direction ) + currentTacho

        # check if the desired tacho is within the stops
        if len(self.stops) == 0:
            # check this way to ensure we don't have index errors
            pass
        elif desiredTacho > self.stops[0] :
            # exceed max
            raise ArmError('Arm motion will exceed maximum')
        elif desiredTacho < self.stops[1] :
            # less than min
            raise ArmError('Arm motion will exceed minimum')
        else:
            # move the arm the desired amount
            self.m.turn(power=power*direction,tacho_units = tacho)
        
    def down(self,tacho,power=100):
        """ move the arm up by tacho degrees """

        self.moveArm(tacho, power = power)

    def up(self, tacho, power = 100):
        """ move the arm down by tacho degrees """

        self.moveArm(tacho, power = power, direction = -1)
        
