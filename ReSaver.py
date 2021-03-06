#!/usr/bin/env python
#---Imports---
from os import listdir, mkdir, path
from shutil import copy, rmtree
from time import sleep, strftime
from winsound import Beep
from sys import exit
#---Global---
bcFolder = 'Backups'
configFile = 'ReSaverConfig.txt'
#---Func---

#---Main---
    # Failsafe for config file
if path.exists(configFile) != True:
    file = open(configFile, 'w')
    file.write('.\\Saves\\\n600\n10\n1\n\nAdd here:\n-source folder,\n-delay (in seconds) between loops,\n-copy count,\n-sound feedback in this file')
    file.close()
    print('Add configuration to app')
    input('\nPress Enter to close application')
    exit()
else: # if exists load data
    file = open(configFile, 'r')
    copyFrom = file.readline()[:-1]
    delayInSec = int(file.readline()[:-1])
    copyCount = int(file.readline()[:-1])
    isSilent = int(file.readline()[:-1])
    file.close()
    
    # Failsafe for source
if path.isdir(copyFrom) != True:
    print('Error in config file! Incorrect route')
    input('\nPress Enter to close application')
    exit()
    
    # Failsafe for backups dir
if path.exists(bcFolder) != True:
    mkdir(bcFolder)
    
# Backups creation block
while True:
    # Old copy deleting
    if len(listdir(path=bcFolder + path.sep)) >= copyCount:
        rmtree(bcFolder + path.sep + listdir(path=bcFolder + path.sep)[0])
        
    # Timestamp folder creation
    newFolder = strftime("%d.%m.%Y %H-%M-%S")
    mkdir(bcFolder + path.sep + newFolder)
    
    # Backups creation
    counter = 0
    for x in listdir(path = copyFrom):
        if path.isfile(copyFrom + path.sep + x) == True: # Failsafe for folders
            copy(copyFrom + path.sep + x, bcFolder + path.sep + newFolder)
            counter += 1
            
    print('From ' + copyFrom + ' to ' + bcFolder + path.sep + newFolder + ' copied ' + str(counter) + ' file(s).\nPress Ctrl+C to exit\n')
    
    if isSilent > 0:
        try:    # Beep feedback
            Beep(200, 100)
            Beep(250, 100)
        except RuntimeError:
            print('Beep allowed only on Windows systems, please disable it in config file')
            
    try:    # Just for clearer stops
        sleep(delayInSec)
    except KeyboardInterrupt:
        print('ReSaver stopped')
        input('\nPress Enter to close application')
        exit()
        
#---Extra---
# pyinstaller --onefile ReSaver.py
