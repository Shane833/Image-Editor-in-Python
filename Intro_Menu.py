from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox 
from ttkbootstrap import *
import ttkbootstrap as tb
from PIL import ImageTk,Image
import os
import sys
sys.path.insert(0,"./Dependencies/") # Adds this folder to the system variables
from Startup_Processes import * # The Dependencies folder contains this module which is required

global filename # This variable will hold the path directory of the project file
global startup # This will be an object of Startup Processes which will be used to access various variables
global project_filename # This is the string values which is retrieved after the 
global start_editor # A variable to know if to start the main editor or not

# Creating an object of Startup Processes Class
startup = Startup_Processes()

# Basic window setup
root = tb.Window(themename = "darkly") # Set the theme of the application using pre-defined stylenames
root.title("IMX Image Editor") # sets the title of the window
root.iconbitmap("Dependencies/System_Images/logo4.ico") # iconbitmap() member function takese the path of the *.ico file which is to assigned as the icon of the application
root.resizable(False,False) # You can disable resizing on a window by passing two False arguments in the resizable method
root.geometry(startup.new_res_list[3]) # takes a string of resolution the form "widthxheight"
root.position_center() # positions the window in the center of the screen at the launch
root.update_idletasks() # it helps the application perform background tasks and continue even in case of user inactivity

# making a canvas equal to the dimensions of the window
canv = tk.Canvas(root,width = startup.new_res_list[4],height = startup.new_res_list[5])
canv.pack(fill = "both",expand = True)

# Opening the resized image to be applied as the background image in the intro menu
logo_img = ImageTk.PhotoImage(Image.open("Dependencies/System_Images/logo.png")) # ImageTk.PhotoImage() converts the image into tkinter supported format
canv.create_image(int(0.4 * startup.new_res_list[4]),int(0.125 * startup.new_res_list[5]),image = logo_img,anchor = "nw") # Displaying the image on the canvas with proper positioning

