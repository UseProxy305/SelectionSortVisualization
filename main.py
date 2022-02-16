import pygame
import const #This file contains necessary constants for this program
from Buttons import Button
from Algorithms import inputChecker
from Algorithms import arrayHeightSetter
from Algorithms import highlightOrder
from Algorithms import barsChangeDraw
import time


screen=pygame.display.set_mode((const.width,const.height))
pygame.font.init()
defaultFont = pygame.font.Font(None, 32)
pygame.display.set_caption("Array")
screen.fill(const.backgroundColour)
quitButton = Button(const.quitStartWidth,const.quitStartHeight,const.quitWidth,const.quitHeight,const.rectangleColor,'QUIT')
ArrayInputText= Button(25,25,200,50,const.backgroundColour,'Enter elements:',True)
startButton=Button(220,100,const.quitWidth,const.quitHeight,const.rectangleColor,'START')
ArrayInput=Button(220,25,100,50,const.rectangleColor)
InvalidInputText= Button(25,75,180,50,const.backgroundColour,'Invalid Input!!',True)
clock = pygame.time.Clock()
bars=[]
for i in range(10):
    bars.append(Button(100+(i*75),const.barsStartHeight,50,const.maksHeightBar,const.backgroundColour))
for i in bars:
    i.draw(screen)

pygame.display.flip()

takeInput=False
userText=''
startCommand=False
setted=False
numberOfStep=0

highlightList=list()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if quitButton.box.collidepoint(event.pos):
                pygame.quit()
            if ArrayInput.box.collidepoint(event.pos):
                takeInput = not takeInput
            if startButton.box.collidepoint(event.pos):
                startCommand= not startCommand
        
        if event.type == pygame.KEYDOWN:
            if takeInput:
                if event.key == pygame.K_RETURN:
                    InvalidInputText.delete(screen)
                    checker=inputChecker(ArrayInput.text,InvalidInputText,screen)
                    if checker:
                        arrayInput=ArrayInput.text.split(",")
                        setted=arrayHeightSetter(bars,arrayInput,InvalidInputText,screen)
                        numberOfStep=0
                        highlightList=highlightOrder(arrayInput)
                    takeInput=not takeInput
                elif event.key == pygame.K_BACKSPACE:
                    ArrayInput.delete(screen)
                    ArrayInput.deleteText()
                else:
                    ArrayInput.addText(event.unicode)
        
        mouse =pygame.mouse.get_pos()
        
        if numberOfStep!=len(highlightList):
            time.sleep(0.2)
            highlighting=highlightList[numberOfStep]
            if not (highlighting[0] in [-1,-2]):

                bars[highlighting[1]].changeColor(const.brightRectangleColor)
                bars[highlighting[1]].draw(screen)

                bars[highlighting[0]].changeColor(const.selectedRectangleColor)
                bars[highlighting[0]].draw(screen)
            elif highlighting[0]== -2:
                bars[highlighting[1]].changeColor(const.rectangleColor)
                bars[highlighting[1]].draw(screen)
            else:
                barsChangeDraw(highlighting[1],highlighting[2],bars,arrayInput,InvalidInputText,screen)
            numberOfStep +=1
            if numberOfStep == len(highlightList):
                numberOfStep=0
                highlightList=[]

        if quitButton.box.collidepoint(mouse) :
            quitButton.changeColor(const.brightRectangleColor)
        elif (quitButton.color == const.brightRectangleColor) :
            quitButton.changeColor(const.rectangleColor)
        if startButton.box.collidepoint(mouse) :
            startButton.changeColor(const.brightRectangleColor)
        elif (startButton.color == const.brightRectangleColor) :
            startButton.changeColor(const.rectangleColor)

        startButton.draw(screen)
        ArrayInputText.draw(screen)
        quitButton.draw(screen)
        ArrayInput.draw(screen)
        #clock.tick(120)
        pygame.display.update()



