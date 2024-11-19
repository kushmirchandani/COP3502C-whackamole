import pygame
import random

GRID_WIDTH = 20
GRID_HEIGHT = 16
SQUARE_SIZE = 32

def random_square():
    random_x = random.randrange(0, GRID_WIDTH) * SQUARE_SIZE
    random_y = random.randrange(0, GRID_HEIGHT) * SQUARE_SIZE
    return random_x, random_y


def draw_grid(screen):
    for x in range(0, 640, SQUARE_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 512))

    for y in range(0, 512, SQUARE_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (640, y))


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")

        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-a-Mole | ®Mirchandani Edition")

        clock = pygame.time.Clock()

        mole_x, mole_y = 0,0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if mole_x <= mouse_x < mole_x + SQUARE_SIZE and mole_y <= mouse_y < mole_y + SQUARE_SIZE:
                    mole_x, mole_y = random_square()


            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, (mole_x, mole_y))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
