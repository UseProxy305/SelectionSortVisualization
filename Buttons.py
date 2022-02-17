import pygame
import const
pygame.font.init()
defaultFont = pygame.font.Font(None, const.fontSize) #Font Size Setting
#Button Class 
class Button:
    #Constructor
    def __init__(self,left,top,width,height,color,text='',blackTxt=False):
        self.top=top
        self.left=left
        self.width=width
        self.height=height
        self.color=color
        self.box=pygame.Rect(self.left,self.top,self.width,self.height)
        self.text=text
        self.blackTxt=blackTxt
        self.updateText()

    #Update Text is setting the position of text and width of Button when there is a long input than expected
    def updateText(self):
        if(self.text!=''):  #If there is a text in the button
            if(self.blackTxt==False):   #Set the color of text
                self.textSurface = defaultFont.render(self.text,True,(255,255,255)) #White Text
            else:    
                self.textSurface = defaultFont.render(self.text,True,(0,0,0))   #Black Text
            self.textRect=self.textSurface.get_rect(center=self.box.center)     #Set the text position on the center
            self.box.width=max(self.width,self.textSurface.get_width()+10)      #Adjust the width when there is a long input
    
    #This Method is for drawing the button into screen which is given as an argument
    def draw(self,screen):
        self.updateText() #Recall update text (In case of something unexpected)
        pygame.draw.rect(screen,self.color,self.box,border_radius=10)   #Draw the button on the screen with an smooth corner
        if(self.text != ''):
            screen.blit(self.textSurface,self.textRect)                 #Draw the text
    
    #Deleting the object on the screen
    #Actually, it is not deleting just drawing with backgroundcolour :)
    def delete(self,screen):
        pygame.draw.rect(screen,const.backgroundColour,self.box,border_radius=10) #Draw the button with backgroundcolor
        if(self.text != ''):
            self.textSurface = defaultFont.render(self.text,True,const.backgroundColour) #The color of text is backgroundColor
            self.textRect=self.textSurface.get_rect(center=self.box.center)
            screen.blit(self.textSurface,self.textRect) #Draw the text with backgroundcolor
    
    #Changing color method
    def changeColor(self,newColor):
        self.color= newColor                            #Set the color
    
    #Method for adding a char or string to text of button 
    def addText(self,newChar):
        self.text+=newChar                              #Add a string or char into that text
        self.updateText()                               #Since text is updated, call the updateText method
    
    #Delete the last char of the text of button
    def deleteText(self):                               
        self.text=self.text[:-1]                        #Last character is ommited
        self.updateText()                               #Since text is updated, call the updateText method

    #Updating height  (for ONLY BARS)
    def updateHeight(self,newHeight):
        #Silly Change (Just for syntactic sugar)
        self.height=newHeight                           #Update height membet (However, it is not affected to draw, since box member is being drawn)
        
        self.box.h=newHeight                            #Update real height parameter of the member "box"
        self.box.top=const.buttomBars -newHeight        #Update the top position for the bar
    
    #Clearing Parameter
    def clearAll(self,screen):
        self.top=const.barsStartHeight
        self.width=50
        self.height=const.maksHeightBar
        self.color=const.backgroundColour
        self.box=pygame.Rect(self.left,self.top,self.width,self.height)
        self.text=''
        self.blackTxt=False
        self.draw(screen)       #ReDraw since color is background color, it is kinda disappeared
