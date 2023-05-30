import pygame
import random

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

window_width = 800
window_height = 600
window_size = (window_width, window_height)


window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Jogo da Cobrinha")


clock = pygame.time.Clock()


snake_block_size = 20
apple_block_size = 20


snake_speed = 15


font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    message_text = font_style.render(msg, True, color)
    window.blit(message_text, [window_width / 6, window_height / 3])


def game_loop():
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0

    apple_x = round(random.randrange(0, window_width - apple_block_size) / 20.0) * 20.0
    apple_y = round(random.randrange(0, window_height - apple_block_size) / 20.0) * 20.0

    game_over = False
    game_close = False

    while not game_over:

        while game_close:
            window.fill(BLACK)
            message("Você perdeu! Pressione S para sair ou J para jogar novamente", RED)
            pygame.display.update()

   
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_j:
                        game_loop()

    #Track do teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # Atualiza a posição da cobra
        x1 += x1_change
        y1 += y1_change
        window.fill(BLACK)
        pygame.draw.rect(window, GREEN, [apple_x, apple_y, apple_block_size, apple_block_size])
        pygame.draw.rect(window, WHITE, [x1, y1, snake_block_size, snake_block_size])
        pygame.display.update()

        
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, window_width - apple_block_size) / 20.0) * 20.0
            apple_y = round(random.randrange(0, window_height - apple_block_size) / 20.0) * 20.0

        
        clock.tick(snake_speed)

    pygame.quit()
game_loop()
