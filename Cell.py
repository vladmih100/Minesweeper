from tkinter import Button
import settings
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
        )
        btn.bind('<Button-1>', self.leftClick) # Left click action
        btn.bind('<Button-3>', self.rightClick) # Roght click action
        self.btnObject = btn

    # Left click actions
    def leftClick(self, event):
        # If clicked cell is mine, cell turns red:
        if self.Mine: 
            self.showMine()
        else:
            self.showCell()

    def showMine(self):
        self.btnObject.configure(bg='red')

    def getCell(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    # Returns array of surrounding cell objects
    @property
    def surroundedCells(self):
        Cells = [
            self.getCell(self.x - 1, self.y - 1),
            self.getCell(self.x - 1, self.y),
            self.getCell(self.x - 1, self.y + 1),
            self.getCell(self.x, self.y - 1),
            self.getCell(self.x, self.y + 1),
            self.getCell(self.x + 1, self.y - 1),
            self.getCell(self.x + 1, self.y),
            self.getCell(self.x + 1, self.y + 1),
        ]
        Cells = [cell for cell in Cells if cell != None]
        return Cells

    # Counts how many mines surronding selected cell
    @property
    def surroundedMines(self):
        count = 0
        for cell in self.surroundedCells:
            if cell.Mine:
                count += 1

        return count

    def showCell(self):
        self.btnObject.configure(text=self.surroundedMines)

    def rightClick(self, event):
        print(event)
        print("I am right clicked")

    @staticmethod
    def randomiseMines():
        pickedCells = random.sample(
            Cell.all,
            settings.mineCount
        )

        for pickedCell in pickedCells:
            pickedCell.Mine = True


    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
