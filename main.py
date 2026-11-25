
import pygame # Importa a biblioteca

pygame.init() # Inicializa o Pygame

personagem = pygame.image.load("imagens/personagem.png")
personagem = pygame.transform.scale(personagem, (100, 150))

# Carrega a spritesheet
spritesheet = pygame.image.load("imagens/spritesheet.png")

# Coordenadas dos seis quadros da corrida 
quadros_corrida = [
    pygame.Rect(698, 92, 139, 200),
    pygame.Rect(812, 93, 161, 200),
    pygame.Rect(962, 93, 145, 199),
    pygame.Rect(1114, 92, 134, 202),
    pygame.Rect(1229, 97, 151, 197),
    pygame.Rect(1356, 92, 156, 203)
]

# Lista que armazenará os quadros recortados 
animacao_corrida = []

for area in quadros_corrida:
    quadro = spritesheet.subsurface(area)
    animacao_corrida.append(quadro)

# Salva cada quadro para conferência
for i, quadro in enumerate(animacao_corrida):
    pygame.image.save(quadro, f"imagens/corrida_{i}.png")

# Redimensiona os quadros da animação 
for i in range(len(animacao_corrida)):
    animacao_corrida[i] = pygame.transform.scale(
        animacao_corrida[i], (100, 150)
    )

# Controle da animação
indice_animacao = 0
tempo_animacao = 0
velociade_animacao = 0.12

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

    # Verifica se o personagem está se movimentando 
    esta_correndo = False

    if teclas[pygame.K_LEFT]:
        x -= velocidade * delta_tempo
        esta_correndo = True

    if teclas[pygame.K_RIGHT]:
        x += velocidade * delta_tempo
        esta_correndo = True

    # Atualiza a animação de corrida 
    if esta_correndo:
        tempo_animacao += delta_tempo

        if tempo_animacao >= velociade_animacao:
            indice_animacao += 1

            if indice_animacao >= len(animacao_corrida):
                indice_animacao = 0 

        tempo_animacao = 0 

    else: 
        indice_animacao = 0 
        tempo_animacao = 0

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
    # Escolhe o quadro que será exibido 
    if esta_correndo:
        imagem_atual = animacao_corrida[indice_animacao]
    else:
        imagem_atual = personagem

    # Desenha o personagem 
    tela.blit(imagem_atual, (x,y))

    pygame.display.flip()

pygame.quit()
