import pygame
from pygame import Surface
from game_of_life.game_of_life import GameOfLife
from game_of_life.default import GLIDER_GUN, HIGHLIFE_REPLICATOR
from game_of_life.highlife import HighLife
from game_of_life.board import generate_random_state


WIDTH = 980
HEIGHT = 980
PIXEL_SIZE = 20


def main_with_classes():
    pygame.init()
    screen: Surface = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()

    done = False

    print(f"SIMULATION SIZE: {(WIDTH//PIXEL_SIZE, HEIGHT//PIXEL_SIZE)}")

    # game_of_life: GameOfLife = GameOfLife(
    #     generate_random_state(WIDTH//PIXEL_SIZE, HEIGHT//PIXEL_SIZE)
    # )

    # game_of_life: GameOfLife = GameOfLife(GLIDER_GUN)

    game_of_life: HighLife = HighLife(HIGHLIFE_REPLICATOR)

    # While the game is not over
    while not done:

        # Listen for all events
        for event in pygame.event.get():
            # Quit the infinite loop when the user presses the close button
            if event.type == pygame.QUIT:
                done = True

        # Effacer l'écran
        screen.fill((0, 0, 0))

        # Déssine l'etat initial_state
        game_of_life.print_state(screen, PIXEL_SIZE)

        # Applique les déssins sur l'écran
        pygame.display.flip()

        # Calcule l'etat suivant
        game_of_life.next_state()

        # print("Update !")
        clock.tick(30)

    pygame.quit()


main_with_classes()
