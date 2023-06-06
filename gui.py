import sys
from time import time

import pygame

import main

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
X = 250
Y = 250
FPS = 60

pygame.init()
screen = pygame.display.set_mode((X, Y))    # flags=pygame.NOFRAME
pygame.display.set_caption('Weather')

font = pygame.font.SysFont('Verdana', 12)
clock = pygame.time.Clock()
start = time()
print(f"Время выполнения {time() - start}")

while True:

    clock.tick(FPS)

    for i, item in enumerate(main.weather()):
        print(i, item)
        text = font.render(item, True, white)
        text_rect = text.get_rect()
        text_rect.x = screen.get_rect().x + 10
        text_rect.y = i * 30 + 20
        screen.blit(text, text_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
