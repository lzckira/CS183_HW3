#!/usr/bin/python

import re
from collections import Counter
mailFrom = []
mailTo = []
ip = []
rejected = 0
temp = ""
fileName = "log4"
with open(fileName, 'r') as inputFile:
	for line in inputFile:
		if (re.search('dnsbl.sorbs.net',line)):
			rejected += 1
			if (re.search('from=<(\w+[.|\w]*@(\w+[.])*(\w)*)>',line)):
				temp = re.search('from=<(\w+[.|\w]*@(\w+[.])*(\w)*)>',line)
				mailFrom.append(temp.group(0))
			if (re.search('to=<(\w+[.|\w]*@(\w+[.])*(\w)*)>',line)):
				temp = re.search('to=<(\w+[.|\w]*@(\w+[.])*(\w)*)>',line)
				mailTo.append(temp.group(0))
			if (re.search('((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))',line)):
				temp = (re.search('((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))',line))
				ip.append(temp.group(0))
	print (str(rejected) + " messages rejected")
	print (str(len(Counter(ip).most_common())) + " unique IP's")
	print (str(len(Counter(mailFrom).most_common())) + " unique from addresses")
	print (str(len(Counter(mailTo).most_common())) + " unique to address")

inputFile.close()
