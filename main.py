import pygame
from Scripts.Tilemap import Tilemap
from Scripts.Player import Player

class Game:

    def __init__(self, res):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((res[0], res[1]))
        self.display = pygame.Surface((res[0]*2, res[1]*2))
        self.scale_multiplier = 1
        self.world = Tilemap(self.display)
        self.player = Player(self.display, [600, 500], 16, self.world)

    def run(self):
        running = True
        velocity = 0
        while running:

            self.screen.fill("black")
            self.display.fill("lightblue")


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_MINUS:
                        self.scale_multiplier -= 0.1
                    if event.key == pygame.K_EQUALS:
                        self.scale_multiplier += 0.1
                    if event.key == pygame.K_d:
                        self.player.velocity[0] = 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.player.velocity[1] = velocity
                        velocity = 0
                    if event.key == pygame.K_d:
                        self.player.velocity[0] = 0

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                velocity = max(-20, velocity - 0.5)

            self.world.render()

            # Testing Region
            self.player.update()
            self.player.render()

            scaled_display = pygame.transform.scale(
                self.display,
                size=(self.screen.get_width() * self.scale_multiplier,
                      self.screen.get_height() * self.scale_multiplier)
            )


            display_rect = scaled_display.get_rect()
            display_rect.center = self.screen.get_rect().center

            self.screen.blit(scaled_display, display_rect)

            self.clock.tick(60)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = Game(res=(600, 450))
    game.run()
