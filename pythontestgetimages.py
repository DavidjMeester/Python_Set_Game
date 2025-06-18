import pygame


pygame.init()


screen = pygame.display.set_mode((600, 320))
pygame.display.set_caption("Set")

clock = pygame.time.Clock()

#32 is font-grootte
font = pygame.font.SysFont(None, 32)

#Get text, antialiasing = True, colors in rgb code
text_surface = font.render("Hier moeten plaatjes", True, (0, 0, 255))  # Blue text

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((0, 0, 0))

    #Call text on screen
    screen.blit(text_surface, (50, 100))
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
