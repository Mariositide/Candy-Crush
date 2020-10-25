#V15 - Blockers of somesort?? Need to fix dual matches and matches with other special sweets in it
import pygame, sys, random
from pygame.locals import *
import time, numbers, Jar, Menu, ToFall
import pygame.freetype # FOR TEXT

#Initialise global variables
width = 470
height = 740
my_caption = 'Task1'
fpsClock = None
BLACK = (0,0,0,255)
RED = (255,0,0)
PURPLE = (150,0,150,50)
PINK = (150,0,150,50)

mySurface = None

def initialise(windowWidth, windowHeight, windowName, windowColour):
    global mySurface
    global fpsClock
    
    pygame.freetype.init()
    #all_fonts = pygame.font.get_fonts()
    #pygame.font.get_fonts()
    
    pygame.init()
    fpsClock  = pygame.time.Clock() 
    mySurface = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
    mySurface.fill(windowColour)

def DisplayBoard(EmptyBoardPic):
    initialise(500, 500, my_caption, PURPLE)
    mySurface.blit( imageName ,(20,20))

   
def clickmenu(Op1, Op2):
    
    Play = pygame.Rect(127,387,200,90)#clickrect
    Rules = pygame.Rect(146,487,180,70)#clickrect
    opX = pygame.Rect(176,297,190,50)
    
    
    Chose1 = False
    Chose2 = False
    
    for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Clicked")
                
            if event.type == pygame.MOUSEBUTTONUP:
                print("Unclicked")
                pos = pygame.mouse.get_pos() # MOUSE
                print(pos)
                if Op1.collidepoint(pos):
                   print("You chose Option 1")
                   Chose1 = True
                   
                if Op2.collidepoint(pos):
                   print("You chose Option 2")
                   Chose2 = True

    return Chose1, Chose2

def Click():
    Clicked = False
    pos1 = pygame.mouse.get_pos()
    P1 = 0

    for row in Board:       #Checks which sweet has been clicked
        for items in row:
            if items.rectPos.collidepoint(pos1):
                P1 = items
                print(items.getColour(), " was clicked")
                Clicked = True

    return Clicked, P1
    

    
def ClickSquare(First, Second, Swipe, P1, P2):
    
    Clicked = False
    for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                First,P1 = Click()               
                
            if event.type == pygame.MOUSEBUTTONUP:
                Second, P2 = Click()          
                Clicked = True  #separeate into 2 functions first click & second click on check second if first true if both true then check if swipe 
    if Clicked:
        if First and Second:
            Swipe = True
            print("Swiper no swiping!")

    return Clicked,Swipe, P1, P2
        

def HeaderTexts(Writing, Xpos, Ypos):    
    font = pygame.freetype.Font(None, 70) # None = the font style. # 20 = the size
   
    text = font.render(Writing,(255,255,255,255)) # text is now a tuple. index 0 = surface & index 1 = rect
    textpos = text[1] #textpos is the rectangle
    
    textpos.centerx = Xpos
    textpos.centery = Ypos # y position of text
    mySurface.blit(text[0],textpos) # place on the screen the actual text (surface) in the rectangles position


def Move(P1,P2, Board): # Swaps two sweets in the board
    
    P1X = P1.getBoard()[0]  # Get the x position on the grid 1-9
    P1Y = P1.getBoard()[1]  # Get the x position on the grid 1-9

    P2X = P2.getBoard()[0]
    P2Y = P2.getBoard()[1]

    Board[P1X][P1Y] = P2    # Put P2 where P1 was
    Board[P2X][P2Y] = P1

    #Setting Variables
    P1.setBoard(P2X, P2Y)   # Set the sweet variables as their new pos
    P2.setBoard(P1X, P1Y)

    P1.setPos( (27 + (P2X * 48)),(210 + (P2Y * 48)) ) # Set the coordinates where 
    P2.setPos(( 27 + (P1X * 48)),(210 + (P1Y * 48)) ) # the image will be loaded

    P1.setClickRect()
    P2.setClickRect()
 
    #print("tbc")     
    return Board
    
    
