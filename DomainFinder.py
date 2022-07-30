import subprocess
import random

whois = "whois/whois.exe"
grep = "grep/grep.exe"
filename = "words/english3.txt"

lines = []

with open(filename) as file:
	lines = file.readlines()
	lines = [line.rstrip() for line in lines]

random.shuffle(lines)

for line in lines:
	if len(line) < 5:
		continue

	domain = f"{line}.com"
	command = f"whois {domain} | grep 'This query returned 0 objects'"
	whois_output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 

	if whois_output.returncode == 0:
		print(f"Domain {domain} does not exist")
	else:
    		print(f"Domain {domain} exists") 