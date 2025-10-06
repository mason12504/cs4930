NAME OF PROJECT:
================
Homework 3 OpenSSL File Encrypt/Decrypt

NAME OF PROGRAMMER:
===================

Mason Andersen

STATEMENT:
==========
I have neither given nor received unauthorized assistance on this work.

SPECIAL INSTRUCTIONS:
=====================

Dependancies: python 3.12 and crytopgrahy library
`pip install cryptography`
To run the program:
Ensure that alice.txt is in the same directory, then run the program and type:
`demo` to show the encryption/decryption of a file.
Alternatively you can use the input loop to encrypt a file with "e" providing the filename,
or decrypt a file with "d" to decrypt a file
alice.txt is the file to encrypt, the encrypted file (alice_ct.enc) and the decrypted file (alice2.txt) will be created
automatically.

All files are in the main directory, alice.txt is the sample plaintext to encrypt, and files
alice_ct.enc and alice2.txt will be created as the encryption and re-decryption respectively.

PROBLEM DESCRIPTION AND REMEDIATION:
====================================

The docs for a python OpenSSL encryption tool were fairly easy to understand, but I did have some
encoding issues when trying to read the file again, so I had to work around that.