def Match(Board, P1, P2):   #Need P1 & P2 inputs too    
    Match = False
    NewXcoord = P2.getBoard()[0]
    NewYcoord = P2.getBoard()[1]
    MatchedSweets  = []
    NumOfMatched = 0
    
    
    if P1.getBoard()[0] == NewXcoord:
        Move = "V"
    else:
        Move = "H"

    if P1.getCB() or P2.getCB() or (P1.getStriped() and P2.getStriped()):
            # If a 2 Match with a colourbomb
            # Or if 2 striped swap  
            Match = True
            MatchedSweets.append(P1)
            MatchedSweets.append(P2)
            NumOfMatched =len(MatchedSweets)
            print("Special CB or 2 stripes Match!!!!!!!!!")
    #Make an elif a match between two striped
        
    else:
        MatchesY1 = CheckSides(P1, 2)
        MatchesX1 = CheckSides(P1, 0)
        MatchesY2 = CheckSides(P2, 2)
        MatchesX2 = CheckSides(P2, 0)
        #can condense all these ifs into one long if..or..or..: once done testing
        if MatchesY1[0] >= 3:   #If the SameY (in a row) is a match 3 or >
            print(MatchesY1, " matches in the Y direction!")  # 
            Match = True
            MatchedSweets = MatchesY1[1]
            NumOfMatched =len(MatchedSweets)
        if MatchesX1[0] >= 3:
            print(MatchesX1, " matches in the X direction!")
            Match = True
            for item in MatchesX1[1]:
                MatchedSweets.append(item)
            NumOfMatched =len(MatchedSweets)
        if MatchesY2[0] >= 3:
            print(MatchesY2, " matches in the Y direction!")
            Match = True
            for item in MatchesY2[1]:
                MatchedSweets.append(item)
            NumOfMatched =len(MatchedSweets)
        if MatchesX2[0] >= 3:
            print(MatchesX2, " matches in the X direction!")
            Match = True
            for item in MatchesX2[1]:
                MatchedSweets.append(item)
            NumOfMatched =len(MatchedSweets)

    if Match:
        for item in MatchedSweets:
            item.setMatch()
            print("Hi", item.getColour())

    #print(str(NumOfMatched) +" ", MatchedSweets)
    return Match, NumOfMatched, MatchedSweets, Move


def WholeBoardMatch(Board): #################################################
    #print("CHECKING FOR SWEEEEEEEEEEEEEEEETS")
    MatchedSweets = []
    FoundMatch = False

    #while row > -1 and column < 9: #add extra conditions in here; need if  column +1 = 9 set both to 0
    
    for row in range(8, -1, -1): # from bottom to top
        for column in range(0, 9, 1): #from left column to right column
            
            CurrentSweet = Board[column][row]
            #FoundMatch, NumofMatched, Check, Move = Match(Board, CurrentSweet, CurrentSweet)
            y = 0
 
            NumMatched, Check = CheckSides(CurrentSweet,0) #0 checks L&R, 2 U&D
            if NumMatched >= 3:
                #do a try except - try to index the sweet your're adding if you
                #can index then its already in there so dont add, if you can
                for Candy in Check:
                    try:
                        MatchedSweets.index(Candy)
                    except ValueError :
                        MatchedSweets.append(Candy)
                        FoundMatch = True
                
            NumMatched, Check = CheckSides(CurrentSweet,2) #0 checks L&R, 2 U&D
            if NumMatched >= 3:
                for Candy in Check:
                        MatchedSweets.append(Candy)
                FoundMatch = True


    ##########################################################################################
    #The set of matched sweets are added to the list once for every sweet?! NEED TO FIX
    """for ListMatch in MatchedSweets:
        Duplicates = True
        while Duplicates:
            Count = MatchedSweets.count(sweet)
            if Count > 1:
                Duplicates = True
                MatchedSweets.remove(sweet)
            elif Count == 1:
                Duplicates = False
    #checkSweet = MatchedSweets[0][0]

    TempLenMS = len(MatchedSweets)
    #check the first sweet in the match list to see
    #if its in any of the other match lists - if it is then need to remove
    #remove that match "Check" list of matches
    for ListMatch in MatchedSweets:
        for sweet in ListMatch:
            if sweet == checkSweet:
                Duplicate = True
    """

                
    for sweet in MatchedSweets:
        Duplicates = True
        while Duplicates:
            Count = MatchedSweets.count(sweet)
            if Count > 1:
                Duplicates = True
                MatchedSweets.remove(sweet)
            elif Count == 1:
                Duplicates = False
        print("IGOT RID AND NOW I HAVE matched sweets list: ", len(MatchedSweets))

    for sweet in MatchedSweets:
        sweet.setMatch() #Flags sweet as matched to then be popped
        BoardCoords = sweet.getBoard()
        print("Found Matches inspaces", BoardCoords, sweet.getColour() )
        print("How many sweets I have in my matched sweets list: ", len(MatchedSweets))
        
    #if len(MatchedSweets) >2:
    #        FoundMatch = True
    """#check = list of the matched sweets 
            if Check[0] > 2:
                for item in Check[1]: #list of matched sweets
                    MatchedSweets.append(item)
                    FoundMatch = True
                                        
    if not FoundMatch :
        print("There was no match found the list is: ", MatchedSweets)
                    
    if FoundMatch:                    
        for sweet in MatchedSweets:
            sweet.setMatch() #Flags sweet as matched to then be popped
            
            BoardCoords = sweet.getBoard()
            print("Found Matches inspaces", BoardCoords, sweet.getColour() )

    return FoundMatch, Board, MatchedSweets"""

    return FoundMatch, MatchedSweets

