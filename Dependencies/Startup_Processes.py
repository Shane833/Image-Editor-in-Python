from win32api import GetSystemMetrics # importing required libraries
from PIL import ImageTk,Image


# make a fail safe in case the initialize function is not called first before calling the get_res function

# Class Definition

class Startup_Processes:
    # making variable to hold the current resolution values
    original_res_list = list() # Created an empty list to store the original resolutions
    new_res_list = list() # Created an empty list to store the new resolutions
    menu_scaling_factor = 0.4 # Fixed scaling factor
    menu_position_factor = list() # A list to hold the x and y factors for positioning of intro menu components
    editor_position_factor = list() # A list to hold the x and y factors for positioning of the edior components
    editor_scaling_factor = list() # A list to hold the x and y factors for scaling the editor components
    button_size_factor = list() # A list to hold various paramters related to button size
    
    
    def initialize(self):
        width = GetSystemMetrics(0) # retrieving screen width
        height = GetSystemMetrics(1) # retrieving screen height
        menu_width = int(self.menu_scaling_factor * width) # computing menu screen width
        menu_height = int(self.menu_scaling_factor * height) # computing menu screen height
        editor_geometry = str(width) + "x" + str(height) # converting the resolution into a single string since tkinter takes a single string as the resolution
        menu_geometry = str(menu_width) + "x" + str(menu_height)
        self.new_res_list = [editor_geometry, width, height, menu_geometry, menu_width, menu_height] # making a list of the resolutions to be written in the file

        # Getting baked data from the files
        file = open("Dependencies/Baked Data.txt",'r+')
        values = file.readlines() # storing the content of the file into a list
        for i in range(len(values)):
            self.original_res_list.append(int(values[i][:-1])) # Storing the values as integers in the list
        file.close()
        
        # Computing and storing the menu position factors into the list
        self.menu_position_factor.append(self.new_res_list[4] / self.original_res_list[2]) 
        self.menu_position_factor.append(self.new_res_list[5] / self.original_res_list[3])

        # Computing and storing the editor position factors into the list
        self.editor_position_factor.append(self.new_res_list[1]/self.original_res_list[0])
        self.editor_position_factor.append(self.new_res_list[2]/self.original_res_list[1])
        
        # Computing and storing the button size paramters
        self.button_size_factor.append(self.original_res_list[3] / 20) # Here the first paramter is the button width which is being factorized in relation to the menu height
                                                                  # Here 20 is the original button width at the original resolution
        self.button_size_factor.append(self.original_res_list[3] / 10) # This second parameter is for the button size and is computed on same basis as the 

    def resize_logo(self): # This function will resize the logo according to the given arguments which are window width and height
        original = Image.open("Dependencies/System_Images/imx final.png") # Opening our original image file
        resized = original.resize((int(self.new_res_list[4] / 2),int(0.75 * self.new_res_list[5]))) # This function takes in a tuple as an argument in the form (width,height)
        resized.save("Dependencies/System_Images/logo.png")

    def __init__(self): # Class Constructor
        self.initialize() # Calling the initialize function for first time 
        self.resize_logo() # Calling resize function to resize the logo
