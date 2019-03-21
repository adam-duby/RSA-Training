#!/usr/bin/python3

from Crypto.PublicKey import RSA

f = open('public.pem','r')
key = RSA.importKey(f.read())
print(key.n)
print(key.e)