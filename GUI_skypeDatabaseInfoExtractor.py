from Tkinter import *
import ttk
import sqlite3
import os

def printProfile(skypeDB):
    conn = sqlite3.connect(skypeDB) # Connect to the skype database
    c = conn.cursor()
    c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM accounts;")
    for row in c: # The SQL statement above returns a list. Here we are looping through that list and assigning each SELECT to a variable
        user = str(row[0])
        skypeUsername = str(row[1])
        city = str(row[2])
        country = str(row[3])
        profileTime = str(row[4])

    return (user, skypeUsername, city, country, profileTime)

def main():
    skypeDB = "path/to/database"
    root = Tk() # Define a root window
    root.title("Skype Database Info Extractor") # Give the root window a title
    root.geometry("600x400") # Set the size of the window
    root.resizable(False, False) # Don't let anyone resize!

    mainframe = ttk.Frame(root, padding = "3 3 12 12") # Add a frame to the root window and give it some padding
    mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S)) # Define a grid in the frame
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)

    titleFormat = "Helvetica 12 italic"

    # Create a Label, tell it which frame to user, what to display and where to go in the frame
    ttk.Label(mainframe, text = "Basic Information", font = titleFormat).grid(column = 1, row = 1, sticky = (W, E))

    ttk.Label(mainframe, text = "Full Name: ").grid(column = 1, row = 2, sticky = (W, E))
    ttk.Label(mainframe, text = printProfile(skypeDB)[0]).grid(column = 2, row = 2, sticky = (W, E))

    ttk.Label(mainframe, text = "Skype Name: ").grid(column = 1, row = 3, sticky = (W, E))
    ttk.Label(mainframe, text = printProfile(skypeDB)[1]).grid(column = 2, row = 3, sticky = (W, E))

    ttk.Label(mainframe, text = "City: ").grid(column = 1, row = 4, sticky = (W, E))
    ttk.Label(mainframe, text = printProfile(skypeDB)[2]).grid(column = 2, row = 4, sticky = (W, E))

    ttk.Label(mainframe, text = "Country: ").grid(column = 1, row = 5, sticky = (W, E))
    ttk.Label(mainframe, text = printProfile(skypeDB)[3]).grid(column = 2, row = 5, sticky = (W, E))

    ttk.Label(mainframe, text = "Profile Timestamp: ").grid(column = 1, row = 6, sticky = (W, E))
    ttk.Label(mainframe, text = printProfile(skypeDB)[4]).grid(column = 2, row = 6, sticky = (W, E))

    for child in mainframe.winfo_children(): child.grid_configure(padx = 5, pady = 5)
    # Start the loop!
    root.mainloop()

if __name__ == "__main__":
    main()
