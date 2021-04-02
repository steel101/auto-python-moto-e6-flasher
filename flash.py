from tkinter import *
from tkinter import ttk
import os
import sys
import time
#folder where root imgs are at
rootdir = 'root\motoe6-root'
#stock firmware files
stockdir = 'un-root\stock-firmware\stock'
if not os.path.exists('acceptterms.txt'):
    with open('acceptterms.txt', 'w'): 
       WriteTxtFile = open("acceptterms.txt", "w")
       WriteTxtFile.write ('0')
       time.sleep(3)
       exit()
f = open("acceptterms.txt", "r") 
data = int(f.read(1))
print(data)


if data == 0:
    root=Tk()
    mainframe = ttk.Frame(root,padding="1 1 12 12")
    root.geometry('840x200')
    root.title("terms and services")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    variable1=StringVar() # Value saved here
    variable1.set("0")
    def search():
      root.destroy()
      return ''
    def search1():
      root.destroy()
      quit()
    ttk.Entry(mainframe, width=20, textvariable=variable1).grid(column=2, row=1)
    ttk.Label(mainframe, text="\nYour warranty is void.\nI am not responsible for bricked devices, dead SD cards\nthermonuclear war, or you getting fired because the alarm app failed.\nPlease do some research if you have any concerns about features included in this flasher before useing it!\nYOU are choosing to make these modifications,\nand if you point the finger at me for messing up your device, I will laugh at you.\n\n\nenter 1 in text box and click accept button to countine").grid(column=1, row=1)
    ttk.Button(mainframe, text="accept", command=search).grid(column=11, row=13)
    ttk.Button(mainframe, text="decline", command=search1).grid(column=10, row=13)
    root.mainloop()
    accept = int(variable1.get())
    if accept > 1:
        accept = 1 
    elif accept == 1:
          accept = 1 	
    elif accept ==0:
          accept =0

    if accept == 1:
          WriteTxtFile = open("acceptterms.txt", "w")
          WriteTxtFile.write ('1')
          import tkinter as tk
          from tkinter import messagebox
          import  os
          import sys
          root= tk.Tk()
          MsgBox = tk.messagebox.askquestion ('use xda unlock bootloader','go to https://forum.xda-developers.com/t/guide-unlock-your-g7-bootloader.3906858/')
          if MsgBox == 'yes':
              os.system('python -m webbrowser -t "https://forum.xda-developers.com/t/guide-unlock-your-g7-bootloader.3906858/"')
              root.destroy()
          else:
              root.destroy()
              root.mainloop()
          import tkinter
          from tkinter import messagebox
          top =  tkinter.Tk()
          top.geometry("150x150")
          messagebox.showinfo        ("Information","turn device on and unlock device")
          top.destroy()
          top =  tkinter.Tk() 
          top.geometry("150x150")
          messagebox.showinfo        ("Information","go to settings and scroll down to system and click system")
          top.destroy()
          top =  tkinter.Tk()
          top.geometry("150x150")
          messagebox.showinfo        ("Information","click about phone and scrool to bottom and click build number 7 times")
          top.destroy()
          top =  tkinter.Tk()
          top.geometry("150x150")
          messagebox.showinfo        ("Information","click the back botton 1 time you should now see advanced with a arrow next to it click it")
          top.destroy()
          top =  tkinter.Tk()
          top.geometry("150x150")
          messagebox.showinfo        ("Information","scroll down untill you see developer options click it")
          top.destroy()
          top =  tkinter.Tk()
          top.geometry("150x150")
          messagebox.showinfo        ("Information","now scroll down untill you see USB debugging click on it")
          top.destroy()
          top =  tkinter.Tk()
          top.geometry("150x150")
          messagebox.showinfo        ("Information","plug your device into your pc now")
          top.destroy()
          top.mainloop() 
    elif  accept == 0:
          quit ()

os.system('adb reboot bootloader')

from tkinter import ttk
root=Tk()
mainframe = ttk.Frame(root,padding="1 1 12 12")
root.geometry('525x100')
root.title("root/unroot/stock flasher 1=flash 0=do-not-flash")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

variable1=StringVar() # Value saved here
variable1.set("0")
variable2=StringVar() # Value saved here
variable2.set("0")
variable3=StringVar() # Value saved here
variable3.set("0")
variable4=StringVar() # Value saved here
variable4.set("0")

