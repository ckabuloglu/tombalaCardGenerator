import pygame
import time
import math
import random

# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

random.seed()

class Card():
    def __init__(self):
        self.color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        self.nums = self.assignNums()
        # self.surface = pygame.display.set_mode((804, 304))

    def assignNums(self):
        random.seed()

        rands = []
        i = 0
        while i < 15:
            rand = random.randint(1, 90)
            if rand not in rands:
                rands.append(rand)
                i += 1
        rands.sort()
        versions = [[1,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0], 
                    [1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1]]
        nums = versions[1] if random.random() > 0.5 else versions[0]

        j = 0
        for i in range(27):
            if nums[i] == 1: 
                nums[i] = rands[j]
                j += 3
                if j == 15: j = 2
                elif j == 17: j = 1

        return nums

    def drawCard(self, surface):
        pygame.draw.rect(surface, self.color, [2, 2, 900, 300])
        for i in range(27):
            sq = Square(self.nums[i], i, self.color, surface)
            sq.drawSquare()

class Square():
    def __init__(self, num, loc, color, surface):
        self.num = num
        self.loc = loc
        self.color = color
        self.surface = surface

    def drawSquare(self):
        x = 2 + 100 * (self.loc % 9)
        y = 2 + 100 * (self.loc // 9)
        pygame.draw.rect(surface, BLACK, [x, y, 100, 100])
        if self.num == 0:
            pygame.draw.rect(surface, self.color, [x + 1,  y + 1, 98, 98])
        else:
            pygame.draw.rect(surface, WHITE, [x + 1, y + 1, 98, 98])
            putText(str(self.num), x + 20, y + 24, WHITE, self.surface)

def putText(text, x, y, bg, surface):
    font = pygame.font.Font('freesansbold.ttf', 50)
    textSurface = font.render(text, True, BLACK, bg)
    textRect = textSurface.get_rect()
    textRect.x = x
    textRect.y = y
    surface.blit(textSurface, textRect)

pygame.init()
clock = pygame.time.Clock()
card1 = Card()
surface = pygame.display.set_mode((904, 304))
surface.fill(BLACK)

while True:
    for event in pygame.event.get():
        # if page is closed, quit the game
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.set_caption('Tombala Karti')
    card1.drawCard(surface)
    pygame.display.update()
    clock.tick(1)


