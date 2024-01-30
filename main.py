import pygame
from random import randint
from enemy import Enemy
from bullet import Bullet

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
    "cooldown": 60,
    "image": "assets/spaceship.png"
}

enemies = []
bullets = []


player_image = pygame.image.load(player["image"]).convert_alpha()
background = pygame.image.load("assets/background.png")
enemy_image = pygame.image.load("assets/asteroid.png").convert_alpha()
bullet_image = pygame.image.load("assets/bullet.png").convert_alpha()

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
    if keys[pygame.K_SPACE] and player["cooldown"] == 0:
        player["cooldown"] = 60
        bullets.append(Bullet(player["x"]+38, player["y"]))

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
        if e.y > player["y"] and e.y < player["y"]+40 and e.x > player["x"]+10 and e.x < player["x"]+74:
            game_over(font, WIDTH, HEIGHT, screen)
        collision_response = e.collided_with(bullets)
        if collision_response[0]:
            bullets.pop(collision_response[1])
            enemies.remove(e)

        # remove old enemies
        elif e.y > 626:
            enemies.remove(e)

    # Shooting
    if player["cooldown"] != 0:
        player["cooldown"] -= 1
    for b in bullets:
        b.y -= b.speed
        if b.y < -100:
            bullets.remove(b)

    # Draw
    screen.blit(background, (0,0))
    screen.blit(player_image, (player["x"], player["y"]))
    for e in enemies:
        screen.blit(enemy_image, (e.x, e.y))
    for b in bullets:
        screen.blit(bullet_image, (b.x, b.y))
    pygame.display.flip()

# pygame.quit()
