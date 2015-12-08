#!/usr/bin/python
import cgi;
import cgitb;
import json;
from SimulatedDriver import *;
cgitb.enable()

arguments=cgi.FieldStorage()
driver = SimulatedDriver()

print("Content-type: text/html\n\n")

if("action" in arguments):
    print("Content-type: text/html\n\n")
    print(arguments["action"])
    action = arguments["action"]
    if(action == "getInfos"):
        data = {'light1':driver.getLight(0),'light2':driver.getLight(1),'sprinkler1':driver.getSprinkler(0),'sprinkler2':driver.getSprinkler(1), 'pump':driver.getPump()}
        data_json=json.dump(data)
        print("Content-type: text/html\n\n")
        print (data_json)
    elif(action=="set"):
        for i in range(0,1):
            if(arguments.has_key("light")+(i+1)):
                print("light"+str(i+1)+" put to"+str(arguments.getvalue("light"+str(i+1))))
                driver.setLight(i+1,arguments.getvalue("light"+str(i+1)))

print("Test that2 !")