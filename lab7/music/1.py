import pygame
import os

pygame.init()

screen = pygame.display.set_mode((200, 200))
font = pygame.font.Font(None, 40)

musics = ["jony.mp3", "jony2.mp3"]
musindex = 0

pygame.mixer.music.load(musics[musindex])
pygame.mixer.music.play()

running =  True
while running:
   
   screen.fill((255, 255, 255))
   mustext = font.render(os.path.basename(musics[musindex]), True, (0, 0, 0))
   screen.blit(mustext, (10, 10))

   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE: 
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                  pygame.mixer.music.unpause()
            elif event.key == pygame.K_n:  
                musindex = (musindex + 1) % len(musics)
                pygame.mixer.music.load(musics[musindex])
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:  
                musindex = (musindex - 1) % len(musics)
                pygame.mixer.music.load(musics[musindex])
                pygame.mixer.music.play()

   pygame.display.flip()
