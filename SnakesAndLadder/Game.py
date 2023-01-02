from Board import Board
from Dice import Dice
from Player import Player

class Game:
    def __init__(self):
        self.board = Board(10, 5, 4)
        self.dice = Dice(1)
        self.winner = None
        p1 = Player("p1", 0)
        p2 = Player("p2", 0)
        self.players = [p1, p2]
        self.playerCount = 2
        self.playerTurn = 0


    def startGame(self):
        while(self.winner == None):
            player = self.players[self.playerTurn]
            print("**********************************************************************************")
            print("Turn Player: ", player.getName(), "\tCurrent Position: ", player.getCurrentPosition())
            diceNumber = self.dice.roll()
            print("Dice rolled: ", diceNumber)
            newPosition = player.getCurrentPosition() + diceNumber
            newPosition = self.jumpCheck(newPosition)
            player.setCurrentPosition(newPosition)
            if(newPosition >= self.board.getBoardSize()**2):
                self.winner = player
                break
            print("New Position: ", newPosition)
            self.playerTurn = (self.playerTurn+1)%self.playerCount
        print("Winner: ", self.winner.getName())
    
    
    def jumpCheck(self, newPosition):
        while(newPosition < self.board.getBoardSize()**2 and self.board.getCell(newPosition).getJumpObj() != None):
            jumpObj = self.board.getCell(newPosition).getJumpObj()
            head, tail = jumpObj.getPos()
            jumpBy = "ladder" if head < tail else "snake"
            print("Jump done by: ", jumpBy)
            newPosition = tail
        return newPosition 
            
