# XcodeProjectAutoConfigurator

----------
A simple Python script used to automatically configure the project.pbxproj file.
This script reads json config files and then apply these configurations to the project targets.

## How To Use ##

Clone this git repository or simply download **mod_pbxproj.py** and **xcode_auto_configurator.py**. Please download **debug.json** and **release.json** if you want. These two files are my own preferences for iOS  projects.

**Command:** 
```
python xocde_auto_configurator.py pbxprojPath [*.json...]
```
**Apply default configurations to the Sample project:**

```
python xcode_auto_configurator.py Sample.xcodeproj/project.pbxproj
```

This command applies debug.json and release.json to the project's debug and release targets.

You also can explicitly indicate json files.

```
python xcode_auto_configurator.py Sample.xcodeproj/project.pbxproj debug.json release.json
```

**How about another target?** 

That's easy.
Let's say the sample project has a target named **beta**.
To setup that target, simply create a **beta.json**, and write your configurations by following the sample json, and then run the command
```
python xcode_auto_configurator.py Sample.xcodeproj/project.pbxproj beta.json
```

**Auto Backup:**

If anything wrong, you always can find your backups inside the xcodeproj folder.
