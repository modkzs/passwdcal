#!/usr/bin/python

import os
import time
import hashlib
import argparse

def getMD5(str):
	m = hashlib.md5()  
	m.update(str)
	passwd =  m.hexdigest()
	return passwd 
	

parser = argparse.ArgumentParser(description='Calculate passwd according to username and applications or website')

parser.add_argument('-u', metavar = "string", help = "username")
parser.add_argument('-a', metavar = "string", help = "application name")
parser.add_argument('-l', metavar = "int", type=int, help = "password length", default=10)

user = parser.parse_args().u
app = parser.parse_args().a
length = parser.parse_args().l
print(getMD5(user + "-" + app).title()[:parser.parse_args().l])
