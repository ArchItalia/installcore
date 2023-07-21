#!/usr/bin/python
#
# Autore : 
# Data: 
# Versione 1.0.0: 
#


import os
import tkinter as tk
import subprocess
from tkinter import PhotoImage
#from PIL import ImageTk, Image

#app = installCore(master=root)
root = tk.Tk(className='installCore')
root.title("installCore")
root.geometry("900x800")
root.minsize(900, 800)
root.maxsize(900, 800)
root.config(bg='#2e3440') 

# Icone
icon = tk.PhotoImage(file="./.assets/icon.png")
root.iconphoto(False, icon)
# Creazione etichette e campi di input
font = ("Architalia", 12, "bold")
font2 = ("Architalia", 26, "bold")
text = ("#d8dee9")
polardark = ("#2e3440") 
polarlight = ("#4c566a") 
polarmiddle = ("#3b4252")
snow = ("#d8dee9") 
frostdark = ("#5e81ac")
frostlight = ("#81a1c1")
green = ("#a3be8c")
red = ("#bf616a")
yellow = ("#ebcb8b")
purple = ("#b48ead")
orange = ("#d08770")




        
        
def save_options():
    # Salvataggio dei valori su file
    option1 = option1_entry.get()
    with open("./data/root", "w") as f:
        f.write(option1)
    option1b = option1b_entry.get()
    with open("./data/root_size", "w") as f:
        f.write(option1b)
    option2 = option2_entry.get()
    with open("./data/country", "w") as f:
        f.write(option2)
    option3 = option3_entry.get()
    with open("./data/localhost", "w") as f:
        f.write(option3)
    option4 = option4_entry.get()
    with open("./data/username", "w") as f:
        f.write(option4)
    option5 = option5_entry.get()
    with open("./data/realname", "w") as f:
        f.write(option5)
    option6 = option6_entry.get()
    with open("./data/rootpw", "w") as f:
        f.write(option6)
    option7 = option7_entry.get()
    with open("./data/userpw", "w") as f:
        f.write(option7)
    option8 = option8_entry.get()
    with open("./data/localegen", "w") as f:
        f.write(option8)
    option9 = option9_entry.get()
    with open("./data/localeconf", "w") as f:
        f.write(option9)
    option10 = option10_entry.get()
    with open("./data/keymap", "w") as f:
        f.write(option10)
    option11 = option11_entry.get()
    with open("./data/localtime", "w") as f:
        f.write(option11)
    option12 = option12_entry.get()
    with open("./data/zram", "w") as f:
        f.write(option12)
    option13 = option13_entry.get()
    with open("./data/efi", "w") as f:
        f.write(option13)
    option13b = option13b_entry.get()
    with open("./data/efi_size", "w") as f:
        f.write(option13b)
    option14 = option14_entry.get()
    with open("./data/home", "w") as f:
        f.write(option14)
    option14b = option14b_entry.get()
    with open("./data/disk", "w") as f:
        f.write(option14b)
        
    subprocess.Popen(['gnome-terminal', '--', '/bin/bash', '-c', './test; exec bash'])
  
  
        
disk = subprocess.check_output("ls /dev | grep -E '^sd[a-z]+$'", shell=True).decode().split()[0]

logo = tk.PhotoImage(file="./.assets/logo.png")
logo_label = tk.Label(root, image=logo, bd=0, bg=polardark)
logo_label.image = logo
logo_label.pack()

options_frame = tk.LabelFrame(root, text="Installation of Core Linux", font=font, fg=frostlight, bg=polardark)
options_frame.pack(pady=10, padx=0)

option2_label = tk.Label(options_frame, text="Country:", font=font, fg=text, bg=polardark)
option2_label.grid(row=0, column=0, padx=5, pady=5)
option2_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option2_entry.grid(row=0, column=1, padx=5, pady=5)
option2_entry.insert(0, "us")

option3_label = tk.Label(options_frame, text="Localhost:", font=font, fg=text, bg=polardark)
option3_label.grid(row=1, column=0, padx=5, pady=5)
option3_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option3_entry.grid(row=1, column=1, padx=5, pady=5)
option3_entry.insert(0, "core")

option4_label = tk.Label(options_frame, text="Username:", font=font, fg=text, bg=polardark)
option4_label.grid(row=2, column=0, padx=5, pady=5)
option4_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option4_entry.grid(row=2, column=1, padx=5, pady=5)
option4_entry.insert(0, "john")

option5_label = tk.Label(options_frame, text="Realname:", font=font, fg=text, bg=polardark)
option5_label.grid(row=3, column=0, padx=5, pady=5)
option5_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option5_entry.grid(row=3, column=1, padx=5, pady=5)
option5_entry.insert(0, "John Wick")

option6_label = tk.Label(options_frame, text="Root Password:", font=font, fg=text, bg=polardark)
option6_label.grid(row=4, column=0, padx=5, pady=5)
option6_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option6_entry.grid(row=4, column=1, padx=5, pady=5)
option6_entry.insert(0, "password")

