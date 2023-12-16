from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.image import Image

Window.fullscreen = "auto"


class BoardLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gl = GameLogic()

        for i in range(1, 43):
            button = Button(pos_hint={"center_x": 1, "center_y": 1})

            button.ids["text"] = f"{i}"
            button.bind(on_press=self.gl.move)
            self.add_widget(button)


class GameLogic(Widget):
    def move(self, button):
        coords = button.pos
        print(coords)
        img = Image(source="./Knight.png")
        img.pos = coords

        self.add_widget(img)


class TroopCapture(App):
    pass


TroopCapture().run()