def CheckSides(P1, NeighValue):
    toCheck = P1.getNeigh(Board) #All the neighbours    
    toCheck = P1.getNeigh(Board)[NeighValue] #Gives the neighbour of the original piece
    SameY = 1

    MatchedSweets = []
    MatchedSweets.append(P1)
    
    try:
        if toCheck.getColour() == P1.getColour(): #compares original and first neigh
            SameY += 1
            Consec = True
            MatchedSweets.append(toCheck)
            
            
            CurrentObj = toCheck ##was P1 changed temp
            while Consec:
                if CurrentObj.getColour() == CurrentObj.getNeigh(Board)[NeighValue].getColour():
                    SameY += 1
                    MatchedSweets.append(CurrentObj.getNeigh(Board)[NeighValue])    #Collecting all the matched sweets so can set flag as matched later
                    
                    CurrentObj = CurrentObj.getNeigh(Board)[NeighValue]
                else:
                    Consec = False
    except AttributeError:
        #print("On an edge")
        SameY = SameY
        #print(P1, P1.getNeigh(Board))
        #print("didn't make it 1 Piece on an edge")

    try:
        toCheck2= P1.getNeigh(Board)
        toCheck2 = P1.getNeigh(Board)[NeighValue+1] #Gives the neighbour of the original piece
      
        if toCheck2.getColour() == P1.getColour():
            SameY += 1
            Consec = True
            MatchedSweets.append(toCheck2)
            
            CurrentObj = toCheck2
            
            while Consec:
                if CurrentObj.getColour() == CurrentObj.getNeigh(Board)[NeighValue+1].getColour():
                    SameY += 1
                    MatchedSweets.append(CurrentObj.getNeigh(Board)[NeighValue+1])
                    CurrentObj = CurrentObj.getNeigh(Board)[NeighValue+1]
                else:
                    Consec = False
    except AttributeError:
        #print("2nd piece on an edge")
        SameY = SameY
        #print("didn't make it 2")

    if len(MatchedSweets) >2:
        print(len(MatchedSweets),"these are all my mactched sweets!: ", MatchedSweets)
    return SameY, MatchedSweets           
                
def DispBoard(imageName):
    width = 500
    height = 700
    initialise(width-7, height-9, "Board", PURPLE)
    
    mySurface.fill((150,0,150,100)) #Fills to a purple colour
    #mySurface.fill((255,186,212,100)) #Fills to a light pink colour
    #mySurface.fill((248,101,252,100)) #Fills to a light purple
    
    mySurface.blit(imageName,(20,20))            


            
def MakeBoard():
    Board = []
    for x in range(9):      #Creates empty 9 by 9 grid
        Board.append([])
        for y in range(9):
            Board[x].append("")
    return Board


