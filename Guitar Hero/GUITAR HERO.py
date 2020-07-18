import pygame
import random
from pygame.locals import *
import time
import sys
import wave
import re
import numpy
import math
import songList

pygame.init()
pygame.mixer.music.load('Legado 47- Fantasmas e Monstros.mp3')
pygame.mixer.music.play()

##COLOURS
BLACK    = (0, 0, 0);   WHITE   = ( 255, 255, 255)
GREEN    = (0, 255, 0); RED     = ( 255, 0, 0)
BLUE     = (0, 0, 255); CYAN    = ( 255, 0, 0)

import ctypes

messageBox = ctypes.windll.user32.MessageBoxW

messageBox(None,"Make sure your sound is on, and enter your name so your score is saved","Musical Keys",0x40 | 0x0)

##Screen Size
size    = (600, 700)
# (467, 700)

##HIGHSCORES FILE

file = open("highscores.txt", "r")
lineList = file.readlines()
file.close()


def controller(key):
    global status
    if status == "stopped":
        if key == K_RETURN:
            pygame.mixer_music.play()
            status = "playing"
            
    elif status == "paused":
        if key == K_RETURN:
            pygame.mixer_music.stop()
            status = "stopped"
        elif key == K_SPACE:
            pygame.mixer.music.unpause()
            status = "playing"

    elif status == "playing":
        if key == K_RETURN:
            pygame.mixer.music.stop()
            status = "stopped"
        elif key == K_SPACE:
            pygame.mixer.music.pause()
            status = "paused"

#if re.search(propieties, "BPM"):
    #print("Playing: song")

##BOOLEANS
done    = False # Loop until the close clicked
intro = False # Loop until intro is over
running = True # another boolean for a loop to blit images
screenopened = False
introm = True
namein = False

#Clock for FPS
clock = pygame.time.Clock() #Load pygame clock for refresh rate

##Number variables
                   #1        #2         #3         #4
colisionCoords = [(77,595), (153,595), (230, 595), (306,595)]
score = 0 
lives = 3
speed = 0
drawcircle = 1
nCircles = 0
pos2 = 20

##IMAGES
hat = pygame.image.load('hat.png')
img = pygame.image.load('background1.png')
imgbackground = pygame.image.load('background.png')

##MUSIC
intromusic = pygame.mixer.Sound("CoolerBackgroundSong.wav")
intromusic.set_volume(0.1)
beepSound = pygame.mixer.Sound("beep-01a.wav")
beepSound.set_volume(0.1)

myfont = pygame.font.SysFont("arial", 30)

while not intro:
    if namein == False:
        name = input("Enter your name: ")
        namein = True
        
    if screenopened == False:
        screen = pygame.display.set_mode(size)
        pygame.display.flip()
        pygame.display.set_caption("Music Keys | Score 0")
        screenopened= True
        
    highscore = myfont.render(lineList[len(lineList)-1], 1, WHITE)
    screen.blit(highscore, (200, 656))

    #FULL SCREEN
    #DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    
    ##SCORE TEXT
    screen.blit(img,(0,0))
    prev = myfont.render("Previous score: ", 1, WHITE)
    highscore = myfont.render(lineList[len(lineList)-1], 1, WHITE)
    screen.blit(highscore, (300, 656))
    screen.blit(prev, (100, 656))

    ##EASY HARD BUTTONS
    rect1 = pygame.draw.rect(screen,WHITE, (60,350,140,100),0)
    rect2 = pygame.draw.rect(screen,WHITE, (280,350,140,100),0)
    rect3 = pygame.draw.rect(screen,WHITE, (280,350,140,100),0)

    imgeasy = pygame.image.load('easy.png')
    screen.blit(imgeasy,(60,360))
    imghard = pygame.image.load('hard.png')
    screen.blit(imghard,(280,360))

    ##MUSIC
    if introm == True:
        pygame.mixer.music.stop()
        intromusic.play()
        introm = False
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            intro = True # Flag that we are done so we exit this loop
            done = True
            intromusic.stop()
            
        ##CLICKING EITHER EASY OR HARD
        position = pygame.mouse.get_pos()
        x = position[0]
        y = position[1]
        if pygame.mouse.get_pressed()[0]:
            is_insidespeed1 = rect1.collidepoint(x,y)
            is_insidespeed2 = rect2.collidepoint(x,y)
            if is_insidespeed1:
                speed = 1
                rect1 = pygame.draw.rect(screen,GREEN, (100,350,100,100),0)
                intro = True
                pygame.display.flip()
                intromusic.stop()
            if is_insidespeed2:
                speed = 3
                rect2 = pygame.draw.rect(screen,GREEN, (250,350,100,100),0)
                intro = True
                pygame.display.flip()
                intromusic.stop()

            
