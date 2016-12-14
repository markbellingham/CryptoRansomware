import platform
from reverseCipher import *
from beaufortCipher import *
import sys
import getopt
import fileinput


# Function that creates the key by concatenating the
# system name and network name and encrypting them with
# the BeaufortCipher
def createKey():
    key = platform.system() + platform.node()
    keyR = reverse(key)
    key = encipher(key, keyR)
    return key


def getOption(argv):
    try:
        opts, args = getopt.getopt(argv, 'de', ["decrypt", "encrypt"])
    except getopt.GetoptError:
        print("main_program.py -e or main_program.py --encrypt to encrypt")
        print("main_program.py -d or main_program.py --decrypt to decrypt")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-d', '--decrypt'):
            mode = 'decrypt'
        if opt in ('-e', '--encrypt'):
            mode = 'encrypt'
    return mode


# Function that switches the mode between encrypt and decrypt
def switchMode(mode):
    if (mode == 'encrypt'):
        mode_2 = 'decrypt'
    elif (mode == 'decrypt'):
        mode_2 = 'encrypt'
    return mode_2


# Function to add the filename to the logfile
def addToLog(path):
    if checkLog(path):
        return
    else:
        with open('hacked.log', 'a') as log:
            log.write(path + '\n')


# Function that checks if the filename is in the logfile
def checkLog(path):
    # print('path: ' + path)
    with open('hacked.log', 'r') as logfile:
        for line in logfile:
            # print('line: ' + line)
            if path in line:
                return True
    return False


# Function that deletes the filename entry from the logfile
def deleteFromLog(filename):
    with open('hacked.log', 'r') as f:
        lines = f.readlines()
        
    with open('hacked.log', 'w') as f:
        for line in lines:
            if line != filename + '\n':
                f.write(line)
