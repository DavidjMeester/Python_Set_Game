import pygame
import os
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# 1. Lees alle .gif bestanden in de map
kaart_pad = "kaarten"
alle_gif_kaarten = [f for f in os.listdir(kaart_pad) if f.endswith(".gif")]

# 2. Kies willekeurig 12 kaarten
gekozen_kaarten = random.sample(alle_gif_kaarten, 12)

# 3. Laad kaarten met posities en selectie-status
kaarten = []
for i, bestandsnaam in enumerate(gekozen_kaarten):
    pad = os.path.join(kaart_pad, bestandsnaam)
    afbeelding = pygame.image.load(pad)
    
    x = 50 + (i % 4) * 150
    y = 50 + (i // 4) * 215
    rect = pygame.Rect(x, y, 100, 200)
    kaarten.append({
        "image": afbeelding,
        "rect": rect,
        "selected": False
    })



# --- Main loop ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for kaart in kaarten:
                if kaart["rect"].collidepoint(event.pos):
                    kaart["selected"] = not kaart["selected"]

    screen.fill((30, 100, 100))

    # Teken alle kaarten
    for kaart in kaarten:
        screen.blit(kaart["image"], kaart["rect"].topleft)
        if kaart["selected"]:
            pygame.draw.rect(screen, (255, 0, 0), kaart["rect"], 4)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
