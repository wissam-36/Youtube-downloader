from customtkinter import *
from tkinter import messagebox
import pytube
from pytube import YouTube
import threading
import os
from PIL import Image


# Window setup
root = CTk()
root.geometry('700x300')
root.resizable(False, False)
root.title("YouTube Downloader")


# Background image
background_image = CTkImage(Image.open(os.path.join("assets", "background.jpg")), size=(700, 300))
background_label = CTkLabel(root, image=background_image, text='')
background_label.pack()


# Fonts and variables
fnt1 = CTkFont(family='Bahnschrift', weight='bold', size=20)
fnt2 = CTkFont(family='Bahnschrift', size=15)
link = StringVar()
resolution = StringVar()


# List to store resolution buttons
resolution_buttons = []



# Function to download video
def download_video():
    try:
        # Get YouTube video
        url = YouTube(str(link.get()))
        
        # Filter video stream by resolution and file extension
        video = url.streams.filter(res=resolution.get(), file_extension="mp4").first()

        # Set path to the Downloads folder
        download_path = os.path.join(os.path.expanduser('~/Downloads'))

        if video:
            # Download the video
            video.download(download_path)
            messagebox.showinfo("Download Complete", f"Your video has been successfully downloaded to:\n{download_path}")

            # Destroy resolution buttons and download button
            for button in resolution_buttons:
                button.destroy()
            resolution_buttons.clear()
        else:
            messagebox.showerror("Error", "No video stream available for the selected resolution.")
    except pytube.exceptions.RegexMatchError:
        messagebox.showerror("Invalid Link", "Please enter a valid YouTube link.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during the download:\n{str(e)}")



# Function to display resolution buttons
def show_resolution_buttons():
    global resolution_buttons
    resolutions = ["360p", "720p", "1080p"]
    for i, res in enumerate(resolutions):
        # Create resolution buttons
        button = CTkButton(root, text=res, font=fnt2, command=lambda r=res: select_resolution(r),
                           fg_color="#F7D761", text_color="black", hover_color="white", width=100, height=10)
        button.place(x=190 + i * 110, y=200)
        resolution_buttons.append(button)



# Function to select resolution
def select_resolution(selected_resolution):
    resolution.set(selected_resolution)
    # Create and place the download button
    download_button = CTkButton(root, text='DOWNLOAD', font=fnt1, command=Downloader, fg_color="#F7D761",
                                 text_color="black", hover_color="white")
    download_button.place(x=280, y=250)
    resolution_buttons.append(download_button)



# Function to initiate download in a separate thread
def Downloader():
    threading.Thread(target=download_video).start()



# GUI elements
CTkLabel(root, text='paste the link here :', font=fnt1, bg_color="#000F2A", text_color="#F7D761").place(x=250, y=65)
CTkEntry(root, font=fnt2, width=500, textvariable=link, text_color="#F7D761").place(x=100, y=100)
CTkButton(root, text='SHOW RESOLUTION', font=fnt1, command=show_resolution_buttons, fg_color="#F7D761",
          text_color="black", hover_color="white").place(x=250, y=150)




root.mainloop()
