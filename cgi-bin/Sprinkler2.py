# coding=utf-8
import os;
import sys
import threading
import time
from SimulatedDriver import *;
from RealDriver import *;

class Sprinkler2(threading.Thread):

    spinsByLiter = 450
    neededWater = 0
    currentGpioNumber = 0
    driver = None

    def __init__(self, neededWater, currentGpioNumber, driver):
        threading.Thread.__init__(self)
        self.neededWater = int(neededWater)
        self.currentGpioNumber = currentGpioNumber
        self.driver = driver
        self.driver.raspberry.gpios[self.currentGpioNumber].setValue(1)
        self.driver.save()

    def run(self):
        i = 0
        timeforOneLiter = 1.0 / (250.0 / self.spinsByLiter);
        temp = self.driver.raspberry.volume
        while i < self.neededWater:
            i += 1
            if i % 2 == 0:
                self.driver.raspberry.volume = temp + i
                self.driver.save()
            time.sleep(timeforOneLiter)
        self.driver.raspberry.volume = temp + self.neededWater
        self.driver.raspberry.gpios[self.currentGpioNumber].setValue(0)
        #print("Arrosage fini")