import kivy
kivy.require('1.9.1')

from kivy.graphics import (
        Color,
        Ellipse,
        Rectangle
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

class ScorePanel(FloatLayout):
    def __init__(self):
        super(ScorePanel, self).__init__(size_hint=(1, 0.1), width=WINDOW_WIDTH, height=WINDOW_HEIGHT*0.1)
        with self.canvas:
            Color(0.5, 0, 0.5)
            self.rect = Rectangle(size=(self.width, self.height), pos=self.pos)
            self.add_widget(Label(text="High Score"))

class GamePanel(FloatLayout):
    def __init__(self, notes):
        super(GamePanel, self).__init__(size_hint=(1, 0.8), width=WINDOW_WIDTH, height=WINDOW_HEIGHT*0.8)
        curr_x = 0
        width = self.width / len(notes)
        with self.canvas:
            for note in notes:
                self.add_widget(GraphicalNote(note, curr_x, width))
                curr_x = curr_x + width

class GraphicalNote(BoxLayout):
    def __init__(self, note, pixel_offset, width):
        super(GraphicalNote, self).__init__()
        self.pos = (pixel_offset, 40)
        with self.canvas:
            Color(0.5, 0, 0)
            self.ellipse = Ellipse(size=(width, width), pos=self.pos)