def PopMatchedSweet(Board):

    #Sweet above needs to fall down to fill Board[x][y] = blank
    column = 0
    row = 7
    #print("Tibble", Board[column][row].getColour())
    for row in range(8, -1, -1): # from bottom to top
        for column in range(0, 9, 1): #from left column to right column
            
            
            if Board[column][row].getBlank(): # if the sweet i am looking is blank
                
                blankAbove = 0 # by default there are 0 blank squares above the current blank square
                count = 1 # by default one because we always swap at least 1 square up from the current blank.
                newRow = row-count 
                while Board[column][newRow].getBlank() and newRow > 0: # works out how many are blank above.
                    #While the next square up is a blank AND we haven't reach the top of the board.
                    count = count + 1 
                    newRow = row-count # decrease the row number = look up another 1 higher.
                    blankAbove = blankAbove + 1 # increase the number of blank squares in a row.

                test = row - blankAbove # if the row - blankabove is zero all squares above must've been blank.
                   #print("Blank Above = ", blankAbove)
                   #print("Sweet colour above = ", Board[column][row-(blankAbove+1)].getColour())
                if test != 0: # test will be zero if all squares are blank - do nothing in this case.
                    newRow = 1 + blankAbove # at least one sweet will drop down + the number of blank square above. 
                    blank = Board[column][row] # get the blank sweet
                    toReplace = Board[column][row-newRow] #get the live sweet that will drop down
                    Board = Move(blank,toReplace, Board) # swap them.
            
    return Board

def Refill(AllQs, Board):

    for row in range(8, -1, -1): # from bottom to top
        for column in range(0, 9, 1): #from left column to right column
            CurrentSweet = Board[column][row]
            if CurrentSweet.getBlank(): # if the sweet i am looking is blank
                NewSweet = AllQs[row].deQueue(row, column)
                #Board = Move(CurrentSweet, NewSweet, Board)
                Board[column][row] = NewSweet
                print("refillingggggg")
        #################################################################################
    
    return Board
         

def Populate(Board, Mode):
        ColourOps = ["P", "B", "G", "O", "R", "Y"]
        #Index = random.randint(0,5)
        xMove = 48
        yMove = 48
        Valid = False
        
        if Mode == "Normal":  
            Normal = open( "No Matches Board Colours.txt", "r")
            Index = 1
            FileContents = []
            for line in Normal:
                FileContents.append(line)

            for j in range (9):
                for i in range (9):
                    """Index = random.randint(0,5)
                    Col = ColourOps[Index]""" #Original
                    Index += 1 
                    Col = ColourOps[int(FileContents[Index])]
                    Board[i][j] = Jar.Sweet(Col,i,j, Board)
                    
        elif Mode == "Random":
             for j in range (9):
                for i in range (9):
                    Index = random.randint(0,5)
                    Col = ColourOps[Index]
                    Board[i][j] = Jar.Sweet(Col,i,j, Board)
        
        for a in range (2):
                for j in range (9):
                    for i in range (9):
                        MatchX = CheckSides(Board[i][j], 0)
                        MatchY = CheckSides(Board[i][j], 2)
                        if MatchX[0] >= 3 or MatchY[0] >= 3 : #check how many matched
                            Col = Board[i][j].getColour()
                            if Board[i][j].getColour() == Col:
                                Index = random.randint(0,5)
                                Col = ColourOps[Index]
                                Board[i][j] = Jar.Sweet(Col,i,j, Board)
        Board[i][j] = Jar.ColourBomb("D", i, j, Board)
        Board[i-1][j]= Jar.Striped("R", i-1, j, Board, "H")
        Board[i-2][j] = Jar.Wrapped("B", i-2, j, Board)
        #print(Board)

def PointCalc(Points, NumOfMatched, StripeMatch, CBMatch, NumAfterCB):

    if NumOfMatched == 3:
        Points += 60
    elif NumOfMatched == 4:
        Points += 120
    elif NumOfMatched == 5:
        Points += 200   
    else:
        Points += (NumOfMatched * 50)

    if StripeMatch:
        Points += (9 * 60)  #for all 9 sweets in the row/column
    if CBMatch:
        Points += 1200
        Points += (NumAfterCB * 60)

        
    return Points

