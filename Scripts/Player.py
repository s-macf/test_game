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
            if self.velocity[1] > 0 and self.rect.colliderect(rect):
                self.pos[1] = rect.top - self.rect.height
                self.velocity[1] = 0
                self.velocity[0] = 0


        self.velocity[1] = min(30, self.velocity[1] + 1)
