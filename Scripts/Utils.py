import pygame

def load_image(file):
    image = pygame.image.load(file).convert_alpha()
    return image

def load_texture(file_path, tile, tile_size):
    x = tile[0] * tile_size
    y = tile[1] * tile_size

    sprite_sheet = load_image(file_path)
    texture = pygame.Surface((tile_size, tile_size)).convert_alpha()
    texture.blit(sprite_sheet, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
    texture.set_colorkey("black")
    return texture