import pygame, sys, time
from pygame.locals import*

#set up pygame
pygame.init()

#set up the window
windowWidth = 600
windowHeight = 600

windowSurface = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
pygame.display.set_caption('Animation')

#set up direction variables
downLeft = 1
downRight = 2
upLeft = 3
upRight = 4

moveSpeed = 1

#set up the colors
black = (0,0,0)
red = (255, 0, 0)
lime = (0, 255, 0)
purple = (128,0,128)

#set up the block data structure
block1 ={'rect':pygame.Rect(300,80,50,100), 'color':red, 'dir':upRight}
block2 ={'rect':pygame.Rect(200, 200, 20, 20), 'color': lime, 'dir':upLeft}
block3 ={'rect':pygame.Rect(100, 150, 60, 60), 'color': purple, 'dir':downLeft}
blocks = [block1, block2, block3]

#run the game loop
while True:
    #check for the quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #draw the black background onto the surface
    windowSurface.fill(black)

    for b in blocks:
        # move the block data structure
        if b['dir'] == downLeft:
            b['rect'].left -= moveSpeed
            b['rect'].top += moveSpeed

        if b['dir'] == downRight:
            b['rect'].left += moveSpeed
            b['rect'].top += moveSpeed

        if b['dir'] == upLeft:
            b['rect'].left -= moveSpeed
            b['rect'].top -= moveSpeed

        if b['dir'] == upRight:
            b['rect'].left += moveSpeed
            b['rect'].top -= moveSpeed

        # check if the block has move out of the window
        # block has moved past the top
        if b['rect'].top < 0:
            if b['dir'] == upLeft:
               b['dir'] = downLeft

            if b['dir'] == upRight:
               b['dir'] = downRight

        # block has moved past the bottom
        if b['rect'].bottom > windowHeight:
            if b['dir'] == downRight:
                b['dir'] = upLeft

            if b['dir'] == downRight:
                b['dir'] = downRight
        # block has moved past the left side
        if b['rect'].left < 0:
            if b['dir'] == downLeft:
                b['dir'] = downRight

            if b['dir'] == upLeft:
                b['dir'] = upRight

        # block has moved past the right side
        if b['rect']. right > windowWidth:
            if b['dir'] == downRight:
                b['dir'] = downLeft

            if b['dir'] == upRight:
               b['dir'] = upLeft

    pygame.draw.rect(windowSurface, b['color'], b['rect'])

    # draw the window onto the screen
    pygame.display.update()
    time.sleep(0.02)
