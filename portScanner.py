import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send("VioletPython\r\n")
		results = connSkt.recv(100)
		screenLock.acquire()
		print "[+]%d/tcp open " % tgtPort
		print "[+] " + str(results)
	except:
		screenLock.acquire()
		print "[-]%d/tcp closed"% tgtPort
	finally:
		screenLock.release()
		connSkt.close()
def portScan(tgtHost, tgtPort):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve  '%s': Unknown host"%tgtHost
		return

	try:
		tgtName = gethostbyaddr(tgtIP)
		print "\n[+] Scan Results for: " + tgtName

	except:
		print "\n[+] SCan Results for: " + tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target = connScan, args = (tgtHost, int(tgtPort)))
		t.start()
def main():
	parser = optparse.OptionParser("usage%prog " + "-H <target host> -p <target port>")
	parser.add_option("-H", dest = "tgtHost", type = "string", help = "Specify a target host")
	parser.add_option("-p", dest = "tgtPort", type = "string", help = "Specify a target port")
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPort = str(options.tgtPort).split(", ")
	if (tgtHost = None) | (tgtPort = None):
		print parser.usage
		exit(0)
	portScan(tgtHost, tgtPorts)
if __name__ == "__main__":
	main()
