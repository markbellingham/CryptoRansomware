'''
implements porta cipher
Author: James Lyons
Created: 2014-02-12
https://github.com/jameslyons/pycipher/blob/master/pycipher/porta.py
'''
from base import *

##########################################################################
"""The Porta Cipher is a polyalphabetic substitution cipher,
and has a key consisting of a word e.g. 'FORTIFICATION'.
:param key: The keyword, any word or phrase will do.
Must consist of alphabetical characters only, no punctuation or numbers.
"""


def portaCipher(string, key, mode):
    key = [k.upper() for k in key]

    if mode == 'encrypt':
        result = encipher(string, key)
    elif mode == 'decrypt':
        result = decipher(string, key)
    return result


def encipher(string, key):
    # Encipher string using Porta cipher according to initialised key.

    ret = ''
    for (i, c) in enumerate(string):
        i = i % len(key)
        if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<>?@[]_{=}½¾þøŧ¶łæßðđŋħµ¢€1234567890':
            if key[i] in 'YZ':
                ret += 'ZNOPQRSTUVWXYBCDEFGHIJKLMAznopqrstuvwxybcdefghijklma!"#$%&()*+,-./:;<>?@[]_{=}ħ½¾þøŧ¶łæßðđŋ¢€1234567890µ'[a2i(c)]
            elif key[i] in 'WX':
                ret += 'YZNOPQRSTUVWXCDEFGHIJKLMAByznopqrstuvwxcdefghijklmab.!"#$%&()*+,-:;<>?@[]_{=}/ŋħ½¾þøŧ¶łæßðđ€1234567890µ¢'[a2i(c)]
            elif key[i] in 'UV':
                ret += 'XYZNOPQRSTUVWDEFGHIJKLMABCxyznopqrstuvwdefghijklmabc-.!"#$%&()*+,;<>?@[]_{=}/:đŋħ½¾þøŧ¶łæßð1234567890µ¢€'[a2i(c)]
            elif key[i] in 'ST':
                ret += 'WXYZNOPQRSTUVEFGHIJKLMABCDwxyznopqrstuvefghijklmabcd,-.!"#$%&()*+<>?@[]_{=}/:;ðđŋħ½¾þøŧ¶łæß234567890µ¢€1'[a2i(c)]
            elif key[i] in 'QR':
                ret += 'VWXYZNOPQRSTUFGHIJKLMABCDEvwxyznopqrstufghijklmabcde+,-.!"#$%&()*>?@[]_{=}/:;<ßðđŋħ½¾þøŧ¶łæ34567890µ¢€12'[a2i(c)]
            elif key[i] in 'OP':
                ret += 'UVWXYZNOPQRSTGHIJKLMABCDEFuvwxyznopqrstghijklmabcdef*+,-.!"#$%&()?@[]_{=}/:;<>æßðđŋħ½¾þøŧ¶ł4567890µ¢€123'[a2i(c)]
            elif key[i] in 'MN':
                ret += 'TUVWXYZNOPQRSHIJKLMABCDEFGtuvwxyznopqrshijklmabcdefg)*+,-.!"#$%&(@[]_{=}/:;<>?łæßðđŋħ½¾þøŧ¶567890µ¢€1234'[a2i(c)]
            elif key[i] in 'KL':
                ret += 'STUVWXYZNOPQRIJKLMABCDEFGHstuvwxyznopqrijklmabcdefgh()*+,-.!"#$%&[]_{=}/:;<>?@¶łæßðđŋħ½¾þøŧ67890µ¢€12345'[a2i(c)]
            elif key[i] in 'IJ':
                ret += 'RSTUVWXYZNOPQJKLMABCDEFGHIrstuvwxyznopqjklmabcdefghi&()*+,-.!"#$%]_{=}/:;<>?@[ŧ¶łæßðđŋħ½¾þø7890µ¢€123456'[a2i(c)]
            elif key[i] in 'GH':
                ret += 'QRSTUVWXYZNOPKLMABCDEFGHIJqrstuvwxyznopklmabcdefghij%&()*+,-.!"#$_{=}/:;<>?@[]øŧ¶łæßðđŋħ½¾þ890µ¢€1234567'[a2i(c)]
            elif key[i] in 'EF':
                ret += 'PQRSTUVWXYZNOLMABCDEFGHIJKpqrstuvwxyznolmabcdefghijk$%&()*+,-.!"#{=}/:;<>?@[]_þøŧ¶łæßðđŋħ½¾90µ¢€12345678'[a2i(c)]
            elif key[i] in 'CD':
                ret += 'OPQRSTUVWXYZNMABCDEFGHIJKLopqrstuvwxyznmabcdefghijkl#$%&()*+,-.!"=}/:;<>?@[]_{¾þøŧ¶łæßðđŋħ½0µ¢€123456789'[a2i(c)]
            elif key[i] in 'AB':
                ret += 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"#$%&()*+,-.!}/:;<>?@[]_{=½¾þøŧ¶łæßðđŋħµ¢€1234567890'[a2i(c)]
        else:
            ret += c   # If the character is not in the alphabet
    return ret