def search():
  root.destroy()
  return ''

ttk.Entry(mainframe, width=7, textvariable=variable1).grid(column=2, row=1)
ttk.Entry(mainframe, width=7, textvariable=variable2).grid(column=4, row=1)
ttk.Entry(mainframe, width=7, textvariable=variable3).grid(column=2, row=2)
ttk.Entry(mainframe, width=7, textvariable=variable4).grid(column=4, row=2)

ttk.Label(mainframe, text="flash stock erase all data").grid(column=1, row=1)
ttk.Label(mainframe, text="flash stock keep userdata").grid(column=3, row=1)
ttk.Label(mainframe, text="flash stock with twrp").grid(column=1, row=2)
ttk.Label(mainframe, text="flash flash root erase all data").grid(column=3, row=2)

ttk.Button(mainframe, text="flash", command=search).grid(column=10, row=13)
root.mainloop()
root = int(variable4.get())
stockead = int(variable1.get())
stockkud = int(variable2.get())
stockwt = int(variable3.get())

if stockead > 1:
        stockead = 1 
elif stockead == 1:
        stockead = 1 	
elif stockead ==0:
	stockead =0

if stockkud > 1:
	stockkud = 1 
elif stockkud == 1:
        stockkud = 1
elif stockkud == 0:
	stockkud = 0

if stockwt > 1:
	stockwt = 1 
elif stockwt == 1:
        stocktwt = 1
elif stockwt == 0:
	stockwt = 0

if root > 1:
	root = 1
elif root == 1:
        root = 1
elif root == 0:
	root = 0
 
if root == 1:
        if stockead == 0:
            if stockkud == 0:
                if stockwt == 0:
                    print("\nrooting:\n")
                    os.chdir(stockdir)                    
                    os.system('fastboot flash bootloader bootloader.img')
                    os.system('fastboot flash modem NON-HLOS.bin')
                    os.system('fastboot flash fsg fsg.mbn')
                    os.system('fastboot erase modemst1')
                    os.system('fastboot flash modemst2')
                    os.system('fastboot flash dsp adspso.bin')
                    os.system('fastboot flash logo logo.bin')
                    os.system('fastboot flash boot boot.img')
                    os.system('fastboot flash dtbo dtbo.img')
                    os.system('fastboot flash system system.img_sparsechunk.0')
                    os.system('fastboot flash system system.img_sparsechunk.1')
                    os.system('fastboot flash system system.img_sparsechunk.2')
                    os.system('fastboot flash system system.img_sparsechunk.3')
                    os.system('fastboot flash system system.img_sparsechunk.4')
                    os.system('fastboot flash system system.img_sparsechunk.5')
                    os.system('fastboot flash system system.img_sparsechunk.6')
                    os.system('fastboot flash system system.img_sparsechunk.7')
                    os.system('fastboot flash system system.img_sparsechunk.8')
                    os.system('fastboot flash system system.img_sparsechunk.9')
                    os.system('fastboot flash recovery recovery.img')
                    os.system('fastboot flash vendor vendor.img')
                    os.system('fastboot flash oem oem.img')
                    os.system('fastboot erase userdata')
                    os.system('fastboot erase cache')
                    os.system('fastboot erase DDR')
                    os.chdir('..') 
                    os.chdir(rootdir)
                    os.system('fastboot -w flash boot boot.img')
                    os.system('fastboot flash system system.img')
                    os.system('fastboot flash dtbo dtbo.img')
                    os.system('fastboot flash vbmeta vbmeta.img')
                    os.system('fastboot flash vendor vendor.img')
                    os.system('fastboot flash recovery recovery.img')
                    os.system('fastboot flash logo logo.bin')          

