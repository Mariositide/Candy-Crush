#Queue Class!!
import random, Jar

class BoardQueue(object):

    def __init__(self, Board): 

        self.Board = Board
        
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
            
        # Circular 
        
    def __enQueue(self):  #Private Function, shouldn't be called in main
        ColourOps = ["P", "B", "G", "O", "R", "Y"]
        Index = random.randint(0,5)
        Col = ColourOps[Index]


        if self.isFull():
            print("The array is full, cannot append soz")
            
        elif not self.isFull():
            self.CurrentSize = self.CurrentSize + 1
            self.Q[self.Rear+1] = Jar.Sweet(Col,self.i,self.j, self.Board ) 
            self.Rear = self.Rear + 1       

            if self.Rear == (self.MaxSize-1):
                self.Rear = -1        
            
        
        return self.Q

    def deQueue(self, newi, newj): #Returns the first item in the Q to leave 
        returning = self.Q[self.Front]

        self.i = newi
        self.j = newj

        returning.setBoard(newj, newi)
        returning.setPos((27 + (newj * 48)),(210 + (newi * 48)))
        returning.setClickRect() #################
        
        if self.isEmpty():
            print("Array is empty so nothing to return soz")
            
        elif not self.isEmpty():
            self.Front += 1
            self.CurrentSize -= 1

            if self.Front == self.MaxSize:
                self.Front = 0

            self.__enQueue()              

        return returning

    def size(self):
        return len(self.queue)
    
    """def pop(self, Position): 
        if len(self.queue) < 0:
            return self.queue.pop(Position)"""
    #^^^ Don't need this function because its sicular and uses pointers

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


        
