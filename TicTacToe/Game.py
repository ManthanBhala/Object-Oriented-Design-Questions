from Board import Board
from Player import Player
from Enums import Options

class Game:
    def __init__(self):
        self.board = Board(3)
        p1 = Player("p1", Options.option1.value)
        p2 = Player("p2", Options.option3.value)
        self.players = [p1, p2]
        self.playingTurn = 0

    def startGame(self):
        n = self.board.getBoardSize()
        turnsLeft = n**2
        while(turnsLeft > 0):
            self.board.printBoard()
            player = self.players[self.playingTurn]
            print("Turn Player: ", player.getName())
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            while(row>=n or row<0 or col>=n or col<0 or self.board.getPiece(row, col).getPieceType() != ' '):
                print("Incorrect Position")
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
            self.board.setPiece(row, col, player.getPlayingPiece())
            if(self.isWinner(row, col, player.getPlayingPiece())):
                print("Winner: ", player.getName())
                break
            self.playingTurn = (self.playingTurn + 1)%len(self.players)
            turnsLeft -= 1
    
    def isWinner(self, row, col, pieceType):
        rowMatch, colMatch, diagMatch, antidiagMatch = True, True, True, True
        n = self.board.getBoardSize()
        for i in range(n):
            if(self.board.getPiece(i, col).getPieceType()==' ' or self.board.getPiece(i, col).getPieceType()!=pieceType):
                rowMatch = False
            if(self.board.getPiece(row, i).getPieceType()==' ' or self.board.getPiece(row, i).getPieceType()!=pieceType):
                colMatch = False
            if(self.board.getPiece(i, i).getPieceType()==' ' or self.board.getPiece(i, i).getPieceType()!=pieceType):
                diagMatch = False
            if(self.board.getPiece(i, n-i-1).getPieceType()==' ' or self.board.getPiece(i, n-i-1).getPieceType()!=pieceType):
                antidiagMatch = False
        return rowMatch or colMatch or diagMatch or antidiagMatch
