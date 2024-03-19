import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))

ekran = (255, 255, 255)
ball = (255, 0, 0)

radius = 25
ballx, bally = 500 // 2, 500 // 2

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                bally = max(bally - 20, radius)

            elif event.key == pygame.K_DOWN:
                bally = min(bally + 20, 500 - radius)

            elif event.key == pygame.K_LEFT:
                ballx = max(ballx - 20, radius)

            elif event.key == pygame.K_RIGHT:
                ballx = min(ballx + 20, 500 - radius)

    screen.fill(ekran)
    pygame.draw.circle(screen, ball, (ballx, bally), radius)
    pygame.display.flip()



