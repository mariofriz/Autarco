# coding=utf-8
from SimulatedGPIO import *;
import json;
import os;

class SimulatedRaspberry:
    gpio1 = SimulatedGPIO()
    gpio2 = SimulatedGPIO()
    gpio3 = SimulatedGPIO()
    gpio4 = SimulatedGPIO()
    gpio5 = SimulatedGPIO()
    gpio6 = SimulatedGPIO()
    gpio7 = SimulatedGPIO()
    gpio8 = SimulatedGPIO()
    gpio9 = SimulatedGPIO()
    gpio10 = SimulatedGPIO()
    gpio11 = SimulatedGPIO()
    gpio12 = SimulatedGPIO()
    gpio13 = SimulatedGPIO()
    gpio14 = SimulatedGPIO()
    gpio15 = SimulatedGPIO()
    gpio16 = SimulatedGPIO()
    gpio17 = SimulatedGPIO()
    gpio18 = SimulatedGPIO()
    gpio19 = SimulatedGPIO()
    gpio20 = SimulatedGPIO()
    gpios = []
    gpios.append(gpio1)
    gpios.append(gpio2)
    gpios.append(gpio3)
    gpios.append(gpio4)
    gpios.append(gpio5)
    gpios.append(gpio6)
    gpios.append(gpio7)
    gpios.append(gpio8)
    gpios.append(gpio9)
    gpios.append(gpio10)
    gpios.append(gpio11)
    gpios.append(gpio12)
    gpios.append(gpio13)
    gpios.append(gpio14)
    gpios.append(gpio15)
    gpios.append(gpio16)
    gpios.append(gpio17)
    gpios.append(gpio18)
    gpios.append(gpio19)
    gpios.append(gpio20)

    def getAllGpios(self):
        return self.gpios

    def getGpio(self,index):
        return self.gpios[index]

    def setGpio(self,index,state,value):
        self.gpios[index].setState(state)
        self.gpios[index].setValue(value)
        if index == 0:
            self.gpios[1].setValue(value)
        if index == 2:
            self.gpios[3].setValue(value)
            
    def exportJson(self):
        export = [];
        for i in range(0, 20):
            export.append(self.gpios[i].getValue())
        return json.dumps(export)
        
    def importJson(self, content):
        imp = json.loads(content)
        for i in range(0,20):
            self.gpios[i] = SimulatedGPIO()
            self.gpios[i].setValue(imp[i])
    