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

    m = None

    # define points where the motor must stop due to mechanical
    # stops
    stops = list()
    
    def __init__(self,motor):
        self.m = motor

    def findStops(self,power=20):
        # find at most two stops in the forward and back direction
        # of the arm

        # if we already have stops set, clear them and then find the
        # stops
        if len(self.stops) >= 2:
            self.clearstops()
        
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
            tc = self.m.get_tacho()
            stopCount = tc.tacho_count
            self.stops.append( stopCount )
            return stopCount
        else:
            # no stop found
            return None

        
            
    def clearStops(self):
        """ clear all stops """
        self.stops = list()

    
      
