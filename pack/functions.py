import tkinter as tk
from pack.sudoku_GUI import *
from tkinter import filedialog, messagebox


def solve_gui(root, button_Solve_SUDOKU, sudoku):  # solves the given sudoku table graphically
    win = pygame.display.set_mode((540, 540))  # creates a window that the sudoku table going to be solved in it
    redraw_window(win, sudoku)  # draws sudoku table in side the window "win"
    pygame.display.update()  # update the window "win" after calling the "redraw_window" function to commit changes
    solve_sudoku(win, sudoku)  # solves sudoku
    redraw_window(win, sudoku)  # draws the solved sudoku in side the window "win"
    pygame.display.update()  # to commit changes in win "pygame"
    root.update()  # to commit changes in root "tkinter"
    button_Solve_SUDOKU.place_forget()  # to delete the button "button_Solve_SUDOKU" from the root window
    # create the button "Solve another SUDOKU" after that the given sudoku has been solved
    tk.Button(root, text="Solve another SUDOKU", width=20, fg='green', command=lambda: [home_page(root, sudoku), pygame.quit()]).place(x=200, y=545)
    # create the button "Quit" after that the given sudoku has been solved
    tk.Button(root, text="Quit", width=20, fg='red', command=root.destroy).place(x=370, y=545)


def pyGame_in_tkinter(root, sudoku):
    pygame.font.init()  # initializes the font module

    embed = tk.Frame(root, width=540, height=542)  # creates embed frame for pygame window
    embed.place(x=0, y=0)

    # embeds a pygame window in a frame in tkinter window, using an SDL drawing frame
    os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

    win = pygame.display.set_mode((540, 600)) # creates a window that the sudoku table going to be drawn in it
    pygame.display.init()  # initializes the pygame display module
    redraw_window(win, sudoku)  # draws sudoku table in side the window "win"
    pygame.display.update()  # to commit changes in win "pygame"
    # creat the button "Solve SUDOKU" in the root window
    button_Solve_SUDOKU = tk.Button(root, text="Solve SUDOKU", width=20,fg='green',
                                    command= lambda: solve_gui(root, button_Solve_SUDOKU, sudoku))
    # place button in position
    button_Solve_SUDOKU.place(x=270, y=555, anchor="center")


def browse_file(root, home_page, sudoku):
    sudoku.clear()  # clear sudoku
    try:

        # return the name of the file and the location of the file
        root.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select A File",
                                                   filetypes=[("Text Files", "*.txt")])

        file_path = tk.Label(home_page, text="Path: %s \n " % root.filename)  # store the file name in a label

        file_path.place(x=20, y=200)  # draw the file name
        tk.Label(home_page, text="validation: ").place(x=20, y=225)

        read_from_file(root.filename, sudoku)  # get sudoku from the chosen file

        if isValidConfig(sudoku,9) == True:  # if the chosen is a valid sudoku table
            # tell the user that this file is valid
            tk.Label(home_page, text="  valid sudoku file ", fg="green").place(x=80, y=225)
            # create a the button "Draw SUDOKU table" and place it in position
            tk.Button(home_page, text="Draw SUDOKU table", width=25, fg='green', state='normal',
                                command=lambda: pyGame_in_tkinter(root, sudoku)).place(x=270, y=500, anchor="center")
        else:
            # tell the user that this file is invalid
            tk.Label(home_page, text="invalid sudoku file", fg="red").place(x=80, y=225)
            # create a disabled button "Draw SUDOKU table" and place it in position
            tk.Button(home_page, text="Draw SUDOKU table", width=25, state='disable',
                      command=lambda: pyGame_in_tkinter(root, sudoku)).place(x=270, y=500, anchor="center")
    except:
         tk.Label(home_page, text=" open file error ", fg="red", width=15).place(x=80, y=225)
        # shows a warning if an error is thrown
         messagebox.showwarning("Open file",  "(%s)\n is not a SUDOKU table\n please choose another one!" % root.filename)


def all_children (root):  # puts all the widgets of the root window in a list
    _list = root.winfo_children()
    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())
    return _list


def home_page(root, sudoku):
    widget_list = all_children(root)  # widget_list contains all widgets in the root window
    for item in widget_list:
        item.place_forget()  # deletes all widgets in the root window

    home_page = tk.Frame(root, width=540, height=541)  # create home page frame

    # draw information in the home page frame
    tk.Label(home_page, text="SUDOKU SOLVER", fg="green" , font=("Courier", 44)).place(x=270, y=50, anchor="center")
    tk.Label(home_page, text="please choose a sudoku file :\n", fg="red", font=("Courier", 15)).place(x=15, y=150)
    tk.Label(home_page, text="notes: \n", fg="red").place(x=15, y=270)
    tk.Label(home_page, text="1- sudoku file must be a txt file \n", fg="red").place(x=25, y=300)
    tk.Label(home_page, text="2- sudoku file must contains a 9X9 table of numbers \n", fg="red").place(x=25, y=330)
    tk.Label(home_page, text="3- empty cells are filled with 0 \n", fg="red").place(x=25, y=360)
    tk.Label(root, text="©2020 Hasan Y Hammad. All Rights Reserved \n").place(x=15, y=580)
    # creates "choose file " button and place it in position
    tk.Button(home_page, text="choose file ", width=15, command=lambda: browse_file(root,home_page, sudoku)).place(x=400, y=150)
    # creates "Draw SUDOKU table" button and place it in position
    tk.Button(home_page, text="Draw SUDOKU table", width=25, state='disable',command=lambda: pyGame_in_tkinter(root, sudoku)).place(x=270, y=500, anchor="center")
    # place the home page frame in position
    home_page.place(x=0, y=0)
    # clear sudoku after the work is done
    sudoku.clear()