while not done:

    pygame.display.flip()

    ##WHERE CIRCLE IS DROPPED
    pos = random.randint(1,4)

    if nCircles == 0:
        pos2 = 20
        if pos == 1:
            pos1 = 77
            COLOUR = RED
            nCircles = 1
            drawcircle = 1
            pygame.display.flip()
        if pos == 2:
            pos1 = 153
            COLOUR = GREEN
            nCircles = 1
            drawcircle = 1
            pygame.display.flip()
        if pos == 3:
            pos1 = 230
            COLOUR = BLACK
            nCircles = 1
            drawcircle = 1
            pygame.display.flip()
        if pos == 4:
            pos1 = 306
            COLOUR = BLUE
            nCircles = 1
            drawcircle = 1
            pygame.display.flip()
            
        if pos == "random":
            print("Special mode: Random")
            

    ##LIVES AND BACKGROUND
    if running == True:
        screen.blit(imgbackground,(0,0)) 
        pos2 = pos2 + speed
    if lives == 3:
        screen.blit(hat,(400,140))
        screen.blit(hat,(400,200))
        screen.blit(hat,(400,260))
    if lives == 2:
        screen.blit(hat,(400,140))
        screen.blit(hat,(400,200))
    if lives == 1:
        screen.blit(hat,(400,140))
    if drawcircle == 1:
        myCircle = pygame.draw.circle(screen,BLUE,(pos1,pos2), 9,0)


    ##Printing live score to the screen
    score = str(score)
    myfont = pygame.font.SysFont("arial", 30)
    scoretext = myfont.render(score, 1, (37,222,255))
    screen.blit(scoretext, (200, 656))
    pygame.display.flip()

    ##If 0 Lives game is over
    if lives == 0:
        done = True # Flag that we are done so we exit this loop

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            messageBox(None,"You lose!","Double Hero",0x40 | 0x0)
            time.sleep(2)
            done = True # Flag that we are done so we exit this loop
            sys.exit()

        if pos2 >= 660:
            lives = lives - 1
            drawcircle = 0
            nCircles = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                is_inside = myCircle.collidepoint(77,595)
                if is_inside:
                    drawcircle = 0
                    nCircles = 0
                    score = int(score) + 1
                    beepSound.play()
                    pygame.display.set_caption("Musical Keys | Score " + str(score))
                else:
                    lives = lives - 1
                    drawcircle = 0
                    nCircles = 0
            if event.key == pygame.K_2:
                is_inside = myCircle.collidepoint(153,595)
                if is_inside:
                    drawcircle = 0
                    nCircles = 0
                    score = int(score) + 1
                    beepSound.play()
                    pygame.display.set_caption("Musical Keys | Score " + str(score))
                else:
                    lives = lives - 1
                    drawcircle = 0
                    nCircles = 0
            if event.key == pygame.K_3:
                is_inside = myCircle.collidepoint(230, 595)
                if is_inside:
                    drawcircle = 0
                    nCircles = 0
                    score = int(score) + 1
                    beepSound.play()
                    pygame.display.set_caption("Musical Keys | Score " + str(score))
                else:
                    lives = lives - 1
                    drawcircle = 0
                    nCircles = 0
            if event.key == pygame.K_4:
                is_inside = myCircle.collidepoint(306,595)
                if is_inside:
                    drawcircle = 0
                    nCircles = 0
                    score = int(score) + 1
                    beepSound.play()
                    pygame.display.set_caption("Musical Keys | Score " + str(score))
                else:
                    lives = lives - 1
                    drawcircle = 0
                    nCircles = 0

            else:
                print("<==========><Input><==========>")

#################################################################################################
            #Testing!
            if event.key == pygame.K_5:
                is_inside = myCircle.collidepoint(153,595)
                if is_inside:
                    drawcircle = 0
                    nCircles = 0
                    score = int(score) + 1
                    beepSound.play()
                    pygame.display.set_caption("Musical Keys | Score " + str(score))
                else:
                    lives = lives - 1
                    drawcircle = 0
                    nCircles = 0

#################################################################################################


##SAVING THE SCORE                    
file = open("highscores.txt", "a")
score = str(score)
file.write(name)
file.write(":  ")
file.write(score)
file.write("\n")
file.close()
pygame.quit()
