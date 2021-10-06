##################
# Sprites/Texture#
##################

from arcade import load_texture, Sprite
from Variaveis import Size_1000550 as TL

# Get Sprites/Texture for Menu
Tela_Iniciar = load_texture('PastSprites_Imagens/Menu_Iniciar.png')  # Menu
Menu_Dino = Sprite('PastSprites_Imagens/Dino_Menu.png', center_x=TL[0], center_y=TL[1])  # Dino
Menu_chao = Sprite('PastSprites_Imagens/Chão_Menu.png', center_x=TL[0], center_y=TL[1])  # menu floor

# Sprites Buttons play
Menu_ButtonPlayList = [Sprite('PastSprites_Imagens/Botão_Play.png', center_x=TL[0], center_y=TL[1]),
                       Sprite('PastSprites_Imagens/Botão_Play_Cima.png', center_x=TL[0], center_y=TL[1]),
                       Sprite('PastSprites_Imagens/Botão_Play_Click.png', center_x=TL[0], center_y=TL[1])]

# Get Sprites for Game
CorDeFundo = Sprite('PastSprites_Imagens/CorDeFundo.png', center_x=TL[0], center_y=TL[1])  # Background color
Game_chao1 = Sprite('PastSprites_Imagens/Game_chao.png', center_x=TL[0], center_y=TL[1])  # game floor 1
Game_chao2 = Sprite('PastSprites_Imagens/Game_chao.png', center_x=TL[0], center_y=TL[1])  # game floor 2

GameOver = Sprite('PastSprites_Imagens/GameOver.png', center_x=TL[0], center_y=TL[1])
Restart = Sprite('PastSprites_Imagens/Recomeçar.png', center_x=TL[0], center_y=TL[1])

# Kakitos
Kakitos_pequenos = [Sprite('PastSprites_Imagens/Kakito_pequeno1.png', center_x=TL[0], center_y=TL[1], scale=2,
                                  hit_box_algorithm='Simple'),
                    Sprite('PastSprites_Imagens/Kakito_pequeno2.png', center_x=TL[0], center_y=TL[1], scale=2,
                                  hit_box_algorithm='Simple'),
                    Sprite('PastSprites_Imagens/Kakito_pequeno3.png', center_x=TL[0], center_y=TL[1], scale=2,
                                  hit_box_algorithm='Simple'),
                    Sprite('PastSprites_Imagens/Kakito_pequeno4.png', center_x=TL[0], center_y=TL[1], scale=2,
                                  hit_box_algorithm='Simple'),
                    Sprite('PastSprites_Imagens/Kakito_pequeno5.png', center_x=TL[0], center_y=TL[1], scale=2,
                                  hit_box_algorithm='Simple'),
                    Sprite('PastSprites_Imagens/Kakito_pequeno6.png', center_x=TL[0], center_y=TL[1], scale=2,
                                  hit_box_algorithm='Simple')]

Kakitos_grandes = [Sprite('PastSprites_Imagens/Kakito_grande1.png', center_x=TL[0], center_y=TL[1], scale=1.8,
                                 hit_box_algorithm='Simple'),
                   Sprite('PastSprites_Imagens/Kakito_grande2.png', center_x=TL[0], center_y=TL[1], scale=1.8,
                                 hit_box_algorithm='Simple'),
                   Sprite('PastSprites_Imagens/Kakito_grande3.png', center_x=TL[0], center_y=TL[1], scale=1.8,
                                 hit_box_algorithm='Simple'),
                   Sprite('PastSprites_Imagens/Kakito_grande4.png', center_x=TL[0], center_y=TL[1], scale=1.8,
                                 hit_box_algorithm='Simple'),
                   Sprite('PastSprites_Imagens/Kakito_grande5.png', center_x=TL[0], center_y=TL[1], scale=1.8,
                                 hit_box_algorithm='Simple'),
                   Sprite('PastSprites_Imagens/Kakito_grande6.png', center_x=TL[0], center_y=TL[1], scale=1.8,
                                 hit_box_algorithm='Simple')]

Kakitos_conjunto = [Sprite('PastSprites_Imagens/Kakitos_conjunto1.png', center_x=TL[0], center_y=TL[1],
                                  scale=1.35, hit_box_algorithm='Simple'),
                    Sprite('PastSprites_Imagens/Kakitos_conjunto2.png', center_x=TL[0], center_y=TL[1],
                                  scale=1.35, hit_box_algorithm='Simple'),
                    Sprite('PastSprites_Imagens/Kakitos_conjunto3.png', center_x=TL[0], center_y=TL[1],
                                  scale=1.35, hit_box_algorithm='Simple'),
                    Sprite('PastSprites_Imagens/Kakitos_conjunto4.png', center_x=TL[0], center_y=TL[1],
                                  scale=1.35, hit_box_algorithm='Simple'),
                    Sprite('PastSprites_Imagens/Kakitos_conjunto5.png', center_x=TL[0], center_y=TL[1],
                                  scale=1.35, hit_box_algorithm='Simple'),
                    Sprite('PastSprites_Imagens/Kakito_pequenim.png', center_x=TL[0], center_y=TL[1],
                                  scale=2, hit_box_algorithm='Simple')]
