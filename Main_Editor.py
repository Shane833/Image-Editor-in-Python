# Importing the required modules
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from PIL import ImageTk,Image
import sys

class Main_Editor:

    #def __init__(self,*args): # Overloading the constructor based on the number of arguments
     #   if
    def __init__(self,startup,name):

        root = tb.Window(themename = "darkly") # Set the theme of the application using pre-defined stylenames
        root.title("IMX Image Editor ~ " + name) # sets the title of the window
        root.iconbitmap("logo4.ico") # iconbitmap() member function takese the path of the *.ico file which is to assigned as the icon of the application
        root.resizable(False,False) # You can disable resizing on a window by passing two False arguments in the resizable method
        root.geometry(startup.new_res_list[0]) # takes a string of resolution the form "widthxheight"
        root.position_center() # positions the window in the center of the screen at the launch
        root.attributes("-fullscreen",True) # providing this command will set the window size to fullscreen
        root.update_idletasks() # it helps the application perform background tasks and continue even in case of user inactivity


        # Creating one big canvas to hold other small canvases
        canv = tk.Canvas(root,width = startup.new_res_list[1],height = startup.new_res_list[2])
        canv.pack(fill = "both",expand = True)
        
        # Creating a second canvas where images will be displayed
        img_canv = tk.Canvas(canv,width = int(0.7 * startup.new_res_list[1]),height = int(0.8 * startup.new_res_list[2]))
        w_img_canv = canv.create_window(int(0.125 * startup.new_res_list[1]),int(0.10 * startup.new_res_list[2]),anchor = NW,window = img_canv)
        img_canv.configure(bg = "#808080")
        
        # Creating a third canvas for holding the tools
        tool_canv = tk.Canvas(canv,width = int(0.075 * startup.new_res_list[1]),height = int(0.8 * startup.new_res_list[2]))
        w_tool_canv = canv.create_window(int(0.025 * startup.new_res_list[1]),int(0.10 * startup.new_res_list[2]),anchor = NW,window = tool_canv)
        tool_canv.configure(bg = "white")

        # Creating a fourth canvas for displaying the no. of images currently present in the editor
        layer_canv = tk.Canvas(canv,width = int(0.125 * startup.new_res_list[1]),height = int(0.8 * startup.new_res_list[2]))
        w_layer_canv = canv.create_window(int(0.85 * startup.new_res_list[1]),int(0.10 * startup.new_res_list[2]),anchor = NW,window = layer_canv)
        layer_canv.configure(bg = "red")

        # Creating a fifth canvas for displaying options such as new file, open file quit etc
        option_canv = tk.Canvas(canv,width = int(0.5 * startup.new_res_list[1]),height = int(0.05 * startup.new_res_list[2]))
        w_option_canv = canv.create_window(int(0.025 * startup.new_res_list[1]),int(0.01 * startup.new_res_list[2]),anchor = NW,window = option_canv)
        option_canv.configure(bg = "yellow")
        
        root.mainloop()
    
