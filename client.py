from re import A
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import time
import ntpath 

from tkinter import filedialog
from pathlib import Path

from playsound import playsound
import pygame
from pygame import mixer

PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox = None
filePathLabel = None

global song_counter
song_counter = 0


    
def musicWindow():
    window = Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')
    
    selectLabel = Label(window, text = "Select Song", bg = 'LightSkyBlue', font = ("Calibri",8))
    selectLabel.place(x=2,y=1)
    
    listBox = Listbox(window, height = 10, width = 39, activestyle = 'dotbox', bg = 'LightSkyBlue', borderwidth = 2, font = ("Calibri", 10))
    listBox.place(x=10,y=25)
    
    scrollBar1 = Scrollbar(listBox)
    scrollBar1.place(relheight = 1, relx=1)
    scrollBar1.config(command = listBox.yview)
    
    PlayButton=Button(window, text = "Play", width = 10, bg = 'SkyBlue', font = ("Calibri",10),command = play)
    PlayButton.place(x=200,y=200)
    
    Stop = Button(window, text = "Stop", bd = 1, width = 10, bg = 'SkyBlue', font = ("Calibri", 10), command = stop)
    Stop.place(x=200,y=200)
    
    Upload = Button(window, text = "Upload", bd = 1, width = 10, bg = 'SkyBlue', font = ("Calibri", 10))
    Upload.place(x=30,y=250)
    
    Download = Button(window, text = "Download", bd = 1, width = 10, bg = 'SkyBlue', font = ("Calibri", 10))
    Download.place(x=200,y=250)
    
    infoLabel = Label(window, text = "", fg="blue", font = ("Calibri", 8))
    infoLabel.place(x=4,y=280)
    
    window.mainloop()
    
    def play():
        global song_selected
        song_selected = listbox.get(ANCHOR)
        
        pygame
        mixer.init()
        mixer.music.load('shared_files/'+song_selected)
        mixer.music.play()
        if(song_selected != ""):
            infoLabel.configure(text = "Now Playing: " + song_selected)
        else:
            infoLabel.configure(text="")
            
            
    def stop():
        global song_selected
        pygame
        mixer.init()
        mixer.music.load('shared_files/'+song_selected)
        mixer.music.pause()
        infoLabel.configure(text="")
    
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    
    musicWindow()

setup()