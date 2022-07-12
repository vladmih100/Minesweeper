from tkinter import Button
import random

# Creating cell object
class Cell:
    all = []
    def __init__(self, x, y, Mine=False):
        self.Mine = Mine
        self.btnObject = None
        self.x = x
        self.y = y

        Cell.all.append(self)

    # Assigns TKinter button to cell object
    def createButton(self, location):
        btn = Button(
            location,
            width=10,
            height=3,
            text=f"{self.x},{self.y}"
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

    @staticmethod
    def randomiseMines():
        pickedCells = random.sample(
            Cell.all,
            9
        )

        for pickedCell in pickedCells:
            pickedCell.Mine = True


    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
