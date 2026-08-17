import pygame
import consts
import random
import soldier

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT ))


def draw_grass(grass_img):
    grassIMG = pygame.image.load(grass_img)
    grass = pygame.transform.scale(grassIMG, (consts.SIDE_LENGTH, consts.SIDE_LENGTH))
    for i in range(20):
        x_location = random.randrange(0, consts.WINDOW_HEIGHT)
        y_location = random.randrange(0, consts.WINDOW_WIDTH)
        screen.blit(grass, (x_location, y_location))

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def create_main_screen():
    screen.fill(consts.BOARD_COLOR)
    draw_grass("grass.png")
    draw_message("Welcome to the flag game! \n have fun :)" , 11, "black", (10, 20) )
    soldier.create_soldier("soldier.png")
    pygame.display.flip()

board = create_main_screen()
while True:
    pygame.quit()
print






