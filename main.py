import pygame
from random import randint
from enemy import Enemy

pygame.init()
from game import game_over

WIDTH, HEIGHT = 417, 626

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bang")
font = pygame.font.Font('freesansbold.ttf', 32)


player = {
    "x": WIDTH/2 - 42,
    "y": HEIGHT-HEIGHT/5,
    "speed": 2,
    "image": "assets/spaceship.png"
}

enemy = {
    "x": 0,
    "y": 0,
    "speed": 2,
    "image": "assets/asteroid.png"
}

enemies = []


player_image = pygame.image.load(player["image"]).convert_alpha()
background = pygame.image.load("assets/background.png")
enemy_image = pygame.image.load(enemy["image"]).convert_alpha()

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

    # Add enemies
    if randint(1, 60) == 27:
        enemies.append(Enemy(randint(20,400), -100))

    # Enemy Movement
    for e in enemies:
        e.y += e.speed
        if e.y > 626:
            enemies.remove(e)
            del e
        elif e.y > player["y"] and e.y < player["y"]+101 and e.x > player["x"] and e.x < player["x"]+84:
            game_over(font, WIDTH, HEIGHT, screen)

    # Draw
    screen.blit(background, (0,0))
    screen.blit(player_image, (player["x"], player["y"]))
    for e in enemies:
        screen.blit(enemy_image, (e.x, e.y))
    pygame.display.flip()

# pygame.quit()