def decipher(string, key):
    """Decipher string using Porta cipher according to initialised key.
    For the Porta cipher, enciphering and deciphering are the same operation.
    """
    return encipher(string, key)


# def encipher(string, key):
#     # Encipher string using Porta cipher according to initialised key.

#     ret = ''
#     for (i, c) in enumerate(string):
#         i = i % len(key)
#         if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<>?@[]_{=}1234567890':
#             if key[i] in 'YZ':
#                 ret += 'ZNOPQRSTUVWXYBCDEFGHIJKLMAznopqrstuvwxybcdefghijklma-.!"#$%&()*+,;<>?@[]_{=}/:1234567890'[a2i(c)]
#             elif key[i] in 'WX':
#                 ret += 'YZNOPQRSTUVWXCDEFGHIJKLMAByznopqrstuvwxcdefghijklmab,-.!"#$%&()*+<>?@[]_{=}/:;2345678901'[a2i(c)]
#             elif key[i] in 'UV':
#                 ret += 'XYZNOPQRSTUVWDEFGHIJKLMABCxyznopqrstuvwdefghijklmabc+,-.!"#$%&()*>?@[]_{=}/:;<3456789012'[a2i(c)]
#             elif key[i] in 'ST':
#                 ret += 'WXYZNOPQRSTUVEFGHIJKLMABCDwxyznopqrstuvefghijklmabcd*+,-.!"#$%&()?@[]_{=}/:;<>4567890123'[a2i(c)]
#             elif key[i] in 'QR':
#                 ret += 'VWXYZNOPQRSTUFGHIJKLMABCDEvwxyznopqrstufghijklmabcde)*+,-.!"#$%&(@[]_{=}/:;<>?5678901234'[a2i(c)]
#             elif key[i] in 'OP':
#                 ret += 'UVWXYZNOPQRSTGHIJKLMABCDEFuvwxyznopqrstghijklmabcdef()*+,-.!"#$%&[]_{=}/:;<>?@6789012345'[a2i(c)]
#             elif key[i] in 'MN':
#                 ret += 'TUVWXYZNOPQRSHIJKLMABCDEFGtuvwxyznopqrshijklmabcdefg&()*+,-.!"#$%]_{=}/:;<>?@[7890123456'[a2i(c)]
#             elif key[i] in 'KL':
#                 ret += 'STUVWXYZNOPQRIJKLMABCDEFGHstuvwxyznopqrijklmabcdefgh%&()*+,-.!"#$_{=}/:;<>?@[]8901234567'[a2i(c)]
#             elif key[i] in 'IJ':
#                 ret += 'RSTUVWXYZNOPQJKLMABCDEFGHIrstuvwxyznopqjklmabcdefghi$%&()*+,-.!"#{=}/:;<>?@[]_9012345678'[a2i(c)]
#             elif key[i] in 'GH':
#                 ret += 'QRSTUVWXYZNOPKLMABCDEFGHIJqrstuvwxyznopklmabcdefghij#$%&()*+,-.!"=}/:;<>?@[]_{0123456789'[a2i(c)]
#             elif key[i] in 'EF':
#                 ret += 'PQRSTUVWXYZNOLMABCDEFGHIJKpqrstuvwxyznolmabcdefghijk"#$%&()*+,-.!}/:;<>?@[]_{=1234567890'[a2i(c)]
#             elif key[i] in 'CD':
#                 ret += 'OPQRSTUVWXYZNMABCDEFGHIJKLopqrstuvwxyznmabcdefghijkl!"#$%&()*+,-./:;<>?@[]_{=}2345678901'[a2i(c)]
#             elif key[i] in 'AB':
#                 ret += 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm.!"#$%&()*+,-:;<>?@[]_{=}/3456789012'[a2i(c)]
#         else:
#             ret += c   # If the character is not in the alphabet
#     return ret