####################
# Variáveis do jogo#
####################

from datetime import datetime

# Play
PlayGame = False

# Screen
LARGURA: int = 1000
ALTURA: int = 550

TITULO: str = 'GoogleDinoPython[BB_Arcade]'

# Para a cena
Size_1000550 = [LARGURA / 2, ALTURA / 2, LARGURA, ALTURA]

# DO menu
delta_timeMenu: float = 0.0

# Datas
Data_Atual = datetime.now()
Hora_Atual = Data_Atual.strftime('%H:%M:%S')

# Texto e Hora
TexH_At = LARGURA / 2
BaF_At: int = 132
