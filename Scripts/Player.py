import pygame
from Scripts.Utils import load_texture

PLAYER_IMAGE = "./Assets/Characters/"

class Player:

    def __init__(self, surface, pos, tile_size, tilemap):
        self.surface = surface
        self.pos = pos
        self.tile_size = tile_size
        self.rect = pygame.Rect(pos[0], pos[1], tile_size*4, tile_size*4)
        self.image = self.load_player(tile_size)
        self.tilemap = tilemap
        self.velocity = [0, 0]
        self.on_ground = False

    def load_player(self, tile_size):
        image = load_texture("./Assets/Characters/Basic Charakter Spritesheet.png", (1, 1), tile_size)
        image = pygame.transform.scale_by(image, 4).convert_alpha()
        return image

    def render(self):
        self.surface.blit(self.image, self.pos)

    def update(self):
        self.rect.width = 64
        self.rect.height = 64
        self.pos[1] += self.velocity[1] * 2
        self.pos[0] += self.velocity[0] * 2

        self.rect.left = self.pos[0]
        self.rect.top = self.pos[1]

        for rect in self.tilemap.objects["Ground"]:
            if self.rect.colliderect(rect):
                if self.rect.bottom > rect.top and self.rect.top < rect.top:
                    self.pos[1] = rect.top - self.rect.height
                    self.velocity[1] = 0
                    self.velocity[0] = 0
                    self.on_ground = True
                elif self.rect.left < rect.right and self.rect.right > rect.right and self.rect.bottom > rect.top:
                    self.pos[0] = rect.right
                    self.velocity[0] *= -1



        self.velocity[1] = min(20, self.velocity[1] + 0.6)
