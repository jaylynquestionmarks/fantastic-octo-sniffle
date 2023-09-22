import pygame
from random import *

pygame.init()

screen = pygame.display.set_mode((1920,1080)) #1920x1080

import player
import auto

BLUE = (0, 150, 255)
COLOR = (80, 50, 30)

#set variables for start; not score, timer, and winscore(set in levels)

end_state = 0
is_game_scene = False
scene = "intro"
timer = 0
score = 0
winscore = 0

#main screen text
font = pygame.font.SysFont('chalkduster.ttf', 100)
title_text = font.render('incredibly interesting game', True, BLUE)
lvl_1_text = font.render('Level 1', True, COLOR)
lvl_2_text = font.render('Level 2', True, COLOR)

#Clock
clock = pygame.time.Clock()
clock_text = font.render(str(timer), True, (0, 128, 0))
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

#render score + win/lose
score_text = font.render(str(score), True, (0, 128, 0))
replay_text = font.render('Replay?', True, (0, 0, 0))
replay = pygame.image.load('blue_button.png').convert_alpha()
replay = pygame.transform.scale(replay, (400, 184.5))
replay_button = replay.get_rect()
replay_button.center = (960, 520)

#Level 1 Button
#image1 = pygame.image.load('image.png') #file name
lvl1start = pygame.image.load('blue_button.png').convert_alpha()
#transform class can also rotate <<<
lvl1start = pygame.transform.scale(lvl1start, (400, 184.5))
#move start button hitbox to where it appears
lvl1_start_button = lvl1start.get_rect()
lvl1_start_button.center = (380,680)
#Level 2 Button
lvl2start = pygame.image.load('blue_button.png').convert_alpha()
lvl2start = pygame.transform.scale(lvl2start, (400, 184.5))
#move start button hitbox to where it appears
lvl2_start_button = lvl2start.get_rect()
lvl2_start_button.center = (1500,680)

#Back Arrow
backarrow = pygame.image.load('backarrow.png').convert_alpha()
backarrow = pygame.transform.scale(backarrow, (64, 64))
backarrow_button = backarrow.get_rect()
backarrow_button.center = (50, 50)

#Sprite(hero)
mc = player.Player(50, 800)

#le nom
nom = auto.Nom()

#enemy
smile = pygame.image.load('image0.png').convert_alpha()
smile = pygame.transform.scale(smile,(500, 500))
ex = 0
ey = 0

def enemy(ex, ey, mc_x, mc_y):
    ex += (mc_x - ex) / 130
    ey += (mc_y - ey) / 130
    screen.blit(smile, (ex, ey))
    return ex, ey

def levels(scene, timer):
    global end_state
    global is_game_scene
    global clock_text
    global ex
    global ey
    global score
    global winscore
    end_state = 0
    is_game_scene = True
    if scene == "lvl1":
        timer = 60
    elif scene == "lvl2":
        timer = 30
    pygame.time.set_timer(timer_event, 1000)
    clock_text = font.render(str(timer), True, (0, 128, 0))

    mc.mc_dict = {"x": 50, "y": 800, "xV": 0, "yV": 0}
    nom.auto_dict["auto_x"] = 1
    nom.auto_dict["auto_y"] = 1
    ex = 0
    ey = 0

    score = 0
    winscore = 5
    return end_state, is_game_scene, scene, timer, clock_text, mc.mc_dict, auto, ex, ey, score, winscore

