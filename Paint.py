#Paint.py
from pygame import*
from random import*
from math import*
from tkinter import *
from tkinter import filedialog
Tk().withdraw()#hides the small extra window

font.init()

width,height=1000,700
screen=display.set_mode((width,height))
init()
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)



pos=0
musicNum=0
#initializing variables which would be used for the number of item in list

myPic=image.load("fullscreenpicture.jpg")
screen.blit(myPic,(0,0))
#displaying picture of background

canvasRect=Rect(360,50,630,500)
colourSelectedRect=Rect(380,70,40,40)
displayRect=Rect(140,80,200,120)
musicRect=Rect(140,230,100,80)
stampsRect=Rect(160,340,100,100)
#dimensions of the canvas, the information area (display), and tools

tool=""
#initalizes tool

cols=[]
picList=[]
historyUndo=[]
historyRedo=[]
uploadedPics=[]
toolsleft=["pencilRect","rectangleRect","circleRect","hexagonRect","fillRect","sprayRect"]
toolsright=["eraserRect","filledrectangleRect","filledcircleRect","filledhexagonRect","brushRect","trashRect"]
musicToolsleft=["previousRect","pauseRect"]
musicToolsright=["nextRect","resumeRect"]
stampsTools=["upArrowRect2","downArrowRect2"]
commandToolsleft=["undoRect","saveRect"]
commandToolsright=["redoRect","loadRect"]
colourRect=["colourRect1","colourRect2","colourRect3","colourRect4","colourRect5","colourRect6","colourRect7","colourRect8","colourRect9","colourRect10"]
picNames=["stamps/1.jpg","stamps/2.jpg","stamps/3.jpg","stamps/4.jpg","stamps/5.jpg","stamps/6.jpg","stamps/7.jpg","stamps/8.jpg","stamps/9.jpg","stamps/10.jpg"]
musicNames=["music/1.mp3","music/2.mp3","music/3.mp3","music/4.mp3","music/5.mp3","music/6.mp3","music/7.mp3","music/8.mp3","music/9.mp3","music/2.mp3"]
#all lists in the program/defining them

for name in picNames:
    pic=image.load(name)
    picList.append(pic)
#assigns the stamps into a list / loads the stamps so that each one can appear later on
    
screen.blit(picList[pos],(160,340))
#shows the first stamp in the stamp picture list

col=WHITE
   

calibriFont=font.SysFont("Calibri",27)
introductionPic1=calibriFont.render("Welcome!",True,WHITE)
pencilPic1=calibriFont.render("Pencil",True,WHITE)
eraserPic1=calibriFont.render("Eraser",True,WHITE)
fillPic1=calibriFont.render("Fill",True,WHITE)
unfilledellipsePic1=calibriFont.render("Ellipse",True,WHITE)
unfilledrectanglePic1=calibriFont.render("Rectangle",True,WHITE)
brushPic1=calibriFont.render("Brush",True,WHITE)
sprayPic1=calibriFont.render("Spray",True,WHITE)
unfilledtrianglePic1=calibriFont.render("Triangle",True,WHITE)
trashPic1=calibriFont.render("Trash",True,WHITE)
filledrectanglePic1=calibriFont.render("Filled Rectangle",True,WHITE)
filledellipsePic1=calibriFont.render("Filled Ellipse",True,WHITE)
filledtrianglePic1=calibriFont.render("Filled Triangle",True,WHITE)
stampsPic1=calibriFont.render("Stamps",True,WHITE)
upArrowPic1=calibriFont.render("Up Arrow",True,WHITE)
downArrowPic1=calibriFont.render("Down Arrow",True,WHITE)
redoPic1=calibriFont.render("Redo",True,WHITE)
undoPic1=calibriFont.render("Undo",True,WHITE)
savePic1=calibriFont.render("Save",True,WHITE)
loadPic1=calibriFont.render("Load",True,WHITE)
resumePic1=calibriFont.render("Resume",True,WHITE)
pausePic1=calibriFont.render("Pause",True,WHITE)
previousPic1=calibriFont.render("Previous",True,WHITE)
nextPic1=calibriFont.render("Next",True,WHITE)
musicPic1=calibriFont.render("Music",True,WHITE)
colourPic1=calibriFont.render("Colour",True,WHITE)
#all titles in the display rect


