from product_cipher import *
from base import *


# Function that runs the core program
def main():

	# Get the key and mode from the user
	key = input('Input the key: ')
	mode = input('Select "encrypt" or "decrypt": ')

	# Specify the root directory and get a list of files
	path = "danger_zone/"
	files = listFiles(path)

	# Open each file one by one and encrypt or decrypt
	for i in range(len(files)):
		working_file = files[i]

		if mode == 'encrypt':
			encrypt(key, mode, working_file)
		elif mode == 'decrypt':
			decrypt(key, mode, working_file)

main()