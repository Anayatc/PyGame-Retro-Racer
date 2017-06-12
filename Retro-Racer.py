import pygame

pygame.init()

# display resolution
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
car_width = 50

# window construction
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Retro Racer')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')


# drawing the car to window
def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.84)
    x_change = 0

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)
        car(x, y)

        if x > display_width - car_width or x < 0:
            game_exit = True

        pygame.display.update()
        clock.tick(120)

game_loop()
pygame.quit()
quit()
