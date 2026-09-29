import pygame

def main():
    pygame.init()

    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    screen.fill("blue")
    pygame.draw.rect(screen, "black", pygame.Rect(0,0,100,100), 0)

    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()