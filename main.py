from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    colors = {
        "black": pygame.Color(0, 0, 0)
    }
    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(colors["black"])

if __name__ == "__main__":
    main()
