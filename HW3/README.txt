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

Dependencies: python 3.12 and crytography library
`pip install cryptography`
To run the program:
Ensure that alice.txt is in the same directory, then run the program and type:
`demo` to show the encryption/decryption of a file.
Alternatively you can use the input loop to encrypt a file with "e" providing the filename,
or decrypt a file with "d" to decrypt a file

All files are in the main directory, alice.txt is the sample plaintext to encrypt, and files
alice_ct.enc and alice2.txt will be created as the encryption and re-decryption respectively.

HW3sample.pdf is another test file you can encrypt and decrypt with "e" or "d" in the input loop
It contains some text and an image that successfully encrypts and decrypts with the program.
PROBLEM DESCRIPTION AND REMEDIATION:
====================================

I initially started in C and switched to python as I'm more familiar with it, and it is generally easier.
The docs for a python OpenSSL encryption tool were fairly easy to understand, but I did have some
encoding issues when trying to read the file again, so I had to work around that initially. Overall though,
There weren't any significant issues with implementing this in python.