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
import random

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 0

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #Keep updating keyboard input
            keys = pygame.key.get_pressed()

            for key in keys:
                #Checking each arrow key explicitly allowing only 1 pressed at time
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i,cube in enumerate(self.body):
            p = cube.pos[:]
            #Keeping track of turns in a list
            if p in self.turns:
                turn = self.turns[p]
                cube.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                #These 4 bring the snake across the screen at walls
                #We can change it later to die if it hits the wall
                if cube.dirnx == -1 and cube.pos[0] <= 0:
                    cube.pos = (cube.rows-1, cube.pos[1])
                elif cube.dirnx == 1 and cube.pos[0] >= cube.rows-1:
                    cube.pos = (0, cube.pos[1])
                elif cube.dirny == 1 and cube.pos[1] >= cube.rows-1:
                    cube.pos = (cube.pos[0], 0)
                elif cube.dirny == -1 and cube.pos[1] <= 0:
                    cube.pos = (cube.pos[0], cube.rows-1)
                else:
                    cube.move(cube.dirnx,cube.dirny)

    def reset(self, pos):
        pass

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        #Depending on movement of snake, we need to add cube on the correct side
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1),tail.pos[1]))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, cube in enumerate(self.body):
            #If it is the first cube of the snake, draw eyes (True), otherwise it is the body
            if i == 0:
                cube.draw(surface, True)
            else:
                cube.draw(surface)

class cube(object):
    rows = 25
    width = 700
    def __init__(self, start, dirnx=1, dirny=0, color=(0,0,255)):
        self.pos = start
        self.dirnx = 0
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        distance = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]

        #Drawing cubs slightly smaller than the size of a 1x1 grid for a better appearance
        pygame.draw.rect(surface, self.color, (i*distance+1,j*distance+1, distance-2, distance-2))

        #If we are creating a snake head then draw an eye
        if eyes:
            center = distance // 2
            radius = 3
            #circleEye1 = (i*distance+center-radius, j*distance+8)
            circleEye2 = (i*distance+distance-radius*2, j*distance+8)
            #pygame.draw.circle(surface, (255,255,255), circleEye1, radius)
            pygame.draw.circle(surface, (255,255,255), circleEye2, radius)

def drawGrid(width, rows, surface):
    #Calculating the distance between each horizontal/vertical line
    sizeBetween = width // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + sizeBetween
        y = y + sizeBetween

        #Drawing horizonal and vertical lines for game
        pygame.draw.line(surface, (255,255,255), (x,0),(x,width))
        pygame.draw.line(surface, (255,255,255), (0,y),(width,y))

def redrawWindow(surface):
    #Will update the window with any changes done within the game
    global rows, width, s, food
    surface.fill((0,0,0))
    s.draw(surface)
    food.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomFood(rows, snake):
    positions = snake.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            #If random food pos is on the snake, run loop again with new randomizations
            continue
        else:
            break
    return (x,y)

def main():
    global width, height, rows, s, food
    width = 700
    height = 700
    rows = 25

    #Create a window of given dimenstions
    window = pygame.display.set_mode((width, height))

    #Creating a snake object
    s = snake((0,255,0), (10,10))

    #Creating a food item
    food = cube(randomFood(rows, s), color=(0,255,0))

    flag = True

    clock = pygame.time.Clock()

    #While loop keeping the game alive
    while flag:
        pygame.event.get()
        pygame.time.delay(50)
        clock.tick(10)
        s.move()

        if s.body[0].pos == food.pos:
            #Bug isolated to addCube function!
            #s.addCube()
            food = cube(randomFood(rows, s), color=(0,255,0))

        redrawWindow(window)

main()
