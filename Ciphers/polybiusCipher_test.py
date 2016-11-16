# Polybius Cipher
# https://github.com/lukaszbanasiak/python-ciphers/blob/master/Polybius.py

# -*- coding: utf-8 -*-
from unicodedata import normalize
import optparse
import codecs
import sys
import re

__author__ = 'Lukasz Banasiak <lukasz@banasiak.me>'
__version__ = '1.1'


def generate_array(key):

    """Create Polybius square with transposition.

    :param key: transposition word
    :return: array
    """
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    array = []
    _tmp = []
    key = re.sub(r'[^a-zA-Z]+', '', key)  # remove non-alpha character
    key = key.upper()

    if key:
        for k in key:
            alphabet = alphabet.replace(k, '')

        alphabet = key + alphabet

    for y in range(5):
        for x in range(5):
            _tmp.append(alphabet[0 + 5 * y + x])
        array.append(_tmp)
        _tmp = []

    return array


def format_cipher(data):

    """Format cipher.

    Every second number put space, e.g. 112423 => 11 24 23

    :param data: cipher
    :return: cipher with spaces
    """

    return " ".join(data[i:i + 2] for i in range(0, len(data), 2))


def encode(words, array):

    """
    Polybius square encryption.

    :param words: string to encrypt
    :return: encrypted string
    """

    cipher = ''

    words = normalize('NFKD', words).encode('ascii', 'ignore')  # replace national characters to ASCII equivalents

    for word in words.upper():
        print('Value of word is %s' % word)
        for i in range(len(array)):
            if word in array[i]:
                oy = str(i + 1)
                print('Value of oy is: %s' % oy)
                ox = str(i)
                print('Value of ox is: %s' % ox)
                cipher += oy + ox
    print('Value of cipher is: %s' % cipher)
    return cipher


def decode(numbers, array):

    """
    Polybius square decryption.

    :param numbers: numbers to decrypt
    :return: decrypted string
    """

    numbers = re.sub(r'[\D]+', '', numbers)  # remove non-digit character

    text = ''

    for number in range(0, len(numbers), 2):
        try:
            oy = int(numbers[number]) - 1
            ox = int(numbers[number + 1]) - 1
            text += array[oy][ox]
        except IndexError:
            pass
        continue
    print('Value of text is: %s' % text)

    return text


def pCipher(msg, key, mode):

    array = generate_array(key)

    if (mode == 'decrypt'):
        text = decode(msg, array)
        print ('Value of text is: %s' % text)
    elif (mode == 'encrypt'):
        text = format_cipher(encode(msg, array))
        print ('Value of text is: %s' % text)
    return text