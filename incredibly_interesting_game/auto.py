import pygame
from random import *

class Nom:
    def __init__(self):
        self.nom_image = pygame.image.load('Drawing.png').convert_alpha()
        self.auto_dict = {"auto_x": 1, "auto_y": 1, "dest_x": 1, "dest_y": 1}
        self.start_x = 1
        self.start_y = 1

        self.new_auto = False
        self.score_changed = False

        self.nom_rect = self.nom_image.get_rect()

    # pick a place to glide to in another quadrant
    def dest(self):
        dest_quad = []
        if self.auto_dict["auto_x"] > 0:
            if self.auto_dict["auto_y"] > 0:
                # quadrant 1
                dest_quad = [2, 3, 4]
            else:
                # quadrant 4
                dest_quad = [1, 2, 3]
        elif self.auto_dict["auto_x"] < 0:
            if self.auto_dict["auto_y"] < 0:
                # quadrant 2
                dest_quad = [1, 3, 4]
            else:
                # quadrant 3
                dest_quad = [1, 2, 4]
        # pick random from dest_quad
        # print(dest_quad)
        dest_quad = choice(dest_quad)
        # random number from coordinates in quadrant
        if dest_quad == 1:
            self.auto_dict["dest_x"] = randrange(0, 800)
            self.auto_dict["dest_y"] = randrange(0, 500)
        if dest_quad == 2:
            self.auto_dict["dest_x"] = randrange(-800, 0)
            self.auto_dict["dest_y"] = randrange(0, 500)
        if dest_quad == 3:
            self.auto_dict["dest_x"] = randrange(0, 800)
            self.auto_dict["dest_y"] = randrange(-500, 0)
        if dest_quad == 4:
            self.auto_dict["dest_x"] = randrange(-800, 0)
            self.auto_dict["dest_y"] = randrange(-500, 0)
        # print(dest_x, dest_y, "destination")

    # there's probably something wrong with this
    def auto(self):
        if self.new_auto == True:
            print("2 seconds?")
            # pick a random starting point
            self.auto_dict["auto_x"] = randrange(-800, 800)
            self.auto_dict["auto_y"] = randrange(-500, 500)
            self.dest()
            self.score_changed = False
            self.new_auto = False
        if self.new_auto == False:
            self.auto_dict["auto_x"] += (self.auto_dict["dest_x"] - self.auto_dict["auto_x"]) / 25
            self.auto_dict["auto_y"] += (self.auto_dict["dest_y"] - self.auto_dict["auto_y"]) / 25

            #is changing too often(not every 2 sec)
            print("dest_x:", self.auto_dict["dest_x"], "," ,"dest_y:", self.auto_dict["dest_y"])
            print("auto_x:", self.auto_dict["auto_x"], ",", "auto_y:", self.auto_dict["auto_y"])

            #if score_changed == False and end_state == 0:
            #    screen.blit(self.nom_image, (self.auto_dict["auto_x"], self.auto_dict["auto_y"]))