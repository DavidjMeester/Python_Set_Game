
import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

selected1 = False   
while running:
    # poll for events
    screen.fill((32, 111, 86))

    plaatje1 = pygame.image.load("kaarten/redovalshaded2.gif")
    
    plaatje1_rect = pygame.Rect(100,100,100,200)
    screen.blit(plaatje1, (100,100))
    plaatje2 = pygame.image.load("kaarten/greenovalshaded3.gif")
    screen.blit(plaatje2, (220, 100))
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if plaatje1_rect.collidepoint(event.pos):
                selected1 = not selected1
                
    if selected1:
        pygame.draw.rect(screen, (255, 0, 0), plaatje1_rect, 4)
      
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()