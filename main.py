from tkinter import *
import settings
import utilities


### Initialising window ###
root = Tk() # Creates window
root.configure(bg='black') # Set background colour
root.geometry(f'{settings.width}x{settings.height}') # Sets window size
root.title('Minesweeper') # Sets window title
root.resizable(False, False) # Prevents resizing of window

### Creating Frames ###
topFrame = Frame(
    root,
    bg='red',
    width = utilities.width_prct(100),
    height = utilities.height_prct(25)
)

topFrame.place(x=0, y=0)

leftFrame = Frame(
    root,
    bg='blue',
    width = utilities.width_prct(25), 
    height = utilities.height_prct(75)
)

leftFrame.place(x=0, y=utilities.height_prct(25))

centreFrame = Frame(
    root,
    bg='green',
    width = utilities.width_prct(75), 
    height = utilities.height_prct(75)
)

centreFrame.place(x=utilities.width_prct(25), y=utilities.height_prct(25))

root.mainloop() # Runs window until closed by user