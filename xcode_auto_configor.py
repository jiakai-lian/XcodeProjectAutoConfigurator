#!/usr/bin/python

from mod_pbxproj import XcodeProject
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

if len(sys.argv) > 2:
    raise Exception("more than one file path")

#read the file path
filePath = sys.argv[1]

#load project file and create a backup
project = XcodeProject.Load(filePath)
project.backup()

rootObject = project["rootObject"]
projectObject = project["objects"][rootObject]["buildConfigurationList"]
    
debugConf = None
releaseConf = None
    
for id in project["objects"][projectObject]["buildConfigurations"]:
    if project["objects"][id]["name"].lower() == "debug":
        debugConf = project["objects"][id]["buildSettings"]
    elif project["objects"][id]["name"].lower() == "release":
        releaseConf = project["objects"][id]["buildSettings"]

#start config
debugConf["GCC_TREAT_WARNINGS_AS_ERRORS"] = "NO"
releaseConf["GCC_TREAT_WARNINGS_AS_ERRORS"] = "YES"

project.save()
    
print "Configuration Complete"