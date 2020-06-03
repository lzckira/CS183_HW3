#!/usr/bin/python

import sys
import re
from collections import Counter
mailFrom = []
mailTo = []
temp = ""
fileName = sys.argv[1]
with open(fileName, 'r') as inputFile:
	for line in inputFile:
		if (re.search('from=<(\w+[.|\w]*@(\w+[.])*(\w)*)>',line)):
			temp = re.search('from=<(\w+[.|\w]*@(\w+[.])*(\w)*)>',line)
			mailFrom.append(temp.group(0))
		if (re.search('to=<(\w+[.|\w]*@(\w+[.])*(\w)*)>',line)):
			temp = re.search('to=<(\w+[.|\w]*@(\w+[.])*(\w)*)>',line)
			mailTo.append(temp.group(0))
	
	print Counter(mailFrom).most_common(5)[0][0].replace("from=<", "From ").replace(">","") + " " + str(Counter(mailFrom).most_common(5)[0][1])
	print Counter(mailFrom).most_common(5)[1][0].replace("from=<", "From ").replace(">","") + " " + str(Counter(mailFrom).most_common(5)[1][1])
	print Counter(mailFrom).most_common(5)[2][0].replace("from=<", "From ").replace(">","") + " " + str(Counter(mailFrom).most_common(5)[2][1])
	print Counter(mailFrom).most_common(5)[3][0].replace("from=<", "From ").replace(">","") + " " + str(Counter(mailFrom).most_common(5)[3][1])
	print Counter(mailFrom).most_common(5)[4][0].replace("from=<", "From ").replace(">","") + " " + str(Counter(mailFrom).most_common(5)[4][1])
	print Counter(mailTo).most_common(5)[0][0].replace("to=<", "To ").replace(">","") + " " + str(Counter(mailTo).most_common(5)[0][1])
	print Counter(mailTo).most_common(5)[1][0].replace("to=<", "To ").replace(">","") + " " + str(Counter(mailTo).most_common(5)[1][1])
	print Counter(mailTo).most_common(5)[2][0].replace("to=<", "To ").replace(">","") + " " + str(Counter(mailTo).most_common(5)[2][1])
	print Counter(mailTo).most_common(5)[3][0].replace("to=<", "To ").replace(">","") + " " + str(Counter(mailTo).most_common(5)[3][1])
	print Counter(mailTo).most_common(5)[4][0].replace("to=<", "To ").replace(">","") + " " + str(Counter(mailTo).most_common(5)[4][1])

inputFile.close()
