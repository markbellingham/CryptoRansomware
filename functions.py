import platform
from reverseCipher import *
from beaufortCipher import *


# Function that creates the key by concatenating the
# system name and network name and encrypting them with
# the BeaufortCipher
def createKey():
    key = platform.system() + platform.node()
    keyR = reverse(key)
    key = encipher(key, keyR)
    return key


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