def SplitColour(MatchedSweets):
    Match1 = []
    Match2 = []
    Colour1 = MatchedSweets[0].getColour()
    for sweet in MatchedSweets:     #Split them in terms of their new X and Y Coords
        if sweet.getColour() == Colour1:
            Match1.append(sweet)
        else:
            Match2.append(sweet)
            
    return Match1, Match2

def SplitPos(MatchedSweets):################################################################
    Match1 = []
    Match2 = []
    CompX, CompY = MatchedSweets[0].getBoard()
    sameX = []
    sameY = []
    for sweet in MatchedSweets:
        xMatch = False
        yMatch = False
        if sweet.getBoard()[0] == CompX:
            sameX.append(sweet)
            xMatch = True
        
        if sweet.getBoard()[1] == CompY:
            sameY.append(sweet)
            yMatch = True
        if not xMatch and not yMatch:
            Match2.append(sweet)
    if len(sameX) > 2:
        Match1 = sameX
    else:
        Match1 = sameY

    if len(Match1) < 3 or len(Match2) < 3:
        Match1 = MatchedSweets
        Match2 = []
    
    for sweet in Match1:
        print("Match1 = ",len(Match1), " with: ", sweet.getColour(), sweet.getBoard() )
    for sweet in Match2:
        print("Match 2 = ",len(Match2), " with: ", sweet.getColour(), sweet.getBoard() )
        
        
        
    return Match1, Match2

def StripeReaction(sweet):
    StrX, StrY = sweet.getBoard()
    WW2D = sweet.getDirection() #Which Way to Destroy
    ToDestr= []
    CB = False

    if WW2D == "V":
        #Destroy all the sweets that are in the same X coord but changing Y
        for i in range(-1, 8):
            Board[StrX][i].setMatch() #setting each sweet as matched
            if Board[StrX][i].getCB(): #if one of the sweets in the column is a CB
                NumAfterCB, ToDestr = CBReaction(Board[StrX][i], sweet,ToDestr) #collect all the sweets of the same colour 
                CB = True
    else:
        #Destroy all X coords in the same Y
        for i in range(-1, 8):
            Board[i][StrY].setMatch()
            if Board[i][StrY].getCB(): #if one of the sweets in the row is a CB
                NumAfterCB, ToDestr= CBReaction(Board[i][StrY], sweet,ToDestr)
                CB = True
    if CB: 
        CBandStripedReaction(ToDestr, False) #turns every sweet of the same colour as the striped into a stripe
        """The line below causes recursion calls a funct which calls stripe reac"""
    #IF DOESNT HAVVE TO TURN INTO STRIPE
    
def CBandStripedReaction(ToDestr,First): #Makes every sweet in TBDestroyed a striped version of that sweet 
    Dir = ["V", "H"]
    Index = random.randint(0,1)
    for sweet in ToDestr:##################################################
        Board[sweet.getBoard()[0]][sweet.getBoard()[1]] = Jar.Striped(sweet.getColour(), sweet.getBoard()[0], sweet.getBoard()[1], Board, Dir[Index])
        Board[sweet.getBoard()[0]][sweet.getBoard()[1]].setMatch()#this should fix it

    if First == True: #if its the first time
        for sweet in ToDestr:
            StripeReaction(sweet) #Every sweet becomes a striped in essesnce

def CBReaction(P1,P2,ToDestr):
    
    for row in range(-1, 8): # from bottom to top
        for column in range(-1, 8): #from left column to right column
            CurrentSweet = Board[column][row]
            if P1.getColour() == "D": # colour of CB is D
                ColourToCompare = P2.getColour()
            else:
                ColourToCompare = P1.getColour()
            #Colour of the sweet swapped with the CB
                
            if CurrentSweet.getColour() == ColourToCompare:
                ToDestr.append(CurrentSweet)
                CurrentSweet.setMatch()
    NumAfterCB = len(ToDestr)

    return NumAfterCB, ToDestr

            
