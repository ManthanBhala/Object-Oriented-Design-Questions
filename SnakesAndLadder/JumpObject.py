class JumpObject:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def getPos(self):
        return self.start, self.end