# Creating a top level for the main editor
def Main_Editor(project_filename):
    
    editor = Toplevel()
    editor.title("IMX Image Editor ~ " + str(project_filename))
    editor.geometry(startup.new_res_list[0])
    editor.state('zoomed')
    #editor.attributes('-fullscreen',True)
    editor.resizable(False,True)
    editor.position_center()
    
    # Creating one big canvas to hold other small canvases
    e_canv = tk.Canvas(editor,width = startup.new_res_list[1],height = startup.new_res_list[2])
    e_canv.pack(fill = "both",expand = True)
    
    # This rectangle will responsible for showing where area on the screen reserved for the image
    e_canv.create_rectangle(int(0.125 * startup.new_res_list[1]),int(0.10 * startup.new_res_list[2]),int(0.125 * startup.new_res_list[1] + 0.7 * startup.new_res_list[1]),int(0.10 * startup.new_res_list[2] + 0.8 * startup.new_res_list[2]),fill = "#808080")

    # This rectangle shows the area designated for the tools
    e_canv.create_rectangle(int(0.025 * startup.new_res_list[1]),int(0.10 * startup.new_res_list[2]),int(0.025 * startup.new_res_list[1] + 0.075 * startup.new_res_list[1]),int(0.10 * startup.new_res_list[2] + 0.8 * startup.new_res_list[2]),outline = "#808080")

    # This rectangle depicts the area reserved for the layers
    e_canv.create_rectangle(int(0.85 * startup.new_res_list[1]),int(0.10 * startup.new_res_list[2]),int(0.85 * startup.new_res_list[1] + 0.125 * startup.new_res_list[1]),int(0.10 * startup.new_res_list[2] + 0.38 * startup.new_res_list[2]),outline = "#808080")
    
    # This rectangle is for showing the functionality of the various tools
    e_canv.create_rectangle(int(0.85 * startup.new_res_list[1]),int(0.5 * startup.new_res_list[2]),int(0.85 * startup.new_res_list[1] + 0.125 * startup.new_res_list[1]),int(0.10 * startup.new_res_list[2] + 0.65 * startup.new_res_list[2]),outline = "#808080")
    
    def add_image():
        image_path = filedialog.askopenfilenames(title = "Add Images",filetypes = (("PNG image","*.png"),("JPG image","*.jpg"),("JPEG image","*.jpeg"),("All Files","*.*")))
        if image_path == "":
            print("Empty") # display message box with message = No image selected
            messagebox.showinfo("Alert","No image was selected!!!") # Displays a popup when no image is selected
        else:
            print(image_path)
            #opened_img = ImageTk.PhotoImage(Image.open(str(image_path[0])))
            # Just some work around in order to display the image for now, later will be binded into a function
            opened_img = Image.open(str(image_path[0]))
            opened_img.save("copied.png")
            new_img = Image.open("copied.png")
            display_img = ImageTk.PhotoImage(new_img)
            e_canv.create_image(0,0,image = display_img,anchor = "nw")

    def close_editor():
        root.deiconify() # This command will show the editor again
        back_button() # This command will showcase the opening screen on the intro menu
        editor.destroy() # closes the editor window

    # This function will check the current tool selected and call another function to perform the specific task
    def check_tool():
        if tool_var.get() == 1:
            pass
    
    # Declaration of buttons
    tool_var = IntVar()
    tool_var.set("0")

    crop_img = ImageTk.PhotoImage(Image.open("Dependencies/System_Images/resized_crop.png"))
    crop_but = tb.Checkbutton(editor,text = "Crop",bootstyle = "light,toolbutton",image = crop_img,variable = tool_var,onvalue = 1,offvalue = 0,command = check_tool)
    w_crop_but = e_canv.create_window(int(0.065 * startup.new_res_list[1]),int(0.16 * startup.new_res_list[2]),window = crop_but)
    e_canv.create_text(int(0.065 * startup.new_res_list[1]),int(0.2175 * startup.new_res_list[2]),text = "Crop",fill = "#adb5bd")

    rotate_img = ImageTk.PhotoImage(Image.open("Dependencies/System_Images/resized_rotate.png"))
    rotate_but = tb.Checkbutton(editor,bootstyle = "light,toolbutton",image = rotate_img,variable = tool_var,onvalue = 2,offvalue = 0,command = check_tool)
    w_rotate_but = e_canv.create_window(int(0.065 * startup.new_res_list[1]),int(0.2875 * startup.new_res_list[2]),window = rotate_but)
    e_canv.create_text(int(0.065 * startup.new_res_list[1]),int(0.345 * startup.new_res_list[2]),text = "Rotate",fill = "#adb5bd")

    text_img = ImageTk.PhotoImage(Image.open("Dependencies/System_Images/resized_text.png"))
    text_but = tb.Checkbutton(editor,bootstyle = "light,toolbutton",image = text_img,variable = tool_var,onvalue = 3,offvalue = 0,command = check_tool)
    w_text_but = e_canv.create_window(int(0.065 * startup.new_res_list[1]),int(0.42 * startup.new_res_list[2]),window = text_but)
    e_canv.create_text(int(0.065 * startup.new_res_list[1]),int(0.4775 * startup.new_res_list[2]),text = "Add Text",fill = "#adb5bd")

    level_img = ImageTk.PhotoImage(Image.open("Dependencies/System_Images/resized_levels.png"))
    level_but = tb.Checkbutton(editor,bootstyle = "light,toolbutton",image = level_img,variable = tool_var,onvalue = 4,offvalue = 0,command = check_tool)
    w_level_but = e_canv.create_window(int(0.065 * startup.new_res_list[1]),int(0.56 * startup.new_res_list[2]),window = level_but)
    e_canv.create_text(int(0.065 * startup.new_res_list[1]),int(0.6175 * startup.new_res_list[2]),text = "Adjust Levels",fill = "#adb5bd")
  
    merge_img = ImageTk.PhotoImage(Image.open("Dependencies/System_Images/resized_merge.png"))
    merge_but = tb.Checkbutton(editor,bootstyle = "light,toolbutton",image = merge_img,variable = tool_var,onvalue = 5,offvalue = 0,command = check_tool)
    w_merge_but = e_canv.create_window(int(0.065 * startup.new_res_list[1]),int(0.70 * startup.new_res_list[2]),window = merge_but)
    e_canv.create_text(int(0.065 * startup.new_res_list[1]),int(0.7575 * startup.new_res_list[2]),text = "Merge",fill = "#adb5bd")

    save_img = ImageTk.PhotoImage(Image.open("Dependencies/System_Images/resized_save.png"))
    save_but = tb.Checkbutton(editor,bootstyle = "light,toolbutton",image = save_img,variable = tool_var,onvalue = 6,offvalue = 0)
    w_save_but = e_canv.create_window(int(0.065 * startup.new_res_list[1]),int(0.835 * startup.new_res_list[2]),window = save_but)
    e_canv.create_text(int(0.065 * startup.new_res_list[1]),int(0.8875 * startup.new_res_list[2]),text = "Save",fill = "#adb5bd")
    
    # This button assigns the images to a specific image object
    add_img_but = tb.Button(editor,text = "Add Images",bootstyle = "success,outline",width = 20,command = add_image)
    w_add_img_but = e_canv.create_window(int(0.9125 * startup.new_res_list[1]),int(0.14 * startup.new_res_list[2]),window = add_img_but)
    
    e_canv.create_text(int(0.9 * startup.new_res_list[1]),int(0.65 * startup.new_res_list[2]),text = "HI",fill = "#adb5bd")

    # This is a common variable for the toolbuttons representing the different images
    img_but_var = IntVar()
    
    # These are all the buttons representing the images
    img_but_1 = tb.Checkbutton(editor,text = "Image 1",bootstyle = "light,toolbutton",variable = img_but_var,onvalue = 1,offvalue = 0,width = 20)
    w_img_but_1 = e_canv.create_window(int(0.9125 * startup.new_res_list[1]),int(0.20 * startup.new_res_list[2]),window = img_but_1)

    img_but_2 = tb.Checkbutton(editor,text = "Image 2",bootstyle = "light,toolbutton",variable = img_but_var,onvalue = 2,offvalue = 0,width = 20)
    w_img_but_2 = e_canv.create_window(int(0.9125 * startup.new_res_list[1]),int(0.26 * startup.new_res_list[2]),window = img_but_2)

    img_but_3 = tb.Checkbutton(editor,text = "Image 3",bootstyle = "light,toolbutton",variable = img_but_var,onvalue = 3,offvalue = 0,width = 20)
    w_img_but_3 = e_canv.create_window(int(0.9125 * startup.new_res_list[1]),int(0.32 * startup.new_res_list[2]),window = img_but_3)

    img_but_4 = tb.Checkbutton(editor,text = "Image 4",bootstyle = "light,toolbutton",variable = img_but_var,onvalue = 4,offvalue = 0,width = 20)
    w_img_but_4 = e_canv.create_window(int(0.9125 * startup.new_res_list[1]),int(0.38 * startup.new_res_list[2]),window = img_but_4)

    img_but_5 = tb.Checkbutton(editor,text = "Image 5",bootstyle = "light,toolbutton",variable = img_but_var,onvalue = 5,offvalue = 0,width = 20)
    w_img_but_5 = e_canv.create_window(int(0.9125 * startup.new_res_list[1]),int(0.44 * startup.new_res_list[2]),window = img_but_5)
    
    # This is the quit button
    quit_but = Button(editor,text = "Quit",bootstyle = "danger,outline",command = close_editor)
    w_but = e_canv.create_window(int(0.9575 * startup.new_res_list[1]),int(0.05 * startup.new_res_list[2]),window = quit_but)
    
    print(e_canv.find_withtag("quit_but"))
    editor.mainloop() # End of the Editor's loop
    

