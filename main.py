import pygame

pygame.init()

WIDTH, HEIGHT = 417, 626

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bang")
background = pygame.image.load("assets/background.png")

player = {
    "x": WIDTH/2 - 42,
    "y": HEIGHT-HEIGHT/5,
    "speed": 2,
    "image": "assets/spaceship.png"
}

player_image = pygame.image.load(player["image"]).convert_alpha()

running = True
while running:
    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player["x"] -= player["speed"]
    if keys[pygame.K_RIGHT]:
        player["x"] += player["speed"]

    if player["x"] < 0:
        player["x"] = 0
    elif player["x"] > WIDTH - 84:
        player["x"] = WIDTH - 84

    # Draw
    screen.blit(background, (0,0))
    screen.blit(player_image, (player["x"], player["y"]))
    pygame.display.flip()

pygame.quit()