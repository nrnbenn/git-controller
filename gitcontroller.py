import tkinter as tk
import subprocess as sp

class app:
    def __init__(self,master):
        self.window = master
        self.window.geometry("500x500")
        self.homepage()

    def clear(self):
        for i in self.window.winfo_children():
            i.destroy()

    def homepage(self):
        self.clear()

        self.title = tk.Label(text = "Welcome to Gitty")
        self.title.place(x=0,y=0)

        self.logframe = tk.Frame(self.window)
        self.logframe.place(x=5,y=475)
        self.loglabel = tk.Label(self.logframe,text="log: ")
        self.loglabel.grid(row=0,column=0)
        self.log = tk.Label(self.logframe,text="")
        self.log.grid(row=0,column=1)

        self.directoryframe = tk.Frame(self.window)
        self.directoryframe.place(x=5,y=450)
        self.directorylabel = tk.Label(self.directoryframe,text="Project Directory: ")
        self.directorylabel.grid(row=0,column=0)
        self.directoryinput = tk.Text(self.directoryframe,height=1,width=45)
        self.directoryinput.grid(row=0,column=1)
        self.directoryreload = tk.Button(self.directoryframe,width=1,height=1,padx=5,text="↻")
        self.directoryreload.grid(row=0,column=2)

    def reloaddirectory(self):
        pass

    def setlog(self,text):
        self.log['text'] = text



window = tk.Tk()
app(window)
window.mainloop()