# Function definitions for Intro_Menu
def new_project_file():
    # when new button is pressed we will hide all the existing button and make the new buttons appear
    for i in range(2,6):
        canv.itemconfig(i,state = "hidden")
    for i in range(6,10):
        canv.itemconfig(i,state = "normal")
    entry_field.insert(0,"Untitled") # By default we provide the entry menu with some value

def open_project_file():
    # This opens a file explorer dialog box through which the user can browse and select the project
    filename = filedialog.askopenfilenames(title = "Open Project Files",filetypes = (("IMX project","*.imx"),("All Files","*.*")))
    if filename == "":
        print("Empty")
    else:
        print(filename)

def options():
    pass

def create_project():
    project_filename = entry_field.get() # .get() retrieves whatever is typed on the entry field
    root.withdraw() # This command hides the main window
    Main_Editor(project_filename) # calling this function to start the editor
    

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
button_style.configure('light.Outline.TButton',font = ("Helvetica",int(startup.new_res_list[5] / startup.button_size_factor[1])))

# Component declaration and definition
new_but = tb.Button(text = "New Project",style = "light.Outline.TButton",width = int(startup.new_res_list[5] / startup.button_size_factor[0]),command = new_project_file) # Obtaining the button width in accordance with the menu resolution
w_new_but = canv.create_window(int(100 * startup.menu_position_factor[0]),int(60 * startup.menu_position_factor[1]),window = new_but) # Positioning the button w.r.t the position factors

