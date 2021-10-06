####################
# Import Dictionary#
####################

from time import time
from timeit import default_timer
from arcade import Window, View, SpriteList, set_viewport
from arcade import check_for_collision, start_render, get_sprites_at_point, run, draw_text, color
import Terminal_markdown as tmd_T
from screeninfo import get_monitors
import Sprites_Imagens as SpIm
import Variaveis as VaVe
from Funções import DEFs_Game as def_GM
from Funções import DEFs_Dino as def_D
from Classes import ClassGameplay as cl_G
from random import randint