calibriFont=font.SysFont("Calibri",16)
introductionPic2=calibriFont.render("select a colour to get started",True,WHITE)
pencilPic2=calibriFont.render("draws a line",True,WHITE)
eraserPic2=calibriFont.render("erases what it presses on",True,WHITE)
fillPic2=calibriFont.render("fills in the canvas",True,WHITE)
unfilledellipsePic2=calibriFont.render("draws an unfilled ellipse",True,WHITE)
filledellipsePic2=calibriFont.render("draws a filled ellipse",True,WHITE)
unfilledrectanglePic2=calibriFont.render("draws an unfilled rectangle",True,WHITE)
filledrectanglePic2=calibriFont.render("draws a filled rectangle",True,WHITE)
brushPic2=calibriFont.render("brushes on the canvas",True,WHITE)
sprayPic2=calibriFont.render("sprays on the canvas",True,WHITE)
unfilledtrianglePic2=calibriFont.render("draws an unfilled triangle",True,WHITE)
filledtrianglePic2=calibriFont.render("draws a filled triangle",True,WHITE)
trashPic2=calibriFont.render("clears the canvas",True,WHITE)
stampsPic2=calibriFont.render("puts a stamp on the canvas",True,WHITE)
previousPic2=calibriFont.render("goes to the previous music",True,WHITE)
upArrowPic2=calibriFont.render("shows the previous stamp",True,WHITE)
nextPic2=calibriFont.render("goes to the next music",True,WHITE)
downArrowPic2=calibriFont.render("shows the next stamp",True,WHITE)
redoPic2=calibriFont.render("redoes the last command",True,WHITE)
undoPic2=calibriFont.render("undoes the last command",True,WHITE)
savePic2=calibriFont.render("saves the canvas",True,WHITE)
loadPic2=calibriFont.render("loads a bitmap",True,WHITE)
resumePic2=calibriFont.render("resumes the music",True,WHITE)
pausePic2=calibriFont.render("pauses the music",True,WHITE)
musicPic2=calibriFont.render("shows a music icon",True,WHITE)
colourDisplayPic2=calibriFont.render("shows the colour selected",True,WHITE)
colourRectPic2=calibriFont.render("shows one of the colours",True,WHITE)
#all descriptions in the display rect

draw.rect(screen,WHITE,canvasRect)
draw.rect(screen,BLACK,canvasRect,3)
#draws the original canvas

screenCap=screen.subsurface(canvasRect).copy()
#canvas screenshot

draw.rect(screen,WHITE,colourSelectedRect)
draw.rect(screen,BLACK,colourSelectedRect,2)
#draws the rectangle which would be used to show which colour is currently selectred

draw.rect(screen,BLACK,displayRect)
draw.rect(screen,WHITE,displayRect,1)
screen.blit(introductionPic1,(180,105))
draw.line(screen,WHITE,(140,150),(340,150))
screen.blit(introductionPic2,(140,170))
#draws the display rect with an introduction

def draw_tools_rect(name, x, y, length, width):
    size=100
    if name == musicToolsleft or name == musicToolsright:
        size=50
    elif name == stampsTools:
        size=54
    elif name == commandToolsleft or name == commandToolsright:
        size=60
    for i in range(len(name)):
        name[i]=Rect(x, y+i*size,length,width)
        if mb[0] and name[i].collidepoint(mx,my):
            draw.rect(screen,GREEN,name[i])
        elif name[i].collidepoint(mx,my):
            draw.rect(screen,RED,name[i])
        else:
            draw.rect(screen,WHITE,name[i])
        
