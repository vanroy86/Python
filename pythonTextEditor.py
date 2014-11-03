import wx
import os
class pythonTextEditor(wx.Frame):
    def __init__(self, parent, title):
        frame = wx.Frame.__init__(self, parent, title = title, size=(600, 400))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A Status bar at the bottom of the window

        # Create a menu to insert into the menu bar
        filemenu = wx.Menu()

        self.hasOpenedFile = False
        self.currentFileName = ""
        self.isNewFile = True

        menuNew = filemenu.Append(wx.ID_NEW, "New", "Create A New File")
        menuOpen = filemenu.Append(wx.ID_OPEN, "Open", "Open A File")
        menuSave = filemenu.Append(wx.ID_SAVE, "Save", "Save A File")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "About", "Information About This Program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit", "Terminate The Program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "File") # Populate our menu bar with our menu
        self.SetMenuBar(menuBar)

        # Set up bind events
        # More information about events can be found at: wiki.wxpython.org/ListOfEvents
        self.Bind(wx.EVT_MENU, self.on_new, menuNew)
        self.Bind(wx.EVT_MENU, self.on_open, menuOpen)
        self.Bind(wx.EVT_MENU, self.on_save, menuSave)
        self.Bind(wx.EVT_MENU, self.on_about, menuAbout)
        self.Bind(wx.EVT_MENU, self.on_exit, menuExit)

        self.Show(True)

    def on_about(self, event):
        dlg = wx.MessageDialog(self, "This is a text editor written in Python using the wxPython Module", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def on_open(self, event):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file to open", os.getcwd(), "", "*.*", wx.OPEN) # Create a File Dialog
        if dlg.ShowModal() == wx.ID_OK: # If the Dialog has shown up
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            fileToRead = os.path.join(self.dirname, self.filename)
            with open(fileToRead, "r") as f:
                self.control.SetValue(f.read()) # Set the Text box value to the file we want to open
        self.hasOpenedFile = True
        self.isNewFile = False
        self.currentFileName = fileToRead
        dlg.Destroy() # Get rid of the Dialog

    def on_save(self, event):
        if self.hasOpenedFile == True and self.isNewFile == False:
            with open(self.currentFileName, "w") as fileToWriteTo:
                fileToWriteTo.write(self.control.GetValue())
        elif self.isNewFile == True and self.hasOpenedFile == False:
            dlg = wx.FileDialog(self, "Choose where to save", os.getcwd(), "", "*.*",wx.SAVE)
            if dlg.ShowModal() == wx.ID_OK:
                print "Save"

    def on_exit(self, event):
        self.Close(True)

    def on_new(self, event):
        self.isNewFile = True
        self.hasOpenedFile = False
        self.currentFileName = ""
        self.control.SetValue("")

app = wx.App(False)
frame = pythonTextEditor(None, "Small editor")
app.MainLoop()
