from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x500')
root.resizable(0, 0)
root.title('Youtube Downloader')
root.config(bg='#AACDE2')

Label(root, text='Descarga tu video', font='arial 20 bold', bg='#AACDE2').pack(pady=20)

link = StringVar()
Label(root, text='Tu link aqui', font='arial 12', bg='#AACDE2').pack()
link_enter = Entry(root, width=70, textvariable=link).pack(pady=10)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text='Descargado con exito', font='arial 13 bold', bg='#AACDE2', fg='#857199').pack(pady=20)

Button(root, text='Descargar', font='arial 13 bold italic', bg='#857199', padx=2, command=Downloader).pack(pady=20)

root.mainloop()
