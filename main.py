from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import pygame


def main():
    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    while 1:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            screen.fill("black")
            pygame.display.flip()
        dt = clock.tick(60)
        print(dt)


if __name__ == "__main__":
    main()
