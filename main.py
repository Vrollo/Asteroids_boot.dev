import pygame

from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Setup a clock object to be used for FPS calculation/limitation
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)

    # Setup player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Clear the screen
        screen.fill((0, 0, 0))
        # Update 
        updatable.update(dt)
        # Draw player
        for object in drawable:
            object.draw(screen)
        # Flip the screen to visible screen
        pygame.display.flip()
        # FPS functions
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
