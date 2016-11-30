'''
base cipher object that other ciphers extend
really only provides mappings a2i and i2a for letter->int->letter conversions
Author:  James Lyons
Created:  2012-04-28
https: //github.com/jameslyons/pycipher/blob/master/pycipher/base.py
'''
# import re


def a2i(ch):
    # print('ch is: %s' % ch)
    arr = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
           'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
           'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,
           'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28,
           'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35,
           'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42,
           'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49,
           'y': 50, 'z': 51, '!': 52, '"': 53, '#': 54, '$': 55, '%': 56,
           '&': 57, '(': 58, ')': 59, '*': 60, '+': 61, ',': 62, '-': 63,
           '.': 64, '/': 65, ':': 66, ';': 67, '<': 68, '>': 69, '?': 70,
           '@': 71, '[': 72, ']': 73, '_': 74, '{': 75, '=': 76, '}': 77,
           '½': 78, '¾': 79, 'þ': 80, 'ø': 81, 'ŧ': 82, '¶': 83, 'ł': 84,
           'æ': 85, 'ß': 86, 'ð': 87, 'đ': 88, 'ŋ': 89, 'ħ': 90, 'µ': 91,
           '¢': 92, '€': 93, '1': 94, '2': 95, '3': 96, '4': 97, '5': 98,
           '6': 99, '7': 100, '8': 101, '9': 102, '0': 103}
    return arr[ch]
# !"#$%&()*+,-./:;<>?@[]_{=}½¾þøŧ¶łæßðđŋħµ¢€


def i2a(i):
    i = i % 104
    arr = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           '!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.',
           '/', ':', ';', '<', '>', '?', '@', '[', ']', '_', '{', '=', '}',
           '½', '¾', 'þ', 'ø', 'ŧ', '¶', 'ł', 'æ', 'ß', 'ð', 'đ', 'ŋ', 'ħ',
           'µ', '¢', '€', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    return arr[i]


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
