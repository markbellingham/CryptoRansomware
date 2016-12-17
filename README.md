# CryptoRansomware
Year 3 Information Security Assignment

***

This program is potentially dangerous and could render the operating system  on your computer unusable. Caution is advised and I am not responsible for any problems that may occur. If in doubt, use the program inside a virtual machine.

***

Usage: From the terminal type:

"python3 main_program.py -e" or "python3 main_program.py --encrypt" to encrypt

"python3 main_program.py -d" or "python3 main_program.py --decrypt" to decrypt

The current target is a test directory. The program can be set to encrypt the user's {home} by switching the comments on lines 43 and 45 in the file 'main_program.py'.

Program to emulate a RansomWare style program using 3 of the classic text encryption algorithms in a product cipher, that encrypts the files on the hard disk and presents a ransom note asking for money to decrypt them. Decryption method is also included. 

The program will encrypt a variety of text-based files such as *.java, *.html, *.csv etc. It will ignore those files which it cannot encrypt such as binary files. A selection of files is included with the program for testing purposes. These are the files that will be encrypted if the path (in main_program.py) is not changed. Each file that is encrypted is renamed to add the .encrypted extension. For each directory that contains encrypted files, another file is added called hacked.htm which contains instructions to the victim on how to get their files back. The program also launches the browser to display hacked.htm. Information about which files have been encrypted is displayed in the terminal output. If the initial command to start the program is given the wrong options, a message is shown indicating correct usage.

When decrypting, the program outputs to the terminal information about each file that is being decrypted. It will decrypt all supported files, restoring them to their original state. If the decrypt function is used on unencrypted files, you can use the encrypt function to restore their contents but the filenames will be different. Decrypted files have the .encrypted extension removed. The hacked.htm file is removed from all directories where it is present. 

The program will work without either product_cipher_encrypt.py or product_cipher_decrypt.py present provided the correct option is given for the file that is present. If decrypt is selected but the decrypt module is not present, the program will display hacked.htm in the browser and quit.

While encrypting, the program generates a log containing a list of all the filenames of encrypted files. While decrypting, the filenames are removed from the log. In this way the program could potentially survive a system restart.


Program source code:

https://github.com/markbellingham/CryptoRansomware
