import os,sys
import curses
import imaplib
import email

class snorkelMail(object):
	def __init__(self):
		self.screen = curses.initscr()


		if curses.has_colors():
			curses.start_color()

		# Set up colour pairs
		curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK) # colour pair number, foreground, background
		curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

	def parse_config_file(self, configFile):
		pass

	def read_mail(self, mailServer, username, password):
		# try to connect to the server
		imap = imaplib.IMAP4_SSL(mailServer)

		try:
			loggedin = imap.login(username, password) # Try to connect, if we can't then raise an error and exit
		except:
			print "There was an error connecting: %s" % sys.exc_info()[1]
			sys.exit(0)

		imap.select("INBOX") # Select the Inbox.

		status, response = imap.search(None, "(UNSEEN)") # Check for unread messages
		unreadMessages = response[0].split()
		self.screen.addstr(2,3,"You have %s unread messages in Inbox" % len(unreadMessages)) # Print how many unread messages there are

		status, response = imap.search(None, "ALL") # Search for all messages
		unreadMessages = response[0]
		ids = unreadMessages.split()
		latestEmails = int(ids[-1])
		k = 4
		t = 30

		for i in range(latestEmails, latestEmails-15, -1): # Only get 15 emails
			k += 1 # This allows us to print on different lines
			t += 1
			typ, data = imap.fetch(i, "(RFC822)") # RFC822 is the standard format for emails
			for response_part in data:
				if isinstance(response_part, tuple):
					msg = email.message_from_string(response_part[1])
					messageSubject = msg["subject"]
					messageFrom = msg["from"]
			# Get rid of unwanted characters
			messageFrom = messageFrom.replace("<", "")
			messageFrom = messageFrom.replace(">", "")

			if len(messageSubject) > 35: # If the subject is too long replace it with "..."
				messageSubject = messageSubject[0:32] + "..."

			if len(messageFrom) > 35:
				messageFrom = messageFrom[0:32] + "..."

			self.screen.addstr(3,3,"[From]")
			self.screen.addstr(3,40,"[Subject]")
			self.screen.addstr(k,3,"[" + messageFrom.split()[-1] + "]") # Print the sender address to the screen. Using an incremented variable to print on different lines.
			self.screen.refresh() # For debugging
			self.screen.addstr(k,40 ,"[" + messageSubject + "]" )

	def get_user_input(self):
		pass

	def mark_mail_as_read(self, mailServer, username):
		pass

	def format_screen(self):
		self.screen.clear()
		self.screen.border(0)


def main():
	mailClient = snorkelMail()

	mainWindow = curses.newwin(curses.LINES-2, curses.COLS, 1,0)
	subWindow = mainWindow.subwin(curses.LINES-6, curses.COLS-4,3,2)
	mainWindow.box()

	x = 0
	mailClient.format_screen()

	# Find a way to make this better
	# Will get this from config file
	mailClient.screen.border(0)
	mailClient.screen.addstr(2,2,"Enter Mail Server: ")
	mailServer = mailClient.screen.getstr()
	mailClient.format_screen()
	mailClient.screen.addstr(2,2,"Enter Email Address: ")
	username = mailClient.screen.getstr()
	mailClient.format_screen()
	mailClient.screen.addstr(2,2,"Enter Password for %s: " % username)
	curses.noecho()
	password = mailClient.screen.getstr()
	mailClient.format_screen()

	mailClient.screen.clear()
	mailClient.screen.addstr("Snorkel", curses.A_REVERSE)
	mailClient.screen.chgat(-1, curses.A_REVERSE)

	# Get mail on start up
	mailClient.read_mail(mailServer, username, password)

	mailClient.screen.noutrefresh()
	subWindow.noutrefresh()

	while x != ord("Q"):
		x = mailClient.screen.getch()
		# Will add calls to other methods here
		if x == ord("R"):
			mailClient.read_mail(mailServer, username, password)

	curses.endwin() # Restore terminal to original user mode

if __name__ == "__main__":
	main()
