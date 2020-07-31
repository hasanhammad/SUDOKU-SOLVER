import pygame
from pack.is_valid import *




def solve_sudoku(win,sudoku):
    row_col = [0, 0]
    if not find_empty_cell(row_col, sudoku):  # checks whether there is an empty cell
        return True
    # store empty cell's coordinates
    row = row_col[0]
    col = row_col[1]

    for num in range(1, 10):
        if is_safe(row, col, num, sudoku):
            sudoku[row][col] = num  # put a number
            draw_change(row, col, win, sudoku, True)  # draw changes
            pygame.time.wait(50)  # wait a little
            # ensures that the program can internally interact with the rest of the operating system
            pygame.event.pump()
            pygame.display.update()  # updates the contents of the entire display
            if solve_sudoku(win, sudoku):
                return True
            sudoku[row][col] = 0
            draw_change(row, col, win, sudoku, False)  # draw changes
            pygame.time.wait(50)  # wait a little
            # ensures that the program can internally interact with the rest of the operating system
            pygame.event.pump()
            pygame.display.update()   # updates the contents of the entire display
    return False


def draw_change(row, col, win, sudoku, flag=True):
    fnt = pygame.font.SysFont("comicsans", 40)  # initialize the font

    gap = int(540 / 9)
    x = col * gap
    y = row * gap

    pygame.draw.rect(win, (255, 255, 255), (x+4, y+4, gap-7, gap-7), 0)  # to draw cells
    if str(sudoku[row][col]) == "0":  # to draw empty cells that had been filled with zeros
        text = fnt.render(" ", 500, (0, 0, 0))
    else:  # to draw numbers inside cells
        text = fnt.render(str(sudoku[row][col]), 500, (0, 0, 0))
        win.blit(text, (x + (int(gap / 2) - int(text.get_width() / 2)), y + (int(gap / 2) - int(text.get_height() / 2))))
    if flag:  # draw green rectangles
        pygame.draw.rect(win, (0, 255, 0), (x+4, y+4, gap-7, gap-7), 2)
    else:  # draw red rectangles
        pygame.draw.rect(win, (255, 0, 0), (x+4, y+4, gap-7, gap-7), 2)


def draw_cell(row, col, win, sudoku):  # to draw cells
    fnt = pygame.font.SysFont("comicsans", 40)  # initialize the font
    gap = int(540 / 9)
    x = col * gap
    y = row * gap

    if not(sudoku[row][col] == 0):  # to draw numbers
        text = fnt.render(str(sudoku[row][col]), 500, (0, 0, 0))
        # draw numbers in cells
        win.blit(text, (x + (int(gap/2) - int(text.get_width()/2)), y + (int(gap/2) - int(text.get_height()/2))))


def draw_lines(win, sudoku):
    # draw sudoku Lines
    gap = int(540 / 9)
    for i in range(10):
        if i % 3 == 0 and i != 0:
            thick = 2  # thick of main lines
        else:
            thick = 1  # thick of the rest of the lines
        pygame.draw.line(win, (0, 0, 0), (0, i*gap), (540, i*gap), thick)  # draw horizontal lines
        pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, 540), thick)  # draw vertical lines

    # draw cells
    for row in range(9):
        for col in range(9):
            draw_cell(row, col, win, sudoku)


def redraw_window(win, sudoku):
    win.fill((255, 255, 255))  # main window
    pygame.font.SysFont("comicsans", 40)  # initialize the font
    draw_lines(win, sudoku)  # to draw lines
