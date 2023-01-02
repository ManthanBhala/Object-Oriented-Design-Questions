from JumpObject import JumpObject

class Cell:
    def __init__(self):
        self.jumpObject = None

    def getJumpObj(self):
        return self.jumpObject

    def setJumpObj(self, jumpObj):
        self.jumpObject = jumpObj
