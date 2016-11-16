'''
base cipher object that other ciphers extend
really only provides mappings a2i and i2a for letter->int->letter conversions
Author: James Lyons
Created: 2012-04-28
https://github.com/jameslyons/pycipher/blob/master/pycipher/base.py
'''
import re

def encipher(string):
    return string
    
def decipher(string):
    return string
    
def a2i(ch):
    #ch = ch.upper()
    arr = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
       'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,
       'V':21,'W':22,'X':23,'Y':24,'Z':25,'a':26,'b':27,'c':28,'d':29,'e':30,
       'f':31,'g':32,'h':33,'i':34,'j':35,'k':36,'l':37,'m':38,'n':39,'o':40,
       'p':41,'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,'y':50,
       'z':51}
    return arr[ch]

def i2a(i):
    i = i%26
    arr = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    return arr[i]
    
def remove_punctuation(text,filter='[^A-Z]'):
    return re.sub(filter,'',text.upper())

# Function that returns the opposite of encrypt or decrypt for the second algorithm
def switchMode(mode):
    if (mode == 'encrypt'):
        mode_2 = 'decrypt'
    elif (mode == 'decrypt'):
        mode_2 = 'encrypt'
    return mode_2