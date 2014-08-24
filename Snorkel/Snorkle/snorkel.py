import os,sys
import urwid
import imaplib
import email

class snorkelMail(object):
	def __init__(self):
		self.screen = urwid

	def parse_config_file(self, configFile):
		pass

	def get_new_mail(self):
		pass


	def get_user_input(self):
		pass

	def mark_mail_as_read(self, mailServer, username):
		pass

	def exit_on_q(self):
		if key in ("q", "Q"):
			raise urwid.ExitMainLoop()

class emailWidget(urwid.WidgetWrap):
	def __init__(self):
		pass
	def selectable(self):
		return True

	def read_mail(self, mailServer, username, password):
		palette = [
			("body", "dark cyan", "", "standout"),
			("focus", "dark red", "", "standout"),
			("head", "light red", "black"),
				]



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
		#self.screen.addstr(2,2,"You have %s unread messages in Inbox" % len(unreadMessages)) # Print how many unread messages there are

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

			self.messageSubject = "[From] %s [Subject] %s " % (messageFrom.split()[-1],  messageSubject)
			self.item = [("fixed",15, urwid.Padding(urwid.AttrWrap(urwid.Text("[From] %s" % messageFrom, "left", "any"), 2)),
								urwid.AttrWrap(urwid.Text("%s" % messageSubject), "left", "any"), )]
		items = []

		for i in range(latestEmails, latestEmails-15, -1):
			items.append(messageSubject)

		header = urwid.AttrMap(urwid.Text("selected:"), "head")
		listbox = urwid.ListBox(urwid.SimpleListWalker(items))
		view = urwid.Frame(urwid.AttrWrap(listbox, "body"), header = header)
		loop = urwid.MainLoop(view, palette)
		loop.run()



def main():
	mailClient = snorkelMail()




	mailClientTest = emailWidget()
	mailClientTest.read_mail("imap.gmail.com", "andrewdarnton12", "021209ab")
	# Get mail on start up
	#mailClient.read_mail(mailServer, username, password)


if __name__ == "__main__":
	main()
