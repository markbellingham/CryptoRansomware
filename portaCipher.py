'''
implements porta cipher
Author: James Lyons
Created: 2014-02-12
https://github.com/jameslyons/pycipher/blob/master/pycipher/porta.py
'''
from base import *

####################################################################################
"""The Porta Cipher is a polyalphabetic substitution cipher, and has a key consisting of a word e.g. 'FORTIFICATION'.

:param key: The keyword, any word or phrase will do. Must consist of alphabetical characters only, no punctuation or numbers.          
"""
def portaCipher(string, key, mode):
    key = [k.upper() for k in key]

    if mode == 'encrypt':
        result = encipher(string, key)
    elif mode == 'decrypt':
        result = decipher(string, key)
    return result
    
def encipher(string, key):
    """Encipher string using Porta cipher according to initialised key. Punctuation and whitespace
    are removed from the input.       

    Example::

        ciphertext = Porta('HELLO').encipher(plaintext)     

    :param string: The string to encipher.
    :returns: The enciphered string.
    """            
    # string = remove_punctuation(string)
    ret = ''
    for (i,c) in enumerate(string):
        i = i%len(key)
        if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if   key[i] in 'AB': ret += 'NOPQRSTUVWXYZABCDEFGHIJKLM'[a2i(c)]
            elif key[i] in 'YZ': ret += 'ZNOPQRSTUVWXYBCDEFGHIJKLMA'[a2i(c)]
            elif key[i] in 'WX': ret += 'YZNOPQRSTUVWXCDEFGHIJKLMAB'[a2i(c)]
            elif key[i] in 'UV': ret += 'XYZNOPQRSTUVWDEFGHIJKLMABC'[a2i(c)]
            elif key[i] in 'ST': ret += 'WXYZNOPQRSTUVEFGHIJKLMABCD'[a2i(c)]
            elif key[i] in 'QR': ret += 'VWXYZNOPQRSTUFGHIJKLMABCDE'[a2i(c)]
            elif key[i] in 'OP': ret += 'UVWXYZNOPQRSTGHIJKLMABCDEF'[a2i(c)]
            elif key[i] in 'MN': ret += 'TUVWXYZNOPQRSHIJKLMABCDEFG'[a2i(c)]
            elif key[i] in 'KL': ret += 'STUVWXYZNOPQRIJKLMABCDEFGH'[a2i(c)]
            elif key[i] in 'IJ': ret += 'RSTUVWXYZNOPQJKLMABCDEFGHI'[a2i(c)]
            elif key[i] in 'GH': ret += 'QRSTUVWXYZNOPKLMABCDEFGHIJ'[a2i(c)]
            elif key[i] in 'EF': ret += 'PQRSTUVWXYZNOLMABCDEFGHIJK'[a2i(c)]
            elif key[i] in 'CD': ret += 'OPQRSTUVWXYZNMABCDEFGHIJKL'[a2i(c)]
        else: ret += c   # If the character is not in the alphabet
    return ret    

def decipher(string, key):
    """Decipher string using Porta cipher according to initialised key. Punctuation and whitespace
    are removed from the input. For the Porta cipher, enciphering and deciphering are the same operation.

    Example::

        plaintext = Porta('HELLO').decipher(ciphertext)     

    :param string: The string to decipher.
    :returns: The deciphered string.
    """   
    return encipher(string, key)