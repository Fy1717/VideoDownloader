import tkinter as tk 
from tkinter import * 
from pytube import YouTube
from tkinter import messagebox , filedialog 

def CreateWidgets():
    linkLabel = Label(root, text="Linki Giriniz : " , bg="skyblue")
    linkLabel.grid(row=1, column=0 , pady=10 , padx=10)

    root.linkText = Entry(root, width=60)
    root.linkText.grid(row=1, column=1 , pady=10 , padx=10 , columnspan=2)

    destinationLabel = Label(root, text="Kayıt Yeri ? : " , bg="skyblue")
    destinationLabel.grid(row=2, column=0 , pady=10 , padx=10)

    root.destinationText = Entry(root , width=38)
    root.destinationText.grid(row=2, column=1 , pady=10 , padx=10)

    browseButton = Button (root, text= "BROWSE", command=Browse , width=15)
    browseButton.grid(row=2, column=2 , pady=10 , padx=10 , columnspan=2)

    dwldButton = Button (root, text= "DOWNLOAD", command=Download , width=30)
    dwldButton.grid(row=3, column=1 , pady=10 , padx=10 )

def Browse():
    root.destinationDIR = filedialog.askdirectory(initialdir="/home/x/Masaüstü")
    root.destinationText.insert('1',root.destinationDIR)

def Download():
    getVideo = YouTube(root.linkText.get())
    videoStream = getVideo.streams.first()
    videoStream.download(root.destinationDIR)
    messagebox.showinfo("BAŞARILI","Video İndirildi . Kayıt Yeri : \n "+root.destinationDIR)

root= tk.Tk()

root.geometry("550x140")
root.title("FY-YoutubeVideoDownloader")
root.resizable(False,False)
root.config(background="skyblue")

CreateWidgets()

root.mainloop()