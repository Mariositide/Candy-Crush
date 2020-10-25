# Candy Crush
# Sweet Class

import pygame, sys, random
from pygame.locals import *

class Sweet(object):

    def __init__(self, colour, XBoard,YBoard, Board):
        
        self.colour = colour
        self.Board = Board
        self.XBoard = XBoard          
        self.YBoard = YBoard
        self.XPos = 27 + (self.XBoard * 48)    #Pixels
        self.YPos = 210 + (self.YBoard * 48)
        self.rectPos = pygame.Rect(self.XPos+1,self.YPos+1, 47,47)

        self.Need2Swap = False  #Need to swap back when invalid move
        
        self.LNeigh = 0
        self.RNeigh = 0
        self.UNeigh = 0
        self.DNeigh = 0

        self.Match = False
        self.Blank = False
        self.ToAnimate = False
        self.Tick = 30
                
        self.Blank = False
        self.Striped = False
        self.Direction = "0"
        self.isColourBomb = False
        self.Wrapped = False
        
        AllCols = ["P", "B", "G", "O", "R", "Y"]
        if self.colour == "P":
            self.img = pygame.image.load("PurpleSweet.png")
            self.img = pygame.transform.scale(self.img, (50,50))
        elif self.colour == "B":
            self.img = pygame.image.load("BlueSweet.png")
            self.img = pygame.transform.scale(self.img, (50,50))
        elif self.colour == "G":
            self.img = pygame.image.load("GreenSweet.png")
            self.img = pygame.transform.scale(self.img, (50,50))
        elif self.colour == "O":
            self.img = pygame.image.load("OrangeSweet.png")
            self.img = pygame.transform.scale(self.img, (50,50))
        elif self.colour == "R":
            self.img = pygame.image.load("RedSweet.png")
            self.img = pygame.transform.scale(self.img, (50,50))
        elif self.colour == "Y":
            self.img = pygame.image.load("YellowSweetN.png")
            self.img = pygame.transform.scale(self.img, (47,50))


    def getWrapped(self):
        return self.Wrapped

    def Animate(self, mySurface):
        if self.Tick == 0:
            self.Blank = True
        else:
            self.Tick = self.Tick - 1
            #rotate
            #move ship X and Y

            SweetImageRotated = pygame.transform.rotozoom(self.img, 1.0, 0.95)
            #height = SweetImageRotated.get_height()/2.0
            #width = SweetImageRotated.get_width()/2.0

            #BlitPos = [self.rndint(p1.position[0]-width),  self.rndint(p1.position[1]+height)]
            mySurface.blit(SweetImageRotated,(self.XPos, self.YPos))
       
            self.img = SweetImageRotated

    #tick
        #rotate
        #return
            
    def rndint(number):
        return int(round(number))
    
    def getCB(self):
            return self.isColourBomb
        
    def getDirection(self):
            return self.Direction

    def getStriped(self):      
        return self.Striped
   
    def getAnimate(self):
        return self.ToAnimate

    def setStriped(self):
        self.Striped = True
    
    def setAnimate(self):
        self.ToAnimate = True
        
    def setBlank(self):
        self.Blank = True

    def getMatch(self):
        return self.Match

    def setMatch(self):
        self.Match = True
        self.setAnimate()
        
    def unBlank(self):
        self.Blank = False
        
    def getBlank(self):
        return self.Blank
              
    def setClickRect(self):
        self.rectPos = pygame.Rect(self.XPos+1,self.YPos+1, 47,47)

    def setSwapStatus(self, State):
        self.Need2Swap = State

    def getSwapStatus(self):
        return self.Need2Swap

    def SetNeigh(self, Direction,Board):
        try:
            if Direction == "D" and (self.YBoard + 1) <= 8:
                self.DNeigh = self.Board[self.XBoard][self.YBoard + 1]
        except IndexError:
            self.DNeigh = 0
        try:
            if Direction == "U" and (self.YBoard -1) >= 0: 
                self.UNeigh = self.Board[self.XBoard][self.YBoard - 1]
        except IndexError:
            self.UNeigh = 0
        try:    
            if Direction == "R" and (self.XBoard + 1) <= 8:
                self.RNeigh = self.Board[self.XBoard+1][self.YBoard]
        except IndexError:
            self.RNeigh = 0
        try:
            if Direction == "L" and (self.XBoard -1) >= 0:
                self.LNeigh = self.Board[self.XBoard-1][self.YBoard]
        except IndexError:
            self.LNeigh = 0

    def getPos(self):
        return self.XPos, self.YPos

    def setPos(self, Xpos, Ypos):
        self.XPos = Xpos
        self.YPos = Ypos
        

    def setBoard(self, NewXBoard, NewYBoard):
        self.XBoard = NewXBoard
        self.YBoard = NewYBoard
        
    def getBoard(self):
        return self.XBoard, self.YBoard
    
    def getNeigh(self, Board):
        Directions = ["L", "R", "U", "D"]       #Could probs move into the initialise func
        for item in Directions:
            Board[self.XBoard][self.YBoard].SetNeigh(item,Board) 
        return self.LNeigh, self.RNeigh, self.UNeigh, self.DNeigh

    def getColour(self):
        return self.colour
    def setImage(self, Image):
        self.img = Image

    def getImage(self):
        return self.img

    def DisplaySweet(self, mySurface, Image):
       
        mySurface.blit(Image,(self.XPos, self.YPos))
        
        #pygame.draw.rect(mySurface, BLACK , (self.XPos+1,self.YPos+1, 47,47)) #PRINTS BLACK BOXES WHERE HIT BOXES ARE
        
