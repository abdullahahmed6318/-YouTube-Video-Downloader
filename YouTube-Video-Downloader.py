from io import TextIOBase
from logging import disable
import tkinter as tk
from tkinter import ttk
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

def onClick():
    got_link = link.get()
    got_path = path.get()
    try:
        yt = YouTube(str(got_link))
    except:
        m_box.showerror("Error", "Connection Problem !")
    else:
        vid = yt.streams.get_highest_resolution()
        destination = str(got_path)
        vid.download(destination)
        os.startfile(got_path)
        return m_box.showinfo('Successfully Downloaded.', f"Your YouTube Vidoe Downloaded Successfully at {got_path}/{yt.title}")


threads = []


def startThredProcess():
    myNewThread = threading.Thread(target=onClick)
    threads.append(myNewThread)
    myNewThread.start()


def open_txt():
    Entry_file= open(FolderName,"r")
    Entry_file= filedialog.askdirectory()
    stuff = FolderName.read()
    download_path.insert(END, stuff)

def openDirectry():
   global FolderName
   FolderName= filedialog.askdirectory()
   if (len(FolderName)>1):
      "fileLocationLabeError".configure(text=FolderName,fg="green")
   else:
      "fileLocationLabeError".config(text="Please choose File",fg="red").start()


# setting switch state:
btnState = False



# setting switch function:
def switch():
    global btnState
    if btnState:
        btn.config(image=offImg, bg="#CECCBE", activebackground="#CECCBE")
        win.config(bg="#fff")
        txt.config(text="Dark Mode: OFF", bg="#fff")
        get_info.config(text="Enter YouTube Video Link......... ",
         bg="#fff",fg="#000000")
        get_info1.config(text="Enter Downloading Path.........",
         bg="#fff",fg="#000000")
        btn2.config(text="Please choose Folder ", 
        bg="#fff" ,fg="#000000",font=("Agency FB",9 ))
        btn1.config(text="Download Video", 
        bg="#fff" ,fg="#000000",font=("Agency FB",9 ))

        btnState = False
    else:
        btn.config(image=onImg, bg="#2B2B2B", activebackground="#2B2B2B")
        win.config(bg="#2B2B2B")
        txt.config(text="Dark Mode: ON", bg="#2B2B2B")
        get_info.config(text="Enter YouTube Video Link......... ",
         bg="#2B2B2B" ,fg="#fff")
        get_info1.config(text="Enter Downloading Path.........",
         bg="#2B2B2B",fg="#fff")
        btn2.config(text="Please choose Folder ", 
        bg="#2B2B2B" ,fg="#fff",font=("Agency FB",9 ))
        btn1.config(text="Download Video", 
        bg="#2B2B2B" ,fg="#fff",font=("Agency FB",9 ))

        btnState = True




#Text.config(text="File Opened: "+FolderName)


win = tk.Tk()
win.geometry("500x400")
win.title("abdalla.YouTube Video Downloader")
win.minsize(500, 400)
win.maxsize(500, 400)
style = ttk.Style()

# loading the switch images:
onImg = PhotoImage(file=r"switch-on.png")
offImg = PhotoImage(file=r"switch-off.png")


# switch widget:
btn = tk.Button(win, text="OFF",image=onImg, relief=RAISED,\
                         cursor="cross",
borderwidth=5, command=switch, bg="#CECCBE", 
activebackground="#CECCBE",height=15, width=15)
btn.place(relx=0.9, rely=0.9,
 anchor="center"
)
btn.config(image=offImg)


# Night mode label:
txt = tk.Label(win, text="Dark Mode: OFF", 
fg="green" ,height=1, width=11, bd=5)
txt.place(relx=0.9, rely=0.80,anchor="center")

get_info = tk.Label(win, text="Enter YouTube Video Link......... ",
                      font=("tajawal",11,"bold"), )
get_info.grid(row=0, column=0, sticky=tk.W)

#entry link
link = tk.StringVar()

yt_link = ttk.Entry(win, width=60, textvariable=link, )
yt_link.grid(row=1, columnspan=3, padx=0, pady=3)

get_info1 = tk.Label(win, text="Enter Downloading Path........."
                        ,font=("tajawal",11,"bold")
 )
get_info1.grid(row=3, column=0, sticky=tk.W)


#entry file
path = tk.StringVar()
global download_path
download_path =ttk.Entry(win, width=60, textvariable=path,)
download_path.grid(row=4, columnspan=3, padx=0, pady=3)

#choose file
btn2 = tk.Button(win,text="Please choose Folder ",
command=openDirectry, height=2, width=30,  )
btn2.grid(row=6, column=0)

#button download
btn1 = tk.Button(win,text="Download Video",
height=2, width=40, 
command=startThredProcess)
btn1.grid(row=8, column=0, padx=0, pady=0)


win.mainloop()
