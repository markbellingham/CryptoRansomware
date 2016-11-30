'''
implements beaufort cipher
Author: James Lyons
Created: 2012-04-28
https://github.com/jameslyons/pycipher/blob/master/pycipher/beaufort.py
'''
from base import *


def beaufortCipher(string, key, mode):
    key = [k.upper() for k in key]

    if mode == 'encrypt':
        result = encipher(string, key)
    elif mode == 'decrypt':
        result = decipher(string, key)
    return result


def encipher(string, key):
    LETTERS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<>?@[]_{=}½¾þøŧ¶łæßðđŋħµ¢€'
    """Encipher string using Beaufort cipher according to initialised key.
    """
    ret = ''
    for (i, c) in enumerate(string):
        i = i % len(key)
        if c in LETTERS:
            ret += i2a(a2i(key[i]) - a2i(c))
        else:
            # Handles unprintable characters such as \n
            ret += c
    return ret


def decipher(string, key):
    """Decipher string using Beaufort cipher according to initialised key.
    For the Beaufort cipher, enciphering and deciphering are the same operation.
    """
    return encipher(string, key)
