# Reverse Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

def reverse(message):
	translated = ''

	i = len(message) - 1
	while i >= 0:
		translated = translated + message[i]
		i = i - 1

	return translated
