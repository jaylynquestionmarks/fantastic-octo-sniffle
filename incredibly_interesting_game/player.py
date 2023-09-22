import pygame

class Player:
    def __init__(self, x, y):
        self.mc_dict = {"x": x, "y": y, "xV": 0, "yV": 0}
        self.mc_image = pygame.image.load('6b74880c-a7be-46a5-8c04-dc4b676292df.sketchpad.png').convert_alpha()
        self.rect = self.mc_image.get_rect()
        # mc = pygame.transform.scale(mc, (246, 170)) #246, 162

    # mc movement logic
    #self is for information you want to save
    def motion(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.mc_dict["yV"] -= 0.7
        if keys[pygame.K_DOWN]:
            self.mc_dict["yV"] += 0.7
        if keys[pygame.K_RIGHT]:
            self.mc_dict["xV"] += 0.7
        if keys[pygame.K_LEFT]:
            self.mc_dict["xV"] -= 0.7
        self.mc_dict["x"] += self.mc_dict["xV"]
        self.mc_dict["y"] += self.mc_dict["yV"]
        self.mc_dict["xV"] = self.mc_dict["xV"] * 0.9
        self.mc_dict["yV"] = self.mc_dict["yV"] * 0.9
        return self.mc_dict

    # borders
    def mc_borders(self):
        if self.mc_dict["x"] < -100:
            self.mc_dict["x"] = -100
        elif self.mc_dict["x"] > 1650:
            self.mc_dict["x"] = 1650
        if self.mc_dict["y"] < -100:
            self.mc_dict["y"] = -100
        elif self.mc_dict["y"] > 850:
            self.mc_dict["y"] = 850

    def mc_hitboxes(self):
        self.rect = self.mc_image.get_rect()
        # outline of image (for hitbox)
        #mask = pygame.mask.from_surface(mc)
        #outline = mask.outline()
        #outline_image = pygame.Surface(rect.size).convert_alpha()
        #outline_image.fill((255, 255, 0))
        #for point in outline:
        #    outline_image.set_at(point, (255, 255, 0))
        self.rect = self.rect.move(self.mc_dict["x"], self.mc_dict["y"])
        #screen.blit(outline_image, (mc_dict["x"], mc_dict["y"]))