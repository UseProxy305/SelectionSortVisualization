import re
import const

#Checks the input is format of "N,N,N,N,..,N"
#return False if it is not correct
#return True if it is correct
def inputChecker(inputText,InvalidInputText,screen):
    checker = re.search(r"[0-9]+(,[0-9]+)*", inputText) #Regex Function
    if (checker == None) or (checker.group()!=inputText):
        #If it is none there is no match. (checker == None)
        #If matched case is not the same with input text, that means it is invalid. (checker.group()!=inputText)
        InvalidInputText.draw(screen)
        return False
    return True

#This function is to set heights of bars
#Also, it is drawing
#Note: It is returning True if size is proper
def arrayHeightSetter(barArray,inputArray,InvalidInputText,screen,green=-1):
    resetAllBars(barArray,screen)                                           #Firstly, reset the bars
    if len(barArray) < len(inputArray):                                     #Compare the length of input and number of bars
        InvalidInputText.draw(screen)                                       #Invalid Input !! is printed
        return False
    maxValue=max([int(i) for i in inputArray])                              #Take the maximum value of input Array
    for ind,val in enumerate(inputArray):
        color=const.rectangleColor                                          #Set the default color
        if green != -1:
            color=const.perfectRectangleColor                               #Change color to green if sorting part is finished
            green-=1                                                        
        newHeight=float(int(val)*const.maksHeightBar)/(maxValue)            #Set the height according to biggest bar
        barArray[ind].updateHeight(newHeight)                               #Update Height
        barArray[ind].changeColor(color)                                    #Make it visible
        barArray[ind].addText(inputArray[ind])                              #Add text
        barArray[ind].draw(screen)                                          #Draw
    return True

#Reseting all bars we have
def resetAllBars(barArray,screen):
    for i in barArray:
        i.delete(screen)        
        i.clearAll(screen)

#Highlight order setter
#returns the order list
def highlightOrder(inputArrayOrg):
    highlightlist=[]                                    #init the list
    #Each elements will be another list
    #If the list starts with an -1, it means one element is sorted (bar color is switched to green)
    #Elif the list starts with an -2, it means selected of minimum index is going to be changed (red colored bar is going to be changed)
    #Otherwise
    inputArray=[int(i) for i in inputArrayOrg]          #init an array to store sorting
    #Apply the Selection sorted algorithm
    for ind in range(len(inputArray)):                  
        min_ind=ind          
        highlightlist.append([min_ind,ind])             #init highlight
        for j in range(ind+1,len(inputArray)):          
            if inputArray[min_ind] > inputArray[j]:     #compare other part
                #If the last biggest part is updated 
                highlightlist.append([min_ind,j])       #put the comparasion
                highlightlist.append([-2,min_ind])      #put with an "-2" means color is red
                min_ind=j                               #Update minimum index
            highlightlist.append([min_ind,j])  
        highlightlist.append([-1,min_ind,ind])          #One element is sorted
        inputArray[ind],inputArray[min_ind] =inputArray[min_ind],inputArray[ind] #Change the elements
        #Go to next cycle
    return highlightlist

#Bars is going to be changed in the given index, ind1 and ind2. 
def barsChangeDraw(ind1,ind2,barArray,inputArray,invalidInputText,screen):
    inputArray[ind1],inputArray[ind2]=inputArray[ind2],inputArray[ind1] #Update array
    arrayHeightSetter(barArray,inputArray,invalidInputText,screen,ind2) #Call the again height setter to apply changes on the screen