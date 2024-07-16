import pygame
from game import perform_move
from solution import moves
from states import state_initial as board


def play_game():
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    # Define Window Variables
    WIDTH = 40
    HEIGHT = WIDTH
    MARGIN = WIDTH / 4

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_HEIGHT = (WIDTH + MARGIN) * len(board) + MARGIN
    WINDOW_WIDTH = (HEIGHT + MARGIN) * len(board[0]) + MARGIN
    WINDOW_SIZE = [WINDOW_HEIGHT, WINDOW_WIDTH]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Grandmas Puzzle Game")

    current_move = 0
    pause = True

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while True:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()
                exit(10)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause

        # Set the screen background
        screen.fill(BLACK)

        # Draw the grid
        for row in range(len(board)):
            for column in range(len(board[0])):
                color = BLACK
                if board[row][column] == 1:
                    color = GREEN
                if board[row][column] == 0:
                    color = WHITE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        # forward the board state
        if current_move < len(moves) and not pause:
            perform_move(board, moves[current_move])
            current_move += 1

        # Limit to 60 frames per second
        clock.tick(1)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


if __name__ == '__main__':
    play_game()
