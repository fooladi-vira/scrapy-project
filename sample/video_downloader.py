import re
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from pytube import YouTube
from tkinter import Button,messagebox,PhotoImage,Label
import requests,bs4

def browse():
    directory = askdirectory(initialdir="YOUR DIRECTORY PATH", title="save")
    download_dir.set(directory)
    place_input.configure(textvariable=download_dir)
    
def download():
    link= video_link.get()
    save_dir = download_dir.get()
    response = requests.get("https://www.aparat.com/v/njOyG")
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    links=soup.find_all('link',href=re.compile('.mp4'))
    print(len(links))
    for info in links:
        link=info.get('href')
        with requests.get(link,stream=True) as r:
            with open (save_dir+'video.mp4','wb') as file:
                for pack in r.iter_content(chunk_size=1024):
                    file.write(pack)
    messagebox.showinfo(title="success",message="your video download succesfully")
    

def msgcallBack(txt):
    messagebox.showinfo("my message",txt)
    
window = tk.Tk()
window.title('youtube downloader')
window.wm_minsize(500,500)  
color_btn_bg='gold'
download_dir = tk.StringVar()
video_link = tk.StringVar()

    

place_lable = tk.Label(window, text=" Directory")
place_lable.grid(row=0,column=0,padx=20,pady=20)
place_lable.config(font=("None",16), fg="gold")

place_input = tk.Entry(window, width=35,textvariable='')
place_input.grid(row=0, column=1,sticky="w")

place_btn = tk.Button(window, text="open",width=10,bg="gold",fg="black",command=browse)
place_btn.grid(row=0,column=2)


link_lable = tk.Label(window, text="video link")
link_lable.grid(row=1,column=0,padx=20,pady=20)
link_lable.config(font=("None",16), fg="gold")

link_input = tk.Entry(window, width=40,textvariable=video_link.get())
link_input.grid(row=1, column=1)

download_btn = tk.Button(text="download Now",command=download)
download_btn.grid(row=2,column=1,padx=20,pady=20)
download_btn.config(height=2,width=15,bg="gold",fg="black")

msg_btn= Button(window, text='message' , fg='black', bg=color_btn_bg,command=lambda: msgcallBack('Have good job'),font=1,padx=15,bd=15,borderwidth=10)
msg_btn.grid(row=3, column=1)


pic=PhotoImage(file='1.png')
lbl=Label(window ,image=pic).grid(row=6, column=0)
window.mainloop()