def WrappedReaction(sweet):
    sweetX, sweetY = sweet.getBoard()

    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if sweetX+i > -1 and sweetX+i < 9 and sweetY+j > -1 and sweetY+j <9:
                Board[sweetX+i][sweetY+j].setMatch()
    
def SortMatchReaction(ListOfMatch, Board):
    StripedMatch = False   
    CBMatch = False
    WrappedReact = False
    NumAfterCB = 0
    ToDestr = [] #only used for the colourbomb sweets to be destroyed
    NumOfMatched = len(ListOfMatch)

    
    for sweet in ListOfMatch:   #From the matched sweets- if striped/colourbomb is one of the matched
        if sweet.getStriped():
            #run matched stripe function
            StripeReaction(sweet)
            StripedMatch = True
        if sweet.getCB():
            CBMatch = True
        if sweet.getWrapped():
            WrappedReact = True
            WrappedReaction(sweet)

    if CBMatch:
        NumAfterCB,ToDestr = CBReaction(P1,P2,ToDestr)


        
    
    if NumOfMatched == 2 and StripedMatch and not CBMatch: #Two Striped Swap
        StripeReaction(ListOfMatch[0])
        StripeReaction(ListOfMatch[1])

    if NumOfMatched == 2 and StripedMatch and CBMatch: #Swapped Striped with colourB
        CBandStripedReaction(ToDestr,True)
                
        
    if NumOfMatched == 5:   #Creates COLOURbOMB if 5 sweets matched
        #added to try and fix background drops of stripes and CBs not happening
        DropX, DropY = ListOfMatch[0].getBoard()
        
        print("Leave a colourbomb here!!")
        Board[DropX][DropY] = Jar.ColourBomb("D", DropX, DropY, Board)
            
                                             
    if NumOfMatched == 4:
        #added to try and fix background drops of stripes and CBs not happening
        DropX, DropY = ListOfMatch[0].getBoard()
        
        print("Leaving a striped sweet here!")
        
        #need to determine whether horiz or vert
        if P1.getColour() == "D":
            Colour = P2.getColour()
        else:
            Colour = P1.getColour()
        Board[DropX][DropY] = Jar.Striped(Colour, DropX, DropY, Board, Direction)
        NewStrSwe = Board[DropX][DropY]
        print("COLOUR AND COORDS: ",NewStrSwe.getColour(), NewStrSwe.getBoard())
    

    #MatchFound = True
    #while MatchFound:
    """
    Check = WholeBoardMatch(Board)      
    
    if Check[0]:
        Board = Check[1]
        ExtraMatched = Check[2]
        print(ExtraMatched)
        for sweet in ExtraMatched:
            sweet.smallImg()
            
        print("             Match found elsewhere")
        #MatchFound = Check[0]                        
        
    #Board = PopMatchedSweet(Board)"""
            #StripedMatch, CBMatch, NumAfterCB 
    return StripedMatch, CBMatch, NumAfterCB      #REturn if ColourBomb Macth for points 

def CheckWrappedMatch(Board):
    #need to fix for xtra matches
    # when they fall you cant compare the first sweet in the list anymore- it has to be the corner one
    WrappedMatch = False
    CompX, CompY = MatchedSweets[0].getBoard()
    for tries in range(2):
        sameX = []
        sameY = []
        for sweet in MatchedSweets:
            if sweet.getBoard()[0] == CompX:
                sameX.append(sweet)
            if sweet.getBoard()[1] == CompY:
                sameY.append(sweet)
        if len(sameX) == len(sameY):
            if sweet.getColour() != "D":
                Board[CompX][CompY] = Jar.Wrapped(sweet.getColour(), CompX, CompY, Board)
                WrappedMatch = True
            else:
                Board[CompX][CompY] = Jar.Wrapped("R" , CompX, CompY, Board)
                WrappedMatch = True
            print("I left a wrapped sweet in : ", CompX, CompY)
    CompX, CompY = MatchedSweets[len(MatchedSweets)-1].getBoard()
    return WrappedMatch


