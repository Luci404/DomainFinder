import subprocess
import random
import socket

whois = "whois/whois.exe"
grep = "grep/grep.exe"
filename = "words/english3.txt"

lines = []

with open(filename) as file:
	lines = file.readlines()
	lines = [line.rstrip() for line in lines]

random.shuffle(lines)

for line in lines:
	if len(line) < 5 or len(line) > 8:
		continue

	domain = f"{line}.com"

	try:
		addr = socket.gethostbyname(domain)
	except:
		print(f"Domain {domain} does not exist")