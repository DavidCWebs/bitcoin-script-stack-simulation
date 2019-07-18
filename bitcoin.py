#!/usr/bin/env python3
import base58
from hashlib import sha256
from utilities.hash160 import hash160_hexstring

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

    def print_stack(self, label):
        print("---")
        print("after running {}".format(label))
        for el in self.stack:
            print(el)
        print("---\n")

class Bitcoin(Stack):
    def __init__(self, display=False):
        Stack.__init__(self)
        self.display=display

    def check_sig(sig, pubkey):
        return False

    def op_dup(self):
        a = self.stack.pop()
        self.push(a)
        self.push(a)
        if self.display: self.print_stack("OP_DUP")

    def op_hash160(self):
        v = self.pop()
        self.push(hash160_hexstring(v).hex())
        if self.display: self.print_stack("OP_HASH160")

    def op_equalverify(self):
        a = self.pop()
        b = self.pop()
        if a == b:
            r = True
        else:
            r = False
        if self.display: self.print_stack("OP_EQUALVERIFY")
        return r

    def op_checksig(self):
        a = self.pop()
        b = self.pop()
        if self.is_empty():
            print("Empty stack.")
        else:
            print("Not empty!")
        if self.display: self.print_stack("OP_CHECKSIG")

    def interpreter(self, func):
        '''Returns a bound method based on the received opcode'''
        switcher = {
                "OP_DUP": self.op_dup,
                "OP_HASH160": self.op_hash160,
                "OP_EQUALVERIFY": self.op_equalverify,
                "OP_CHECKSIG": self.op_checksig
                }
        return switcher.get(func, lambda: "Invalid opcode")
