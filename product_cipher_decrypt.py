# Import cipher files
from vigenereCipher import *
from transpositionCipher import *
from beaufortCipher import *
from reverseCipher import *
from functions import *
import os

n = 0

def decrypt(key_1, mode_1, working_file):
    # Open the file and get the contents
    with open(working_file, 'r') as file:
        msg = file.read()

    # This gives us our alternate key and changes the mode
    key_2 = reverse(key_1)
    mode_2 = switchMode(mode_1)

    for i in range(len(key_1)):
        # Implement the ciphers
        first_cipher = vigenereCipher(msg, key_2, mode_1)

        second_cipher = transpositionCipher(first_cipher, key_2, mode_2)

        third_cipher = beaufortCipher(second_cipher, key_1, mode_1)

        # Write the encrypted data back to the file
        with open(working_file, 'w') as file:
            file.write(third_cipher)

        n = i + 1

    # Remove the .encrypted extension
    os.rename(working_file, working_file[:-10])

    # Tell the user about each file that has been decrypted
    print('File ' + working_file + ' has been decrypted ' + str(n) + ' times')