from PlayingPiece import PlayingPiece

class Board:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.pieces = []
        for i in range(boardSize):
            row = []
            for j in range(boardSize):
                row += [PlayingPiece()]
            self.pieces += [row]
    
    def printBoard(self):
        for i in range(self.boardSize):
            print('', end='|')
            for j in range(self.boardSize):
                print(self.pieces[i][j].getPieceType(), end='|')
            print('\n')
    
    def getBoardSize(self):
        return self.boardSize
    
    def getPiece(self, row, col):
        return self.pieces[row][col]

    def setPiece(self, row, col, pieceType):
        self.pieces[row][col].setPieceType(pieceType)
