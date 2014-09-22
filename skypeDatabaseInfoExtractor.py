import sqlite3

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

def main():
    skypeDB = "/path/to/database"
    printProfile(skypeDB)

if __name__ == "__main__":
    main()
