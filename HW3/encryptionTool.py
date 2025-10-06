# Mason Andersen
# I did use ChatGPT to find docs on this exact problem, but the code is based on the examples at
# https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
# https://cryptography.io/en/latest/hazmat/primitives/padding/

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# get some random data for the key and iv to encrypt with
key = os.urandom(32) # 32 bytes, 256 bit key for AES256
iv = os.urandom(16)  # IV is 128 bit


def main():

    inputLoop()
    #print("decryption of the ciphertext: ", decPlain)

# encrypt/decrypt multiple files, or run a basic test
#
def inputLoop():
    looping = True
    while(looping):
        print("Enter \"e\" to encrypt a file, \"d\" to decrypt a file, or type \"demo\" for an example with alice.txt")
        print("Press q at any time to exit")

        selection = input("")
        # have a quit option
        if (selection == 'q') or (selection == 'Q'):
            print("Exiting...")
            break
        elif selection == 'demo':
            # run it and show it works on a sample file
            encryptAES256CBC("alice.txt", "alice_ct.enc", key, iv)
            decryptAES256CBC("alice_ct.enc", "alice2.txt", key, iv)
            print("File encrypted and decrypted. ")
            print("Original file snippet: ")
            printFileSnippet("alice.txt")
            print("encrypted file snippet: ")
            printFileSnippet("alice_ct.enc")
            print("decryption of the encrypted file snippet: ")
            printFileSnippet("alice2.txt")

        elif selection == 'e':
            fileName = input("Enter the file to encrypt: ")
            raw, ext =  os.path.splitext(fileName)
            encryptAES256CBC(fileName, raw + "_ct.enc", key, iv)
            print("File", fileName, "Encrypted as: ", raw + "_ct.enc.")

        elif selection == 'd':
            fileName = input("Enter the file to decrypt: ")
            raw, ext =  os.path.splitext(fileName)
            ext = input("Enter the file extension for the decrypted output: ")
            decryptAES256CBC(fileName, raw+"2."+ext, key, iv)
            print("File", fileName, "Decrypted as: ", raw + "2."+ext)


# encrypt a file with AES256CBC
# param pt_path the plaintext file path to encrypt
# param ct_path the output ciphertext file path
# key the symmetric key
# iv the initialization vector
def encryptAES256CBC(pt_path, ct_path, key, iv):

    fileBytes = fileByteRead(pt_path)
    # set up the AES 256 CBC cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    # pad before giving to encryption function so we're within block size
    padder = padding.PKCS7(128).padder()
    paddedInput = padder.update(fileBytes)
    paddedInput += padder.finalize()
    ct = encryptor.update(paddedInput) + encryptor.finalize()

    # writes the file with the encrypted text format
    fileByteWrite(ct_path, ct)

def printFileSnippet(file_path):
    print(file_path)
    try:
        with open(file_path, 'rb') as inFile:
            for i in range(3):
                print(inFile.readline())
        inFile.close()
    except:
        "An error occured. Check your file name."

# decrypt a file with AES256CBC
# param ct_path the ciphertext file to decrypt
# param pt_path the plaintext file to put the decrypted message into
# key the symmetric key
# iv the initialization vector
def decryptAES256CBC(ct_path, pt_path, key, iv):

    # set up cipher for decryption given our key and iv
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    # decrypt the file
    fileBytes = fileByteRead(ct_path)
    decPlain = decryptor.update(fileBytes) + decryptor.finalize()

    # unpad the message
    # pad before giving to encryption function so we're within block size
    unpadder = padding.PKCS7(128).unpadder()
    unPaddedOut = unpadder.update(decPlain) # atp decPlain still has all the padding so we feed that in
    unPaddedOut += unpadder.finalize() # remove the padding

    # write the decrypted format back into the file
    fileByteWrite(pt_path, unPaddedOut)
    #print(unPaddedOut.decode('utf-8'))


# reads a file into bytes for encryption/decryption
# param file_path, path to the file
# returns the raw file data as bytes
def fileByteRead(file_path):
    try:
        with open(file_path, 'rb') as inFile:
            fileBytes = inFile.read()
    except:
        "An error occured. Check your file name."

    inFile.close()
    return fileBytes

# writes data to a file for output
# param file_path the file
# param data, the content to write
# returns nothing
def fileByteWrite(file_path, data):
    # make sure the file for writing valid
    try:
        with open(file_path, 'wb') as outFile:
            outFile.write(data)
    except:
        "An error occured. Check your file name."
    outFile.close()

# for writing decoded data back into a normal txt file
def fileTextWrite(file_path, data):
    # make sure the file for writing valid
    try:
        with open(file_path, 'w', encoding='utf-8') as outFile:
            outFile.write(data)
    except:
        "An error occured. Check your file name."
    outFile.close()

main()