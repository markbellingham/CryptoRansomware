from product_cipher import *
import os
# from base import listFiles


# Main controller that gets input from the user and a list of files 
# and sends them off to be encrypted or decrypted
def main():

	# Get the key and mode from the user
	key = input('Input the key: ')
	mode = input('Select "encrypt" or "decrypt": ')

	# Specify the root directory and get a list of files
	path = "target_folder/"

	ext = ('.txt','.xhtml','.html','.htm','.css','.php','.sql',
        '.java','.jsp','.js','.xml','.xsl','.xsd','.xslt','.xlog',
        '.json','.py','.rtf','.srt','.sub','.csv','.conf','.log',
        '.manifest','.lrc','.html5','.linux','.sha1','.sha512',
        '.err','.readme','.man')

	# Open each file one by one and encrypt or decrypt
	for root, subdir, files in os.walk(path):
		for filename in files:
		    if filename.endswith(tuple(ext)):
		        if mode == 'encrypt':
		            encrypt(key, mode, os.path.join(root, filename))
		        elif mode == 'decrypt':
		            decrypt(key, mode, os.path.join(root, filename))

main()