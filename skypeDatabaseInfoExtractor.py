import sqlite3
import os
import optparse

def printProfile(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM accounts;")
    for row in c:
        print "[*] -- Found Account --"
        print "[+] User: " + str(row[0])
        print "[+] Skype Username: " + str(row[1])
        print "[+] Location: " + str(row[2]) + ", " + str(row[3])
        print "[+] Profile Date: " + str(row[4])

def printContacts(skypeDB):
    conn = sqlite3.conntect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;")
    for row in c:
        print "[*] -- Found Contacts --"
        print "[+] User: " + str(row[0])
        print "[+] Skype Username: " + str(row[1])
        if str(row[2]) != "" and str(row[2]) != "None":
            print "[+] Location: " + str(row[2]) + ", " + str(row[3])
        if str(row[4]) != "None":
            print "[+] Mobile Number: " + str(row[4])
        if str(row[5]) != "None":
            print "[+] Birthday: " + str(row[5])

def printCallLog(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(begin_timestamp, 'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    for row in c:
        print "\n[*] -- Found Calls --"
        print "[+] Time: " + str(row[0]) + "| " + str(row[1])

def printMessages(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(timestamp, 'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
    print "\n-- Found Messages --"
    print "[*] Messages Output at: " + os.getcwd() + "/output.txt"

    # If the output file already exists then overwrite everything in it and make it blank
    if os.path.isfile(os.getcwd() + "/output.txt"):
        with open(os.getcwd() + "/output.txt", "w") as blankFile:
            blankFile.write("")

    for row in c:
         try:
             if "partlist" not in str(row[3]):
                 if str(row[1]) != str(row[2]):
                     msgDirection = "To: " + str(row[1]) + ": "
             else:
                 msgDirection = "From: " + str(row[2]) + ": "

             with open(os.getcwd() + "/output.txt", "a") as outputMessages:
                 outputMessages.write( "Time: " + str(row[0]) + " " + msgDirection + str(row[3]) + "\n")
         except:
             pass

def main():
    parser = optparse.OptionParser("usage%prog -d <target database>")
    parser.add_option("-d", dest = "skypeDB", type = "string", help = "Specify a target Skype database")
    (options, args) = parser.parse_args()
    skypeDB = options.skypeDB

    if skypeDB == None:
        print parser.usage
    elif os.path.isfile(skypeDB) == False:
        print "[!] Skype Database does not exist: " + skypeDB
    else:
        printProfile(skypeDB)
        printCallLog(skypeDB)
        printMessages(skypeDB)

if __name__ == "__main__":
    main()
