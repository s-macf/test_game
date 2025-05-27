import pygame


class Game:

    def __init__(self, res):
        pygame.init()
        self.screen = pygame.display.set_mode((res[0], res[1]))
        self.display = pygame.Surface((res[0]/2, res[1]/2))
        self.scale_multiplier = 1

    def run(self):
        running = True
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

            scaled_display = pygame.transform.scale(
                self.display,
                size=(self.screen.get_width() * self.scale_multiplier,
                      self.screen.get_height() * self.scale_multiplier)
            )

            display_rect = scaled_display.get_rect()
            display_rect.center = self.screen.get_rect().center

            self.screen.blit(scaled_display, display_rect)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = Game(res=(640, 320))
    game.run()
