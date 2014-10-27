
#! encoding=utf-8

# Author        : kesalin@gmail.com
# Blog          : http://kesalin.github.io
# Date          : 2014/10/27
# Description   : Encrypt/decrypt data. 
# PyCrypto      : 2.6
# Python        : 2.7.3
#

import hashlib
import base64
import sys
from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex, a2b_hex

def md5(str):
    return hashlib.md5(str).hexdigest()

def sha1(str):
    return hashlib.sha1(str).hexdigest();

class AESCipher:
    def __init__(self, key):
        self.bs = 32
        if len(key) >= 32:
            self.key = key[:32]
        else:
            self.key = self._pad(key)

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        result = base64.b64encode(iv + cipher.encrypt(raw))
        return b2a_hex(result)

    def decrypt(self, raw):
        enc = base64.b64decode(a2b_hex(raw))
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

def encryptData(key, str):
    aes = AESCipher(md5(key))
    result = aes.encrypt(str)
    return result

def decryptData(key, str):
    aes = AESCipher(md5(key))
    result = aes.decrypt(str)
    return result

if __name__ == '__main__':
    key = '0123456789abcdef'
    data = "test"
    en = encryptData(key, data)
    de = decryptData(key, en)
    print " >>> data:", data
    print " >>> encrypt:", en
    print " >>> decrypt:", de