def DisplayFullBoard(EmptyBoardPic, NumOfMoves, Points):
    #Displaying Board
    fpsClock.tick(60)
    DispBoard(EmptyBoardPic)
    HeaderTexts(str(NumOfMoves) , mySurface.get_rect().centerx , 65)
    HeaderTexts(str(Points) , 400 , 65)
    for a in range(9):              #Displaying all sweets
        for b in range (9):
            if Board[a][b].getMatch():
                #print("popped!")
                b+=1
            else:
                Image = Board[a][b].getImage()
                Board[a][b].DisplaySweet(mySurface, Image)
    





#MAIN CODE LOOPs
               
Board = MakeBoard()
Populate(Board, "Random")
AllQs = [0,0,0, 0,0,0, 0,0,0]
for i in range(9):
    AllQs[i] = ToFall.BoardQueue(Board)


#45 & 40

initialise(width, height, my_caption, BLACK)
Choices = False,False
EmptyBoardPic = pygame.image.load("NormalEmptyBoard.png")
EmptyBoardPic = pygame.transform.scale(EmptyBoardPic, (450,650))

First= False
Second = False
Swipe = False
P1 = 0
P2 = 0
Matched = True
NumOfMoves = 20
Points = 0


Xtra = 0
Animation = False
Play = pygame.Rect(127,387,200,90)#clickrect
Rules = pygame.Rect(146,487,180,70)#clickrect
Normal = pygame.Rect(105,258,271,96)#clickrect
Extras = pygame.Rect(107,390,271,96)#clickrect

while not Choices[0]: #While haven't selected play
    while Choices == (False,False):
        fpsClock.tick(60)
        Menu.DisplayMenu("Menu2.png")
        
        Choices = clickmenu(Play, Rules)

    Back = (False, False)
    if Choices[1]: #if you clicked on Op2 = Rules button
        while not Back[0]: # until you click on the back button
            initialise(width-5, 685, my_caption, BLACK)
            Menu.DisplayRules()

            BackButton = pygame.Rect(28,32,117,59)
            Back = clickmenu(BackButton, Rules)
        Choices = (False,False)
    
    
