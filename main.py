from customtkinter import *
from tkinter import messagebox
import pytube
from pytube import YouTube
import threading
import os
from PIL import Image


# Window
root = CTk()
root.geometry('700x300')
root.resizable(False,False)
root.title("YouTube Downloader")

background_image = CTkImage(Image.open(os.path.join("assets","background.jpg")), size=(700, 300))
background_label = CTkLabel(root,image=background_image, text='')
background_label.pack()


fnt1 = CTkFont(family='Bahnschrift', weight='bold', size=20)
fnt2 = CTkFont(family='Bahnschrift', size=15)
link = StringVar()


def download_video():
    try:
        url = YouTube(str(link.get()))
        video = url.streams.first()

        # Set path to the Downloads folder
        download_path = os.path.join(os.path.expanduser('~/Downloads'))


        video.download(download_path)
        messagebox.showinfo("Download Complete", f"Your video has been successfully downloaded to:\n{download_path}")
    except pytube.exceptions.RegexMatchError:
        messagebox.showerror("Invalid Link", "Please enter a valid YouTube link.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during the download:\n{str(e)}")

def Downloader():
    threading.Thread(target=download_video).start()



CTkLabel(root, text='paste the link here :', font=fnt1,bg_color="#000F2A",text_color="#F7D761").place(x=250, y=65)
CTkEntry(root, font=fnt2, width=500, textvariable=link,text_color="#F7D761").place(x=100, y=100)
CTkButton(root, text='DOWNLOAD', font=fnt1, command=Downloader,fg_color="#F7D761",text_color="black",hover_color="white").place(x=270, y=150)



root.mainloop()
