from tkinter import *
import settings
import utilities
from Cell import Cell

### Initialising window ###
root = Tk() # Creates window
root.configure(bg='black') # Set background colour
root.geometry(f'{settings.width}x{settings.height}') # Sets window size
root.title('Minesweeper') # Sets window title
root.resizable(False, False) # Prevents resizing of window

### Creating Frames ###
topFrame = Frame(
    root,
    bg='black',
    width = utilities.width_prct(100),
    height = utilities.height_prct(25)
)

topFrame.place(x=0, y=0)

leftFrame = Frame(
    root,
    bg='black',
    width = utilities.width_prct(25), 
    height = utilities.height_prct(75)
)

leftFrame.place(x=0, y=utilities.height_prct(25))

centreFrame = Frame(
    root,
    bg='black',
    width = utilities.width_prct(75), 
    height = utilities.height_prct(75)
)

centreFrame.place(x=utilities.width_prct(25), y=utilities.height_prct(25))

for x in range(settings.gridSize):
    for y in range(settings.gridSize):
        c = Cell(x, y)
        c.createButton(centreFrame)
        c.btnObject.grid(
            column=x, row=y
        )


Cell.randomiseMines()

root.mainloop() # Runs window until closed by user