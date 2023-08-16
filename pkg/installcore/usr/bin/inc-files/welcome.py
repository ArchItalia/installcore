#!/usr/bin/env python3
#
# Author :
# Date:
# Version 1.0.0:
# gtk3 glib2 pango gobject-introspection

import gi
import os
import shutil
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Pango


class ContentStyle:
    def __init__(self):
        self.font = 'Architalia'
        self.color = '#ffffff'

    def apply_to_label(self, label):
        label.override_font(Pango.FontDescription.from_string(self.font))
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA.from_string(self.color))


class SidebarStyle:
    def __init__(self):
        self.color = "#333333"
        self.size = 12
        self.font_desc = Pango.FontDescription()

    def set_font(self, font):
        self.font_desc.set_family(font)

    def set_color(self, color):
        self.color = color

    def set_size(self, size):
        self.size = size
        self.font_desc.set_size(size * Pango.SCALE)

    def apply_to_sidebar(self, sidebar):
        context = sidebar.get_style_context()
        css_provider = Gtk.CssProvider()
        css = ".sidebar-row { color: %s; }" % self.color
        css_provider.load_from_data(css.encode())
        context.add_provider(css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

        for row in sidebar.get_children():
            self.apply_to_sidebar_row(row)

    def apply_to_sidebar_row(self, row):
        for child in row.get_children():
            if isinstance(child, Gtk.Label):
                font_markup = "<span font_desc=\"%s\"><b>%s</b></span>" % (self.font_desc.to_string(), child.get_text())
                child.set_markup(font_markup)


class SidebarItem(Gtk.ListBoxRow):
    def __init__(self, icon_path, title, description):
        super().__init__()

        # Creazione di un contenitore per l'icona e il testo
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)

        # Aggiunta dell'icona all'interno del contenitore
        icon_pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(icon_path, 24, 24, True)
        icon_image = Gtk.Image()
        icon_image.set_from_pixbuf(icon_pixbuf)
        hbox.pack_start(icon_image, False, False, 0)

        # Aggiunta del titolo e della descrizione all'interno del contenitore come etichette
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        title_label = Gtk.Label(label=title, xalign=0)
        title_label.set_markup("<b>%s</b>" % title)
        vbox.pack_start(title_label, False, False, 0)

        description_label = Gtk.Label(label=description, xalign=0)
        vbox.pack_start(description_label, False, False, 0)

        hbox.pack_start(vbox, False, False, 0)

        # Aggiunta del contenitore alla riga della barra laterale
        self.add(hbox)


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_default_size(1000, 650)
        self.set_size_request(1000, 650)
        self.set_resizable(False)
        
        
        # Creazione della sidebar
        self.sidebar = Gtk.ListBox()
        self.sidebar.set_selection_mode(Gtk.SelectionMode.SINGLE)
        self.sidebar.connect("row-selected", self.on_sidebar_item_selected)

        # Impostazione della larghezza della sidebar
        self.sidebar.set_size_request(200, -1)

        # Aggiunta delle voci del menu alla sidebar
        sidebar_items = [
            {"icon_path": "/usr/share/welcome/icn/welcome.png", "title": "Welcome", "description": "About Core Linux"},
            {"icon_path": "/usr/share/welcome/icn/timeshift.png", "title": "Timeshift", "description": "First step"},
            {"icon_path": "/usr/share/welcome/icn/color-folders.png", "title": "Color Folders", "description": "Papirus folders"},
            {"icon_path": "/usr/share/welcome/icn/clean.png", "title": "Clean", "description": "System cleaner"},
            {"icon_path": "/usr/share/welcome/icn/downgrade.png", "title": "Downgrade", "description": "Roll back"},
            {"icon_path": "/usr/share/welcome/icn/reflector.png", "title": "Reflector", "description": "update mirrorlist"},
            {"icon_path": "/usr/share/welcome/icn/packages.png", "title": "Packages", "description": "Search and install"},
            {"icon_path": "/usr/share/welcome/icn/firewall.png", "title": "Security", "description": "Configure Firewall"}
        ]
        for item in sidebar_items:
            listbox_row = SidebarItem(item["icon_path"], item["title"], item["description"])
            self.sidebar.add(listbox_row)

        # Creazione del contenitore principale per sidebar e pagina di contenuto
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.add(main_box)

        # Aggiunta della sidebar al contenitore principale
        main_box.pack_start(self.sidebar, False, False, 0)

        # Creazione del contenitore per la pagina di contenuto
        content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        main_box.pack_start(content_box, True, True, 0)

        # Creazione delle pagine di contenuto
        self.pages = []

        
        # Pagina 1 welcome
        page1_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        page1_box.set_margin_top(40)
        
        output = subprocess.check_output('uname -r', shell=True)
        kernel = output.decode('utf-8').strip()
        image = Gtk.Image.new_from_file('/usr/share/welcome/icn/core.png')
        page1_box.pack_start(image, False, False, 0)
        
        label1_0 = Gtk.Label()
        label1_0.set_markup("<span font_desc='Helvetica Bold 25' foreground='#000000' font_family='Helvetica'> </span>")
        label1_1 = Gtk.Label()
        label1_1.set_markup("<span font_desc='Architalia Bold 25' foreground='#d8dee9' font_family='Architalia'>Welcome to Core Linux!</span>")
        label1_2 = Gtk.Label()
        label1_2.set_markup("<span font_desc='Architalia 20' foreground='#d8dee9' font_family='Architalia'>Core Linux is a distribution based on Arch Linux</span>")
        label1_3 = Gtk.Label()
        label1_3.set_markup("<span font_desc='Architalia 14' foreground='#81a1c1' font_family='Architalia'>Core Linux is a project developed by the Italian community team of Architalia.</span>")
        link_button0 = Gtk.LinkButton.new_with_label("", "")
        link_button = Gtk.LinkButton.new_with_label("https://architalia.github.io/core", "Web Site Core Linux")
        link_button2 = Gtk.LinkButton.new_with_label("https://architalia.github.io/site", "Web Site Architalia")
        link_button3 = Gtk.LinkButton.new_with_label("https://gitlab.com/architalialinux/ai-repo", "Repository")
        label1_4 = Gtk.Label()
        label1_4.set_markup("<span font_desc='Helvetica Bold 25' foreground='#000000' font_family='Helvetica'> </span>")
        label1_5a = Gtk.Label()
        label1_5a.set_markup(f"<span font_desc='Architalia 14' foreground='#ebcb8b' font_family='Architalia'>Kernel {kernel}</span>")
        label1_5 = Gtk.Label()
        label1_5.set_markup("<span font_desc='Architalia 14' foreground='#d8dee9' font_family='Architalia'>Core Linux 2023.08 Beta</span>")
        label1_6 = Gtk.Label()
        label1_6.set_markup("<span font_desc='Architalia 14' foreground='#81a1c1' font_family='Architalia'>Developed by Jonathan Sanfilippo, Klod Cripta.</span>")
        page1_box.pack_start(label1_0, False, False, 0)
        page1_box.pack_start(label1_1, False, False, 0)
        page1_box.pack_start(label1_2, False, False, 0)
        page1_box.pack_start(label1_3, False, False, 0)

        page1_box.pack_start(link_button0, False, False, 0)
        page1_box.pack_start(link_button, False, False, 0)
        page1_box.pack_start(link_button2, False, False, 0)
        page1_box.pack_start(link_button3, False, False, 0)
        page1_box.pack_start(label1_4, False, False, 0)
        page1_box.pack_start(label1_5a, False, False, 0)
        page1_box.pack_start(label1_5, False, False, 0)
        page1_box.pack_start(label1_6, False, False, 0)
        self.pages.append(page1_box)
        content_box.pack_start(page1_box, True, True, 0)
        
        # Pagina 2 timeshift
        page2_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        page2_box.set_margin_top(40)
        
        image = Gtk.Image.new_from_file('/usr/share/welcome/icn/timeshift.png')
        page2_box.pack_start(image, False, False, 0)

        
        label2_1 = Gtk.Label()
        label2_1.set_markup("<span font_desc='Architalia Bold 25' foreground='#d8dee9' font_family='Architalia'>Timeshift</span>")
        label2_2 = Gtk.Label()
        label2_2.set_markup("<span font_desc='Architalia Bold 14' foreground='#d8dee9' font_family='Architalia'>System restore tool for Linux</span>")
        label2_0 = Gtk.Label()
        label2_0.set_markup("<span font_desc='Helvetica Bold 25' foreground='#000000' font_family='Helvetica'> </span>")
        label2_3 = Gtk.Label()
        label2_3.set_markup("<span font_desc='Architalia 14' foreground='#d8dee9' font_family='Architalia'>Creates filesystem snapshots using rsync+hardlinks, or BTRFS snapshots.</span>")
        label2_4 =Gtk.Label()
        label2_4.set_markup("<span font_desc='Architalia 14' foreground='#81a1c1' font_family='Architalia'>A minimum of two daily and two boot snapshots are racommended.</span>")
        label2_5 =Gtk.Label()
        label2_5.set_markup("<span font_desc='Architalia 14' foreground='#ebcb8b' font_family='Architalia'>If anything breaks, you can then restore your computer to its previous working state.</span>")
        label2_00 = Gtk.Label()
        label2_00.set_markup("<span font_desc='Helvetica Bold 40' foreground='#000000' font_family='Helvetica'> </span>")
        
        button = Gtk.Button.new_with_label('Timeshift Launch')
        button.connect('clicked', lambda _: subprocess.check_call('timeshift-launcher', shell=True))
        button.set_size_request(200, 50) 
        
        page2_box.pack_start(label2_1, False, False, 0)
        page2_box.pack_start(label2_2, False, False, 0)
        page2_box.pack_start(label2_0, False, False, 0)
        page2_box.pack_start(label2_3, False, False, 0)
        page2_box.pack_start(label2_4, False, False, 0)
        page2_box.pack_start(label2_5, False, False, 0)
        page2_box.pack_start(label2_00, False, False, 0)
        page2_box.pack_start(button, False, False, 10)



        self.pages.append(page2_box)
        content_box.pack_start(page2_box, True, True, 0)
        
        # Pagina 3 color folders
        page3_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        page3_box.set_margin_top(40)
        
        command_output = subprocess.check_output('papirus-folders -l --theme Papirus-Dark | grep ">"', shell=True)
        folder = command_output.decode("utf-8")

        image0 = Gtk.Image.new_from_file('/usr/share/welcome/icn/color-folders.png')
        image = Gtk.Image.new_from_file('/usr/share/icons/Papirus-Dark/64x64/places/folder-favorites.svg')
        

        label3_000 = Gtk.Label()
        label3_000.set_markup("<span font_desc='Helvetica Bold 10' foreground='#000000' font_family='Helvetica'> </span>")
        label3_1 = Gtk.Label()
        label3_1.set_markup("<span font_desc='Architalia Bold 25' foreground='#d8dee9' font_family='Architalia'>Color Folders</span>")
        label3_2 = Gtk.Label()
        label3_2.set_markup("<span font_desc='Architalia Bold 14' foreground='#d8dee9' font_family='Architalia'>Choose your favorite color</span>")
        label3_0 = Gtk.Label()
        label3_0.set_markup("<span font_desc='Helvetica Bold 25' foreground='#000000' font_family='Helvetica'> </span>")
        label3_3 = Gtk.Label()
        label3_3.set_markup("<span font_desc='Architalia 14' foreground='#d8dee9' font_family='Architalia'>Use Color Folders to change the style of your Papirus folders.</span>")
        label3_4 =Gtk.Label()
        label3_4.set_markup("<span font_desc='Architalia 14' foreground='#81a1c1' font_family='Architalia'>There are 45 different color types available for your Papirus folders.</span>")
        label3_5 =Gtk.Label()
        label3_5.set_markup("<span font_desc='Architalia 14' foreground='#ebcb8b' font_family='Architalia'>To apply the selected color to the desktop icons,</span>")
        label3_6 =Gtk.Label()
        label3_6.set_markup("<span font_desc='Architalia 14' foreground='#ebcb8b' font_family='Architalia'>right-click on the desktop after choosing your preferred theme.</span>")
        label3_99 = Gtk.Label()
        label3_99.set_markup(f"<span font_desc='Architalia 12' foreground='#d8dee9' font_family='Architalia'>Current color{folder}</span>")
        label3_00 = Gtk.Label()
        label3_00.set_markup("<span font_desc='Helvetica Bold 40' foreground='#000000' font_family='Helvetica'> </span>")
        
        button = Gtk.Button.new_with_label('Color Folders Launch')
        button.connect('clicked', lambda _: subprocess.check_call(["gnome-terminal", "--", "/usr/bin/color-folders"], shell=False))
        button.set_size_request(200, 50)
        
        page3_box.pack_start(image0, False, False, 0)
        page3_box.pack_start(label3_000, False, False, 0)
        page3_box.pack_start(label3_1, False, False, 0)
        page3_box.pack_start(label3_2, False, False, 0)
        page3_box.pack_start(label3_0, False, False, 0)
        page3_box.pack_start(label3_3, False, False, 0)
        page3_box.pack_start(label3_4, False, False, 0)
        page3_box.pack_start(label3_5, False, False, 0)
        page3_box.pack_start(label3_6, False, False, 0)
        page3_box.pack_start(label3_00, False, False, 0)
        page3_box.pack_start(image, False, False, 0)
        page3_box.pack_start(label3_99, False, False, 0)
        page3_box.pack_start(button, False, False, 10)



        self.pages.append(page3_box)
        content_box.pack_start(page3_box, True, True, 0)
        
        # Pagina 4 clean
        page4_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        page4_box.set_margin_top(40)
        
        

        image0 = Gtk.Image.new_from_file('/usr/share/welcome/icn/clean.png')
        

        label4_000 = Gtk.Label()
        label4_000.set_markup("<span font_desc='Helvetica Bold 10' foreground='#000000' font_family='Helvetica'> </span>")
        label4_1 = Gtk.Label()
        label4_1.set_markup("<span font_desc='Architalia Bold 25' foreground='#d8dee9' font_family='Architalia'>Clean</span>")
        label4_2 = Gtk.Label()
        label4_2.set_markup("<span font_desc='Architalia Bold 14' foreground='#d8dee9' font_family='Architalia'>System Cleaner</span>")
        label4_0 = Gtk.Label()
        label4_0.set_markup("<span font_desc='Helvetica Bold 25' foreground='#000000' font_family='Helvetica'> </span>")
        label4_3 = Gtk.Label()
        label4_3.set_markup("<span font_desc='Architalia 14' foreground='#d8dee9' font_family='Architalia'>Clean is a tool created by the Core Linux team developers for system maintenance</span>")
        label4_4 =Gtk.Label()
        label4_4.set_markup("<span font_desc='Architalia 14' foreground='#81a1c1' font_family='Architalia'>to remove orphan packages, package cache, user cache, and trash.</span>")
        label4_6 =Gtk.Label()
        label4_6.set_markup("<span font_desc='Architalia 14' foreground='#ebcb8b' font_family='Architalia'>Just type the clean command or use the application in the menu.</span>")
        label4_00 = Gtk.Label()
        label4_00.set_markup("<span font_desc='Helvetica Bold 40' foreground='#000000' font_family='Helvetica'> </span>")
        
        button = Gtk.Button.new_with_label('Clean Launch')
        button.connect('clicked', lambda _: subprocess.check_call(["gnome-terminal", "--", "/usr/bin/clean"], shell=False))
        button.set_size_request(200, 50)
        
        page4_box.pack_start(image0, False, False, 0)
        page4_box.pack_start(label4_000, False, False, 0)
        page4_box.pack_start(label4_1, False, False, 0)
        page4_box.pack_start(label4_2, False, False, 0)
        page4_box.pack_start(label4_0, False, False, 0)
        page4_box.pack_start(label4_3, False, False, 0)
        page4_box.pack_start(label4_4, False, False, 0)
        page4_box.pack_start(label4_6, False, False, 0)
        page4_box.pack_start(label4_00, False, False, 0)
        page4_box.pack_start(button, False, False, 10)



        self.pages.append(page4_box)
        content_box.pack_start(page4_box, True, True, 0)
        


        # Pagina 5
        page5_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        page5_box.set_margin_top(40)

        image = Gtk.Image.new_from_file('/usr/share/welcome/icn/downgrade.png')
        label5_1 = Gtk.Label()
        label5_1.set_markup("<span font_desc='Architalia Bold 25' foreground='#d8dee9' font_family='Architalia'>Downgrade Packages</span>")
        label5_2 = Gtk.Label()
        label5_2.set_markup("<span font_desc='Architalia Bold 14' foreground='#d8dee9' font_family='Architalia'>Roll back to a previous package version</span>")
        label5_0 = Gtk.Label()
        label5_0.set_markup("<span font_desc='Helvetica Bold 25' foreground='#000000' font_family='Helvetica'> </span>")
        label5_3 = Gtk.Label()
        label5_3.set_markup("<span font_desc='Architalia 14' foreground='#d8dee9' font_family='Architalia'>Downgrade is a useful tool for rolling back to a previous package version.</span>")
        label5_4 = Gtk.Label()
        label5_4.set_markup("<span font_desc='Architalia 14' foreground='#81a1c1' font_family='Architalia'>Write the name of the package you want to downgrade and press the button.</span>")
        name_label = Gtk.Label()
        name_label.set_markup("<span font_desc='Architalia 14' foreground='#ebcb8b' font_family='Architalia'>Enter package name:</span>")
        
        def on_entry_changed(entry):
            pkg = entry.get_text()

        self.name_entry = Gtk.Entry()
        self.name_entry.set_placeholder_text("Enter package name")
        self.name_entry.set_size_request(200, 30)
        self.name_entry.connect('changed', self.on_entry_changed)

        button = Gtk.Button.new_with_label('Downgrade Launch')
        button.set_size_request(200, 50)
        button.connect('clicked', self.on_button_clicked)
        
        
        terminal="gnome-terminal" 
    

       
    
        page5_box.pack_start(image, False, False, 0)
        page5_box.pack_start(label5_1, False, False, 0)
        page5_box.pack_start(label5_2, False, False, 0)
        page5_box.pack_start(label5_0, False, False, 0)
        page5_box.pack_start(label5_3, False, False, 0)
        page5_box.pack_start(label5_4, False, False, 0)
        page5_box.pack_start(name_label, False, False, 10)
        page5_box.pack_start(self.name_entry, False, False, 0)
        page5_box.pack_start(button, False, False, 10)

        
        self.pages.append(page5_box)
        content_box.pack_start(page5_box, True, True, 0)


        # Pagina 6
        page6_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        page6_box.set_margin_top(40)
        
        image = Gtk.Image.new_from_file('/usr/share/welcome/icn/reflector.png')
        label6_1 = Gtk.Label()
        label6_1.set_markup("<span font_desc='Architalia Bold 25' foreground='#d8dee9' font_family='Architalia'>Reflector Pacman Mirrorlist</span>")
        label6_2 = Gtk.Label()
        label6_2.set_markup("<span font_desc='Architalia Bold 14' foreground='#d8dee9' font_family='Architalia'>Automatic mirrorlist generator</span>")
        label6_0 = Gtk.Label()
        label6_0.set_markup("<span font_desc='Helvetica Bold 25' foreground='#000000' font_family='Helvetica'> </span>")
        label6_3 = Gtk.Label()
        label6_3.set_markup("<span font_desc='Architalia 14' foreground='#d8dee9' font_family='Architalia'>Reflector is an automatic Pacman mirrorlist generator, optimized for faster downloads.</span>")
        label6_4 = Gtk.Label()
        label6_4.set_markup("<span font_desc='Architalia 14' foreground='#81a1c1' font_family='Architalia'>Enter the country and press the button to generate the mirrorlist.</span>")
        
        name_label = Gtk.Label()
        name_label.set_markup("<span font_desc='Architalia 14' foreground='#ebcb8b' font_family='Architalia'>Enter the country e.g. GB, NL</span>")
        self.name_entry = Gtk.Entry()
        self.name_entry.set_size_request(200, 30)
        
        buttonx = Gtk.Button.new_with_label('Reflector Launch')
        buttonx.set_size_request(200, 50)
        
        command = "reflector --verbose -c $country --latest 10 --age 12 --fastest 10 --protocol https --sort rate --save /etc/pacman.d/mirrorlist"
        buttonx.connect("clicked", lambda x: subprocess.check_call(["gnome-terminal", "--", "sh", "-c", command.replace("$country", self.name_entry.get_text())], shell=False))
        
        page6_box.pack_start(image, False, False, 0)
        page6_box.pack_start(label6_1, False, False, 0)
        page6_box.pack_start(label6_2, False, False, 0)
        page6_box.pack_start(label6_0, False, False, 0)
        page6_box.pack_start(label6_3, False, False, 0)
        page6_box.pack_start(label6_4, False, False, 0)
        page6_box.pack_start(name_label, False, False, 10)
        page6_box.pack_start(self.name_entry, False, False, 0)
        page6_box.pack_start(buttonx, False, False, 10)
        
        self.pages.append(page6_box)
        content_box.pack_start(page6_box, True, True, 0)


        # Pagina 7
        page7_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        page7_box.set_margin_top(40)
        
        image = Gtk.Image.new_from_file('/usr/share/welcome/icn/packages.png')
        label7_000 = Gtk.Label()
        label7_000.set_markup("<span font_desc='Helvetica Bold 10' foreground='#000000' font_family='Helvetica'> </span>")
        label7_1 = Gtk.Label()
        label7_1.set_markup("<span font_desc='Architalia Bold 25' foreground='#d8dee9' font_family='Architalia'>Package Search</span>")
        label7_2 = Gtk.Label()
        label7_2.set_markup("<span font_desc='Architalia Bold 14' foreground='#d8dee9' font_family='Architalia'>General Package Search Tool</span>")
        label7_0 = Gtk.Label()
        label7_0.set_markup("<span font_desc='Helvetica Bold 25' foreground='#000000' font_family='Helvetica'> </span>")
        label7_3 = Gtk.Label()
        label7_3.set_markup("<span font_desc='Architalia 14' foreground='#d8dee9' font_family='Architalia'>You can use one of the following commands to install packages:</span>")
        label7_4 = Gtk.Label()
        label7_4.set_markup("<span font_desc='Architalia 14' foreground='#81a1c1' font_family='Architalia'>Enter the package name you want to search for and press the button.</span>")
        
        name_label = Gtk.Label()
        name_label.set_markup("<span font_desc='Architalia 14' foreground='#ebcb8b' font_family='Architalia'>Enter the package name:</span>")
        
        def on_entry_changed(entry):
            pkgx = entry.get_text()

        self.name_entry2 = Gtk.Entry()
        self.name_entry2.set_placeholder_text("Enter package name")
        self.name_entry2.set_size_request(200, 30)
        self.name_entry2.connect('changed', self.on_entry_changed2) 


        button = Gtk.Button.new_with_label('Search')
        button.set_size_request(200, 50)
        button.connect('clicked', self.on_button_clicked2)
        
        button2 = Gtk.Button.new_with_label('Uninstall')
        button2.set_size_request(200, 50)
        button2.connect('clicked', self.on_button_clicked3)
        
 
        
        page7_box.pack_start(image, False, False, 0)
        page7_box.pack_start(label7_000, False, False, 0)
        page7_box.pack_start(label7_1, False, False, 0)
        page7_box.pack_start(label7_2, False, False, 0)
        page7_box.pack_start(label7_0, False, False, 0)
        page7_box.pack_start(label7_3, False, False, 0)
        page7_box.pack_start(label7_4, False, False, 0)
        page7_box.pack_start(name_label, False, False, 10)
        page7_box.pack_start(self.name_entry2, False, False, 0)
        page7_box.pack_start(button, False, False, 5)
        page7_box.pack_start(button2, False, False, 5)

        self.pages.append(page7_box)
        content_box.pack_start(page7_box, True, True, 0)

        # Pagina 8
        page8_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        page8_box.set_margin_top(40)
        
        image = Gtk.Image.new_from_file('/usr/share/welcome/icn/firewall.png')
        page8_box.pack_start(image, False, False, 0)

        
        label8_1 = Gtk.Label()
        label8_1.set_markup("<span font_desc='Architalia Bold 25' foreground='#d8dee9' font_family='Architalia'>Firewall</span>")
        label8_2 = Gtk.Label()
        label8_2.set_markup("<span font_desc='Architalia Bold 14' foreground='#d8dee9' font_family='Architalia'>Configuration tool for network security</span>")
        label8_0 = Gtk.Label()
        label8_0.set_markup("<span font_desc='Helvetica Bold 25' foreground='#000000' font_family='Helvetica'> </span>")
        label8_3 = Gtk.Label()
        label8_3.set_markup("<span font_desc='Architalia 14' foreground='#d8dee9' font_family='Architalia'>Monitors incoming and outgoing network traffic and blocks unauthorized access.</span>")
        label8_4 =Gtk.Label()
        label8_4.set_markup("<span font_desc='Architalia 14' foreground='#81a1c1' font_family='Architalia'>It is recommended to create rules based on your network's security requirements.</span>")
        label8_5 =Gtk.Label()
        label8_5.set_markup("<span font_desc='Architalia 14' foreground='#ebcb8b' font_family='Architalia'>In case of an attack or security breach, the firewall can prevent further damage to your system.</span>")
        label8_00 = Gtk.Label()
        label8_00.set_markup("<span font_desc='Helvetica Bold 40' foreground='#000000' font_family='Helvetica'> </span>")
        
        firewall_command = None
        if subprocess.call(['which', 'gufw'], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
            # Gufw is installed, set the button label and command
            firewall_button_label = 'Gufw Launch'
            firewall_command = 'gufw'
        elif subprocess.call(['which', 'firewall-config'], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
            # Firewall-config is installed, set the button label and command
            firewall_button_label = 'Firewall Config Launch'
            firewall_command = 'firewall-config'
        else:
            # No firewall tools are installed, disable the button
            firewall_button_label = 'No Firewall installed'
            firewall_button_enabled = False
        
        
        button = Gtk.Button.new_with_label(firewall_button_label)
        if firewall_command:
            button.connect('clicked', lambda _: subprocess.check_call(firewall_command, shell=True))
        button.set_size_request(200, 50)
        
        page8_box.pack_start(label8_1, False, False, 0)
        page8_box.pack_start(label8_2, False, False, 0)
        page8_box.pack_start(label8_0, False, False, 0)
        page8_box.pack_start(label8_3, False, False, 0)
        page8_box.pack_start(label8_4, False, False, 0)
        page8_box.pack_start(label8_5, False, False, 0)
        page8_box.pack_start(label8_00, False, False, 0)
        page8_box.pack_start(button, False, False, 10)



        self.pages.append(page8_box)
        content_box.pack_start(page8_box, True, True, 0)

        # Applicazione dello stile ai widget nella barra laterale.
        my_sidebar_style = SidebarStyle()
        my_sidebar_style.set_font('Architalia')
        my_sidebar_style.set_color('#333333')
        my_sidebar_style.set_size(12)
        my_sidebar_style.apply_to_sidebar(self.sidebar)

        # Mostra la prima pagina di contenuto all'avvio
        self.pages[0].show()

        

    def on_sidebar_item_selected(self, listbox, listbox_row):
        # Nasconde tutte le pagine e mostra solo quella selezionata dalla sidebar
        for page in self.pages:
            page.hide()

        selected_page_index = listbox_row.get_index()
        self.pages[selected_page_index].show()

    def on_entry_changed(self, entry):
        self.pkgx = entry.get_text()

    def on_button_clicked(self, widget):
        pkg = self.pkg
        print(f"il pacchetto: {pkg}")
        terminal="gnome-terminal"
        os.system(f"{terminal} -- /bin/bash -c 'sudo downgrade {pkg}'")    

    def on_entry_changed2(self, entry):
        self.pkg = entry.get_text()

    def on_button_clicked2(self, widget):
        if shutil.which('aura') is not None:
            aur_helper = 'sudo aura -Ss'
            stop = "; echo Done - Press enter to exit; read _"
        elif shutil.which('paru') is not None:
            aur_helper = 'paru'
            stop = "; echo Done - Press enter to exit; read _"
        elif shutil.which('yay') is not None:
            aur_helper = 'yay'
            stop = "; echo Done - Press enter to exit; read _"
        elif shutil.which('pikaur') is not None:
            aur_helper = 'pikaur'
            stop = "; echo Done - Press enter to exit; read _"
        else:
            raise Exception('Nessun helper AUR trovato')
        pkg = self.pkg
        print(f"il pacchetto: {pkg}")
        terminal="gnome-terminal"
        os.system(f"{terminal} -- /bin/bash -c '{aur_helper} {pkg} {stop}'")     
        


    def on_button_clicked3(self, widget):
        if shutil.which('aura') is not None:
            aur_helper = 'sudo aura -Rns'
            stop = "; echo Done - Press enter to exit; read _"
        elif shutil.which('paru') is not None:
            aur_helper = 'paru -Rns'
            stop = "; echo Done - Press enter to exit; read _"
        elif shutil.which('yay') is not None:
            aur_helper = 'yay -Rns'
            stop = "; echo Done - Press enter to exit; read _"
        elif shutil.which('pikaur') is not None:
            aur_helper = 'pikaur -Rns'
            stop = "; echo Done - Press enter to exit; read _"
        else:
            raise Exception('Nessun helper AUR trovato')
        pkg = self.pkg
        print(f"il pacchetto: {pkg}")
        terminal="gnome-terminal"
        os.system(f"{terminal} -- /bin/bash -c '{aur_helper} {pkg} {stop}'")      
        

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
