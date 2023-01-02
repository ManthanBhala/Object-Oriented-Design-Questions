from Cell import Cell
from JumpObject import JumpObject
import random

class Board:
    def __init__(self, boardSize, snakesCount, ladderCount):
        self.boardSize = boardSize
        self.cells = []
        for i in range(self.boardSize):
            row = []
            for j in range(self.boardSize):
                row += [Cell()]
            self.cells += [row]
        for i in range(snakesCount):
            head, tail = random.sample(set(range(1, self.boardSize**2-2)), 2)
            if(head < tail):
                head, tail = tail, head
            row, col = self.getCellPosition(head)
            self.cells[row][col].setJumpObj(JumpObject(head, tail))
        for i in range(ladderCount):
            head, tail = random.sample(set(range(1, self.boardSize**2-2)), 2)
            if(head > tail):
                head, tail = tail, head
            row, col = self.getCellPosition(head)
            self.cells[row][col].setJumpObj(JumpObject(head, tail))

    def getCellPosition(self, playerPosition):
        boardRow = playerPosition//self.boardSize
        boardCol = playerPosition%self.boardSize
        return boardRow, boardCol

    def getCell(self, playerPosition):
        row, col = self.getCellPosition(playerPosition)
        return self.cells[row][col]
    
    def getBoardSize(self):
        return self.boardSize