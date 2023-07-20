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
from PIL import ImageTk, Image


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Creazione etichette e campi di input
        font = ("Architalia", 12, "bold")
        text = ("#d8dee9")
        textbk = ("#2e3440") 
        font2 = ("Architalia", 26, "bold")
        text2 = ("#d8dee9")
        textbk2 = ("#2e3440") 
        text3 = ("#d8dee9")
        textbk3 = ("#4c566a") 
        text4 = ("#3b4252")
        textbk4 = ("#d8dee9") 
        
        self.disk = subprocess.check_output("ls /dev | grep -E '^sd[a-z]+$'", shell=True).decode().split()[0]
        
        logo = tk.PhotoImage(file="./.assets/logo.png")
        self.logo_label = tk.Label(self.master, image=logo, bd=0, bg=textbk)
        self.logo_label.image = logo
        self.logo_label.pack()
        
        options_frame = tk.LabelFrame(self.master, text="installation settings", font=font, fg=text, bg=textbk)
        options_frame.pack(pady=20, padx=0)
        
        self.option2_label = tk.Label(options_frame, text="Country:", font=font, fg=text, bg=textbk)
        self.option2_label.grid(row=0, column=0, padx=5, pady=5)
        self.option2_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option2_entry.grid(row=0, column=1, padx=5, pady=5)
        self.option2_entry.insert(0, "us")
        
        self.option3_label = tk.Label(options_frame, text="Localhost:", font=font, fg=text, bg=textbk)
        self.option3_label.grid(row=1, column=0, padx=5, pady=5)
        self.option3_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option3_entry.grid(row=1, column=1, padx=5, pady=5)
        self.option3_entry.insert(0, "core")
        
        self.option4_label = tk.Label(options_frame, text="Username:", font=font, fg=text, bg=textbk)
        self.option4_label.grid(row=2, column=0, padx=5, pady=5)
        self.option4_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option4_entry.grid(row=2, column=1, padx=5, pady=5)
        self.option4_entry.insert(0, "john")
        
        self.option5_label = tk.Label(options_frame, text="Realname:", font=font, fg=text, bg=textbk)
        self.option5_label.grid(row=3, column=0, padx=5, pady=5)
        self.option5_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option5_entry.grid(row=3, column=1, padx=5, pady=5)
        self.option5_entry.insert(0, "John Wick")
        
        self.option6_label = tk.Label(options_frame, text="Root Password:", font=font, fg=text, bg=textbk)
        self.option6_label.grid(row=4, column=0, padx=5, pady=5)
        self.option6_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option6_entry.grid(row=4, column=1, padx=5, pady=5)
        self.option6_entry.insert(0, "password")
        
        self.option7_label = tk.Label(options_frame, text="User Password:", font=font, fg=text, bg=textbk)
        self.option7_label.grid(row=5, column=0, padx=5, pady=5)
        self.option7_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option7_entry.grid(row=5, column=1, padx=5, pady=5)
        self.option7_entry.insert(0, "password")
        
        self.option8_label = tk.Label(options_frame, text="Locale Gen:", font=font, fg=text, bg=textbk)
        self.option8_label.grid(row=6, column=0, padx=5, pady=5)
        self.option8_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option8_entry.grid(row=6, column=1, padx=5, pady=5)
        self.option8_entry.insert(0, "en_US.UTF-8 UTF-8")
        
        self.option9_label = tk.Label(options_frame, text="Language:", font=font, fg=text, bg=textbk)
        self.option9_label.grid(row=7, column=0, padx=5, pady=5)
        self.option9_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option9_entry.grid(row=7, column=1, padx=5, pady=5)
        self.option9_entry.insert(0, "en_US.UTF-8")
        
        self.option10_label = tk.Label(options_frame, text="Keymap:", font=font, fg=text, bg=textbk)
        self.option10_label.grid(row=8, column=0, padx=5, pady=5)
        self.option10_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option10_entry.grid(row=8, column=1, padx=5, pady=5)
        self.option10_entry.insert(0, "us")
        
        self.option11_label = tk.Label(options_frame, text="Local Time Zone:", font=font, fg=text, bg=textbk)
        self.option11_label.grid(row=9, column=0, padx=5, pady=5)
        self.option11_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option11_entry.grid(row=9, column=1, padx=5, pady=5)
        self.option11_entry.insert(0, "Europe/London")
        
        self.option12_label = tk.Label(options_frame, text="ZRAM Swap (GB):", font=font, fg=text, bg=textbk)
        self.option12_label.grid(row=10, column=0, padx=5, pady=5)
        self.option12_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option12_entry.grid(row=10, column=1, padx=5, pady=5)
        self.option12_entry.insert(0, "16")
        
        self.option13_label = tk.Label(options_frame, text="Partition EFI:", font=font, fg=text, bg=textbk)
        self.option13_label.grid(row=11, column=0, padx=5, pady=5)
        self.option13_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option13_entry.grid(row=11, column=1, padx=5, pady=5)
        self.option13_entry.insert(0, self.disk + "1")
        self.option13b_label = tk.Label(options_frame, text="Size (MB):", font=font, fg=text, bg=textbk)
        self.option13b_label.grid(row=11, column=2, padx=5, pady=5)
        self.option13b_entry = tk.Entry(options_frame, width=5, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option13b_entry.grid(row=11, column=3, padx=5, pady=5)
        self.option13b_entry.insert(0, "512")
        
        self.option1_label = tk.Label(options_frame, text="Partition Root:", font=font, fg=text, bg=textbk)
        self.option1_label.grid(row=12, column=0, padx=20, pady=5)
        self.option1_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option1_entry.grid(row=12, column=1, padx=5, pady=5)
        self.option1_entry.insert(0, self.disk + "2")
        self.option1b_label = tk.Label(options_frame, text="Size (GB):", font=font, fg=text, bg=textbk)
        self.option1b_label.grid(row=12, column=2, padx=5, pady=5)
        self.option1b_entry = tk.Entry(options_frame, width=5, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option1b_entry.grid(row=12, column=3, padx=5, pady=5)
        self.option1b_entry.insert(0, "64")
        
        self.option14_label = tk.Label(options_frame, text="Partition Home:", font=font, fg=text, bg=textbk)
        self.option14_label.grid(row=13, column=0, padx=20, pady=5)
        self.option14_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option14_entry.grid(row=13, column=1, padx=5, pady=5)
        self.option14_entry.insert(0, self.disk + "3")
        
        self.option14b_label = tk.Label(options_frame, text="Disk for Installation:", font=font, fg=text, bg=textbk)
        self.option14b_label.grid(row=14, column=0, padx=20, pady=5)
        self.option14b_entry = tk.Entry(options_frame, width=20, bg=textbk4,fg=text4,font=font, highlightthickness=0)
        self.option14b_entry.grid(row=14, column=1, padx=5, pady=5)
        self.option14b_entry.insert(0, self.disk)
        
        # Creazione pulsante per salvare le opzioni
        self.save_button = tk.Button(self.master, text="Install", command=self.save_options, font=font, fg=text3, bg=textbk3, highlightthickness=0)
        self.save_button.pack(pady=15)
        
    def save_options(self):
        # Salvataggio dei valori su file
        option1 = self.option1_entry.get()
        with open("./data/root", "w") as f:
            f.write(option1)
        option1b = self.option1b_entry.get()
        with open("./data/root_size", "w") as f:
            f.write(option1b)
        option2 = self.option2_entry.get()
        with open("./data/country", "w") as f:
            f.write(option2)
        option3 = self.option3_entry.get()
        with open("./data/localhost", "w") as f:
            f.write(option3)
        option4 = self.option4_entry.get()
        with open("./data/username", "w") as f:
            f.write(option4)
        option5 = self.option5_entry.get()
        with open("./data/realname", "w") as f:
            f.write(option5)
        option6 = self.option6_entry.get()
        with open("./data/rootpw", "w") as f:
            f.write(option6)
        option7 = self.option7_entry.get()
        with open("./data/userpw", "w") as f:
            f.write(option7)
        option8 = self.option8_entry.get()
        with open("./data/localegen", "w") as f:
            f.write(option8)
        option9 = self.option9_entry.get()
        with open("./data/localeconf", "w") as f:
            f.write(option9)
        option10 = self.option10_entry.get()
        with open("./data/keymap", "w") as f:
            f.write(option10)
        option11 = self.option11_entry.get()
        with open("./data/localtime", "w") as f:
            f.write(option11)
        option12 = self.option12_entry.get()
        with open("./data/zram", "w") as f:
            f.write(option12)
        option13 = self.option13_entry.get()
        with open("./data/efi", "w") as f:
            f.write(option13)
        option13b = self.option13b_entry.get()
        with open("./data/efi_size", "w") as f:
            f.write(option13b)
        option14 = self.option14_entry.get()
        with open("./data/home", "w") as f:
            f.write(option14)
        option14b = self.option14b_entry.get()
        with open("./data/disk", "w") as f:
            f.write(option14b)
            
        subprocess.Popen(['gnome-terminal', '--', '/bin/bash', '-c', './test; exec bash'])


root = tk.Tk()
app = Application(master=root)
root.title("InstallCore")
root.geometry("900x800")
root.minsize(900, 800)
root.maxsize(900, 800)
root.config(bg='#2e3440') 
#icons
icon = tk.PhotoImage(file="./.assets/icon.png")
root.iconphoto(False, icon)


app.mainloop()
