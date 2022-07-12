from tkinter import Button

# Creating cell object
class Cell:
    def __init__(self, Mine=False):
        self.Mine = Mine
        self.btnObject = None

    # Assigns TKinter button to cell object
    def createButton(self, location):
        btn = Button(
            location,
            text='Hi'
        )
        btn.bind('<Button-1>', self.leftClick) # Left click action
        btn.bind('<Button-3>', self.rightClick) # Roght click action
        self.btnObject = btn

    def leftClick(self, event):
        print(event)
        print("I am left clicked")

    def rightClick(self, event):
        print(event)
        print("I am right clicked")