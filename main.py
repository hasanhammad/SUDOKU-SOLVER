from pack.functions import *
import tkinter as tk

sudoku =[]  # sudoku table

root = tk.Tk()  # main window
root.title('Sudoku solver')  # title of the main window
root.minsize(540, 600)  # size of the main window

home_page(root, sudoku)  # calling home_page function which draws the frame of the home page

# the main loop of the program
root.mainloop()