class Striped(Sweet):
    def __init__(self, colour, X, Y, Board, VorH):
        super(Striped, self).__init__(colour, X, Y, Board)
        self.Direction = VorH
        self.colour = colour
        self.img = pygame.image.load("StrRed.png")
        self.img = pygame.transform.scale(self.img, (50,52))
        AllCols = ["P", "B", "G", "O", "R", "Y"]
        AllHPics = ["HStrPurple", "HStrBlue", "HStrGreen", "HStrOrange", "HStrRed", "HStrYellow"]
        AllVPics = ["VStrPurple", "VStrBlue", "VStrGreen", "VStrOrange", "VStrRed", "VStrYellow"]

        self.Striped = True     #Polymophism!!
        
        #Img Loaded by displaying pic in same colour index

        if self.Direction == "V":
            self.img = pygame.image.load(AllVPics[AllCols.index(self.colour)] + ".png")
            self.img = pygame.transform.scale(self.img, (52,52))
        if self.Direction == "H":
            self.img = pygame.image.load(AllHPics[AllCols.index(self.colour)] + ".png")# Erroring here
            self.img = pygame.transform.scale(self.img, (52,52))
            
        #def destroy row/column

class Wrapped(Sweet):
    def __init__(self, colour, X, Y, Board):
        super(Wrapped, self).__init__(colour, X, Y, Board)
        self.colour = colour
        AllCols = ["P", "B", "G", "O", "R", "Y"]
        AllPics = ["WraPurple", "WraBlue", "WraGreen", "WraOrange", "WraRed", "WraYellow"]
       

        self.Wrapped = True     #Polymophism!!
        self.XPos = 28 + (self.XBoard * 48)    #Pixels
        self.YPos = 216 + (self.YBoard * 48)
        
        #Img Loaded by displaying pic in same colour index
        index = AllCols.index(colour)
        self.img = pygame.image.load(AllPics[index] + ".png")
        self.img = pygame.transform.scale(self.img, (48,38))
                    
        #def destroy row/column

        

class ColourBomb(Sweet):
    def __init__(self, colour, X, Y, Board):
        super(ColourBomb, self).__init__(colour, X, Y, Board)
        self. Dcolour = "ALL"      #destroy colour to be determined when swapped
        self.img = pygame.image.load("ColourBomb.png")
        self.img = pygame.transform.scale(self.img, (45,45))
        self.XPos = 30 + (self.XBoard * 48)    #Pixels
        self.YPos = 212 + (self.YBoard * 48)

        self.isColourBomb = True    #Polymorphism
    
    
