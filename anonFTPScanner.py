import ftplib
def anonLogin(hostname):
	try:
		ftp.ftplib.FTP(hostname)
		ftp.login("anonymous","someone@domain.com")
		print "\n[*] " + str(hostname) + " FTP Anonymous Logon Succeeded."
		ftp.quit()
		return True
	except Exception, e:
		print "\n[-] " + str(hostname) + " FTP Anonymous Logon Failed."
		return False
host = "192.168.1.4"
anonLogin(host)
