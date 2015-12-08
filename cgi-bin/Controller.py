#!/usr/bin/python
import cgi;
import cgitb;
import json;
from SimulatedDriver import *;
from Sprinkler import *;
from SprinklerSimulator import *;
cgitb.enable()

arguments = cgi.FieldStorage()
driver = SimulatedDriver()

def dumpInfos():
    data = {'light1':driver.getLight(0),'light2':driver.getLight(1),'sprinkler1':driver.getSprinkler(0),'sprinkler2':driver.getSprinkler(1), 'pump':driver.getPump()}
    data_json = json.dumps(data)
    print (data_json)

if "action" in arguments:
    print("Content-type: text/html\n")
    action = arguments.getvalue("action")
    if action == "getInfos":
        dumpInfos()
    elif action == "set":
        for i in range(0,2):
            curLight="light"+str((i+1))
            if curLight in arguments:
                #print(curLight+" put to"+str(arguments.getvalue(curLight)))
                driver.setLight(i,arguments.getvalue(curLight))
        for i in range(0,2):
            curWater="water"+str((i+1))
            if curWater in arguments:
                #print(curWater+" put to"+str(arguments.getvalue(curWater)))
                quantity = arguments.getvalue(curWater)
                sp = Sprinkler(quantity, driver.gpioSprinklers[i], driver)
                sps = SprinklerSimulator(driver)
                sp.start()
                sps.start()
        driver.save()
        dumpInfos()
