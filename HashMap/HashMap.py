class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.entry = None

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.entry = None
    
    def setKey(self, key):
        self.key = key
    
    def setValue(self, value):
        self.value = value
    
    def setNext(self, entry):
        self.entry = entry
    
    def getKey(self):
        return self.key
    
    def getValue(self):
        return self.value
    
    def getNext(self):
        return self.entry

class HashMap:
    defaultSize = 16
    maxCapacity = 2**30

    def __init__(self, capacity=defaultSize):
        self.capacity = 2**self.getTableSize(capacity)
        self.hashTable = [None]*self.capacity
    
    def getTableSize(self, capacity):
        n = capacity - 1
        tableSize = 0
        while(n > 0):
            n = n>>1
            tableSize += 1
        return tableSize
    
    def hashFunction(self, key):
        return hash(key)%self.capacity
    
    def put(self, key, value):
        index = self.hashFunction(key)
        node = self.hashTable[index]
        if(node == None):
            self.hashTable[index] = Entry(key, value)
        else:
            while(node.getNext() != None):
                if(node.getKey() == key):
                    node.setValue(value)
                    return
                node = node.getNext()
            if(node.getKey() == key):
                node.setValue(value)
                return
            node.setNext(Entry(key, value))
                
    def get(self, key):
        index = self.hashFunction(key)
        node = self.hashTable[index]
        while(node != None):
            if(node.getKey() == key):
                return node.getValue()
            node = node.getNext()
        return None
        