op_but = tb.Button(text = "Open Project",style = "light.Outline.TButton",width = int(startup.new_res_list[5] / startup.button_size_factor[0]),command = open_project_file)
w_op_but = canv.create_window(int(100 * startup.menu_position_factor[0]),int(100 * startup.menu_position_factor[1]),window = op_but)

opt_but = tb.Button(text = "Options",style = "light.Outline.TButton",width = int(startup.new_res_list[5] / startup.button_size_factor[0]),command = options)
w_opt_but = canv.create_window(int(100 * startup.menu_position_factor[0]),int(140 * startup.menu_position_factor[1]),window = opt_but)

exit_but = tb.Button(text = "Quit",style = "light.Outline.TButton",width = int(startup.new_res_list[5] / startup.button_size_factor[0]),command = close_window)
w_exit_but = canv.create_window(int(100 * startup.menu_position_factor[0]),int(180 * startup.menu_position_factor[1]),window = exit_but)

back_img = ImageTk.PhotoImage(Image.open("Dependencies/System_Images/small_back_arrow.png")) # Adding an image to the back button
back_but = tb.Button(style = "light.Outline.TButton",image = back_img,width = int((startup.new_res_list[5] / 2 ) / startup.button_size_factor[0]),command = back_button)
w_back_but = canv.create_window(int(45 * startup.menu_position_factor[0]),int(60 * startup.menu_position_factor[1]),window = back_but) 

create_but = tb.Button(text = "Create",style = "light.Outline.TButton",width = int((startup.new_res_list[5] / 2 ) / startup.button_size_factor[0]),command = create_project)
w_create_but = canv.create_window(int(136 * startup.menu_position_factor[0]),int(180 * startup.menu_position_factor[1]),window = create_but) 

# Creating an entry field to take input from the user
entry_field = tb.Entry(text = "Project Name",style = "light.TEntry",width = int(startup.new_res_list[5] / (startup.button_size_factor[0] / 1.25)))
entry_field.place(height = 50)
w_entry_field = canv.create_window(int(100 * startup.menu_position_factor[0]),int(130 * startup.menu_position_factor[1]),window = entry_field)


canv.create_text(int(100 * startup.menu_position_factor[0]),int(100 * startup.menu_position_factor[1]),text = "Project Name",font = ("Helvetica",int(startup.new_res_list[5] / startup.button_size_factor[1])),fill = "#808080")

for i in range(6,10): # By default we are hiding 4 elements
    canv.itemconfig(i,state = "hidden")
             
# A text with names of all the project members
canv.create_text(int(270 * startup.menu_position_factor[0]),int(280 * startup.menu_position_factor[1]),text = "-- Collaborative Project by : Anant, Keshav, Shivang, Shivam, Zeeshan --",font = ("Helvetica",int(startup.new_res_list[5] / startup.button_size_factor[1])),fill = "#adb5bd")

root.mainloop() # The whole application runs in a loop from the creation of the window to this very method 