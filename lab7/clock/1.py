import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((800, 800))

clock = pygame.image.load("mickey.png")
min_hand = pygame.image.load("right.png")
sec_hand = pygame.image.load("left.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(clock, (0, 0))

    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    min_angle = -((now.minute+1) * 6) +90
    sec_angle = -(now.second * 6) +90


    rotated_min_hand = pygame.transform.rotate(min_hand, min_angle)
    min_rect = rotated_min_hand.get_rect(center=(800 // 2, 800 // 2))
    screen.blit(rotated_min_hand, min_rect)

    rotated_sec_hand = pygame.transform.rotate(sec_hand, sec_angle)
    sec_rect = rotated_sec_hand.get_rect(center=(800 // 2, 800 // 2))
    screen.blit(rotated_sec_hand, sec_rect)

    pygame.display.flip() 