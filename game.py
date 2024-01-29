import pygame

def game_over(font, width, height, screen):
    game_over = True
    while game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        text = font.render('Game Over', True, (0, 255, 0), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (width // 2, height // 2)
        screen.blit(text, textRect)
        pygame.display.flip()