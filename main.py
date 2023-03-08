import pygame

pygame.init()

screen = pygame.display.set_mode((1920,1080)) #1920x1080

BLUE = (0, 150, 255)
COLOR = (80, 50, 30)

#set variables for start; not score, timer, and winscore(set in levels)
end_state = 0
is_game_scene = False
scene = "intro"
timer = 0
winscore = 0
scene_changed = True

#main screen text
font = pygame.font.SysFont('chalkduster.ttf', 100)
title_text = font.render('incredibly interesting game', True, BLUE)
lvl_1_text = font.render('Level 1', True, COLOR)

#Clock
clock = pygame.time.Clock()
clock_text = font.render(str(timer), True, (0, 128, 0))
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

#Level 1 Button
#image1 = pygame.image.load('image.png') #file name
lvl1start = pygame.image.load('blue_button.png')
#transform class can also rotate <<<
lvl1start = pygame.transform.scale(lvl1start, (400, 184.5))
#move start button hitbox to where it appears
lvl1_start_button = lvl1start.get_rect()
lvl1_start_button.center = (380,680)

#Back Arrow
backarrow = pygame.image.load('backarrow.png')
backarrow = pygame.transform.scale(backarrow, (64, 64))
backarrow_button = backarrow.get_rect()
backarrow_button.center = (50, 50)

#Sprite(hero)
xV = 0
yV = 0
x = 50
y = 800
mc = pygame.image.load('6b74880c-a7be-46a5-8c04-dc4b676292df.sketchpad.png')
mc = pygame.transform.scale(mc, (246, 170)) #246, 162

#what
def motion(x, y, xV, yV):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        yV -= 0.8
    if keys[pygame.K_DOWN]:
        yV += 0.8
    if keys[pygame.K_RIGHT]:
        xV += 0.8
    if keys[pygame.K_LEFT]:
        xV -= 0.8
    x += xV
    y += yV
    xV = xV*0.9
    yV = yV*0.9
    return x, y, xV, yV

while True:
    screen.fill('white')
    clock.tick(60)

    #main page
    if scene == "intro":
        pygame.draw.circle(screen, 'black', (960, 520), 100)  # 1080/2 = 540, 1920/2 = 960 |||||| set hero to (960,950)
        screen.blit(title_text, (550, 300))
        screen.blit(lvl1start, (200, 600))
        screen.blit(lvl_1_text, (280, 655))

    if scene != "intro":
        screen.blit(backarrow, (20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")

            if scene != "intro":
                print(pygame.mouse.get_pos())
                print(backarrow_button)
                if backarrow_button.collidepoint(event.pos):
                    is_game_scene = False
                    scene = "intro"
                    scene_changed = True
                    print("scene changed")

            if lvl1_start_button.collidepoint(event.pos):
                x = 50
                y = 800
                end_state = 0
                is_game_scene = True
                scene = "lvl1"

                timer = 60
                pygame.time.set_timer(timer_event, 1000)
                clock_text = font.render(str(timer), True, (0, 128, 0))

                winscore = 10
                scene_changed = True
                print("scene changed")

        if is_game_scene == True:
            #timer
            if event.type == timer_event:
                screen.blit(clock_text, (1800, 50))
                timer -= 1
                clock_text = font.render(str(timer), True, (0, 128, 0))
                if timer == 0:
                    pygame.time.set_timer(timer_event, 0)
                    end_state = "purgatory"
                    is_game_scene = False
                    print(end_state)
                    scene = "intro"
    if is_game_scene == True:
        screen.blit(clock_text, (1800, 50))
        x, y, xV, yV = motion(x, y, xV, yV)
        screen.blit(mc, (x, y))

   #screen.blit(image,(0,0))

    #leave at bottom
    pygame.display.update()