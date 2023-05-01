# Importing the required modules
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from PIL import ImageTk,Image
from Startup_Processes import *
from Main_Editor import *
import os

class Intro_Menu:
    
    global filename # This variable will hold the path directory of the project file
    global startup # This will be an object of Startup Processes which will be used to access various variables
    global project_filename # This is the string values which is retrieved after the 
    
    def __init__(self): # Class Constructor
        # Creating an object of Startup Processes Class
        self.startup = Startup_Processes()

        # Basic window setup
        root = tb.Window(themename = "darkly") # Set the theme of the application using pre-defined stylenames
        root.title("IMX Image Editor") # sets the title of the window
        root.iconbitmap("logo4.ico") # iconbitmap() member function takese the path of the *.ico file which is to assigned as the icon of the application
        root.resizable(False,False) # You can disable resizing on a window by passing two False arguments in the resizable method
        root.geometry(self.startup.new_res_list[3]) # takes a string of resolution the form "widthxheight"
        root.position_center() # positions the window in the center of the screen at the launch
        root.update_idletasks() # it helps the application perform background tasks and continue even in case of user inactivity

        # making a canvas equal to the dimensions of the window
        canv = tk.Canvas(root,width = self.startup.new_res_list[4],height = self.startup.new_res_list[5])
        canv.pack(fill = "both",expand = True)

        # Opening the resized image to be applied as the background image in the intro menu
        logo_img = ImageTk.PhotoImage(Image.open("logo.png")) # ImageTk.PhotoImage() converts the image into tkinter supported format
        canv.create_image(int(0.4 * self.startup.new_res_list[4]),int(0.125 * self.startup.new_res_list[5]),image = logo_img,anchor = "nw") # Displaying the image on the canvas with proper positioning
        
        # Function definitions
        def new_project_file():
            # when new button is pressed we will hide all the existing button and make the new buttons appear
            for i in range(2,6):
                canv.itemconfig(i,state = "hidden")
            for i in range(6,10):
                canv.itemconfig(i,state = "normal")
            entry_field.insert(0,"Untitled") # By default we provide the entry menu with some value
        
        def open_project_file():
            # This opens a file explorer dialog box through which the user can browse and select the project
            self.filename = filedialog.askopenfilenames(title = "Open Project Files",filetypes = (("IMX project","*.imx"),("All Files","*.*")))
            if self.filename == "":
                print("Empty")
            else:
                print(self.filename)

        def options():
            pass

        def create_project():
            self.project_filename = entry_field.get() # .get() retrieves whatever is typed on the entry field
            root.destroy() # This will close the existing window
            main = Main_Editor(self.startup,self.project_filename)  
        
        def back_button():
            # If back button pressed showing all the previous buttons and hiding the new ones
            for i in range(2,6):
                canv.itemconfig(i,state = "normal")
            for i in range(6,10):
                canv.itemconfig(i,state = "hidden")
            entry_field.delete(0,END)
            
        def close_window(): 
            root.destroy() # This will close the window
        
        # Varible Declaration
        button_style = tb.Style() # This style widget will let us change the button size
        button_style.configure('light.Outline.TButton',font = ("Helvetica",int(self.startup.new_res_list[5] / self.startup.button_size_factor[1])))

        # Component declaration and definition
        new_but = tb.Button(text = "New Project",style = "light.Outline.TButton",width = int(self.startup.new_res_list[5] / self.startup.button_size_factor[0]),command = new_project_file) # Obtaining the button width in accordance with the menu resolution
        w_new_but = canv.create_window(int(100 * self.startup.menu_position_factor[0]),int(60 * self.startup.menu_position_factor[1]),window = new_but) # Positioning the button w.r.t the position factors

        op_but = tb.Button(text = "Open Project",style = "light.Outline.TButton",width = int(self.startup.new_res_list[5] / self.startup.button_size_factor[0]),command = open_project_file)
        w_op_but = canv.create_window(int(100 * self.startup.menu_position_factor[0]),int(100 * self.startup.menu_position_factor[1]),window = op_but)

        opt_but = tb.Button(text = "Options",style = "light.Outline.TButton",width = int(self.startup.new_res_list[5] / self.startup.button_size_factor[0]),command = options)
        w_opt_but = canv.create_window(int(100 * self.startup.menu_position_factor[0]),int(140 * self.startup.menu_position_factor[1]),window = opt_but)

        exit_but = tb.Button(text = "Quit",style = "light.Outline.TButton",width = int(self.startup.new_res_list[5] / self.startup.button_size_factor[0]),command = close_window)
        w_exit_but = canv.create_window(int(100 * self.startup.menu_position_factor[0]),int(180 * self.startup.menu_position_factor[1]),window = exit_but)
    
        back_img = ImageTk.PhotoImage(Image.open("small_back_arrow.png")) # Adding an image to the back button
        back_but = tb.Button(style = "light.Outline.TButton",image = back_img,width = int((self.startup.new_res_list[5] / 2 ) / self.startup.button_size_factor[0]),command = back_button)
        w_back_but = canv.create_window(int(45 * self.startup.menu_position_factor[0]),int(60 * self.startup.menu_position_factor[1]),window = back_but) 
        
        create_but = tb.Button(text = "Create",style = "light.Outline.TButton",width = int((self.startup.new_res_list[5] / 2 ) / self.startup.button_size_factor[0]),command = create_project)
        w_create_but = canv.create_window(int(136 * self.startup.menu_position_factor[0]),int(180 * self.startup.menu_position_factor[1]),window = create_but) 
        
        entry_field = tb.Entry(text = "Project Name",style = "light.TEntry",width = int(self.startup.new_res_list[5] / (self.startup.button_size_factor[0] / 1.25)))
        entry_field.place(height = 50)
        w_entry_field = canv.create_window(int(100 * self.startup.menu_position_factor[0]),int(130 * self.startup.menu_position_factor[1]),window = entry_field)
        
        
        canv.create_text(int(100 * self.startup.menu_position_factor[0]),int(100 * self.startup.menu_position_factor[1]),text = "Project Name",font = ("Helvetica",int(self.startup.new_res_list[5] / self.startup.button_size_factor[1])),fill = "#808080")
        
        for i in range(6,10): # By default we are hiding 4 elements
            canv.itemconfig(i,state = "hidden")
                     
        # A text with names of all the project members
        canv.create_text(int(270 * self.startup.menu_position_factor[0]),int(280 * self.startup.menu_position_factor[1]),text = "-- Collaborative Project by : Anant, Keshav, Shivang, Shivam, Zeeshan --",font = ("Helvetica",int(self.startup.new_res_list[5] / self.startup.button_size_factor[1])),fill = "#adb5bd")
        
        root.mainloop() # The whole application runs in a loop from the creation of the window to this very method

