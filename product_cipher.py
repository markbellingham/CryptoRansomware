# Import cipher files
from vigenereCipher import *
from transpositionCipher import *
from portaCipher import *
from reverseCipher import reverse
from base import switchMode



# Function that runs the core program
def main():
	# Read text from file
	working_file = 'confirm_order.php'
	with open(working_file, 'r') as file:
		msg = file.read()

	# Get the key and mode from the user
	#print ('msg is: %s' % msg)
	key_1 = input('Input the key: ')
	mode_1 = input('Select "encrypt" or "decrypt": ')

	# This gives us our alternate key and changes the mode
	key_2 = reverse(key_1)
	mode_2 = switchMode(mode_1)


	if mode_1 == 'encrypt':
		# Implement the first algorithm
		first_cipher = portaCipher(msg, key_1, mode_1)
		#print ('Value of first_cipher is: %s' % first_cipher)

		# Implement the second algorithm
		second_cipher = transpositionCipher(first_cipher, key_2, mode_2)
		#print ('Value of second_cipher is: %s' % second_cipher)

		# Implement the third algorithm
		third_cipher = vigenereCipher(second_cipher, key_2, mode_1)
		#print ('Value of third_cipher is: %s' % third_cipher)

		# Write the encrypted data back to the file
		with open(working_file, 'w') as file:
			file.write(third_cipher)


	elif mode_1 == 'decrypt':
		# Implement the first algorithm
		first_cipher = vigenereCipher(msg, key_2, mode_1)
		#print ('Value of first_cipher is: %s' % first_cipher)

		# Implement the second algorithm
		second_cipher = transpositionCipher(first_cipher, key_2, mode_2)
		#print ('Value of second_cipher is: %s' % second_cipher)

		# Implement the third algorithm
		third_cipher = portaCipher(second_cipher, key_1, mode_1)
		#print ('Value of third_cipher is: %s' % third_cipher)

		# Write the encrypted data back to the file
		with open(working_file, 'w') as file:
			file.write(third_cipher)


main()