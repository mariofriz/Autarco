# coding=utf-8
import os;
from Driver import *;

class RealDriver(Driver):
    #gpio 0 et 1 liés (0 out, 1 in)
    #gpio 2 et 3 liés (2 out, 3 in)
    #gpio 2 : compteur d'eau
    
    def __init__(self):
        for i in range(0,1):
            os.system('gpio mode '+str(Driver.gpioLights[i])+' out')
            os.system('gpio mode '+str(Driver.gpioSprinklers[i])+' out')
            os.system('gpio mode '+str(Driver.gpioPump)+' out')
            os.system('gpio mode '+str(2)+' out')
            os.system('gpio mode '+str(0)+' out')

    def getGPIO(self,index):
        return int(os.popen('gpio read '+str(index),"r").readline())

    def setGPIO(self,index,value):
        os.system("gpio write "+str(index)+" "+str(value))




