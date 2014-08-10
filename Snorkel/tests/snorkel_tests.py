from nose.tools import *
from Snorkel.snorkel import snorkelMail

def test_login():
	mail = snorkelMail()
	mail.read_mail("imap.gmail.com", "andrewdarnton12", "password")

def test_get_new_mail():
	pass

def test_parse_config():
	pass

def test_mark_mail_as_read():
	pass
