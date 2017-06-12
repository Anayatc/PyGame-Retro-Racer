import pygame
import time

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


def text_objects(text, font):
    text_surf = font.render(text, True, black)
    return text_surf, text_surf.get_rect()


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surface, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(text_surface, text_rect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display('You Crashed')


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.84)
    x_change = 0

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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
            crash()

        pygame.display.update()
        clock.tick(120)

game_loop()
pygame.quit()
quit()
