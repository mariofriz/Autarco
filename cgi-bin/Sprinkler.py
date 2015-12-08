# coding=utf-8
import os;
import sys
import threading
import time
from SimulatedDriver import *;
from RealDriver import *;

class Sprinkler(threading.Thread):

    nbBallSpins = 0.0
    usedWater = 0
    spinsByLiter = 450
    neededWater = 0
    currentGpio = 0
    driver = None

    def __init__(self, neededWater, currentGpioNumber, driver):
        threading.Thread.__init__(self)
        self.neededWater = neededWater
        self.currentGpioNumber = currentGpioNumber
        self._stopevent = threading.Event( )
        self.driver = driver
        self.driver.raspberry.gpios[self.currentGpioNumber].setValue(1)

    def run(self):
        actualValue = 0
        activation = 0
        while (not self._stopevent.isSet()) and (self.usedWater < self.neededWater):
            ballValue = self.driver.getGPIO(3)
            if actualValue != ballValue:
                if actualValue == 0:
                    activation = 1
                actualValue = ballValue
            #print activation
            if activation == 1:
                self.nbBallSpins = self.nbBallSpins + 1
                self.usedWater = self.nbBallSpins / self.spinsByLiter
                activation = 0
        if self.usedWater >= self.neededWater:
            print("Arrosage fini")
            self.driver.raspberry.gpios[self.currentGpioNumber].setValue(0)
            self.stop()
        
    def stop(self):
        self._stopevent.set( )