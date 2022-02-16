import pygame
import const
pygame.font.init()
defaultFont = pygame.font.Font(None, 32)
class Button:
    def __init__(self,left,top,width,height,color,text='',blackTxt=False):
        self.top=top
        self.left=left
        self.width=width
        self.height=height
        self.color=color
        self.box=pygame.Rect(left,top,width,height)
        self.text=text
        self.blackTxt=blackTxt
        self.updateText()

    def updateText(self):
        if(self.text!=''):
            if(self.blackTxt==False):
                self.textSurface = defaultFont.render(self.text,True,(255,255,255))
            else:    
                self.textSurface = defaultFont.render(self.text,True,(0,0,0))
            self.textRect=self.textSurface.get_rect(center=self.box.center)
            self.box.width=max(self.width,self.textSurface.get_width()+10)
    def draw(self,screen):
        self.updateText()
        pygame.draw.rect(screen,self.color,self.box,border_radius=10)
        if(self.text != ''):
            screen.blit(self.textSurface,self.textRect)
    
    def delete(self,screen):
        pygame.draw.rect(screen,const.backgroundColour,self.box,border_radius=10)
        if(self.text != ''):
            self.textSurface = defaultFont.render(self.text,True,const.backgroundColour)
            self.textRect=self.textSurface.get_rect(center=self.box.center)
            screen.blit(self.textSurface,self.textRect)
      
    def changeColor(self,newColor):
        self.color= newColor
    
    def addText(self,newChar):
        self.text+=newChar
        self.updateText()
    
    def deleteText(self):
        self.text=self.text[:-1]
        self.updateText()

    def updateHeight(self,newHeight):
        self.box.h=newHeight
        self.box.top=const.buttomBars -newHeight
    
    def clearAll(self,screen):
        self.top=const.barsStartHeight
        self.width=50
        self.height=const.maksHeightBar
        self.color=const.backgroundColour
        self.box=pygame.Rect(self.left,self.top,self.width,self.height)
        self.text=''
        self.blackTxt=False
        self.draw(screen)
