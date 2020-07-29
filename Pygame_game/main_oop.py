import pygame
import time
import numpy as np

pygame.init()
win = pygame.display.set_mode((928, 793))

pygame.display.set_caption("Bensstats Videogame")


class player(object):
    def __init__(self, x, y, wd, height):
        self.x = x
        self.y = y
        self.wd = wd
        self.height = height
        self.isJump = False
        self.jumpCount = 8
        self.left = False
        self.right = False
        self.WalkCount = 0
        self.vel = 5
        self.isMelee = False
        self.attackCount = 0
        self.isStanding =False
        self.StandCount = 0
        self.position = False # False = Right, True = Left
        self.hurt = False
        self.hurtCount= 0

    def draw(self, win):
        if self.WalkCount + 1 >= 18:
            self.WalkCount = 0
        if self.attackCount + 1 >= 51:
            self.attackCount = 0

        if self.isStanding:
            if self.position:
                self.StandCount += 1
                win.blit(StandRight[self.StandCount // 3], (self.x, self.y))
                if self.StandCount + 1 >= 12:
                    self.StandCount = 0
            else:
                self.StandCount += 1
                win.blit(StandLeft[self.StandCount // 3], (self.x, self.y))
                if self.StandCount + 1 >= 12:
                    self.StandCount = 0

        if self.isMelee:
            self.hurt = False
            if self.position:
                win.blit(slashRight[self.attackCount // 3], (self.x, self.y))
                self.attackCount += 1
            else:
                win.blit(slashLeft[self.attackCount // 3], (self.x, self.y))
                self.attackCount += 1
        elif self.left:
            win.blit(walkLeft[self.WalkCount // 3], (self.x, self.y))
            self.WalkCount += 1
        elif self.right:
            win.blit(walkRight[self.WalkCount // 3], (self.x, self.y))
            self.WalkCount += 1

        if self.isJump:
            self.hurt=False
            if self.position:
                win.blit(jumpRight[self.jumpCount // 3], (self.x, self.y))
            else:
                win.blit(jumpLeft[self.jumpCount // 3], (self.x, self.y))
        if self.hurt:
            if prot.hurtCount + 1 >= 21:
                prot.hurtCount = 0
            if self.position:

                win.blit(damageRight[self.hurtCount//7],(self.x,self.y))
            else:

                win.blit(damageLeft[self.hurtCount // 7], (self.x, self.y))


#### Protagonist Movement

walkRight = [pygame.image.load('run3\\adventurer-run3-00.png'),
             pygame.image.load('run3\\adventurer-run3-01.png'),
             pygame.image.load('run3\\adventurer-run3-02.png'),
             pygame.image.load('run3\\adventurer-run3-03.png'),
             pygame.image.load('run3\\adventurer-run3-04.png'),
             pygame.image.load('run3\\adventurer-run3-05.png')]

walkLeft = [pygame.image.load('Run Left\\run_left 01.png'),
            pygame.image.load('Run Left\\run_left 02.png'),
            pygame.image.load('Run Left\\run_left 03.png'),
            pygame.image.load('Run Left\\run_left 04.png'),
            pygame.image.load('Run Left\\run_left 05.png'),
            pygame.image.load('Run Left\\run_left 06.png')]

StandRight = [pygame.image.load("Adventurer\\Individual Sprites\\adventurer-idle-2-00.png"),
              pygame.image.load("Adventurer\\Individual Sprites\\adventurer-idle-2-01.png"),
              pygame.image.load("Adventurer\\Individual Sprites\\adventurer-idle-2-02.png"),
              pygame.image.load("Adventurer\\Individual Sprites\\adventurer-idle-2-03.png")]

StandLeft = []

for img in StandRight:
    StandLeft.append(pygame.transform.flip(img, True, False))

slashRight = [pygame.image.load('Attack\\adventurer-attack1-00.png'),
              pygame.image.load('Attack\\adventurer-attack1-01.png'),
              pygame.image.load('Attack\\adventurer-attack1-02.png'),
              pygame.image.load('Attack\\adventurer-attack1-03.png'),
              pygame.image.load('Attack\\adventurer-attack1-04.png'),
              pygame.image.load('Attack\\adventurer-attack2-00.png'),
              pygame.image.load('Attack\\adventurer-attack2-01.png'),
              pygame.image.load('Attack\\adventurer-attack2-02.png'),
              pygame.image.load('Attack\\adventurer-attack2-03.png'),
              pygame.image.load('Attack\\adventurer-attack2-04.png'),
              pygame.image.load('Attack\\adventurer-attack2-05.png'),
              pygame.image.load('Attack\\adventurer-attack3-00.png'),
              pygame.image.load('Attack\\adventurer-attack3-01.png'),
              pygame.image.load('Attack\\adventurer-attack3-02.png'),
              pygame.image.load('Attack\\adventurer-attack3-03.png'),
              pygame.image.load('Attack\\adventurer-attack3-04.png'),
              pygame.image.load('Attack\\adventurer-attack3-05.png')]

slashLeft = []

for img in slashRight:
    slashLeft.append(pygame.transform.flip(img, True, False))

jumpRight = [pygame.image.load("Adventurer\\Individual Sprites\\adventurer-jump-00.png"),
             pygame.image.load("Adventurer\\Individual Sprites\\adventurer-jump-01.png"),
             pygame.image.load("Adventurer\\Individual Sprites\\adventurer-jump-02.png"),
             pygame.image.load("Adventurer\\Individual Sprites\\adventurer-jump-03.png"),
             pygame.image.load("Adventurer\\Individual Sprites\\adventurer-smrslt-00.png"),
             pygame.image.load("Adventurer\\Individual Sprites\\adventurer-smrslt-01.png"),
             pygame.image.load("Adventurer\\Individual Sprites\\adventurer-smrslt-02.png"),
             pygame.image.load("Adventurer\\Individual Sprites\\adventurer-smrslt-03.png")]

jumpLeft = []

for img in jumpRight:
    jumpLeft.append(pygame.transform.flip(img, True, False))

damageRight = [pygame.image.load("Adventurer\Individual Sprites\\adventurer-die-00.png"),
               pygame.image.load("Adventurer\Individual Sprites\\adventurer-die-01.png"),
               pygame.image.load("Adventurer\Individual Sprites\\adventurer-die-02.png"),
               pygame.image.load("Adventurer\Individual Sprites\\adventurer-die-03.png"),
               pygame.image.load("Adventurer\Individual Sprites\\adventurer-die-04.png"),
               pygame.image.load("Adventurer\Individual Sprites\\adventurer-die-05.png"),
               pygame.image.load("Adventurer\Individual Sprites\\adventurer-die-06.png")]
damageLeft = []

for img in damageRight:
    damageLeft.append(pygame.transform.flip(img,True,False))


####


### Enemies

class enemy_a(object):


######### Walking #################

    walkRight = [pygame.image.load("Skeleton Walk\\tile000.png"),
                 pygame.image.load("Skeleton Walk\\tile001.png"),
                 pygame.image.load("Skeleton Walk\\tile002.png"),
                 pygame.image.load("Skeleton Walk\\tile003.png"),
                 pygame.image.load("Skeleton Walk\\tile004.png"),
                 pygame.image.load("Skeleton Walk\\tile005.png"),
                 pygame.image.load("Skeleton Walk\\tile006.png"),
                 pygame.image.load("Skeleton Walk\\tile007.png"),
                 pygame.image.load("Skeleton Walk\\tile008.png"),
                 pygame.image.load("Skeleton Walk\\tile009.png"),
                 pygame.image.load("Skeleton Walk\\tile010.png"),
                 pygame.image.load("Skeleton Walk\\tile011.png"),
                 pygame.image.load("Skeleton Walk\\tile012.png")]

    walkLeft = []
    for img in walkRight:
        walkLeft.append(pygame.transform.flip(img, True, False))

    ## Attack

    attackRight =[pygame.image.load("Skeleton Attack\\tile000.png"),
                  pygame.image.load("Skeleton Attack\\tile001.png"),
                  pygame.image.load("Skeleton Attack\\tile002.png"),
                  pygame.image.load("Skeleton Attack\\tile003.png"),
                  pygame.image.load("Skeleton Attack\\tile004.png"),
                  pygame.image.load("Skeleton Attack\\tile005.png"),
                  pygame.image.load("Skeleton Attack\\tile006.png"),
                  pygame.image.load("Skeleton Attack\\tile007.png"),
                  pygame.image.load("Skeleton Attack\\tile008.png"),
                  pygame.image.load("Skeleton Attack\\tile009.png"),
                  pygame.image.load("Skeleton Attack\\tile010.png"),
                  pygame.image.load("Skeleton Attack\\tile011.png"),
                  pygame.image.load("Skeleton Attack\\tile012.png"),
                  pygame.image.load("Skeleton Attack\\tile013.png"),
                  pygame.image.load("Skeleton Attack\\tile014.png"),
                  pygame.image.load("Skeleton Attack\\tile015.png"),
                  pygame.image.load("Skeleton Attack\\tile016.png"),
                  pygame.image.load("Skeleton Attack\\tile017.png"),
                  ]

    attackLeft =[]
    for img in attackRight:
        attackLeft.append(pygame.transform.flip(img, True, False))

    damageRight=[pygame.image.load("Skeleton Hit\\tile000.png"),
                 pygame.image.load("Skeleton Hit\\tile001.png"),
                 pygame.image.load("Skeleton Hit\\tile002.png"),
                 pygame.image.load("Skeleton Hit\\tile003.png"),
                 pygame.image.load("Skeleton Hit\\tile004.png"),
                 pygame.image.load("Skeleton Hit\\tile005.png"),
                 pygame.image.load("Skeleton Hit\\tile006.png"),
                 pygame.image.load("Skeleton Hit\\tile007.png"),]

    damageLeft=[]
    for img in damageRight:
        damageLeft.append(pygame.transform.flip(img,True,False))

    def __init__(self, x, y, width, height, end):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.WalkCount = 0
        self.Walking = True
        self.vel = 2
        self.isMelee= False
        self.attackCount = 0
        self.position =True  # False = Right, True = Left
        self.hurt =False
        self.hurtCount =0

    def draw(self, win):
        self.move()
        if self.WalkCount + 1 >= 39:
            self.WalkCount = 0
        if self.attackCount+1 >= 18:
            self.attackCount=0

        if self.Walking:
            if self.vel > 0:
                win.blit(self.walkRight[self.WalkCount // 3], (self.x, self.y))
                self.WalkCount += 1
        else:
            if self.vel < 0:
                win.blit(self.walkLeft[self.WalkCount // 3], (self.x, self.y))
                self.WalkCount += 1

        if self.isMelee:
            if self.position:
                win.blit(self.attackRight[self.attackCount // 2], (self.x, self.y))
                self.attackCount += 1
            else:
                win.blit(self.attackLeft[self.attackCount // 2], (self.x, self.y))
                self.attackCount += 1
        if self.hurt:
            if self.hurtCount +1 >= 24:
                self.hurtCount=0
            if self.position:
                win.blit(self.damageRight[self.hurtCount // 3], (self.x, self.y))
                self.hurtCount += 1
            else:
                win.blit(self.damageLeft[self.hurtCount // 3], (self.x, self.y))
                self.hurtCount += 1

    def move(self):

        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.WalkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * - 1
                self.WalkCount = 0



bg = pygame.image.load("Background.png")
clock = pygame.time.Clock()
prot = player(500, 700, 50, 37)
enemy= enemy_a(0, 700, 22, 33, 900)




def redraw_game_window():
    win.blit(bg, (0, 0))
    prot.draw(win)
    enemy.draw(win)
    pygame.display.update()


run = True

# pygame.mixer.init()
# pygame.mixer.music.load("Music.mp3")
# pygame.mixer.music.play(loops=-1)

while run:

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            prot.isMelee = True
            prot.StandCount = 0
            print("Click")
        if event.type == pygame.MOUSEBUTTONUP:
            prot.isMelee = False

    keys = pygame.key.get_pressed()
    space_bar = pygame.key

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and prot.x > prot.vel:
        prot.x -= prot.vel
        prot.left = True
        prot.right = False
        prot.isStanding = False
        prot.position = False
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and prot.x < 928 - prot.wd - prot.vel:
        prot.x += prot.vel
        prot.left = False
        prot.right = True
        prot.isStanding = False
        prot.position = True
    elif prot.isMelee:
        prot.hurt = False
        prot.isStanding = False
        prot.right = False
        prot.left = False
        prot.WalkCount = 0

    else:
        prot.isStanding = True
        prot.right = False
        prot.left = False
        prot.WalkCount = 0

    if not (prot.isJump):
        if keys[pygame.K_SPACE]:
            prot.hurt = False
            prot.isJump = True
            prot.right = False
            prot.left = False
            prot.isStanding = False
            prot.WalkCount = 0
    else:
        if prot.jumpCount >= -8:
            neg = 1
            if prot.jumpCount < 0:
                neg = -1
            prot.y -= (prot.jumpCount ** 2) * 0.5 * neg
            prot.jumpCount -= 1
            prot.isStanding = False
            prot.left = False
            prot.right = False

        else:
            prot.isJump = False
            prot.hurt=False
            prot.jumpCount = 8

    if abs(prot.x-enemy.x) < 33:
        enemy.vel= 0
        enemy.isMelee = True
    else:
        if np.sign(prot.x-enemy.x) > 0:
            enemy.position =True
            enemy.isMelee=False
            enemy.vel= 2
            enemy.Walking=True
            enemy.hurt=False
        else:
            enemy.position=False
            enemy.Walking = False
            enemy.isMelee = False
            enemy.hurt=False
            enemy.vel = -2

    if enemy.isMelee == True and prot.isMelee ==False:
        enemy.hurt=False
        prot.hurt = True
        prot.hurt=True
        prot.right=False
        prot.left=False
        prot.isStanding=False
        prot.hurtCount+=1
    else:
        prot.hurt=False

    if prot.isMelee==True and abs(prot.x-enemy.x) < 33:
        enemy.isMelee=False
        enemy.hurt=True



    redraw_game_window()

pygame.quit()
