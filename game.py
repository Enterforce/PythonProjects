import pygame
#adding comment

WIDTH = 1024
HEIGHT = 768
BACKGOUND = (0, 0, 0,)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()


    while True:
        screen.fill(BACKGOUND)
        pygame.display.flip()

        clock.tick(60)



if __name__ == "__main__":
    main()


# Another test commit with python 