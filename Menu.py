#Displays The Menu- initialises etc
import pygame, sys, random
from pygame.locals import *
import pygame.freetype # FOR TEXT
width = 475
height = 750
my_caption = 'Task1'
fpsClock = None
BLACK = (0,0,0,255)
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
#Render
    
def DisplayMenu(imgstring):
       
    mySurface.fill((150,0,150,100)) #Fills to a purple colour
    imageName = pygame.image.load(imgstring)
    imageName = pygame.transform.scale(imageName, (425,700))

    #rect = imageName.get_rect()
    
    mySurface.blit(imageName,(20,20))

    pygame.display.update()

def DisplayRules():
       
    mySurface.fill((247,186,212,100)) #Fills to a purple colour
    imageName = pygame.image.load("RulesScreen.png")
    imageName = pygame.transform.scale(imageName, (425,638))

    #rect = imageName.get_rect()
    
    mySurface.blit(imageName,(20,20))

    pygame.display.update()

initialise(width, height, my_caption, BLACK)
