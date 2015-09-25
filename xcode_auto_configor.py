#!/usr/bin/python

from mod_pbxproj import XcodeProject
import sys
import json

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

if len(sys.argv) < 2:
    raise Exception("need project.pbxproj file path")


#read the file path
filePath = sys.argv[1]

if len(sys.argv) > 2:
    configFiles = list(sys.argv)
    del configFiles[0:2]
else:
    configFiles = ["debug.json","release.json"]

print configFiles

configNames = list();

#load each config
for config in configFiles:
    configNames.append(config.split(".")[0])

print configNames

configJsons = list()

#load each json files
for config in configFiles:
    with open(config) as data_file:
        configJsons.append(json.load(data_file))

print configJsons

#load project file and create a backup
project = XcodeProject.Load(filePath)
project.backup()

rootObject = project["rootObject"]
projectObject = project["objects"][rootObject]["buildConfigurationList"]

configEntries = list()
    
for id in project["objects"][projectObject]["buildConfigurations"]:
    for configName in configNames:
        if project["objects"][id]["name"].lower() == configName:
            configEntries.append(project["objects"][id]["buildSettings"])

#start config

#debug conf
for i in range(0, len(configEntries)):
    entry = configEntries[i];
    for key in configJsons[i]:
    #    print key
        entry[key] = configJsons[i][key]

project.save()

print "Auto Configuration Complete"