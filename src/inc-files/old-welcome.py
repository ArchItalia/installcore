#!/usr/bin/env python3
#
# Author : 
# Date: 
# Version 1.0.0: 
#

import tkinter as tk
import webbrowser
import subprocess
from PIL import Image, ImageTk

root = tk.Tk(className='Welcome') # definizione della root window
root.title("Welcome to Core Linux")
# Set window size
root.geometry("900x900")
root.minsize(900, 900) 
root.maxsize(900, 900)
polar = "#d8dee9"
nord = "#2e3440"
nord2 = "#4c566a"
# create the canvas and scrollbar widget
canvas = tk.Canvas(root, bg=nord, highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill='y')
canvas.config(yscrollcommand=scrollbar.set)
canvas.pack(expand=True, fill='both')
    
    

    
# create a new frame to hold the elements
frame = tk.Frame(canvas, bg=nord)
canvas.create_window((60, 0), window=frame, anchor='nw')
#visualizzazione immagine 0
image = Image.open("/usr/share/welcome/icn/core.png")
photo0 = ImageTk.PhotoImage(image)
label = tk.Label(frame, image=photo0, bg=nord)
label.grid(row=0, column=0, pady=15, sticky='n')
# Welcome Label
welcome_label = tk.Label(frame, text="Welcome to Core Linux!", font=("Architalia", 20), bg=nord, fg=polar)
welcome_label.grid(row=1, column=0, columnspan=2, pady=0, sticky='n')
# Description
description_label = tk.Label(frame, text="Core Linux is a distribution based on Arch Linux",font=("Architalia", 16), bg=nord, fg=polar)
description_label.grid(row=2, column=0, columnspan=2, pady=0, sticky='n')

#visualizzazione immagine 1
image = Image.open("/usr/share/welcome/icn/timeshift.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(frame, image=photo, bg=nord)
label.grid(row=3, column=0, pady=15, sticky='n')
# Timeshift Button
description_label2 = tk.Label(frame, text="Timeshift is a backup and system restore utility for Linux systems. \n It takes snapshots of the filesystem at regular intervals and allows users to easily restore the system\n to a previous point in time in case of system failure or data loss.",font=("Architalia", 12), bg=nord, fg=polar)
description_label2.grid(row=4, column=0, sticky='n',pady=15, padx=50)
timeshift_button = tk.Button(frame, text="Open Timeshift", font=("Architalia", 12),
                             bg=nord2, fg=polar, command=lambda: subprocess.Popen(["timeshift-launcher"]))
timeshift_button.grid(row=5, column=0, pady=(0,20), sticky='n', padx=50)
# visualizzazione immagine 2
image = Image.open("/usr/share/welcome/icn/color-folders.png")
photo2 = ImageTk.PhotoImage(image)
label2 = tk.Label(frame, image=photo2, bg=nord)
label2.grid(row=6, column=0, pady=15, sticky='n')
# Colored Folders Button
description_label2 = tk.Label(frame, text="Use Color-Folders to change the style of your Papirus folders. \nChoose one of 45 available colors.",font=("Architalia", 12), bg=nord, fg=polar)
description_label2.grid(row=7, column=0, sticky='n',pady=15, padx=50)

color_folders_button = tk.Button(frame, text="Open Color-folders", font=("Architalia", 12),
                         bg=nord2, fg=polar, command=lambda: subprocess.Popen(["gnome-terminal", "--", "sh", "-c", "/usr/bin/color-folders; echo Done - Press enter to exit; read _"]))
color_folders_button.grid(row=8, column=0, pady=(0,20), sticky='n', padx=50)
# visualizzazione immagine 3
image = Image.open("/usr/share/welcome/icn/clean.png")
photo3 = ImageTk.PhotoImage(image)
label2 = tk.Label(frame, image=photo3, bg=nord)
label2.grid(row=9, column=0, pady=15, sticky='n')

# Clean Button
description_label3 = tk.Label(frame, text="Clean is a tool created by the Core Linux team developers for system maintenance \nto remove orphan packages, package cache, user cache, and trash.",font=("Architalia", 12), bg=nord, fg=polar)
description_label3.grid(row=10, column=0, sticky='n',pady=15, padx=50)

color_folders_button = tk.Button(frame, text="Open Clean", font=("Architalia", 12),
                         bg=nord2, fg=polar, command=lambda: subprocess.Popen(["gnome-terminal", "--", "sh", "-c", "clean"]))
color_folders_button.grid(row=11, column=0, pady=(0,20), sticky='n', padx=50)
# Description
description_label4 = tk.Label(frame, text="",font=("Architalia", 10,"bold"), bg=nord, fg="#5e81ac")
description_label4.grid(row=12, column=0, columnspan=2, pady=0, sticky='n')
description_label5 = tk.Label(frame, text="Core Linux 2023.08 beta",font=("Architalia", 10,"bold"), bg=nord, fg=polar)
description_label5.grid(row=13, column=0, columnspan=2, pady=0, sticky='n')
description_label6 = tk.Label(frame, text="Core Linux is a project by Architalia community.",font=("Architalia", 10,"bold"), bg=nord, fg="#81a1c1")
description_label6.grid(row=14, column=0, columnspan=2, pady=0, sticky='n')
# Update the canvas scroll region when the frame size changes
frame.bind("<Configure>", lambda event, canvas=canvas: canvas.config(scrollregion=canvas.bbox("all")))
        
        

# Centering the frame
for i in range(8):
    frame.grid_rowconfigure(i, weight=1)
frame.grid_columnconfigure(0, weight=1)
        
    
        

# Start the application
root.mainloop()