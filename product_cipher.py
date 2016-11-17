# Import cipher files
from vigenereCipher import *
from transpositionCipher import *
from portaCipher import *
from reverseCipher import reverse
from base import *
from os import rename



def encrypt(msg, key_1, mode_1, working_file):
	# Implement the ciphers
	first_cipher = portaCipher(msg, key_1, mode_1)

	# This gives us our alternate key and changes the mode
	key_2 = reverse(key_1)
	mode_2 = switchMode(mode_1)

	second_cipher = transpositionCipher(first_cipher, key_2, mode_2)

	third_cipher = vigenereCipher(second_cipher, key_2, mode_1)

	# Write the encrypted data back to the file
	with open(working_file, 'w') as file:
		file.write(third_cipher)

	# Tell the user about each file that has been encrypted
	print('File %s has been encrypted' % working_file)



def decrypt(msg, key_1, mode_1, working_file):
	# This gives us our alternate key and changes the mode
	key_2 = reverse(key_1)
	mode_2 = switchMode(mode_1)

	# Implement the ciphers
	first_cipher = vigenereCipher(msg, key_2, mode_1)

	second_cipher = transpositionCipher(first_cipher, key_2, mode_2)

	third_cipher = portaCipher(second_cipher, key_1, mode_1)

	# Write the encrypted data back to the file
	with open(working_file, 'w') as file:
		file.write(third_cipher)

	# Tell the user about each file that has been decrypted
	print('File %s has been decrypted' % working_file)
