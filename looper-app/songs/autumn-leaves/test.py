import tkinter as tk
from PIL import Image, ImageTk
import os
import time

class ImageSlider:
    def __init__(self, root, image_folder):
        self.root = root
        self.image_folder = image_folder
        self.image_list = self.load_images()
        self.current_image_index = 0
        self.image_label = tk.Label(root)
        self.image_label.pack()
        self.change_image()

    def load_images(self):
        image_files = [file for file in os.listdir(self.image_folder) if file.endswith(('jpg', 'jpeg', 'png', 'gif'))]
        images = [Image.open(os.path.join(self.image_folder, file)) for file in image_files]
        return [ImageTk.PhotoImage(img) for img in images]

    def change_image(self):
        self.image_label.config(image=self.image_list[self.current_image_index])
        self.current_image_index = (self.current_image_index + 1) % len(self.image_list)
        self.root.after(2000, self.change_image)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Slider")
    image_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images", "small")
    slider = ImageSlider(root, image_folder)
    root.mainloop()
