#!/usr/bin/python

import re
from collections import Counter
known = []
unknown = []
temp = []
fileName = "log2"
with open(fileName, 'r') as inputFile:
	for line in inputFile:
		if (re.search(': connect from unknown',line) and re.search('unknown',line)):
			temp = re.split('n|\r',line)
			unknown.append(temp[-2])
		elif (re.search(': connect from ',line)):
			temp = re.split('\[|\r',line)
			known.append(temp[-2])
	print("Total Known connection: " + str(len(Counter(known))) + " - [" + Counter(known).most_common(1)[0][0] + " accounts for " + str(Counter(known).most_common(1)[0][1]) + " connections")
	print("Total Unknown connection: " + str(len(Counter(unknown))) + " - " + Counter(unknown).most_common(1)[0][0] + " accounts for " + str(Counter(unknown).most_common(1)[0][1]) + " connections")

inputFile.close()
