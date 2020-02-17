##Dylan Rodriguez
## TCMG 412
## Project 3 -- Python Stuff
## This uses Python 3

import urllib.request
import os.path 
from os	import path

url = "https://s3.amazonaws.com/tcmg476/http_access_log"

print("Checking to see if log already exists:")

if  not path.exists('log'):
	print("Log did not exist, downloading from: ")
	print(url)
	urllib.request.urlretrieve(url, 'log')
else:
	print("Log existed, skipping download.")

file = open('log', 'r')