running=True

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONUP:#mouse released
            screenCap = screen.subsurface(canvasRect).copy()

        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:#left click
                sx,sy=evt.pos #the click position
                if commandToolsleft[1].collidepoint(mx,my):
                    fname=filedialog.asksaveasfilename(defaultextension=".png")
                    #fname is a string which has the full path for the picture, this automatically sets any picture saved into a png file
                    image.save(screen.subsurface(canvasRect),fname) #screenshots the canvasRect screen and saves it
                if commandToolsright[1].collidepoint(mx,my):
                    fname=filedialog.askopenfilename()
                    imageUploaded=image.load(fname)
                    smallimageUploaded=transform.scale(imageUploaded,(200,100))
                    uploadedPics.append(smallimageUploaded)
                    #opens the file path which you would later on be able to upload a picture from
                    
            
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    draw_tools_rect(toolsleft, 20, 100, 44, 44)
    #draws the tool rectangles which appear to the far left of the screen
    #if u hover over any of the rectangles it will turn red, if u press on any of the rectangles it will turn green
            
    draw_tools_rect(toolsright, 80, 100, 44, 44)
    #draws the tool rectangles which appear next to the far left ones (right from the tools  of the toolsLeft)
    #if u hover over any of the rectangles it will turn red, if u press on any of the rectangles it will turn green 
    #its default higlight is white
            
    draw_tools_rect(musicToolsleft, 251, 225, 44, 44)
    #draws the left music tools' rectangles which appear to the right of the music icon but to the left of the other music tools 
    #if u hover over any of the rectangles it will turn red, if u press on any of the rectangles it will turn green 
    #its default higlight is white
            
    draw_tools_rect(musicToolsright, 300, 225, 44, 44)
    #draws the right music tools' rectangles which appear to the right of the other music tools 
    #if u hover over any of the rectangles it will turn red, if u press on any of the rectangles it will turn green
    #its default higlight is white

    draw_tools_rect(stampsTools, 271, 338, 52, 52)
    #draws the stamps tools' rectangles which appear to the right of the other stamps rectangle/stamps picture 
    #if u hover over any of the rectangles it will turn red, if u press on any of the rectangles it will turn green
    #its default higlight is white

    draw_tools_rect(commandToolsleft, 180, 460, 44, 44)
    #draws the left command tools' rectangles which appear to the bottom of the stamps and stamps tools 
    #if u hover over any of the rectangles it will turn red, if u press on any of the rectangles it will turn green
    #its default higlight is white
            
    draw_tools_rect(commandToolsright, 240, 460, 44, 44)
    #draws the right command tools' rectangles which appear to the bottom of the stamps and stamps tools 
    #if u hover over any of the rectangles it will turn red, if u press on any of the rectangles it will turn green
    #its default higlight is white
            
    for i in range(len(colourRect)):
        colourRect[i]=Rect(400+i*60,570,25,25)
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        cols.append((r,g,b))
        draw.rect(screen,cols[i],colourRect[i])
        draw.rect(screen,WHITE,colourRect[i],1)
        if mb[0] and colourRect[i].collidepoint(mx,my):
            col=screen.get_at((mx,my))
            draw.rect(screen,GREEN,colourRect[i],2)
            draw.rect(screen,col,colourSelectedRect)
            draw.rect(screen,BLACK,colourSelectedRect,2)
            draw.rect(screen,BLACK,displayRect)
            draw.rect(screen,WHITE,displayRect,1)
            screen.blit(colourPic1,(200,105))
            draw.line(screen,WHITE,(140,150),(340,150))
            screen.blit(colourRectPic2,(152,170))
        elif colourRect[i].collidepoint(mx,my):
            draw.rect(screen,RED,colourRect[i],2)
    #draws the colour rectangles which appear to the bottom of the canvas 
    #if u hover over any of the rectangles it will turn red, if u press on any of the rectangles it will turn green and states what it is on the display rect
    #its default higlight is white
    #it also changes the colourSelectRect such that the colour that was pressed on from the colour rect will be placed on the colourSelectRect
            
    if mb[0] and stampsRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,stampsRect,2)
    elif stampsRect.collidepoint(mx,my):
        draw.rect(screen,RED,stampsRect,2)
    else:
        draw.rect(screen,WHITE,stampsRect,2)
    #draws the stamps rectangle which displays stamps 
    #if u hover over it, it will turn red, if u press on it,it will turn green 
    #its default higlight is white
        
    if mb[0] and musicRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,musicRect)
    elif musicRect.collidepoint(mx,my):
        draw.rect(screen,RED,musicRect)
    else:
        draw.rect(screen,WHITE,musicRect)
    #draws the music rectangle which will show a music icon later on in the code
    #if u hover over it, it will turn red, if u press on it,it will turn green 
    #its default higlight is white
        
    Pencil=image.load("tools/pencil.png")
    screen.blit(Pencil,(22,102))
    Eraser=image.load("tools/eraser.png")
    screen.blit(Eraser,(82,102))
    UnfilledRectangle=image.load("tools/rectangle.jpg")
    screen.blit(UnfilledRectangle,(22,202))
    FilledRectangle=image.load("tools/rectangle.png")
    screen.blit(FilledRectangle,(82,202))
    UnfilledCircle=image.load("tools/circle.jpg")
    screen.blit(UnfilledCircle,(22,302))
    FilledCircle=image.load("tools/circle.png")
    screen.blit(FilledCircle,(82,302))
    Triangle=image.load("tools/triangle.png")
    screen.blit(Triangle,(22,402))
    Filledtriangle=image.load("tools/filledtriangle.png")
    screen.blit(Filledtriangle,(82,402))
    Fill=image.load("tools/fill.jpeg")
    screen.blit(Fill,(22,502))
    Brush=image.load("tools/brush.png")
    screen.blit(Brush,(82,502))
    Spray=image.load("tools/spray.jpg")
    screen.blit(Spray,(22,602))
    Trash=image.load("tools/trash.jpg")
    screen.blit(Trash,(82,602))
    upArrow=image.load("Arrows/up.png")
    screen.blit(upArrow,(272,339))
    undoArrow=image.load("Arrows/undo.png")
    screen.blit(undoArrow,(179,461))
    redoArrow=image.load("Arrows/redo.png")
    screen.blit(redoArrow,(239,461))
    Save=image.load("tools/save.png")
    screen.blit(Save,(182,522))
    Load=image.load("tools/load.jpg")
    screen.blit(Load,(242,522))
    downArrow=image.load("Arrows/down.jpg")
    screen.blit(downArrow,(272,393))
    resume=image.load("tools/resume.jpg")
    screen.blit(resume,(302,277))
    Next=image.load("tools/next.jpg")
    screen.blit(Next,(302,227))
    Previous=image.load("tools/previous.jpg")
    screen.blit(Previous,(253,227))
    pause=image.load("tools/pause.jpg")
    screen.blit(pause,(253,277))
    Music=image.load("music/musicIcon.png")
    screen.blit(Music,(140,230))
    #shows/blits all the images that are asked and in the file in the specific area specified


    
    if mb[0] and colourSelectedRect.collidepoint(mx,my):
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(colourPic1,(200,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(colourDisplayPic2,(150,170))
    #if clicked on the rectangle which is used to show the colour that is selected
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and toolsleft[0].collidepoint(mx,my):
        tool="pencil"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(pencilPic1,(205,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(pencilPic2,(195,170))
    #if clicked on the pencil rectangle
    #the tool will be pencil
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and toolsright[0].collidepoint(mx,my):
        tool="eraser"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(eraserPic1,(200,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(eraserPic2,(150,170))
    #if clicked on the eraser rectangle
    #the tool will be eraser
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and toolsleft[1].collidepoint(mx,my):
        tool="unfilledrectangle"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(unfilledrectanglePic1,(180,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(unfilledrectanglePic2,(145,170))
    #if clicked on the unfilled rectangle rectangle
    #the tool will be unfilledrectangle
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and toolsright[1].collidepoint(mx,my):
        tool="filledrectangle"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(filledrectanglePic1,(140,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(filledrectanglePic2,(160,170))
    #if clicked on the filled rectangle rectangle
    #the tool will be filledrectangle
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and toolsleft[2].collidepoint(mx,my):
        tool="unfilledellipse"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(unfilledellipsePic1,(200,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(unfilledellipsePic2,(155,170))
    #if clicked on the unfilled ellipse rectangle
    #the tool will be unfilledellipse
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and toolsright[2].collidepoint(mx,my):
        tool="filledellipse"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(filledellipsePic1,(165,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(filledellipsePic2,(165,170))
    #if clicked on the filled ellipse rectangle
    #the tool will be filledellipse
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and toolsleft[3].collidepoint(mx,my):
        tool="unfilledtriangle"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(unfilledtrianglePic1,(190,105))
        draw.line(screen,WHITE,(140,150),(335,150))
        screen.blit(unfilledtrianglePic2,(150,170))
    #if clicked on the unfilled triangle rectangle
    #the tool will be unfilledtriangle
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and toolsright[3].collidepoint(mx,my):
        tool="filledtriangle"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(filledtrianglePic1,(155,105))
        draw.line(screen,WHITE,(140,150),(335,150))
        screen.blit(filledtrianglePic2,(165,170))
    #if clicked on the filled triangle rectangle
    #the tool will be filledtriangle
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and toolsleft[4].collidepoint(mx,my):
        tool="fill"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(fillPic1,(220,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(fillPic2,(180,170))
    #if clicked on the fill rectangle
    #the tool will be fill
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and toolsright[4].collidepoint(mx,my):
        tool="brush"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(brushPic1,(205,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(brushPic2,(160,170))
    #if clicked on the brush rectangle
    #the tool will be brush
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and toolsleft[5].collidepoint(mx,my):
        tool="spray"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(sprayPic1,(205,105))
        draw.line(screen,WHITE,(140,150),(335,150))
        screen.blit(sprayPic2,(160,170))
    #if clicked on the spray rectangle
    #the tool will be spray
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and toolsright[5].collidepoint(mx,my):
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(trashPic1,(205,105))
        draw.line(screen,WHITE,(140,150),(335,150))
        screen.blit(trashPic2,(180,170))
        draw.rect(screen,WHITE,canvasRect)
        draw.rect(screen,BLACK,canvasRect,3)
        draw.rect(screen,col,colourSelectedRect)
        draw.rect(screen,BLACK,colourSelectedRect,2)
    #if clicked on the trash rectangle
    #it will make the canvas white again to seem to have been cleared 
    #draws the colourselectedrect again so that it is seen to just have cleared any tools,stamps,etc from the canvas
    #the display rect will specify what that rectangle pressed is, with a title and description
        
    if mb[0] and musicToolsleft[0].collidepoint(mx,my):
        musicNum=(musicNum-1)%10
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(previousPic1,(190,105))
        draw.line(screen,WHITE,(140,150),(335,150))
        screen.blit(previousPic2,(145,170))
    #if clicked on the previous rectangle
    #it will remove 1 from the musicNum so that it changes the music, goes to the last song
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and musicToolsright[0].collidepoint(mx,my):
        musicNum=(musicNum+1)%10
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(nextPic1,(210,105))
        draw.line(screen,WHITE,(140,150),(335,150))
        screen.blit(nextPic2,(162,170))
    #if clicked on the next rectangle
    #it will add 1 to the musicNum so that it changes the music, goes to the next song
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and musicToolsleft[1].collidepoint(mx,my):
        mixer.music.stop()
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(pausePic1,(200,105))
        draw.line(screen,WHITE,(140,150),(335,150))
        screen.blit(pausePic2,(175,170))
    #if clicked on the pause rectangle
    #it will stop the music
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and musicToolsright[1].collidepoint(mx,my):
        mixer.music.load(musicNames[musicNum])
        mixer.music.play() 
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(resumePic1,(185,105))
        draw.line(screen,WHITE,(140,150),(335,150))
        screen.blit(resumePic2,(170,170))
    #if clicked on the resume rectangle
    #it will play the music
    #the display rect will specify what that rectangle pressed is, with a title and description

    if mb[0] and musicRect.collidepoint(mx,my):
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(musicPic1,(200,105))
        draw.line(screen,WHITE,(140,150),(335,150))
        screen.blit(musicPic2,(160,170))
    #if clicked on the music icon rectangle
    #the display rect will specify what that rectangle pressed is, with a title and description

    if mb[0] and stampsTools[0].collidepoint(mx,my):
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(upArrowPic1,(185,105))
        draw.line(screen,WHITE,(140,150),(335,150))
        screen.blit(upArrowPic2,(150,170))
        pos=(pos-1)%10
        screen.blit(picList[pos],(160,340))
    #if clicked on the uparrow rectangle
    #it will remove 1 from pos so that it changes the stamps, goes to the last image
    #it then prints the new image
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and stampsTools[1].collidepoint(mx,my):
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(downArrowPic1,(165,105))
        draw.line(screen,WHITE,(140,150),(335,150))
        screen.blit(downArrowPic2,(162,170))
        pos=(pos+1)%10
        screen.blit(picList[pos],(160,340))
    #if clicked on the downarrow rectangle
    #it will add 1 to pos so that it changes the stamps, goes to the next image
    #it then prints the new image
    #the display rect will specify what that rectangle pressed is, with a title and description
        
    if mb[0] and stampsRect.collidepoint(mx,my):
        tool="stamps"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(stampsPic1,(190,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(stampsPic2,(143,170))
    #if clicked on the stamps rectangle
        #the tool is now stamps
    #the display rect will specify what that rectangle pressed is, with a title and description

    if mb[0] and commandToolsleft[0].collidepoint(mx,my):
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(undoPic1,(205,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(undoPic2,(147,170))
        if historyUndo==[]: #if the history undo is an empty list
            draw.rect(screen,WHITE,canvasRect)
            draw.rect(screen,BLACK,canvasRect,3)
            draw.rect(screen,col,colourSelectedRect)
            draw.rect(screen,BLACK,colourSelectedRect,2)
            #sets the canvas rect back to its default
        else:
            newCanvas=historyUndo.pop()#removes the last screenshot in the undo history list so that when undo is pressed it can "erase" the last action
            screen.blit(newCanvas,(360,50))#prints the new screenshot of the canvas rec
            crop=screen.subsurface(canvasRect).copy()#screenshots canvas rect
            historyRedo.append(crop)#adds the screenshot into the historyredo list
    #if clicked on the undo rectangle
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and commandToolsright[0].collidepoint(mx,my):
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(redoPic1,(205,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(redoPic2,(150,170))
        if historyRedo==[]: #if the history redo is an empty list
            continue
        else:
            newCanvas=historyRedo.pop()#removes the last screenshot in the redo history list so that when redo is pressed it can "readd" the last action
            screen.blit(newCanvas,(360,50))#prints the new screenshot of the canvas rec
            crop=screen.subsurface(canvasRect).copy()#screenshots canvas rect
            historyUndo.append(crop)#adds the screenshot into the historyundo list
    #if clicked on the redo rectangle
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and commandToolsleft[1].collidepoint(mx,my):
        tool="save"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(savePic1,(207,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(savePic2,(180,170))
    #if clicked on the save rectangle
    #the tool is now save
    #the display rect will specify what that rectangle pressed is, with a title and description
    if mb[0] and commandToolsright[1].collidepoint(mx,my):
        tool="load"
        draw.rect(screen,BLACK,displayRect)
        draw.rect(screen,WHITE,displayRect,1)
        screen.blit(loadPic1,(207,105))
        draw.line(screen,WHITE,(140,150),(340,150))
        screen.blit(loadPic2,(185,170))
    #if clicked on the load rectangle
    #the tool is now load
    #the display rect will specify what that rectangle pressed is, with a title and description

    if mb[0] and colourRect[i].collidepoint(mx,my):
        col=screen.get_at((mx,my))
    #if clicked on any of the colours in the colour rectangles
    #col becomes the colour that was clicked on in the colour rect
    if mb[0] and canvasRect.collidepoint(mx,my): #if clicked on the canvas
        if tool=="pencil": #if tool is pencil
            draw.line(screen,col,(omx,omy),(mx,my)) #draws freely on the canvas with the colour selected
            copy=screen.subsurface(canvasRect).copy()#screenshot of the canvas screen
            historyUndo.append(copy)#adds the screenshot into the historyundo list
        elif tool=="eraser": #if tool is eraser
            draw.circle(screen,WHITE,(mx,my),10) #erases (draws a white circle at the point pressed with radius 10)
            crop=screen.subsurface(canvasRect).copy() #screenshot of the canvas screen
            historyUndo.append(crop)#adds the screenshot into the historyundo list
        elif tool=="fill": #if tool is fill
            draw.rect(screen,col,canvasRect) #fill the canvas with the colour selected
            draw.rect(screen,col,colourSelectedRect) #draws the colour rect again
            draw.rect(screen,BLACK,colourSelectedRect,2) #draws the outline for the colour rect again
            crop=screen.subsurface(canvasRect).copy()#screenshot of the canvas screen
            historyUndo.append(crop)#adds the screenshot into the historyundo list
        elif tool=="unfilledrectangle": #if tool is unfilledrectangle
            screen.blit(screenCap,canvasRect)
            draw.rect(screen,col,colourSelectedRect) #draws the colour rect again
            draw.rect(screen,BLACK,colourSelectedRect,2)#draws the outline for the colour rect again
            myRect=Rect(sx,sy,mx-sx,my-sy)#coordinates of the rectangle (so that you are able to drag)
            myRect.normalize()#makes it so that if any coordinates have a negative, the rectangle still draws and just flips
            draw.rect(screen,col,myRect,1)#draws the rectangle which you will drag with an outline of the colour selected
            crop=screen.subsurface(canvasRect).copy()#screenshot of the canvas screen
            historyUndo.append(crop)#adds the screenshot into the historyundo list
        elif tool=="filledrectangle": #if tool is filledrectangle
            screen.blit(screenCap,canvasRect) #prints clear canvas
            draw.rect(screen,col,colourSelectedRect)#draws the colour rect again
            draw.rect(screen,BLACK,colourSelectedRect,2)#draws the outline for the colour rect again
            myRect=Rect(sx,sy,mx-sx,my-sy) #coordinates of the rectangle (so that you are able to drag)
            myRect.normalize() #makes it so that if any coordinates have a negative, the rectangle still draws and just flips
            draw.rect(screen,col,myRect)#draws the rectangle which you will drag with a fill of the colour selected
            crop=screen.subsurface(canvasRect).copy()#screenshot of the canvas screen
            historyUndo.append(crop)#adds the screenshot into the historyundo list
        elif tool=="unfilledellipse":#if tool is unfilledellipse
            screen.blit(screenCap,canvasRect)#prints clear canvas
            draw.rect(screen,col,colourSelectedRect)#draws the colour rect again
            draw.rect(screen,BLACK,colourSelectedRect,2)#draws the outline for the colour rect again
            myRect=Rect(sx,sy,mx-sx,my-sy)#coordinates of the ellipse (so that you are able to drag)
            myRect.normalize()#makes it so that if any coordinates have a negative, the ellipse still draws and just flips
            draw.ellipse(screen,col,myRect,1)#draws the ellipse which you will drag with an outline of the colour selected
            crop=screen.subsurface(canvasRect).copy()#screenshot of the canvas screen
            historyUndo.append(crop)#adds the screenshot into the historyundo list
        elif tool=="filledellipse":#if tool is unfilledellipse
            screen.blit(screenCap,canvasRect)#prints clear canvas
            draw.rect(screen,col,colourSelectedRect)#draws the colour rect again
            draw.rect(screen,BLACK,colourSelectedRect,2)#draws the outline for the colour rect again
            myRect=Rect(sx,sy,mx-sx,my-sy)#coordinates of the ellipse (so that you are able to drag)
            myRect.normalize()#makes it so that if any coordinates have a negative, the ellipse still draws and just flips
            draw.ellipse(screen,col,myRect)#draws the ellipse which you will drag with a fill of the colour selected
            crop=screen.subsurface(canvasRect).copy()#screenshot of the canvas screen
            historyUndo.append(crop)#adds the screenshot into the historyundo list
        elif tool=="unfilledtriangle":#if tool is unfilledtriangle
            screen.blit(screenCap,canvasRect)#prints clear canvas
            draw.rect(screen,col,colourSelectedRect)#draws the colour rect again
            draw.rect(screen,BLACK,colourSelectedRect,2)#draws the outline for the colour rect again
            draw.polygon(screen,col,[(sx,sy),(mx,my),(360+sx-my,my)],1) #draws the triangle which you will drag with an outline of the colour selected
            crop=screen.subsurface(canvasRect).copy()#screenshot of the canvas screen
            historyUndo.append(crop)#adds the screenshot into the historyundo list
        elif tool=="filledtriangle":#if tool is filledtriangle
            screen.blit(screenCap,canvasRect)#prints clear canvas
            draw.rect(screen,col,colourSelectedRect)#draws the colour rect again
            draw.rect(screen,BLACK,colourSelectedRect,2)#draws the outline for the colour rect again
            draw.polygon(screen,col,[(sx,sy),(mx,my),(360+sx-my,my)]) #draws the triangle which you will drag with a fill of the colour selected
            crop=screen.subsurface(canvasRect).copy()#screenshot of the canvas screen
            historyUndo.append(crop)#adds the screenshot into the historyundo list
        elif tool=="stamps":#if tool is stamps
            screen.blit(picList[pos],(mx-50,my-50)) #prints the stamp which is currently show on the stamp rect, onto the canvas
            crop=screen.subsurface(canvasRect).copy()#screenshot of the canvas screen
            historyUndo.append(crop)#adds the screenshot into the historyundo list
        elif tool=="load": #if tool is load
            screen.blit(uploadedPics[0],(mx-100,my-50)) #prints the image that was loaded on the onto the canvas
            if len(uploadedPics)==2:
                del uploadedPics[0]
                draw.rect(screen,WHITE,canvasRect)
                draw.rect(screen,BLACK,canvasRect,3)
                draw.rect(screen,col,colourSelectedRect)
                draw.rect(screen,BLACK,colourSelectedRect,2)
            crop=screen.subsurface(canvasRect).copy()#screenshot of the canvas screen
            historyUndo.append(crop)#adds the screenshot into the historyundo list
        elif tool == "brush":
            draw.line(screen,col,(omx,omy),(mx,my), 7) #draws freely on the canvas with the colour selected
            copy=screen.subsurface(canvasRect).copy()#screenshot of the canvas screen
            historyUndo.append(copy)#adds the screenshot into the historyundo list
            #for _ in range(30):  # density: number of dots per event
             #   offset_x = randint(-6, 6)
              #  offset_y = randint(-6, 6)
               # radius = randint(4, 7)  # smaller dots for textured brush effect
               # draw.circle(screen, col, (mx + offset_x, my + offset_y), radius)
            draw.rect(screen, col, colourSelectedRect)
            draw.rect(screen, BLACK, colourSelectedRect, 2)
            #crop = screen.subsurface(canvasRect).copy()
            #historyUndo.append(crop)
        elif tool == "spray":
            spray_radius = 10
            density = 15  # number of dots sprayed per event
            for _ in range(density):
                angle = random() * 2 * pi
                radius = sqrt(random()) * spray_radius
                dot_x = int(mx + radius * cos(angle))
                dot_y = int(my + radius * sin(angle))
                draw.circle(screen, col, (dot_x, dot_y), 1)  # small dots for spray effect
            draw.rect(screen, col, colourSelectedRect)
            draw.rect(screen, BLACK, colourSelectedRect, 2)
            crop = screen.subsurface(canvasRect).copy()
            historyUndo.append(crop)
    omx,omy=mx,my
    display.flip()
quit()  
