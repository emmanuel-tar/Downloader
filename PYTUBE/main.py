import tkinter as tk
import customtkinter 
from pytube import YouTube


def start_download():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title,text_color="green")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Download Error!",text_color="red")
    #finishLabel.configure(text = 'DownLoaded')
    
    
    
def on_progress(streams,chunk,bytes_remaining):
    total_size=streams.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded/total_size * 100
    per = str(int(percentage_of_completion))
    pPercenatge.configure(text=per + "%")
    pPercenatge.update()
    
    #Update Progress bar
    progressBar.set(float(percentage_of_completion) /100)

# system Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")


# adding UI elements
title = customtkinter.CTkLabel(app,text="Insert a Youtube Link")
title.pack(padx=10, pady=10)

# Adding Link Input
url_var = tk.StringVar()
link= customtkinter.CTkEntry(app,width=350, height=40, textvariable=url_var)
link.pack()

# finish Downloading
finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack()

#Progress Number Percentage /Bar
pPercenatge = customtkinter.CTkLabel(app, text="0%")
pPercenatge.pack()


ProgressBar = customtkinter.CTkProgressBar(app,width=400)
ProgressBar.set(0)
ProgressBar.pack(padx = 10,pady =10)



# download Button
download = customtkinter.CTkButton(app,text="Download", command=start_download)
download.pack(padx = 10, pady = 10)

# Run app
app.mainloop()
