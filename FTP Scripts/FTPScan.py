import ftplib
import optparse
def returnDefault(ftp):
	# Try and issue the command to list directory contents
	try:
		dirList = ftp.nlst()
	except:
		dirList = []
		print "[-] Could not list directory contents"
		print "[-] Skipping To Next Target"
		return
	retList = []
	for fileName in dirList:
		fn = fileName.lower()
		if ".php" in fn or ".htm" in fn or ".asp" in fn:
			print "[+] Found Default Page: " + fileName
			retList.append(fileName)
def main():
	parser = optparse.OptionParser("Usage: " + "-H <Target Host> -U <Target User> -P <Target Password>")
	parser.add_option("-H", dest = "targetHost", type = "string", help = "Specify a Target Host")
	parser.add_option("-U", dest = "targetUser", type = "string", help = "Specify a Target User")
	parser.add_option("-P", dest = "targetPassword", type = "string", help = "Specify a Target Password")
	(options,args) = parser.parse_args()

	if (options.targetHost == None or options.targetUser == None or options.targetPassword == None):
		print parser.usage
	else:
		targetHost = options.targetHost
		targetUser = options.targetUser
		targetPassword = options.targetPassword

	ftp  = ftplib.FTP(targetHost)
	ftp.login(targetUser,targetPassword)
	returnDefault(ftp)
if __name__ == "__main__":
	main()
