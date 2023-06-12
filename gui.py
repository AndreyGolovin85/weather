import sys
from time import time

import pygame

import main

white = (255, 255, 255)
gray = (100, 100, 100)
X = 200
Y = 150
FPS = 20

pygame.init()
screen = pygame.display.set_mode((X, Y))  # flags=pygame.NOFRAME
pygame.display.set_caption('Weather')
font = pygame.font.SysFont('Verdana', 12)
screen.fill(gray)
pygame.display.flip()
clock = pygame.time.Clock()
start = time()


def draw_text(text: list) -> list:
    for i, item in enumerate(text):
        text = font.render(item, True, white)
        text_rect = text.get_rect()
        text_rect.x = screen.get_rect().x + 10
        text_rect.y = i * 20 + 20
        screen.blit(text, text_rect)


draw_text(main.weather())


while True:

    clock.tick(FPS)
    if time() - start > 600:
        screen.fill(gray)
        start = time()
        draw_text(main.weather())

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
