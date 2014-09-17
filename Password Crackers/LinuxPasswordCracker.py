import crypt

def testPassSHA(cryptPass):
	# Open the dictonary we want to use in read mode.
	dictFile = open("dictonary.txt", "r")
	for word in dictFile.readlines():
		# Go through each line in the dictonary and remove new line characters
		word = word.strip("\n")
		# Set the salt equal to the first 12 characters of the password
		salt = cryptPass[:12]
		# Encrypt each word in the dictonary with the same salt from the actual password we're cracking
		cryptWord = crypt.crypt(word, salt)
		# Compare the word from the dictonary we just encrypted with the password we want to crack, if it's the same then we've found the password!
		if (cryptWord == cryptPass):
			# Print the password to screen if we've found it
			print "[+] Found Password: " + word + "\n"
			return 1
		
	print "[-] Password Not Found.\n"
	return 0

def main():
	# Open the list of passwords we want to crack
	passFile = open("passwords.txt", "r")
	for line in passFile.readlines():
		if ":" in line:
			# If there are ":" in the password then split the line and display the text before the ":" as the user name
			user = line.split(":")[0]
			# Remove ":" and blank spaces from the password
			cryptPass = line.split(":")[1].strip(" ")
			print "[*] Cracking Password For: " +user
			testPassSHA(cryptPass)

if __name__ == "__main__":
	main()
