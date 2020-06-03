#!/usr/bin/python

import sys
import re

rejects = 0
amavis = 0
current = "00"
temp = []

if len(sys.argv) != 0:
	fileName = sys.argv[1]
	with open(fileName, 'r') as inputFile:
		outputFile = open("hourlyInfo", 'w')
		for line in inputFile:
			temp = re.split(':',line)
			if len(temp) > 1:
				if temp[1] != current:
					outputFile.write(temp[0] + ":" + temp[1] + "  [postfix rejects:" + str(rejects) + "]  [amavis quarantines:" + str(amavis) + "]\n")
					rejects = 0
					amavis = 0
					current = temp[1]
				else:
					if "postfix" in line and "reject" in line:
						rejects += 1
					if "" in line and "quarantine" in line:
						amavis += 1
		outputFile.close()
	inputFile.close()
