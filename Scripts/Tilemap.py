import pygame
import pytmx
from pytmx.util_pygame import load_pygame

class Tilemap:

    def __init__(self, surface):
        self.surface = surface
        self.world_image = None
        self.objects = {"Ground" : []}
        self.load_world_data()

    def load_world_data(self):
        tmx_data = load_pygame("./Tiled_Project/untitled.tmx")
        for layer in tmx_data.layers:
            if isinstance(layer, pytmx.TiledImageLayer):
                self.world_image = layer.image
            else:
                for obj in layer:
                    obj_rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                    self.objects[obj.type].append(obj_rect)

    def render(self):
        self.surface.blit(self.world_image, (0,0))

        # for rect in self.objects["Ground"]:
        #     pygame.draw.rect(self.surface, "red", rect)
