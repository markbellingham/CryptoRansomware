from product_cipher import *
from functions import *
import os


# Main controller that gets input from the user and a list of files
# and sends them off to be encrypted or decrypted
def main():

    # Get the key and mode from the user
    key = createKey()
    mode = input('Select "encrypt" or "decrypt": ')

    # Specify the root directory and get a list of files
    path = "target_folder/"

    # List of the filetypes that are supported by the program
    ext = ('.txt', '.xhtml', '.html', '.htm', '.css', '.php', '.sql',
           '.java', '.jsp', '.js', '.xml', '.xsl', '.xsd', '.xslt', '.xlog',
           '.json', '.py', '.rtf', '.srt', '.sub', '.csv', '.conf', '.log',
           '.manifest', '.lrc', '.html5', '.linux', '.sha1', '.sha512',
           '.err', '.readme', '.man')

    # Search the filesystem. For each file found, check if the extension is
    # on the supported list. If it is, create a full filename including
    # the path and pass it to either encrypt or decrypt depending on the mode
    for root, subdir, files in os.walk(path):
        for filename in files:
            if filename.endswith(tuple(ext)):
                filename = os.path.join(root, filename)
                if mode == 'encrypt':
                    encrypt(key, mode, filename)
                elif mode == 'decrypt':
                    decrypt(key, mode, filename)



main()
