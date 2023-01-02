class Player:
    def __init__(self, name, playingPiece):
        self.name = name
        self.playingPiece = playingPiece
    
    def getName(self):
        return self.name
    
    def getPlayingPiece(self):
        return self.playingPiece