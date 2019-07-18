#!/usr/bin/env python3

from bitcoin import Bitcoin

def verify_p2pkh():
    """
    Unlocking P2PKH script
    """
    b = Bitcoin(True)
    # From the Redeemer
    sig = input("Input sig: ")
    pubkey = input("Input pubkey: ")
    b.push(sig)
    b.push(pubkey)

    # Unlocking Script
    locking_script = input("Enter locking script:")
    for word in locking_script.split():
        if word[:2] == "OP":
            b.interpreter(word)()
        else:
            print("pushing {}".format(word))
            b.push(word)

def main():
    verify_p2pkh()

if __name__ == '__main__':
    main()
