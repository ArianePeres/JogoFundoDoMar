import pygame

print('setup star')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('setup end')

print('loop start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # fecha janela
            quit()  # encerra a inicialização do pygame
