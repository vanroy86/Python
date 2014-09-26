import pyPdf
from pyPdf import PdfFileReader
from threading import Thread
import optparse

foundPass = False
def bruteForcePdf(fileName, passPhrase):
    global foundPass
    foundPass = False
    try:
        fileToCrack = PdfFileReader(file(fileName, "rb"))
        if fileToCrack.decrypt(passPhrase):
             foundPass = True
             print "[+] Found pasword: " + passPhrase + "\n"
    except:
        foundPass = False
        print "[-] Password not found"
        pass

def main():
    parser = optparse.OptionParser("Usage: -f -l")
    parser.add_option("-f", dest = "fileName", type = "string", help = "-f <Specify a PDF file to crack>")
    parser.add_option("-l", dest = "passList", type = "string", help = "-l <Specify a password list>")

    (options, args) = parser.parse_args()

    if (options.fileName == None) | (options.passList == None):
        print parser.usage
        exit(0)
    else:
        fileName = options.fileName
        passList = options.passList

    password = open(passList)
    for line in password.readlines():
        if foundPass == False:
            passPhrase = line.strip("\n")
            t = Thread(target = bruteForcePdf, args = (fileName, passPhrase))
            t.start()
        else:
            print "[*] Password already found"

if __name__ == "__main__":
    main()
