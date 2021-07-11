import arcade
from constant import Constants

class InstructionView(arcade.View):

    def __init__(self):

        super().__init__()
        self.texture = arcade.load_texture(".jpg")
        arcade.set_viewport(0, Constants.SCREEN_WIDTH - 1, 0, Constants.SCREEN_HEIGHT - 1)

    def on_draw(self):
        
        arcade.start_render()
        self.texture.draw_sized(Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 2,
                                Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)

class GameOverView(arcade.View):

    def __init__(self, archivo_de_imagen):
        
        super().__init__()
        self.texture = arcade.load_texture(archivo_de_imagen)
        Audio().solo_una_vez("GameOver.mp3")

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        # para restablecer la ventana gráfica al inicio para que podamos ver lo que dibujamos.
        arcade.set_viewport(0, Constants.SCREEN_WIDTH, 0, Constants.SCREEN_HEIGHT)
        # dibujar esta vista
        self.texture.draw_sized(Constants.SCREEN_WIDTH/2, Constants.SCREEN_HEIGHT/2, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # Si el usuario presiona el botón del mouse, reinicie el juego
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)


class Ventana_Ganador(arcade.View):
    """ 
    Window when the player wins
    """

    def __init__(self, archivo_de_imagen):
        # Ver para mostrar cuando el juego termine
        super().__init__()
        self.texture = arcade.load_texture(archivo_de_imagen)
        Audio().solo_una_vez("YouWin.mp3")

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        # para restablecer la ventana gráfica al inicio para que podamos ver lo que dibujamos.
        arcade.set_viewport(0, Constants.SCREEN_WIDTH, 0, Constants.SCREEN_HEIGHT)
        # dibujar esta vista
        self.texture.draw_sized(Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 2,
                                Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # Si el usuario presiona el botón del mouse, reinicie el juego
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)