#!/usr/bin/env python3
import base58
from hashlib import sha256

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) <= 0:
            print("Empty stack")
            return False
        else:
            return self.stack.pop()

    def is_empty(self):
        if len(self.stack):
            return False
        return True

class Bitcoin(Stack):
    def __init__(self):
        Stack.__init__(self)

    def check_sig(sig, pubkey):
        return False

    def dup(self):
        a = self.stack.pop()
        self.push(a)
        self.push(a)

    def hash(self):
        v = self.pop().encode('utf-8')
        self.push(sha256(v).digest().hex())

    def equal_verify(self):
        a = self.pop()
        b = self.pop()
        if a == b:
            self.push(1)
        else:
            self.push(0)

    def checksig(self):
        a = self.pop()
        b = self.pop()
        if self.is_empty():
            print("Empty stack.")
        else:
            print("Not empty!")

def main():
    """
    Unlocking P2PKH script
    """
    b = Bitcoin()
    sig = input("Input sig: ")
    pubkey = input("Input pubkey: ")
    b.push(sig)
    b.push(pubkey)
    b.dup()                             # OP_DUP
    b.hash()                            # HASH_160
    pubkeyhash = input("Input PubKHash:")
    b.push(pubkeyhash)
    b.equal_verify()                    # EQUALVERIFY
    if (b.pop()):
        print("hashes verified")
        b.checksig()                    # CHECKSIG
    else:
        print("not verified.")
#    print(b.pop().digest().hex())

if __name__ == '__main__':
    main()
