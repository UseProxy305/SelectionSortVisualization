#COLOR CONSTANTS
rectangleColor=(0,0,133) #Normal Rectangle color also this is the color of buttons
backgroundColour=(178,102,255) #Background Color
perfectRectangleColor=(0,204,0) #This is the color whenever a rectangle is going to be shifted
selectedRectangleColor = (204,0,0)  #This color shows the current searched (iterated) rectangle

#Time consts
fps=60          #FPS for the project 
sleepAmount=0.25 #Each step wait for sleepAmount (in sec)

#Screen Settings
width=1000
height=700

#Button and Message Settings
heightButtandMsg=50 #Height pixels for buttons and messages
quitWidth=80   #Width pixels of Quit button 
buttomBars=650  #This pixel shows the bottom pixel of bars
maksHeightBar=300   #This pixel shows the height pixel for the bar with the biggest value
arrayInputMsgWidth=200  #Width pixels of Message "Enter Elements"
arrayInputMsgLft=25     #Left point for Message "Enter Elements"
arrayInputMsgTop=25     #Top point for Message "Enter Elements"
arrayInputBoxWidth=100  #Width pixels for Box to be inserted elements as inputs
offset=25               #The height between top of start button and bottom of input box   
fontSize=32             #Font Size for whole project


#Default Other Settings (Do not change)
quitHeight=heightButtandMsg
arrayInputMsgHeight=heightButtandMsg
arrayInputBoxHeight=heightButtandMsg
invalidInputMsgHeight=heightButtandMsg
startLeft = arrayInputMsgLft+arrayInputMsgWidth
startTop=arrayInputMsgTop+arrayInputMsgHeight+offset
quitStartWidth=width-quitWidth-quitHeight
quitStartHeight=quitHeight
quitEndWidth=width-quitHeight
quitEndHeight=2*quitHeight
barsStartHeight=buttomBars-maksHeightBar
brightRectangleColor=tuple(i/2 for i in rectangleColor)