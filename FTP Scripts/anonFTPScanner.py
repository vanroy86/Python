import optparse
import ftplib
def anonLogin(hostname, email):
	try:
		ftp.ftplib.FTP(hostname)
		ftp.login("anonymous",email)
		print "\n[*] " + str(hostname) + " FTP Anonymous Logon Succeeded."
		ftp.quit()
		return True
	except Exception, e:
		print "\n[-] " + str(hostname) + " FTP Anonymous Logon Failed."
		return False
def main():
	parser = optparse.OptionParser("Usage: " + "-H <Target Host> -E <Specify an Email Address>")
	parser.add_option("-H", dest = "host", type = "string", help = "Specify a Target Host")
	parser.add_option("-E", dest = "emailAddress", type = "string", help = "Specify an Email Address")
	(options, args)  = parser.parse_args()

	if (options.host == None or options.emailAddress == None):
		print parser.usage
		exit(0)
	else:
		host = options.host
		emailAddress = options.emailAddress
	anonLogin(host, emailAddress)
if __name__ == "__main__":
	main()
