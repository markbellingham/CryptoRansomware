# Import cipher files
from vigenereCipher import *
from transpositionCipher import *
from beaufortCipher import *
from reverseCipher import *
from functions import *
import os

n = 0


def encrypt(key_1, mode_1, working_file):
    # Open the file and get the contents
    with open(working_file, 'r') as file:
        msg = file.read()

    # This gives us our alternate key and changes the mode
    key_2 = reverse(key_1)
    mode_2 = switchMode(mode_1)

    # Number of times the files are encrypted is set by the length of the key
    for i in range(len(key_1)):
        # Implement the ciphers
        first_cipher = beaufortCipher(msg, key_1, mode_1)

        second_cipher = transpositionCipher(first_cipher, key_2, mode_2)

        third_cipher = vigenereCipher(second_cipher, key_2, mode_1)

        # Write the encrypted data back to the file
        with open(working_file, 'w') as file:
            file.write(third_cipher)

        n = i + 1

    # Rename the file with a .encrypted extension
    os.rename(working_file, working_file + '.encrypted')

    # Tell the user about each file that has been encrypted
    print('File ' + working_file + ' has been encrypted ' + str(n) + ' times')