option7_label = tk.Label(options_frame, text="User Password:", font=font, fg=text, bg=polardark)
option7_label.grid(row=5, column=0, padx=5, pady=5)
option7_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option7_entry.grid(row=5, column=1, padx=5, pady=5)
option7_entry.insert(0, "password")

option8_label = tk.Label(options_frame, text="Locale Gen:", font=font, fg=text, bg=polardark)
option8_label.grid(row=6, column=0, padx=5, pady=5)
option8_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option8_entry.grid(row=6, column=1, padx=5, pady=5)
option8_entry.insert(0, "en_US.UTF-8 UTF-8")

option9_label = tk.Label(options_frame, text="Language:", font=font, fg=text, bg=polardark)
option9_label.grid(row=7, column=0, padx=5, pady=5)
option9_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option9_entry.grid(row=7, column=1, padx=5, pady=5)
option9_entry.insert(0, "en_US.UTF-8")

option10_label = tk.Label(options_frame, text="Keymap:", font=font, fg=text, bg=polardark)
option10_label.grid(row=8, column=0, padx=5, pady=5)
option10_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option10_entry.grid(row=8, column=1, padx=5, pady=5)
option10_entry.insert(0, "us")

option11_label = tk.Label(options_frame, text="Local Time Zone:", font=font, fg=text, bg=polardark)
option11_label.grid(row=9, column=0, padx=5, pady=5)
option11_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option11_entry.grid(row=9, column=1, padx=5, pady=5)
option11_entry.insert(0, "Europe/London")

option12_label = tk.Label(options_frame, text="ZRAM Swap (GB):", font=font, fg=text, bg=polardark)
option12_label.grid(row=10, column=0, padx=5, pady=5)
option12_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option12_entry.grid(row=10, column=1, padx=5, pady=5)
option12_entry.insert(0, "16")

option13_label = tk.Label(options_frame, text="Partition EFI:", font=font, fg=text, bg=polardark)
option13_label.grid(row=11, column=0, padx=5, pady=5)
option13_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option13_entry.grid(row=11, column=1, padx=5, pady=5)
option13_entry.insert(0, disk + "1")
option13b_label = tk.Label(options_frame, text="Size (MB):", font=font, fg=text, bg=polardark)
option13b_label.grid(row=11, column=2, padx=5, pady=5)
option13b_entry = tk.Entry(options_frame, width=5, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option13b_entry.grid(row=11, column=3, padx=5, pady=5)
option13b_entry.insert(0, "512")

option1_label = tk.Label(options_frame, text="Partition Root:", font=font, fg=text, bg=polardark)
option1_label.grid(row=12, column=0, padx=20, pady=5)
option1_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option1_entry.grid(row=12, column=1, padx=5, pady=5)
option1_entry.insert(0, disk + "2")
option1b_label = tk.Label(options_frame, text="Size (GB):", font=font, fg=text, bg=polardark)
option1b_label.grid(row=12, column=2, padx=5, pady=5)
option1b_entry = tk.Entry(options_frame, width=5, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option1b_entry.grid(row=12, column=3, padx=5, pady=5)
option1b_entry.insert(0, "64")

option14_label = tk.Label(options_frame, text="Partition Home:", font=font, fg=text, bg=polardark)
option14_label.grid(row=13, column=0, padx=20, pady=5)
option14_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option14_entry.grid(row=13, column=1, padx=5, pady=5)
option14_entry.insert(0, disk + "3")

option14b_label = tk.Label(options_frame, text="Disk for Installation:", font=font, fg=text, bg=polardark)
option14b_label.grid(row=14, column=0, padx=20, pady=5)
option14b_entry = tk.Entry(options_frame, width=20, bg=snow,fg=polarmiddle,font=font, highlightthickness=0)
option14b_entry.grid(row=14, column=1, padx=5, pady=5)
option14b_entry.insert(0, disk)
        
# Creazione pulsante per salvare le opzioni
save_button = tk.Button(root, text="Install", command=save_options, font=font, fg=snow, bg=polarlight, highlightthickness=0)
save_button.pack(pady=15)
        
       # product_name = subprocess.check_output("sudo dmidecode -t baseboard | grep 'Product Name'", shell=True).decode().strip()
       # product_name = product_name.split()[2]
       
       # manufacturer = subprocess.check_output("sudo dmidecode -t baseboard | grep 'Manufacturer'", shell=True).decode().strip()
       # manufacturer = manufacturer.split()[1]
        
      #  optionxb_label = tk.Label(root, text=f"Real Machine {manufacturer} {product_name}", font=font, fg=green, bg=polardark)
      #  optionxb_label.pack(pady=5)
optionxb_label = tk.Label(root, text="UEFI, btrfs filesystem with subvolumes @, @home.", font=font, fg=yellow, bg=polardark)
optionxb_label.pack(pady=5)
        



root.mainloop()
