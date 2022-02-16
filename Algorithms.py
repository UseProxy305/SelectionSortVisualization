import re
import const
import time
import pygame
def inputChecker(inputText,InvalidInputText,screen):
    checker = re.search(r"[0-9]+(,[0-9]+)*", inputText)
    if (checker == None) or (checker.group()!=inputText):
        InvalidInputText.draw(screen)
        return False
    return True

def arrayHeightSetter(barArray,inputArray,InvalidInputText,screen,green=-1):
    resetAllBars(barArray,screen)
    if len(barArray) < len(inputArray):
        print("ERROR")
        InvalidInputText.draw(screen)
        return False
    maxValue=max([int(i) for i in inputArray])
    for ind,val in enumerate(inputArray):
        color=const.rectangleColor
        if green != -1:
            color=const.perfectRectangleColor
            green-=1
        newHeight=float(int(val)*const.maksHeightBar)/(maxValue)
        barArray[ind].updateHeight(newHeight)
        barArray[ind].changeColor(color)
        barArray[ind].addText(inputArray[ind])
        barArray[ind].draw(screen)
    return True

def resetAllBars(barArray,screen):
    for i in barArray:
        i.delete(screen)        
        i.clearAll(screen)

def highlightOrder(inputArrayOrg):
    highlightlist=[]
    inputArray=[int(i) for i in inputArrayOrg]
    for ind in range(len(inputArray)):
        min_ind=ind
        highlightlist.append([min_ind,ind])
        for j in range(ind+1,len(inputArray)):
            if inputArray[min_ind] > inputArray[j]:
                highlightlist.append([-2,min_ind])
                highlightlist.append([min_ind,j])
                min_ind=j
            highlightlist.append([min_ind,j])
        highlightlist.append([-1,min_ind,ind])
        inputArray[ind],inputArray[min_ind] =inputArray[min_ind],inputArray[ind]
    return highlightlist

def barsChangeDraw(ind1,ind2,barArray,inputArray,invalidInputText,screen):
    #barArray[ind1],barArray[ind2]=barArray[ind2],barArray[ind1]
    inputArray[ind1],inputArray[ind2]=inputArray[ind2],inputArray[ind1]
    arrayHeightSetter(barArray,inputArray,invalidInputText,screen,ind2)