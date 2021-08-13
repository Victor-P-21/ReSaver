#---Imports---
from os import listdir, mkdir, path
from shutil import copy, rmtree
from time import sleep, strftime
from winsound import Beep
#---Global---

#---Func---

#---Main---
rootDir = './'
bcFolder = 'Backups'
configFile = 'ReSaverConfig.txt'

    # Failsafe for config file
if listdir(path=rootDir).count(configFile) < 1:
    file = open(configFile, 'w')
    file.write('.\\Saves\\\n600\n10\n1\n\nAdd here:\nsource folder,\ndelay (in seconds) between loops,\ncopy count,\nsound feedback in this file')
    file.close()
    print('Add config first')
    exit()
else:
    file = open(configFile, 'r')
    copyFrom = file.readline()[:-1] # Cutting out last symbol in line (\n)
    delayInSec = int(file.readline()[:-1])
    copyCount = int(file.readline()[:-1])
    isSilent = int(file.readline()[:-1])
    file.close()
    
    # Failsafe for source
if path.isdir(copyFrom) != True:
    print('Error in source file! Incorrect route')
    exit()
    
    # Failsafe for backups dir
if listdir(path=rootDir).count(bcFolder) < 1:
    mkdir(bcFolder)
    
# Backups creation block
while True:
    # Old copy deleting
    if len(listdir(path=bcFolder + path.sep)) >= copyCount:
        rmtree(bcFolder + path.sep + listdir(path=bcFolder + path.sep)[0])
        
    # Timestamp folder creation
    nFolder = strftime("%d.%m.%Y %H-%M-%S")
    mkdir(bcFolder + path.sep + nFolder)
    
    # Backups creation
    counter = 0
    for x in listdir(path = copyFrom):
        if path.isfile(copyFrom + path.sep + x) == True: # Failsafe for folders
            copy(copyFrom + path.sep + x, bcFolder + path.sep + nFolder)
            counter += 1
            
    print('From ' + copyFrom + ' to ' + bcFolder + path.sep + nFolder + ' copied ' + str(counter) + ' file(s).\nPress Ctrl+C to exit\n')
    if isSilent > 0:
        try:    # Beep feedback
            Beep(200, 100)
            Beep(250, 100)
        except RuntimeError:
            print('Beep allowed only on Win systems, please disable it')
            
    try:    # Just for clearer stops
        sleep(delayInSec)
    except KeyboardInterrupt:
        print('ReSaver stopped')
        exit()
