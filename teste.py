import pygame
from pygame import Surface, Rect

W_WIDTH = 576
W_HEIGHT = 324
# Inicializar o módulo pygame
pygame.init()
print('setup start')
# Criando uma window
window: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

# Carregar imagem e gerar uma superficie
bg_surf = pygame.image.load('./asset/bg.png').convert_alpha()
player1_surf = pygame.image.load('./asset/player1.png').convert_alpha()

# Obter o retangulo da superficie
bg_rect: Rect = bg_surf.get_rect(left=0, top=0)
player1_rect: Rect = player1_surf.get_rect(left=100, top=100)

# Desenhar na janela (window)
window.blit(source=bg_surf, dest=(bg_rect))
window.blit(source=player1_surf, dest=(player1_rect))
# Atualizar a janela
pygame.display.flip()

# Colocar um relogio no jogo
clock = pygame.time.Clock()

# Carregar som e deixar ela tocando

pygame.mixer_music.load('./asset/music1.wav')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.1)

print('setup end')
print('loop start')
while True:
    clock.tick(60)  # Esse loop esta acontecendo 30x por segundo
    # print(f'{clock.get_fps() :.0f}') # Printar o FPS
    window.blit(source=bg_surf, dest=(bg_rect))
    window.blit(source=player1_surf, dest=(player1_rect))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('loop end')
            pygame.quit()
            quit()

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        player1_rect.centery += 1
    if pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1
    if pressed_key[pygame.K_d]:
        player1_rect.centerx += 1
