from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
from player import Player
from shot import Shot
import sys
from asteroid import Asteroid



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    dt = 0

    # game loop
    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        if player.timer > 0:
            player.timer -= dt

        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                sys.exit()

            for bullet in shots:
                if obj.collision(bullet):
                    bullet.kill()
                    obj.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit fps to 60
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()
