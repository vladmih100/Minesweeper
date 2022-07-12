from tkinter import Button

class Cell:
    def __init__(self, Mine=False):
        self.Mine = Mine
        self.btnObject = None

    def createButton(self, location):
        btn = Button(
            location,
            text='Hi'
        )
        btn.bind('<Button-1>', self.leftClick)
        self.btnObject = btn

    def leftClick(self, event):
        print("I am left clicked")