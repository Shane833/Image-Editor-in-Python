from PIL import Image
import os

class Image_Handler:

    global image

    def __init__(self,image_loc):
        self.image = Image.open(image_loc)

    def get_image():
        return self.image

    