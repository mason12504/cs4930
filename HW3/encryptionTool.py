# Mason Andersen
# I did use ChatGPT to find docs on this exact problem, but the code is from the examples on
# https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
# https://cryptography.io/en/latest/hazmat/primitives/padding/

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# get some random data for the key and iv to encrypt with
key = os.urandom(32) # 32 bytes, 256 bit key for AES256
iv = os.urandom(16)  # IV is 128 bit


def main():
    inputMsg = "a secret message 12345"
    print("input message: ", inputMsg)
    ciphertext = encryptAES256CBC(inputMsg, key, iv)
    print("encrypted version: ", ciphertext)
    decPlain = decryptAES256CBC(ciphertext, key, iv)
    print("decryption of the ciphertext: ", decPlain)

def encryptAES256CBC(pt, key, iv):

    # set up the AES 256 CBC cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    # pad before giving to encryption function so we're within block size
    padder = padding.PKCS7(128).padder()
    ptBytes = pt.encode('utf-8')
    paddedInput = padder.update(ptBytes)
    paddedInput += padder.finalize()
    # convert the message to bytecode to be encrypted
    ct = encryptor.update(paddedInput) + encryptor.finalize()
    return ct

# decrypt a file with AES256CBC
# param ct the ciphertext to decrypt
# key the symmetric key
# iv the initialization vector
def decryptAES256CBC(ct, key, iv):

    # set up cipher for decryption given our key and iv
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    # decrypt the message
    decPlain = decryptor.update(ct) + decryptor.finalize()

    # unpad the message
    # pad before giving to encryption function so we're within block size
    unpadder = padding.PKCS7(128).unpadder()
    unPaddedOut = unpadder.update(decPlain) # atp decPlain still has all the padding so we feed that in
    unPaddedOut += unpadder.finalize() # remove the padding

    # return the final output
    return unPaddedOut.decode('utf-8') # when we decrypt it ends up in bytes so decode it into plain string format

main()