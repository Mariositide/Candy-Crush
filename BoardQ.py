#Queue Class!!

class BoardQueue:

    def __init__(self): 

        self.Front = 0
        self.Rear = -1 
        self.MaxSize = 9
        self.CurrentSize = 0
        self.Q = [0,0,0, 0,0,0, 0,0,0]

        self.i = 0
        self.j = 0

        for x in range(9):
            self.__enQueue()

        print("Q one: ",self.Q)
            

    def __enQueue(self):  #Private Function, shouldn't be called in main
        ColourOps = ["P", "B", "G", "O", "R", "Y"]
        Index = random.randint(0,5)
        Col = ColourOps[Index]


        if self.isFull():
            print("The array is full, cannot append soz")
            
        elif not self.isFull():
            self.CurrentSize = self.CurrentSize + 1
            self.Q[self.Rear+1] = Jar.Sweet(Col,self.i,self.j, Board) 
            self.Rear = self.Rear + 1       

            if self.Rear == self.MaxSize:
                self.Rear = 0        
            
        
        return self.Q

    def deQueue(self): #Returns the first item in the Q to leave 
        returning = self.Q[self.Front]

        if self.isEmpty():
            print("Array is empty so nothing to return soz")
            
        elif not self.isEmpty():
            self.Front += 1
            self.CurrentSize -= 1

            if self.Front == self.MaxSize:
                self.Front = 0
        #ENTER ENQ FUNCTION HERE       
            return returning

    def size(self):
        return len(self.queue)
    
    def pop(self, Position):
        if len(self.queue) < 0:
            return self.queue.pop(Position)

    def printQ(self):
        return self.queue

    def isEmpty(self):
        if self.CurrentSize == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.MaxSize == self.CurrentSize:
            return True


        
