from tkinter import *
from io import TextIOBase
from logging import disable, root
import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import Button, Entry, Frame, Label, LabelFrame
import os
from tkinter import filedialog
from tkinter.constants import COMMAND, END, RAISED, W
from typing import Text, TextIO
from pytube import YouTube
from tkinter import messagebox as m_box
import subprocess
import threading
from tkinter import PhotoImage
from PIL import ImageTk, Image
import webbrowser

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytError.config(text="Paste Link again!!",fg="red")


    #download function
    select.download(Folder_Name)
    ytError.config(text="Download Completed!!")




# setting switch state:
btnState = False


# setting switch function:
def switch():
    global btnState
    if btnState:
        btn.config(image=offImg, bg="#CECCBE", activebackground="#CECCBE")
        win.config(bg="#fff")
        txt.config(text="Dark Mode: OFF", bg="#fff")
        DownloadVideoLink.config(text="Enter YouTube Video Link......... ",
         bg="#fff",fg="#000000")
        saveLabel.config(text="Enter Downloading Save the Video File .........",
         bg="#fff",fg="#000000")
        btn2.config(text="Please choose Folder ", 
        bg="#fff" ,fg="#000000",font=("Agency FB",9 ))
        btn1.config(text="Download Video", 
        bg="#fff" ,fg="#000000",font=("Agency FB",9 ))
        ytError.config(text="Please Url video ", 
        bg="#fff" ,fg="#000000",font=("Agency FB",9 ))
        locationError.config(text=Folder_Name, 
        bg="#fff" ,fg="#000000",font=("Agency FB",9 ))
        ytQuality.config(text="Select Quality", 
        bg="#fff" ,fg="#000000",font=("Agency FB",9 ))
        my_menu.config(bg="#fff" ,fg="#000000")

        
        btnState = False
    else:
        btn.config(image=onImg, bg="#2B2B2B", activebackground="#2B2B2B")
        win.config(bg="#2B2B2B")
        txt.config(text="Dark Mode: ON", bg="#2B2B2B")
        DownloadVideoLink.config(text="Enter YouTube Video Link......... ",
         bg="#2B2B2B" ,fg="#fff")
        saveLabel.config(text="Enter Downloading Save the Video File .........",
         bg="#2B2B2B",fg="#fff")
        btn2.config(text="Please choose Folder ", 
        bg="#2B2B2B" ,fg="#fff",font=("Agency FB",9 ))
        btn1.config(text="Download Video", 
        bg="#2B2B2B" ,fg="#fff",font=("Agency FB",9 ))
        ytError.config(text="Please Url video ", 
        bg="#2B2B2B" ,fg="#fff",font=("Agency FB",9 ))
        locationError.config(text=Folder_Name, 
        bg="#2B2B2B" ,fg="#fff",font=("Agency FB",9 ))
        ytQuality.config(text="Select Quality", 
        bg="#2B2B2B" ,fg="#fff",font=("Agency FB",9 ))
        my_menu.config(
        bg="#2B2B2B" ,fg="#fff")
        btnState = True


def callback(url):
    webbrowser.open_new(url)




def donothing():
   filewin = Toplevel(win)
   filewin.geometry("100x100")
   link1 = Label(filewin, text="facebook", fg="blue", cursor="hand2")
   link1.place(x=0,y=10)
   link1.bind("<Button-1>", lambda e: callback("https://www.facebook.com/abdalla1850/"))
   link1 = Label(filewin, text="twitter", fg="blue", cursor="hand2")
   link1.place(x=0,y=30)
   link1.bind("<Button-1>", lambda e: callback("https://twitter.com/abdalla1850"))
   link1 = Label(filewin, text="github", fg="blue", cursor="hand2")
   link1.place(x=0,y=50)
   link1.bind("<Button-1>", lambda e: callback("https://github.com/abdullahahmed6318"))




win = tk.Tk()
win.title("YouTube Video Downloader")
win.geometry("500x400")
#win.columnconfigure(0,weight=1)



#menu
my_menu = Menu(win)
win.config(menu=my_menu)
filemenu = Menu(my_menu, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=win.quit)
my_menu.add_cascade(label="File", menu=filemenu)
editmenu = Menu(my_menu, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

my_menu.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(my_menu, tearoff=0)
helpmenu.add_command(label="About...", command=donothing)
my_menu.add_cascade(label="Help", menu=helpmenu)

win.config(menu=my_menu)





# loading the switch images:
onImg = PhotoImage(file=r"")
offImg = PhotoImage(file=r"")
#"switch-on1.png")

# switch widget:
btn = Button(win, text="OFF",
image=onImg, 
relief=RAISED,\
                         cursor="cross",
borderwidth=5,
command=switch, 
 bg="#CECCBE", 
activebackground="#CECCBE",height=15, width=19)
btn.place(relx=0.9, rely=0.9,
 anchor="center"
)
btn.config(image=offImg)


# Night mode label:
txt = Label(win, text="Dark Mode: OFF", 
fg="green" ,height=1, width=11, bd=5)
txt.place(relx=0.9, rely=0.80,anchor="center")



#Ytd Link Label
DownloadVideoLink = Label(win,text="Enter YouTube Video Link......... ",font=("jost",15))
DownloadVideoLink.grid()

#Entry Bo
ytdEntryVar = StringVar()
ytdEntry = Entry(win,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Msg
ytError = Label(win,text="Please Url video ",font=("jost",10))
ytError.grid()
ytError. place(x=351,y=9)

#Asking save file label
saveLabel = Label(win,text="Enter Downloading Save the Video File .........",)
saveLabel.grid()

#btn of save file
btn2 = Button(win,width=30,text="Please choose Folder",command=openLocation)
btn2.grid()

#Error Msg location
locationError = Label(win,text="Please file save",)
locationError. place(x=350,y=70)

#Download Quality
ytQuality = Label(win,text="Select Quality",)
ytQuality.grid()

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(win,values=choices)
ytdchoices.grid()

#donwload btn
btn1 = Button(win,text="Donwload",width=20,command=DownloadVideo)
btn1.grid()






win.mainloop()
