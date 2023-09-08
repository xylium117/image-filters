from tkinter import *
from tkinter import font
from tkinter import filedialog
import cv2
import numpy as np
from matplotlib import pyplot as plt

global filename
def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select an Image", filetypes=(("Image files","*.png;*.jpg;*.jpeg;"),))

def toGrayscale():
    img = cv2.imread(filename)
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscale_image.jpg", grayscale_img) # Saves in Directory

def toBilateral():
    img = cv2.imread(filename)
    # apply bilateral blur
    kernel = np.ones((5, 5), np.float32) / 25
    blur = cv2.bilateralFilter(img, 9, 75, 75)
    cv2.imwrite("bilateral_blurred_image.jpg", blur) # Saves in Directory

def toGaussian():
    img = cv2.imread(filename)
    # apply gaussian blur on src image
    gaussianBlur = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
    cv2.imwrite("gaussian_blur_image.jpg", gaussianBlur)

def toThreshold():
    img = cv2.imread(filename)
    # apply threshold on src image
    retval, threshold = cv2.threshold(img, 62, 255, cv2.THRESH_BINARY)
    cv2.imwrite("threshold_image.jpg", threshold)

root = Tk()  # create root window
root.title("Image Filters | Python")  # title of the GUI window
root.maxsize(900, 600)  # specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color

# Create left and right frames
left_frame = Frame(root, width=200, height=400, bg='lightgrey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Create frames and labels in left_frame
Button(left_frame, text="Import Image", command = browseFiles).grid(row=0, column=0, padx=5, pady=5)

# load image to be "edited"
image = PhotoImage(file="rain.gif")
original_image = image.subsample(6,6)  # resize image using subsample
Label(left_frame, image=original_image).grid(row=1, column=0, padx=10, pady=10)

# Display image in right_frame
Label(right_frame, image=image).grid(row=0,column=0, padx=5, pady=5)

# Create tool bar frame
tool_bar = Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Example labels that serve as placeholders for other widgets
Label(tool_bar, text="Tools", font=font.Font(weight="bold"), relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(tool_bar, text="Filters", font=font.Font(weight="bold"), relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

# Example labels that could be displayed under the "Tool" menu
Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)

Button(tool_bar, text="Grayscale", command = toGrayscale).grid(row=1, column=1, padx=5, pady=5)
Button(tool_bar, text="Bilateral Blur", command = toBilateral).grid(row=2, column=1, padx=5, pady=5)
Button(tool_bar, text="Gaussian Blur", command = toGaussian).grid(row=3, column=1, padx=5, pady=5)
Button(tool_bar, text="Threshold", command = toThreshold).grid(row=4, column=1, padx=5, pady=5)


root.mainloop()