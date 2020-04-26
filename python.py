'''
    Bryan Chavez
    4/18/2020
    Python Game

    This is the begining of my small project I will be working on.
    I want to develop a small game of snake, called "Python".
    This will help me review and refamilarize myself with Python language,
    such as simple logic and object movement.

'''
import pygame

class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

class cube(object):
    def __init__(self, color):
        pass

    def move(self):
        pass

    def draw(self):
        pass

def drawGrid(w, rows, surface):
    sizeBetween = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + sizeBetween
        y = y + sizeBetween

        #Drawing horizonal and vertical lines
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))

def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()

def main():
    global width, height, rows
    width = 700
    height = 700
    rows = 20
    window = pygame.display.set_mode((width, height))

    s = snake((0,255,0), (10,10))

    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.event.get()
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(window)


    pass
main()
