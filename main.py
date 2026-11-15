
import pygame # Importa a biblioteca

pygame.init() # Inicializa o Pygame

personagem = pygame.image.load("imagens/personagem.png")
personagem = pygame.transform.scale(personagem, (100, 150))

LARGURA = 800 # Definem o tamanho da janela
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA)) # Cria a janela
pygame.display.set_caption("Abacaxi Adventure") # Define o título

rodando = True # Mantém o jogo funcionando

x = 100
y = 200
velocidade = 250 
velocidade_y = 0 
gravidade = 1200

CHAO_Y = 500

relogio = pygame.time.Clock()

forca_pulo = -550
no_chao = False

while rodando:
    # Controla a velocidade de atualização do jogo
    delta_tempo = relogio.tick(60) / 1000

    # Verifica os eventos da janela
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Verifica as teclas pressionadas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        x -= velocidade * delta_tempo

    if teclas[pygame.K_RIGHT]:
        x += velocidade * delta_tempo

    if teclas[pygame.K_SPACE] and no_chao:
        velocidade_y = forca_pulo
        no_chao = False

        # Impede o personagem de sair da tela
    if x < 0:
        x = 0

    if x > LARGURA - personagem.get_width():
        x = LARGURA - personagem.get_width()

        # Aplica a gravidade
    velocidade_y += gravidade * delta_tempo
    y += velocidade_y * delta_tempo

    # Verifica se chegou ao chão
    if y + personagem.get_height() >= CHAO_Y:
        y = CHAO_Y - personagem.get_height()
        velocidade_y = 0
        no_chao = True 
    else: 
        no_chao = False

    # Desenha o cenário e o personagem
    tela.fill((135, 206, 235))
    pygame.draw.rect(tela, (70, 160, 70), (0, CHAO_Y, LARGURA, ALTURA - CHAO_Y))
    tela.blit(personagem, (x, y))

    pygame.display.flip()

pygame.quit()
