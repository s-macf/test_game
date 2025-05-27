import pygame

class Game:

    def __init__(self, res):
        pygame.init()
        self.screen = pygame.display.set_mode((res[0], res[1]))

    
    def run(self):
        running = True
        while running:

            self.screen.fill("black")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = Game(res = (640, 320))
    game.run()