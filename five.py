#!/usr/bin/python

import sys
import re

temp = []
delete = 0
fileName = sys.argv[1]
keyWords = sys.argv[2:]
with open(fileName, 'r') as inputFile:
	for line in inputFile:
		for word in keyWords:
			if word in line:
				delete = 1
		if delete == 0:
			temp.append(line)
		delete = 0
inputFile.close()
with open(fileName, 'w') as outputFile: 
	for x in temp:
		outputFile.write(x)
outputFile.close()