if stockead == 1:
        if root == 0:
            if stockkud == 0:
                if stockwt == 0:
                    print("\nflashing stock erase all data:\n")
                    os.chdir(stockdir)
                    os.system('fastboot flash bootloader bootloader.img')
                    os.system('fastboot flash modem NON-HLOS.bin')
                    os.system('fastboot flash fsg fsg.mbn')
                    os.system('fastboot erase modemst1')
                    os.system('fastboot flash modemst2')
                    os.system('fastboot flash dsp adspso.bin')
                    os.system('fastboot flash logo logo.bin')
                    os.system('fastboot flash boot boot.img')
                    os.system('fastboot flash dtbo dtbo.img')
                    os.system('fastboot flash system system.img_sparsechunk.0')
                    os.system('fastboot flash system system.img_sparsechunk.1')
                    os.system('fastboot flash system system.img_sparsechunk.2')
                    os.system('fastboot flash system system.img_sparsechunk.3')
                    os.system('fastboot flash system system.img_sparsechunk.4')
                    os.system('fastboot flash system system.img_sparsechunk.5')
                    os.system('fastboot flash system system.img_sparsechunk.6')
                    os.system('fastboot flash system system.img_sparsechunk.7')
                    os.system('fastboot flash system system.img_sparsechunk.8')
                    os.system('fastboot flash system system.img_sparsechunk.9')
                    os.system('fastboot flash recovery recovery.img')
                    os.system('fastboot flash vendor vendor.img')
                    os.system('fastboot flash oem oem.img')
                    os.system('fastboot erase userdata')
                    os.system('fastboot erase cache')
                    os.system('fastboot erase DDR')
                    
if stockwt == 1:
        if stockead == 0:
            if stockkud == 0:
                if root == 0:
                    print("\nflash stock with twrp\n")     
                    os.chdir(stockdir)
                    os.system('fastboot flash bootloader bootloader.img')
                    os.system('fastboot flash modem NON-HLOS.bin')
                    os.system('fastboot flash fsg fsg.mbn')
                    os.system('fastboot erase modemst1')
                    os.system('fastboot flash modemst2')
                    os.system('fastboot flash dsp adspso.bin')
                    os.system('fastboot flash logo logo.bin')
                    os.system('fastboot flash boot boot.img')
                    os.system('fastboot flash dtbo dtbo.img')
                    os.system('fastboot flash system system.img_sparsechunk.0')
                    os.system('fastboot flash system system.img_sparsechunk.1')
                    os.system('fastboot flash system system.img_sparsechunk.2')
                    os.system('fastboot flash system system.img_sparsechunk.3')
                    os.system('fastboot flash system system.img_sparsechunk.4')
                    os.system('fastboot flash system system.img_sparsechunk.5')
                    os.system('fastboot flash system system.img_sparsechunk.6')
                    os.system('fastboot flash system system.img_sparsechunk.7')
                    os.system('fastboot flash system system.img_sparsechunk.8')
                    os.system('fastboot flash system system.img_sparsechunk.9')
                    os.chdir('..')
                    os.chdir(rootdir)
                    os.system('fastboot flash recovery recovery.img')
                    os.chdir('..')
                    os.chdir(stockdir)
                    os.system('fastboot flash vendor vendor.img')
                    os.system('fastboot flash oem oem.img')
                    os.system('fastboot erase userdata')
                    os.system('fastboot erase cache')
                    os.system('fastboot erase DDR')
if stockkud == 1:
        if stockead == 0:
            if root == 0:
                if stockwt == 0:
                    print("\nflash stock keep user data:\n")
                    os.chdir(stockdir)
                    os.system('fastboot flash bootloader bootloader.img')
                    os.system('fastboot flash modem NON-HLOS.bin')
                    os.system('fastboot flash fsg fsg.mbn')
                    os.system('fastboot erase modemst1')
                    os.system('fastboot flash modemst2')
                    os.system('fastboot flash dsp adspso.bin')
                    os.system('fastboot flash logo logo.bin')
                    os.system('fastboot flash boot boot.img')
                    os.system('fastboot flash dtbo dtbo.img')
                    os.system('fastboot flash system system.img_sparsechunk.0')
                    os.system('fastboot flash system system.img_sparsechunk.1')
                    os.system('fastboot flash system system.img_sparsechunk.2')
                    os.system('fastboot flash system system.img_sparsechunk.3')
                    os.system('fastboot flash system system.img_sparsechunk.4')
                    os.system('fastboot flash system system.img_sparsechunk.5')
                    os.system('fastboot flash system system.img_sparsechunk.6')
                    os.system('fastboot flash system system.img_sparsechunk.7')
                    os.system('fastboot flash system system.img_sparsechunk.8')
                    os.system('fastboot flash system system.img_sparsechunk.9')
                    os.system('fastboot flash recovery recovery.img')
                    os.system('fastboot flash vendor vendor.img')
                    os.system('fastboot flash oem oem.img')

exit                      