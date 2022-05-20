import cv2
import tkinter as tk
from tkinter import filedialog

class photo:
    def __int__(self,name):
        self.name=name

    def get_img(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

    def p_img(self):
        img = cv2.imread(self.get_img())
        cv2.imshow(self.name, img)
        cv2.waitKey(0)

    def d_img(self):
        img = cv2.imread(self.get_img())
        cv2.imwrite(f"{self.name}.png", img)



asd=photo()
asd.name='022'

print(asd.get_img())
asd.d_img()
asd.p_img()
