import pygame
import sys
from constants import *
from logger import log_state, log_event
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\n"
          f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids: pygame.sprite.Group[Asteroid] = pygame.sprite.Group()
    shots: pygame.sprite.Group[Shot] = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    

    asteroid_field = AsteroidField()
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        updatable.update(dt)

        for aster in asteroids:
            if aster.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        pygame.display.flip()




if __name__ == "__main__":
    main()