while True:
    screen.fill('white')
    clock.tick(60)

    #main page
    if scene == "intro":
        pygame.draw.circle(screen, 'black', (960, 520), 100)  # 1080/2 = 540, 1920/2 = 960 |||||| set hero to (960,950)
        screen.blit(title_text, (550, 300))
        screen.blit(lvl1start, (200, 600))
        screen.blit(lvl_1_text, (280, 655))
        screen.blit(lvl2start, (1300, 600))
        screen.blit(lvl_2_text, (1380, 655))

    if scene != "intro":
        screen.blit(backarrow, (20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")
            print(event.pos)

            if scene != "intro":
                if backarrow_button.collidepoint(event.pos):
                    is_game_scene = False
                    end_state = 0
                    scene = "intro"
                    print("scene changed")
            if scene == 'intro':
                if lvl1_start_button.collidepoint(event.pos):
                    #level 1
                    scene = "lvl1"
                    end_state, is_game_scene, scene, timer, clock_text, mc.mc_dict, auto, ex, ey, score, winscore = levels(scene, timer)
                    print("lvl 1")

                elif lvl2_start_button.collidepoint(event.pos):
                    #level 2
                    scene = "lvl2"
                    end_state, is_game_scene, scene, timer, clock_text, mc.mc_dict, auto, ex, ey, score, winscore = levels(scene, timer)
                    print("lvl 2")
            if end_state != 0:
                if replay_button.collidepoint(event.pos):
                    end_state, is_game_scene, scene, timer, clock_text, mc.mc_dict, auto, ex, ey, score, winscore = levels(scene, timer)
                    score_text = font.render(str(score), True, (0, 128, 0))
                    screen.blit(score_text, (1800, 200))
                    print(end_state, is_game_scene, scene, timer, clock_text, mc.mc_dict, auto, ex, ey, score, winscore)
                    print("replay")

        if is_game_scene == True:
            #timer
            if event.type == timer_event and end_state == 0:
                screen.blit(clock_text, (1800, 50))
                timer -= 1

                if timer % 2 == 0:
                    nom.new_auto = True

                clock_text = font.render(str(timer), True, (0, 128, 0))
                if timer == 0:
                    pygame.time.set_timer(timer_event, 0)
                    end_state = "lose"
    #if in game
    if is_game_scene == True and end_state == 0:
        screen.blit(clock_text, (1800, 50))
        #show the score in game
        screen.blit(score_text, (1800, 200))

        #auto hitboxes
        nom.nom_rect = nom.nom_image.get_rect()
        nom.nom_rect.update(nom.auto_dict["auto_x"] + 850, nom.auto_dict["auto_y"] + 370, 180, 180)
        #makes auto move and stuff
        nom.auto()
        if nom.score_changed == False and end_state == 0:
            screen.blit(nom.nom_image, (nom.auto_dict["auto_x"], nom.auto_dict["auto_y"]))

        #enemy hitbox
        smile_rect = smile.get_rect()
        smile_rect.update(ex + 160, ey+140, 170, 190)
        '''
        mask = pygame.mask.from_surface(smile)
        e_outline = mask.outline()
        e_outline_image = pygame.Surface(smile_rect.size).convert_alpha()
        e_outline_image.fill((255, 255, 0))
        for point in e_outline:
            e_outline_image.set_at(point, (255, 255, 0))

        show smile and hitbox
        screen.blit(e_outline_image, (ex + 160, ey+140))
        '''
        ex, ey = enemy(ex, ey, mc.mc_dict["x"], mc.mc_dict["y"])

        #run motion code
        mc.motion()
        #borders
        mc.mc_borders()
        #hitboxes
        mc.mc_hitboxes()

        if end_state == 0:
            screen.blit(mc.mc_image, (mc.mc_dict["x"], mc.mc_dict["y"]))

            if mc.rect.colliderect(nom.nom_rect) == True and nom.score_changed == False:
                # print(rect, nom_rect)
                score += 1
                nom.score_changed = True
                score_text = font.render(str(score), True, (0, 128, 0))
                print(score)

    #end_state
        if mc.rect.colliderect(smile_rect) == True:
            end_state = 'lose'
        elif score == winscore:
            end_state = 'win'


    if end_state == 'lose' or end_state == 'win':
        end_state_text = font.render("You " + str(end_state) + "!", True, (0, 128, 0))
        screen.blit(end_state_text, (870, 300))
        screen.blit(replay, (830, 440))
        screen.blit(replay_text, (900, 500))


    #leave at bottom
    pygame.display.update()