#!/usr/bin/env python3
import ecdsa

def main():
    pass

if __name__ == '__main__':
    main()

'''
The way that VerifyingKey works is that it will actually hash the message before it verifies. The default hashing algorithm is sha1, so you will need to specify it to be sha256 as that is what Bitcoin uses. Furthermore, you are passing it the fully hashed message. What you need to do is pass it the step before hashing the message. Since Bitcoin uses SHA256 double, you need to give it the result of the first SHA256 hash and let it generate the second SHA256 hash by itself.

'''
