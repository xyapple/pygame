import pygame, sys, random
from pygame.locals import *

def doRectOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True
    return False

def isPointInsideRect (x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

pygame.init()
mainClock = pygame.time.Clock()

#set up the window
windownWidth = 500
winddowHeight = 500
windowSurface = pygame.display.set_mode((windownWidth, winddowHeight), 0, 32)
pygame.display.set_caption('Collision Detection')

#set up direction variables
downLeft = 1
downRight = 3
upLeft = 7
upRight = 9

moveSpeed = 1

#set up the colors
black = (0,0,0)
green = (0, 255, 0)
white = (255, 255, 255)

# set up the bouncer and food data structures
foodCounter = 0
newFood = 40
foodSize = 20

bouncer = {'rect':pygame.Rect(300,100,50,50), 'dir': upLeft}
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, windownWidth - foodSize),
                 random.randint(0, winddowHeight - foodSize), foodSize, foodSize))

# run the game loop
while True:
    # check for the quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    foodCounter += 1
    if foodCounter >= newFood:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, windownWidth - foodSize),
                 random.randint(0, winddowHeight - foodSize), foodSize,foodSize))

    windowSurface.fill(black)

    if bouncer['dir'] == downLeft:
        bouncer['rect'].left -= moveSpeed
        bouncer['rect'].top += moveSpeed

    if bouncer['dir'] == downRight:
        bouncer['rect'].left += moveSpeed
        bouncer['rect'].top += moveSpeed

    if bouncer['dir'] == upLeft:
        bouncer['rect'].left -= moveSpeed
        bouncer['rect'].top -= moveSpeed

    if bouncer['dir'] == upRight:
        bouncer['rect'].left += moveSpeed
        bouncer['rect'].top -= moveSpeed

    if bouncer['rect'].top <0:
        if bouncer['dir'] == upLeft:
            bouncer['dir'] = downLeft
        if bouncer['dir'] ==  upRight:
            bouncer['dir'] = downRight

    if bouncer['rect'].bottom > winddowHeight:
        if bouncer['dir'] == downLeft:
            bouncer['dir'] = upLeft
        if bouncer['dir'] == downRight:
            bouncer['dir'] = upRight

    if bouncer['rect'].left <0:
        if bouncer['dir'] == downLeft:
            bouncer['dir'] = downRight
        if bouncer['dir'] == upLeft:
            bouncer['dir'] = upRight

    if bouncer['rect'].right > windownWidth:
        if bouncer['dir'] == downRight:
            bouncer['dir'] = downLeft
        if bouncer['dir'] == upRight:
            bouncer['dir'] = upLeft

    pygame.draw.rect(windowSurface, white, bouncer['rect'])

    for food in foods[:]:
        if doRectOverlap(bouncer['rect'], food):
            foods.remove(food)

    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, green, foods[i])

    pygame.display.update()
    mainClock.tick(45)






