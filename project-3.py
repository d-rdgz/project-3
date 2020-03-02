##Dylan Rodriguez
## TCMG 412
## Project 3 -- Python Stuff
## This uses Python 3

import urllib.request
import os.path 
from os	import path
import re
from collections import Counter

url = "https://s3.amazonaws.com/tcmg476/http_access_log"

#Regular expression used to parse the log file -- breaks the line into groups 
regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

print("Checking to see if log already exists:")

if  not path.exists('log'):
	print("Log did not exist, downloading from: ")
	print(url)
	urllib.request.urlretrieve(url, 'log')
	print("Done downloading")
else:
	print("Log existed, skipping download.\n")

file = open('log', 'r')

logfile =[]

#array to hold 
broken_line =[]

#Loop through the file, place each line into logfile array
for line in file:
    logfile.append(line)

code_4xx = 0
code_3xx = 0
file_requests = []

#Loop throough logfile array, break each line using regex
for element in logfile:
	pieces = re.split(regex, element)
	#Look at the 3rd item in pieces, add that item to file_requests array
	try:
		file_requests.append(pieces[4])
		if pieces[6].startswith('3'):
			code_3xx+=1
		if pieces[6].startswith('4'):
			code_4xx+=1
	except IndexError:
		pass
	continue

total_count = 0
for item in logfile:
    total_count+=1


print("***** Total 4xx respones *****")
print(code_4xx)
percent_4xx = (code_4xx/total_count) * 100
print(round(percent_4xx,2))
print("***** Total 4xx respones *****\n")

print("***** Total 3xx respones *****")
print(code_3xx)
percent_3xx = (code_3xx / total_count) * 100
print(round(percent_3xx,2))
print("***** Total 3xx respones *****")

#Count most requested file 
Counter = Counter(file_requests)
most_freq = Counter.most_common(1)
print(most_freq)


#print(pieces)
#print(file_requests)

##Total Count
total_count = 0
for item in logfile:
    total_count+=1

print("Total line count= \n") 
print(total_count)

##Calculate percentages of 3xx codes  -- ROUND to 2 decimals


##Calculate percentages of 4xx codes -- ROUND to 2 decimals






##Count per day - week - month


##Percentage not successful -- 4xx codes


##Percentage redirected else -- 3xx codes


##Most requested file


##Least requested file




