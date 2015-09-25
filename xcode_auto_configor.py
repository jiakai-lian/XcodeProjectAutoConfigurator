#!/usr/bin/python

from mod_pbxproj import XcodeProject
import sys
import json

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

class Configuration:
    def __init__(self,jsonFileName):
        self.jsonFileName = jsonFileName
        #find config name
        self.name = jsonFileName.split(".")[0].lower()
        
        #load json data
        with open(jsonFileName) as data_file:
            self.jsonContent = json.load(data_file)


if len(sys.argv) < 2:
    raise Exception("need project.pbxproj file path")


#read the file path
filePath = sys.argv[1]

if len(sys.argv) > 2:
    jsonFiles = list(sys.argv)
    del jsonFiles[0:2]
else:
    jsonFiles = ["debug.json","release.json"]

print jsonFiles

#create configuration objects
dictOfConfig = dict();
for file in jsonFiles:
    config = Configuration(file)
    dictOfConfig[config.name] = config

#load project file and create a backup
project = XcodeProject.Load(filePath)
project.backup()

rootObject = project["rootObject"]
projectObject = project["objects"][rootObject]["buildConfigurationList"]
    
for id in project["objects"][projectObject]["buildConfigurations"]:
    name = project["objects"][id]["name"].lower()
    
    #if this configuration need to be changed
    if dictOfConfig[name] is not None:
        entry = project["objects"][id]["buildSettings"]
        #for each setting in the json, apply to the target entry
        for key in dictOfConfig[name].jsonContent:
            entry[key] = dictOfConfig[name].jsonContent[key]

project.save()

print "Auto Configuration Complete"