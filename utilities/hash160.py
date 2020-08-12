#!/usr/bin/env python3

import hashlib
import sys
import binascii

def hash160(preimage_bytes):
    '''hash input with sha256 followed by ripemd160'''
    return hashlib.new('ripemd160', hashlib.sha256(preimage_bytes).digest()).digest()

def hash160_string(preimage):
    return (hash160(preimage.encode('utf-8')))

def hash160_hexstring(hexstring):
    return (hash160(binascii.unhexlify(hexstring)))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        hexstring = input("Enter the hexstring to hash: ")
    else:
        hexstring = sys.argv[1]
    print(hash160_hexstring(hexstring).hex())
