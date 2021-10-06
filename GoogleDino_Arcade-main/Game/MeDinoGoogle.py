##########################
# Python game from arcade#
##########################

import Imports as I

##################
# Dictator Window#
##################

try:
    init = I.time()


    class Janelas(I.Window):  # Creates the main window
        def __init__(self, altura, largura, titulo, statistics_fps: bool = False):
            """ Initializer """
            super().__init__(altura, largura, titulo, statistics_fps)
            self.set_location(I.get_monitors()[0].width - I.VaVe.LARGURA - 1, 0)
            self.statistics_fps: bool = statistics_fps

            # Time for on_update
            self.processing_time: float = 0
            # Time for on_draw
            self.draw_time: float = 0
            # Variables used to calculate frames per second
            self.frame_count: float = 0
            self.fps_start_timer = None
            self.fps = None

        def on_draw(self):
            """ Draw everything """

            if self.statistics_fps:
                # Start timing how long this takes
                start_time = I.default_timer()

                fps_calculation_freq: int = 60
                # Once every 60 frames, calculate our FPS
                if self.frame_count % fps_calculation_freq == 0:
                    # Do we have a start time?
                    if self.fps_start_timer is not None:
                        # Calculate FPS
                        total_time = I.default_timer() - self.fps_start_timer
                        self.fps = fps_calculation_freq / total_time
                    # Reset the timer
                    self.fps_start_timer = I.default_timer()
                # Add one to our frame count
                self.frame_count += 1

                # Display timings
                output = f"Processing time: {self.processing_time:.2f}"
                I.draw_text(output, I.VaVe.LARGURA - 320, I.VaVe.ALTURA - 25, I.color.BLACK, 18)

                output = f"Drawing time: {self.draw_time:.2f}"
                I.draw_text(output, I.VaVe.LARGURA - 320, I.VaVe.ALTURA - 50, I.color.BLACK, 18)
                if self.fps is not None:
                    output = f"FPS: {self.fps:.0f}"
                I.draw_text(output, I.VaVe.LARGURA - 320, I.VaVe.ALTURA - 75, I.color.BLACK, 18)
                # Stop the draw timer, and calculate total on_draw time.
                self.draw_time = I.default_timer() - start_time

        def on_key_press(self, symbol: int, modifiers: int):
            """ Enables and disables the fps status """
            if symbol == 188978561024 and not self.statistics_fps:
                self.statistics_fps = True
            elif not symbol != 188978561024 and self.statistics_fps:
                self.statistics_fps = False

    ############
    # Menu body#
    ############
    class Menu(I.View):
        def __init__(self):
            super().__init__()
            self.Cena_Inicial, self.MenuInicial_Dino, self.MenuButton_Play \
                = I.SpriteList(), I.SpriteList(), I.SpriteList()

            self.Menu_InicialSprites: tuple = (I.SpIm.CorDeFundo, I.SpIm.Menu_chao, I.SpIm.Menu_ButtonPlayList[0])
            self.Text_Hours = None
            self.BarraAnimV: int = 132
            self.BarraAnimA: int = 0
            self.TextAnim: int = 235
            self.Button_Play_Menu_Position: int = 275

            self.Animacao_Play: str = 'None'

            self.valor_mouse_Ebutton: int = 1

            # Add sprites to the scene
            self.MenuButton_Play.append(I.SpIm.Menu_ButtonPlayList[0])
            for index, item in enumerate(self.Menu_InicialSprites):
                self.Cena_Inicial.append(self.Menu_InicialSprites[index])
            self.MenuInicial_Dino.append(I.SpIm.Menu_Dino)

        """ View to show instructions """

        def on_show(self):
            # Reset the viewport, necessary if we have a scrolling game and we need
            # to reset the viewport back to the start so we can see what we draw.
            I.set_viewport(0, I.VaVe.Size_1000550[0], 0, I.VaVe.Size_1000550[1])

        def on_draw(self):
            """ Draw this view """
            I.start_render()
            # Draw Sprites
            self.Cena_Inicial.draw()
            self.MenuInicial_Dino.draw()

            self.Text_Hours = I.def_GM.text_screen(I.VaVe.Hora_Atual, I.VaVe.LARGURA - 850 - self.TextAnim,
                                                   I.VaVe.ALTURA + 585,
                                                   self.BarraAnimA)

        def on_mouse_press(self, _x, _y, _button, _modifiers):
            """ Take the position of the card with the mouse """
            self.Button_Play_Menu_Position = I.get_sprites_at_point((_x, _y), self.MenuButton_Play)

            # Checks: Button press
            if _button == self.valor_mouse_Ebutton:
                I.def_GM.button_play_game(self.Button_Play_Menu_Position, self.Cena_Inicial,
                                          I.SpIm.Menu_ButtonPlayList[0],
                                          I.SpIm.Menu_ButtonPlayList[2])

        def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
            """ calls the play button animation """
            if button == self.valor_mouse_Ebutton:
                I.def_GM.button_play_game(self.Button_Play_Menu_Position, self.Cena_Inicial,
                                          I.SpIm.Menu_ButtonPlayList[2],
                                          I.SpIm.Menu_ButtonPlayList[0])

                self.MenuButton_Play.append(I.SpIm.Menu_ButtonPlayList[2])
                if len(self.Button_Play_Menu_Position) > 0:
                    self.Animacao_Play: str = 'PLayGame'

        def on_update(self, delta_time: float):

            """ If the user presses the mouse button, start the game. """
            if self.Animacao_Play == 'PLayGame':
                # Animation of exiting the screen
                I.def_GM.animation_menu_start(self.Button_Play_Menu_Position, self.MenuButton_Play, self.Animacao_Play,
                                              -400 * delta_time)

                # Reverses the animation of the hour
                if not self.Text_Hours <= 2.5:  # For the animation so that there is no error
                    self.TextAnim += 400 * delta_time
                    self.BarraAnimA -= 4

                # Confirm and change scene
                if I.SpIm.Menu_ButtonPlayList[0].position[0] <= 75:
                    game_view = Gameplay()
                    game_view.setup()
                    self.window.show_view(game_view)

            # Shows the time
            if not self.BarraAnimA >= self.BarraAnimV and not self.Animacao_Play == 'PlayGame':
                """ Time entry animation """
                self.BarraAnimA += 110 * delta_time
                self.TextAnim -= 174.5 * delta_time

    ############
    # Game mode#
    ############
    class Gameplay(I.View):
        def __init__(self):
            super().__init__()
            """ Set Properties """
            self.delta_time = None

            self.Background = None
            self.Obstacles = None
            self.sprite_restart = None

            self.Menu_InicialSprites = None
            self.Kakitos_sprites = None

            self.Dino = I.cl_G.Dino()
            self.Dino_died = None

            self.Scale_Dino = None
            self.Progscale_Dino = None

            self.PosJanela_Dino = None

            self.floor2_xTF = None
            self.Vel_background, self.up_background = None, None
            self.floor1_x, self.floor2_x = None, None
            self.floor_X, self.floor_X_P = (None, None), (None, None)

            self.spawn = None

            self.kakito_p_origin_pequeno = (None, None)
            self.kakito_p_origin_grande = (None, None)
            self.kakito_p_origin_conjunto = (None, None)

            self.kakito_p_origin = None

            self.kakito_random = (None, None)
            self.kakito_random_sty = None
            self.kakito_random_sprite = None

            self.Button_Play_Menu_Position = None

        def setup(self):
            """ Start Properties """
            self.Background, self.Obstacles, self.sprite_restart = I.SpriteList(), I.SpriteList(), I.SpriteList()

            self.Menu_InicialSprites: tuple = (I.SpIm.CorDeFundo, I.SpIm.Game_chao1, I.SpIm.Game_chao2)
            self.Kakitos_sprites: tuple = (I.SpIm.Kakitos_pequenos, I.SpIm.Kakitos_grandes, I.SpIm.Kakitos_conjunto)

            # Adiciona os sprites na cena
            for index, item in enumerate(self.Menu_InicialSprites):
                self.Background.append(self.Menu_InicialSprites[index])

            self.Dino_died: bool = False

            """ game background settings """
            self.Menu_InicialSprites[2].center_x = 3900
            self.Vel_background: int = 12
            self.up_background: float = 0.0006
            self.floor2_xTF: bool = False
            self.floor_X = (2010, 3900)
            self.floor_X_P = (0, 1)

            """ Characteristics of kakito """
            self.spawn: bool = False

            self.kakito_p_origin_pequeno: tuple = (1600, 87)
            self.kakito_p_origin_grande: tuple = (1700, 94)
            self.kakito_p_origin_conjunto: tuple = (1900, 105)

        def sprite_generation(self):  # Change the kakito sprite and its size

            self.kakito_random: tuple = (I.randint(0, 2), I.randint(0, 5))
            self.kakito_random_sty: int = self.kakito_random[0]
            self.kakito_random_sprite: int = self.kakito_random[1]

            if self.kakito_random_sty >= 0:
                self.kakito_p_origin = self.kakito_p_origin_grande \
                    if self.kakito_random_sty <= 1 else self.kakito_p_origin_pequeno
            elif self.kakito_random_sty == 2:
                self.kakito_p_origin = self.kakito_p_origin_conjunto

        def move_ground_origin(self):
            """ Creates the floor loop """
            if self.Menu_InicialSprites[1].center_x <= -1890: self.floor2_xTF = True

            self.floor1_x, self.floor2_x = self.floor_X[self.floor_X_P[1]] \
                                               if self.Menu_InicialSprites[1].center_x <= -3005 \
                                               else self.Menu_InicialSprites[1].center_x, \
                                           self.floor_X[self.floor_X_P[0]] \
                                               if self.Menu_InicialSprites[2].center_x <= -3005 \
                                               else self.Menu_InicialSprites[2].center_x

            if self.floor2_x <= 492:
                self.floor_X_P = (1, 0)
            elif self.floor1_x <= 492:
                self.floor_X_P = (0, 1)

        def break_dino(self):
            if I.check_for_collision(self.Dino.Dino_Sprite,
                                     self.Kakitos_sprites[self.kakito_random_sty][self.kakito_random_sprite]):
                """ stop game """
                self.Vel_background: int = 0
                self.up_background: int = 0
                self.Dino.Dou_jump = 'None'
                self.Dino_died: bool = True
                # add game over screen
                I.def_GM.game_over(I.SpIm.GameOver, I.SpIm.Restart, self.Background, self.sprite_restart)

        def on_show(self):
            # Reset the viewport, necessary if we have a scrolling game and we need
            # to reset the viewport back to the start so we can see what we draw.
            I.set_viewport(0, I.VaVe.LARGURA - 1, 0, I.VaVe.ALTURA - 1)

        def on_draw(self):
            """ Draw this view """
            I.start_render()

            # Desenha Sprites
            self.Background.draw()
            self.Dino.draw()
            self.Obstacles.draw()

            """ Make the kakito appear and check if it collided with the player """
            if self.Dino.game and not self.spawn:
                self.sprite_generation()

                self.spawn = I.def_GM.spawn_kakito(
                    self.Kakitos_sprites[self.kakito_random_sty][self.kakito_random_sprite],
                    self.Obstacles, self.kakito_p_origin)

            if self.spawn:
                self.break_dino()

        def on_update(self, delta_time: float):
            """ Update screen """
            self.Dino.update_animation()  # Update Player
            if self.spawn:
                self.Obstacles.update_location(self.Kakitos_sprites[self.kakito_random_sty][self.kakito_random_sprite])

            if self.Dino.game:
                """ Move ground """
                self.move_ground_origin()

                self.Vel_background += self.up_background

                # self.move_ground()
                I.def_GM.move_ground(self.Menu_InicialSprites[1], self.Menu_InicialSprites[2], self.Vel_background,
                                     self.floor1_x, self.floor2_x, self.floor2_xTF)

                """ Move the kakito then check if it 
                disappeared from the screen generates
                a new sprite adds removes the old one and returns it to the origin point """

                if self.spawn:
                    I.def_GM.move_kakitos(self.Obstacles, -self.Vel_background)

                    if self.Kakitos_sprites[self.kakito_random_sty][self.kakito_random_sprite].center_x <= -100:
                        self.sprite_generation()

                        I.def_GM.spawn_kakito(self.Kakitos_sprites[self.kakito_random_sty][self.kakito_random_sprite],
                                              self.Obstacles, self.kakito_p_origin)

                        self.Obstacles.remove(self.Obstacles[0])
                        self.Kakitos_sprites[self.kakito_random_sty][self.kakito_random_sprite].center_x = \
                            self.kakito_p_origin[0]

        def on_key_press(self, symbol: int, modifiers: int):

            # Check Space and Jump
            if symbol == 32 and not self.Dino_died: I.def_D.jump(self.Dino)

        def on_mouse_press(self, _x, _y, _button, _modifiers):
            """ Take the position of the card with the mouse """
            if self.Dino_died:
                self.Button_Play_Menu_Position = I.get_sprites_at_point((_x, _y), self.sprite_restart)

                # Checks: Button press
                if _button == 1 and len(self.Button_Play_Menu_Position) > 0:
                    self.Dino.GameOver = True
                    self.setup()


    fim = I.time()
    result = fim - init
    print(f'Valor da inicialização: {result}')

finally:
    I.tmd_T.M.text_md(I.tmd_T.M(), '''
    # - **Initializing Game** [Markdown reader originally made by @AXGKI and modified for my project by @ClasRCDM :)]
    ''')


####################
# Brain of the Game#
####################

def main():
    """ Main method """

    janela_principal = Janelas(I.VaVe.LARGURA, I.VaVe.ALTURA, I.VaVe.TITULO)
    start_view = Menu()
    janela_principal.show_view(start_view)
    I.run()


if __name__ == "__main__":
    main()
