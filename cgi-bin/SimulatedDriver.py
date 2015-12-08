# coding=utf-8
import os;
import json;
from Driver import *;
from SimulatedRaspberry import *;

class SimulatedDriver(Driver):
    #gpio 0 et 1 liés (0 out, 1 in)
    #gpio 2 et 3 liés (2 out, 3 in)
    #gpio 2 : compteur d'eau
    
    raspberry = SimulatedRaspberry()

    def __init__(self):
        self.load()
        for i in range(0,2):
            self.raspberry.setGpio(Driver.gpioLights[i],1,self.getGPIO(Driver.gpioLights[i]))
            self.raspberry.setGpio(Driver.gpioSprinklers[i],1,self.getGPIO(Driver.gpioSprinklers[i]))
        self.raspberry.setGpio(Driver.gpioPump,1,self.getGPIO(Driver.gpioPump))
        self.raspberry.setGpio(2,1,self.getGPIO(2))
        self.raspberry.setGpio(0,1,self.getGPIO(0))

    def save(self):
        #print(self.raspberry.exportJson())
        out_file = open("gpio.json","w")
        out_file.write(self.raspberry.exportJson())
        out_file.close()
        
    def load(self):
        in_file = open("gpio.json","r")
        content = in_file.read()
        self.raspberry.importJson(content)
        in_file.close()

    def getGPIO(self,index):
        return self.raspberry.getGpio(index).getValue()

    def setGPIO(self,index,value):
        self.raspberry.setGpio(index,-1,value)