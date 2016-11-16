# Import cipher files
from vigenereCipher import *
from transpositionCipher import *
from portaCipher import *
from reverseCipher import reverse
from base import switchMode
from glob import glob
from os.path import join
from os import rename



# Function that runs the core program
def main():

	# Get the key and mode from the user
	key_1 = input('Input the key: ')
	mode_1 = input('Select "encrypt" or "decrypt": ')

	# This gives us our alternate key and changes the mode
	key_2 = reverse(key_1)
	mode_2 = switchMode(mode_1)


	# This is a list of all the file types that are supported
	# The program will ignore all other file types
	ext = ('*.txt','*.xhtml','*.html','*.htm','*.css','*.php','*.sql',
		'*.java','*.jsp','*.xml','*.xsl','*.xsd','*.xslt','*.xlog',
		'*.json','py','*.rtf','*.srt','*.sub','*.csv','*.conf','*.log',
		'*.manifest','*.lrc','*.html5','*.linux','*.sha1','*.sha512',
		'*.err','*.readme','*.man')

	# Put the file names into an array
	files = []
	for e in (ext):
		files.extend(glob(join("danger_zone/", e)))


	# Open each file one by one and encrypt or decrypt
	for i in range(len(files)):
		working_file = files[i]
		with open(working_file, 'r') as file:
			msg = file.read()


		if mode_1 == 'encrypt':
			# Implement the ciphers
			first_cipher = portaCipher(msg, key_1, mode_1)

			second_cipher = transpositionCipher(first_cipher, key_2, mode_2)

			third_cipher = vigenereCipher(second_cipher, key_2, mode_1)

			# Write the encrypted data back to the file
			with open(working_file, 'w') as file:
				file.write(third_cipher)

			# Tell the user about each file that has been encrypted
			print('File %s has been encrypted' % working_file)


		elif mode_1 == 'decrypt':
			# Implement the ciphers
			first_cipher = vigenereCipher(msg, key_2, mode_1)

			second_cipher = transpositionCipher(first_cipher, key_2, mode_2)

			third_cipher = portaCipher(second_cipher, key_1, mode_1)

			# Write the encrypted data back to the file
			with open(working_file, 'w') as file:
				file.write(third_cipher)

			# Tell the user about each file that has been decrypted
			print('File %s has been decrypted' % working_file)


main()