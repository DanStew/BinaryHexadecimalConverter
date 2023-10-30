#Importing all of the functions from the CLI Code
#This was done just to simplify the code in this file, as I felt no need for the functions to be repeated here
from BinaryHexadecimalConverter import *
import tkinter

#Building the GUI
root = tkinter.Tk()
root.geometry("500x400")
root.title("BDH Converter")
root.columnconfigure(3)
root.rowconfigure(3)

text_result = tkinter.Text(root, height = 2, width = 16, font=("Arial",24))
text_result.insert(1.0,"Hello")
text_result.grid(columnspan=3)

#Mainloop infinitely runs the application, waits for an event to occur, then runs that event
root.mainloop()






