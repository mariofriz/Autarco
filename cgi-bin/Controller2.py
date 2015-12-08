#!/usr/bin/python
# coding=utf-8
import cgi;
import cgitb;
import json;
from SimulatedDriver import *;
from RealDriver import *;
from Sprinkler import *;
from SprinklerSimulator import *;
cgitb.enable()

driver = SimulatedDriver()

sp = Sprinkler(2,6,driver)
sps = SprinklerSimulator(driver)
sp.start()
sps.start()

print ("go !")
print ("fini ! Litres utilisés :")
print (sp.usedWater)