if Choices[0]:      #if you chose play Chose Op 1
    #Menu.DisplayMenu("Options.png") #if decide to add another level
    Level = clickmenu(Normal, Extras)
    EndGame = False
    while not EndGame:     #Running the game
        if NumOfMoves == 0:  #should be if == -1
            EndGame = True
            #show endscreen ###############################################################################
            
        Matched = True
        
        # Display Sweets in Board:
        DisplayFullBoard(EmptyBoardPic, NumOfMoves, Points)
        

        ### have the select menu display if true then have a full JellyBoard to display
        ### reneder obstacles - if not jelly level then doesn't have anything to render

        
        #Actual Game - Clicking and Swiping
                    
        ### Can make the pop return its co-ords of popped - deal with jelly that way?
        
        Board = PopMatchedSweet(Board)  # if blank remove
        ### CheckObstacle(COORDS) Can run this function to deal with jelly, if no jelly then no prob
        Refill(AllQs, Board)
                               # if match then animate is done automitically in the setMatch function
                               
        Animate = False
        for row in range(8, -1, -1): # from bottom to top
            for column in range(0, 9, 1): #from left column to right column
                Sweet = Board[row][column]
                if Sweet.getAnimate():
                    Sweet.Animate(mySurface)
                    Animate = True              #and disable other code


        if not Animate:
            #not checked - set after every move
            #are matches
            #no matches
            """ XtraMatches = 0 #Not known
                XtraMatches = True # There are Matches in the board
                XtraMatches = False # There are no matches in the board   """
            if Xtra == 0: #So not checked the rest of the board
                Xtra, XtraBoardMatches = WholeBoardMatch(Board)#then check the rest of the board
                #ExtraMatches = true or false dependent on whether match
                
            if Xtra == True : #there ARE matches
                Xtra = 0  #then the board has changed so need to check again
                print("Extra board matches = ", len(XtraBoardMatches))
                if len(XtraBoardMatches) > 5:
                    WrappedMatch = CheckWrappedMatch(Board)
                    if not WrappedMatch:####################################### what if wrapped and other matches
                        XMatch1, XMatch2 = SplitColour(XtraBoardMatches)
                        if len(XMatch1) > 5:
                            XMatch1a, XMatch1b = SplitPos(XtraBoardMatches)
                            StripedMatch, CBMatch, NumAfterCB  = SortMatchReaction(XMatch1a, Board)
                            StripedMatch, CBMatch, NumAfterCB  = SortMatchReaction(XMatch1b, Board)
                            StripedMatch, CBMatch, NumAfterCB  = SortMatchReaction(XMatch2, Board)
                            print("EXTRA MATCHES length: ", len(XMatch1a), len(XMatch1b), len(XMatch2))
                        elif len(XMatch2) > 5:
                            XMatch2a, XMatch2b = SplitPos(XtraBoardMatches)
                            StripedMatch, CBMatch, NumAfterCB  = SortMatchReaction(XMatch2a, Board)
                            StripedMatch, CBMatch, NumAfterCB  = SortMatchReaction(XMatch2b, Board)
                            StripedMatch, CBMatch, NumAfterCB  = SortMatchReaction(XMatch1, Board)
                            print("EXTRA MATCHES length: ", len(XMatch1), len(XMatch2a), len(XMatch2b))
                        else:
                            StripedMatch, CBMatch, NumAfterCB  = SortMatchReaction(XMatch1, Board)
                            StripedMatch, CBMatch, NumAfterCB  = SortMatchReaction(XMatch2, Board)
                            print("EXTRA MATCHES length: ", len(XMatch1), len(XMatch2))
                    else:
                                StripedMatch = False
                                CBMatch = False
                                NumAfterCB = 0
                else:
                    StripedMatch, CBMatch, NumAfterCB  = SortMatchReaction(XtraBoardMatches, Board)
                    Points = PointCalc(Points, len(XtraBoardMatches), StripedMatch, CBMatch, NumAfterCB)
                
            if Xtra == False:  #arent any extra matches
                try:          
                    Clicked, Swipe, P1, P2 = ClickSquare(First, Second, Swipe, P1, P2)
                except AttributeError:  #checking collide point but can't for integer -1
                    print("after click- shocks")#dont shouldnt be -1 for long time
                                            #the sweets above would fall b4 nxt click
                if not isinstance(P1, numbers.Real) and not isinstance(P2, numbers.Real) and (NumOfMoves > 0 ) and P1 != P2 and (P1 in P2.getNeigh(Board)):

                    print(P1.getColour(), P2.getColour())
                    Board   = Move(P1,P2, Board)
                    Matched, NumOfMatched, MatchedSweets, Direction = Match(Board,P1,P2) #returns Direction
                    print("NUMBER OF MATCHED SWEETS: ", NumOfMatched)

                    
                    if NumOfMatched != 0: # if there is a match and theyre neighbours
                        DropX, DropY = P1.getBoard()
                        Colour = P1.getColour()
                        # More than 1 set of match make list
                        if NumOfMatched > 5:
                            WrappedMatch = CheckWrappedMatch(Board)
                            if not WrappedMatch:
                                print("there are two different sets of matches happening")
                                Match1, Match2 = SplitColour(MatchedSweets)
                                #pUT these if statements in a func and call for both lists here
                                StripedMatch, CBMatch, NumAfterCB  = SortMatchReaction(Match1, Board)
                                StripedMatch, CBMatch, NumAfterCB  = SortMatchReaction(Match2, Board)
                            else:
                                StripedMatch = False
                                CBMatch = False
                                NumAfterCB = 0
                        else:
                            StripedMatch, CBMatch, NumAfterCB = SortMatchReaction(MatchedSweets, Board)

                        NumOfMoves -= 1
                        
                        
                        Points = PointCalc(Points, NumOfMatched, StripedMatch, CBMatch, NumAfterCB)
                        #Edit Points Calc for Striped row/Coloumn and ColourBomb Points

                        XtraMatches = 0
                        #to disable background checks
                        XtraMatches = False
                        
                    else: # if there wasn't a match move them back
                        Board = Move(P1,P2, Board)
                        

                    print("looping main code")
                    print("RESET")
                    P1 = 0
                P2 = 0
                       

        pygame.display.update() # updates the display







    
