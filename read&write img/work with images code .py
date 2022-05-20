import cv2
import tkinter as tk
from tkinter import filedialog

# select image file form selection :
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# read image file from path :
img = cv2.imread(file_path)

# show image file:
cv2.imshow('img',img)
cv2.waitKey(0)

# write (download) with name and type  image file :
cv2.imwrite('mg.png',img)
