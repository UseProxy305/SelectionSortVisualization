#Libraries
import pygame #It is the base for project
import const #This file contains necessary constants for this program
from time import sleep # Sleep function is imported
from Buttons import Button #Button Class is imported see Buttons.py
#Algorithms that are going to be applied
from Algorithms import inputChecker
from Algorithms import arrayHeightSetter
from Algorithms import highlightOrder
from Algorithms import barsChangeDraw

 

#Initialize Part
screen=pygame.display.set_mode((const.width,const.height)) #Set Width & Height
pygame.font.init() #Writing with a text is enabled
defaultFont = pygame.font.Font(None, const.fontSize) #Setted Font Size
pygame.display.set_caption("Selection Sort Algorithm Visualtion")   #Caption for the application
screen.fill(const.backgroundColour) #Background Color is painted into that whole screen
#Buttons
quitButton = Button(const.quitStartWidth,const.quitStartHeight,const.quitWidth,const.quitHeight,const.rectangleColor,'QUIT')
arrayInputMessage= Button(const.arrayInputMsgLft,const.arrayInputMsgTop,const.arrayInputMsgWidth,const.arrayInputMsgHeight,const.backgroundColour,'Enter elements:',True)
startButton=Button(const.startLeft,const.startTop,const.quitWidth,const.quitHeight,const.rectangleColor,'START')
inputArrayBox=Button(const.startLeft,const.arrayInputMsgTop,const.arrayInputBoxWidth,const.arrayInputBoxHeight,const.rectangleColor)
invalidInputText= Button(const.arrayInputMsgLft,const.startTop,180,const.invalidInputMsgHeight,const.backgroundColour,'Invalid Input!!',True)
creditsInfo=Button(325,75,450,50,const.backgroundColour,'made by Berkay IPEK',True)
#Note: Credits Info is not setted according to const.py 
clock = pygame.time.Clock() #To be able to set 60 FPS
bars=[Button(100+(i*75),const.barsStartHeight,50,const.maksHeightBar,const.backgroundColour) for i in range(10)] #Set default bar settings
#Note: It is filled with backgroundColor therefore it looks like disabled
#Note 2: It is made by Button Class although it is a bar 
for i in bars:
    i.draw(screen) #draw all bars with a backgroundcolor so it is dissapeared
pygame.display.flip()

#Init variables 
takeInput=False #Take input flag
userText='' #Input string 
startCommand=False  #Start button is pressed flag
setted=False        #Highlight start flag
numberOfStep=0      #Step Counter
highlightList=list()    #Highlight List

#MAIN LOOP
while True:
    for event in pygame.event.get(): #If position of mouse is shifted or a key is pressed
        if event.type == pygame.QUIT:   # Default quit button is pressed
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN: #If there is a click
            if quitButton.box.collidepoint(event.pos): #if quit button is pressed
                pygame.quit()
            if inputArrayBox.box.collidepoint(event.pos): #if input box is pressed  
                takeInput = not takeInput   #Ready to take input (or it is finished)
            if startButton.box.collidepoint(event.pos): #if start button is pressed
                startCommand= not startCommand #Ready to sort array 
        
        if event.type == pygame.KEYDOWN: #If a button of keyboard is pressed
            if takeInput: #If it is ready to take input
                if event.key == pygame.K_RETURN:                #If a ENTER is pressed 
                    invalidInputText.delete(screen)                 #See delete method of Button Class
                    checker=inputChecker(inputArrayBox.text,invalidInputText,screen) #Check the input format see inputChecker func in Algorithms.py
                    if checker:                                     #If it is in correct format
                        arrayInput=inputArrayBox.text.split(",")        #Turn this into a string array
                        setted=arrayHeightSetter(bars,arrayInput,invalidInputText,screen)   #Set heights of bars see in Algorithms.py
                        numberOfStep=0                                  #Clear the integer variable "numberOfStep"
                        highlightList=highlightOrder(arrayInput)        #Highlight Order is set see in Algorithms.py
                    takeInput=not takeInput
                elif event.key == pygame.K_BACKSPACE:           #If a backspace is pressed
                    inputArrayBox.delete(screen)
                    inputArrayBox.deleteText()                      #Delete the last character of current character
                else:                                           #Otherwise
                    inputArrayBox.addText(event.unicode)            #Just add the charac   
    #END OF EVENT WAITING

    if startCommand and numberOfStep!=len(highlightList):       #wait for start button and checks # of step
        sleep(const.sleepAmount)                                    #wait some time to be more eye-pleasing
        highlighting=highlightList[numberOfStep]                    #Highlight the numberOfStep'th elements 
        
        #This part is directly related to highlightOrder Function see in Algorithms.py
        if not (highlighting[0] in [-1,-2]):
            bars[highlighting[1]].changeColor(const.brightRectangleColor)
            bars[highlighting[1]].draw(screen)
            bars[highlighting[0]].changeColor(const.selectedRectangleColor)
            bars[highlighting[0]].draw(screen)
        elif highlighting[0]== -2:
            bars[highlighting[1]].changeColor(const.brightRectangleColor)
            bars[highlighting[1]].draw(screen)
        else:
            barsChangeDraw(highlighting[1],highlighting[2],bars,arrayInput,invalidInputText,screen)
        
        numberOfStep +=1 #Go to next step
        if numberOfStep == len(highlightList): #When it is finished clear all necessary variables
            numberOfStep=0
            highlightList=[]
            startCommand=False
    
    mouse =pygame.mouse.get_pos() #Get the position of mouse
    if quitButton.box.collidepoint(mouse) : #If mouse is on the Quit Button
        quitButton.changeColor(const.brightRectangleColor)  #Highlight the button
    elif (quitButton.color == const.brightRectangleColor) : #If mouse is no longer on the Quit Button
        quitButton.changeColor(const.rectangleColor)        #No longer highlighted color
    if startButton.box.collidepoint(mouse) : #If mouse is on the Start Button
        startButton.changeColor(const.brightRectangleColor) #Highlight the button
    elif (startButton.color == const.brightRectangleColor) : #If mouse is no longer on the Start Button
        startButton.changeColor(const.rectangleColor)         #No longer highlighted color

    #Drawing Part
    startButton.draw(screen)
    arrayInputMessage.draw(screen)
    quitButton.draw(screen)
    inputArrayBox.draw(screen)
    creditsInfo.draw(screen)

    clock.tick(const.fps) #Set FPS
    pygame.display.update()#Update the frame
#END OF WHILE LOOP



