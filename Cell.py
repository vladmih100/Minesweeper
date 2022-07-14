from tkinter import Button, Label
import settings
import random
import ctypes
import sys

# Creating cell object
class Cell:
    all = []
    allZero = []
    unvisitedZero = []
    cellCount = settings.cellCount
    cellCountlab = None
    def __init__(self, x, y, Mine=False):
        self.Mine = Mine
        self.btnObject = None
        self.x = x
        self.y = y
        self.opened = False
        self.marked = False

        Cell.all.append(self)

    # Assigns TKinter button to cell object
    def createButton(self, location):
        btn = Button(
            location,
            width=1,
            height=1,
        )
        btn.bind('<Button-1>', self.leftClick) # Left click action
        btn.bind('<Button-3>', self.rightClick) # Roght click action
        self.btnObject = btn

    @staticmethod
    def createCountLabel(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            font = ("", 30),
            text=f'Cells left: {Cell.cellCount}'
        )

        Cell.cellCountlab = lbl


    # Left click actions
    def leftClick(self, event):
        # If clicked cell is mine, cell turns red:
        if self.Mine: 
            self.showMine()
        else:
            self.showCell()
            if self.surroundedMines == 0:
                Cell.allZero.append(self)
                for cell in self.surroundedCells:
                    cell.showCell()
                    if cell.surroundedMines == 0:
                        Cell.allZero.append(cell)
                        Cell.unvisitedZero.append(cell)

                while len(Cell.unvisitedZero) > 0:
                    for cell in Cell.unvisitedZero[0].surroundedCells:
                        cell.showCell()
                        if cell.surroundedMines == 0 and cell not in Cell.allZero:
                            Cell.allZero.append(cell)
                            Cell.unvisitedZero.append(cell)
                    del Cell.unvisitedZero[0]
            if Cell.cellCount == settings.mineCount:
                ctypes.windll.user32.MessageBoxW(0, "You won!!", "Game Over", 0)
                

        self.btnObject.unbind('<Button-1>')
        self.btnObject.unbind('<Button-3>')
            
    def showMine(self):
        # End game if mine is clicked
        self.btnObject.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, "You're dead bro", "Game Over", 0)
        sys.exit()
        
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
        if not self.opened:
            Cell.cellCount -= 1
            self.btnObject.configure(text=self.surroundedMines)
            # Update cell count label
            if Cell.cellCountlab:
                Cell.cellCountlab.configure(
                    text=f'Cells left: {Cell.cellCount}'
                    )
        # Cell is marked as opened
        self.opened = True
        self.btnObject.configure(
            bg="SystemButtonFace"
        )

    def rightClick(self, event):
        if not self.marked:
            self.btnObject.configure(
                bg='aqua'
                )
            self.marked = True
        else:
            self.btnObject.configure(
                bg='SystemButtonFace'
                )
            self.marked = False

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
