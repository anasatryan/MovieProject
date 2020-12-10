class Deque:
    def __init__(self, size):
        self.rear = 0
        self.front = -1
        self.size = size
        self.items = [None] * self.size


    def isFull(self):
        if ((self.front == 0 and self.rear == self.size - 1) or self.front == self.rear + 1):
            self.items *= 2

    def addFirst(self, key):
        self.isFull()
        if (self.front == -1):
            self.front = 0
            self.rear = 0
        elif (self.front == 0):
            self.front = self.size - 1
        else:
            self.front = self.front - 1

        self.items[self.front] = key

    def addLast(self, key):
        self.isFull()
        if (self.front == -1):
            self.front = 0
            self.rear = 0
        elif (self.rear == self.size - 1):
            self.rear = 0
        else:
            self.rear = self.rear + 1

        self.items[self.rear] = key

    def removeFirst(self):
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            if (self.front == self.size - 1):
                self.front = 0
            else:
                self.front = self.front + 1

    def removeLast(self):
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        elif (self.rear == 0):
            self.rear = self.size - 1
        else:
            self.rear = self.rear - 1

    def first(self):
        return self.items[self.front]

    def last(self):
        return self.items[self.rear]
    def printDeq(self):
        for favMov in self.items:
            if (favMov != None):
                print(favMov)

