import subprocess

whois = "whois/whois.exe"
grep = "grep/grep.exe"
filename = "words/english3.txt"

lines = []

with open(filename) as file:
	lines = file.readlines()
	lines = [line.rstrip() for line in lines]

for line in lines:
	domain = $"{line}.com"
	command = $"whois {domain} | grep 'This query returned 0 objects'"
	whois_output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 

	if whois_output.returncode == 0:
    		print($"Domain {domain} does not exist")
	else:
    		print($"Domain {domain} exists") 