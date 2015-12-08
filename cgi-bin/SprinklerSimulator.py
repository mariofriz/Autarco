# coding=utf-8
import os;
import sys
import threading
import time
from SimulatedDriver import *;
from RealDriver import *;

class SprinklerSimulator(threading.Thread):
    
    driver = None
    
    def __init__(self, driver):
        threading.Thread.__init__(self)
        self._stopevent = threading.Event( )
        self.driver = driver

    def run(self):
        i = 0
        run = True
        while (not self._stopevent.isSet()) and run:
            if i%2:
                self.driver.setGPIO(2,1)
            else:
                self.driver.setGPIO(2,0)
            i += 1
            time.sleep(0.001)
            run = (self.driver.raspberry.gpios[6].getValue() == 1) or (self.driver.raspberry.gpios[7].getValue() == 1)
        self.stop()

    def stop(self):
        self._stopevent.set( )
