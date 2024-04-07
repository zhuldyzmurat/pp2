import pygame
import math

#function to draw a rectangle
def rectangle(surf, cur, end, d, color):
    # Extract coordinates from cur and end points
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1] 
    # Calculate width and height of the rectangle
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    # Draw the rectangle on the surface
    pygame.draw.rect(surf, color, (min(x1, x2), min(y1, y2), a, b), d)

#for a pen
def pen(surf, cur, end, d, color):
    pygame.draw.line(surf, color, cur, end, d)
    
#for a circle
def circle(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1]
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    pygame.draw.circle(surf, color, (min(x1,x2)+a//2, min(y1, y2)+b//2), min(a, b)//2, d)

#function to erase
def eraser(surf, cur):
    x1, y1 = cur[0], cur[1]
    pygame.draw.circle(surf, "Black", (x1, y1), 20)

#for a square
def square(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1] 
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    pygame.draw.rect(surf, color, (min(x1, x2), min(y1, y2), min(a, b),min(a,b)), d) 

#to draw a right triangle
def righttriangle(surf, cur, end, d, color):
    x1, x2, y1, y2 = cur[0], cur[1], end[0], end[1]
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    pygame.draw.polygon(surf, color, ((x1, y1), (x2, y1), (x1, y2)), d) 
    
#for an equilateral triangle
def equilateraltriangle(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1]
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    x3 = x1 + min(a, b)
    y3 = y1 + math.sqrt(3) / 2 * min(a, b)
    pygame.draw.polygon(surf, color, ((x1, y1), (x2, y2), (x3, y3)), d)

#for a rhombus
def rhombus(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1]
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    cx = (x1 + x2) // 2  
    cy = (y1 + y2) // 2 
    pygame.draw.polygon(surf, color, ((cx, y1), (x2, cy), (cx, y2), (x1, cy)), d)

#initializing and setup the screen
FPS = 60
W = 640
H = 480
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Paint')
baseLayer = pygame.Surface((640, 480))
clock = pygame.time.Clock()

#setting initial mode and color
mode = "Rectangle"
color = "Red"
isMouseDown = False 

running = True

#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            #change mode based on key pressed
            if event.key == pygame.K_1:
                mode = "Rectangle"
            elif event.key == pygame.K_2:
                mode = "Circle"
            elif event.key == pygame.K_3:
                mode = "Pen"
            elif event.key == pygame.K_4:
                mode = "Eraser"
            elif event.key == pygame.K_5:
                mode = "Square"
            elif event.key == pygame.K_6:
                mode = "Right Triangle"
            elif event.key == pygame.K_7:
                mode = "Equilateral Triangle"
            elif event.key == pygame.K_8:
                mode = "Rhombus"

        if event.type == pygame.MOUSEBUTTONDOWN:
            #update mouse position on click
            xnow, ynow = event.pos
            last_pos = (xnow, ynow)
            isMouseDown = True

        if event.type == pygame.MOUSEBUTTONUP:
            #reset flag on mouse release and update the base layer
            isMouseDown = False
            baseLayer.blit(screen, (0,0))

        if event.type == pygame.MOUSEMOTION:
            if isMouseDown and last_pos != (-1, -1):
                #draw when mouse is moving and pen mode is selected
                xnow, ynow = event.pos
                if mode == 'Pen':
                    pen(baseLayer, last_pos, (xnow, ynow), 2, color)
                    last_pos = (xnow, ynow)

    if isMouseDown and last_pos != (-1, -1):
        #draw the selected shape if mouse is down
        screen.blit(baseLayer, (0, 0))
        if mode == 'Rectangle':
            rectangle(screen, last_pos,(xnow, ynow), 2, color)
        elif mode == 'Circle':
            circle(screen, last_pos, (xnow, ynow), 2, color)
        elif mode == "Eraser":
            eraser(baseLayer, (xnow, ynow))
        elif mode == 'Square':
            square(screen, last_pos, (xnow, ynow), 2, color)
        elif mode == 'Right Triangle':
            righttriangle(screen ,last_pos, (xnow, ynow), 2, color)
        elif mode == 'Equilateral Triangle':
            equilateraltriangle(screen, last_pos,(xnow,ynow), 2, color)
        elif mode == "Rhombus":
            rhombus(screen, last_pos, (xnow, ynow), 2 , color)

    pygame.display.update()
    clock.tick(FPS)