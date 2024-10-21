import pygame
import math
pygame.init()

info = pygame.display.Info()
x = info.current_w
y = info.current_h-50
window = pygame.display.set_mode((x,y),pygame.RESIZABLE)
pygame.display.set_caption("Game")

bg = pygame.image.load('Assets/BG.png')
bg = pygame.transform.scale(bg,(x,y))
playi = pygame.image.load('Assets/Play.png')
playi = pygame.transform.scale(playi,(200,75))
setti = pygame.image.load('Assets/Sett.png')
setti = pygame.transform.scale(setti,(300,75))
helpi = pygame.image.load('Assets/Help.png')
helpi = pygame.transform.scale(helpi,(200,75))
quiti = pygame.image.load('Assets/quit.png')
quiti = pygame.transform.scale(quiti,(200,75))
backi = pygame.image.load('Assets/Back.png')
backi = pygame.transform.scale(backi,(100,100))

player = pygame.image.load("Assets/player.png")
player = pygame.transform.scale(player, (100,150))
coin = pygame.image.load("Assets/coins.png")
coin = pygame.transform.scale(coin, (100,100))

a = 70
tile2 = pygame.image.load('Assets/tile 2.png')
tile2 = pygame.transform.scale(tile2,(a,a))
tile5 = pygame.image.load('Assets/tile 5.png')
tile5 = pygame.transform.scale(tile5,(a,a))
bg1 = pygame.image.load('Assets/bg1.png')
bg1 = pygame.transform.scale(bg1,(x-200,y))
scroll = 0
tiles = math.ceil(x / (x-200)) + 1

White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
Black = (0,0,0)
size = 100
font = pygame.font.SysFont(None,size)

sound1 = pygame.mixer.Sound('Assets/Menu.mp3')
sound2 = pygame.mixer.Sound('Assets/Play screen.mp3')
sound1.set_volume(0.03)
sound2.set_volume(0.5)

def text(content, colour, xpos, ypos):
    msg = font.render(content,True,colour)
    window.blit(msg,(xpos,ypos))


def game():
    scroll = 0
    menu = True
    play = False
    settings = False
    help = False
    score = 0
    mpos = 0,0
    collide = True

    plx = 300
    ply = 200

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mpos = pygame.mouse.get_pos()
        window.fill(White)
        sound1.play()
        settings = False
        help = False
        window.blit(bg,(0,0))
        size = 100
        text("Adam's Adventure", Black, x / 2-300, 100)
        window.blit(playi, (x/2-100, 200))
        window.blit(setti, (x/2-150, 300))
        window.blit(helpi, (x/2-100, 400))
        window.blit(quiti, (x / 2 - 100, 500))
        if mpos[0] > x/2-100 and mpos[0] < x/2+100 and mpos[1] > 200 and mpos[1] < 275:
            play = True
            menu = False
        if mpos[0] > x/2-150 and mpos[0] < x/2+150 and mpos[1] > 300 and mpos[1] < 375:
            help = True
            menu = False
        if mpos[0] > x/2-100 and mpos[0] < x/2+100 and mpos[1] > 400 and mpos[1] < 475:
            help = True
            menu = False
        if mpos[0] > x/2-100 and mpos[0] < x/2+100 and mpos[1] > 500 and mpos[1] < 575:
            pygame.quit()
        pygame.display.update()
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mpos = pygame.mouse.get_pos()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                        ply = ply - 10
                if event.key == pygame.K_a:
                    plx = plx - 10
                if event.key == pygame.K_d:
                    plx = plx + 10
        window.fill(White)
        sound1.stop()
        sound2.play()
        menu = False
        settings = False
        help = False
        play = True
        for i in range(0,tiles):
            window.blit(bg1, (i * (x-200) + scroll, 0))
        scroll -= 5
        if abs(scroll) > x-200:
            scroll = 0
        for i in range(0,20):
            window.blit(tile2, (a*i, 530))
            window.blit(tile5, (a * i, 600))
            i = i+1
        for i in range(0,3):
            window.blit(tile2,(200+(a*i),350))
            window.blit(tile2, (500 + (a * i), 200))
            window.blit(tile2, (700 + (a * i), 350))
            i = i+1
        window.blit(backi, (10, 10))
        if mpos[0] > 10 and mpos[0] < 110 and mpos[1] > 10 and mpos[1] < 110:
            sound2.stop()
            game()
        window.blit(player,(plx,ply))
        window.blit(coin,(500,500))
        if ply > 530 and plx > 0 and plx < x:
            collide = True
        pygame.display.update()
    while help:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mpos = pygame.mouse.get_pos()
        window.fill(White)
        menu = False
        play = False
        settings = False
        text("Press WASD to move.",Black,x/2-300, 100)
        text("Press P to Pause/Play.",Black,x/2-300,200)
        window.blit(backi,(10,10))
        if mpos[0] > 10 and mpos[0] < 110 and mpos[1] > 10 and mpos[1] < 110:
            game()
        pygame.display.update()
    while settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        window.fill(White)
        menu = False
        play = False
        help = False
        pygame.display.update()


game()
