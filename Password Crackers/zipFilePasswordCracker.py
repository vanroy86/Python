import zipfile
from threading import Thread
import optparse

def extractFile(zFile, password):
	try:	
		# Extract the zip file using the password
		zFile.extractall(pwd=password)
		# If the zip file is extracted then we found the right password so we print it to the screen
		print "[+] Found password: " + password + "\n"
	except:
		# If an exception is thrown don't do anything, just continue with looking for the right password
		pass
def main():
	# Give the parser some options
	parser = optparse.OptionParser("Usage is: "+ "-f <zipfile> -d <dictonary>")
	parser.add_option("-f", dest="zName", type="string", help = "specify zip file")
	parser.add_option("-d", dest="dName", type="string", help = "specify a dictonary file")
	
	# Pass the options and arguments to the parser	
	(options, args) = parser.parse_args()
	
	# If there aren't any arguments given then print the useage and exit
	if (options.zName == None) | (options.dName == None):
		print parser.usage
		exit(0)
	else:
		# Set some variables to the arguments given from the parser
		zName = options.zName
		dName = options.dName 
	
	# Set the zip file to the one given in the argument
	zFile = zipfile.ZipFile(zName)
	# Open the file where the passwords are stored
	passFile = open(dName)
	
	# For each line in the password file strip away the new line breaks and use that word to try and extract the zip file
	for line in passFile.readlines():
		password = line.strip("\n")
		# Declare a Thread and use it on the extractFile Function. Give the Thread the zipFile and password arguments to pass to the Fuction
		# Using a Thread will allow for faster cracking of the password
		t = Thread(target=extractFile, args=(zFile, password))
		t.start()
		
if __name__ == "__main__":
	main()
