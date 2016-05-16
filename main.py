import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.graphics import (
        Color,
        Ellipse,
        Rectangle
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

class Level:

    def __init__(self, file, score, title):
        self.file = file
        self.score = score
        self.title = title

class Score:
    """
    'Score' refers to the music notes on a staff. This class defines the note positions for a piece.
    """
    def __init__(self):
        self.beats_per_measure = 4    # Top number of meter.
        self.beat_value = 4            # Bottom number of meter.
        self.tempo = 120            # Beats per minute.
        self.notes = []                # All notations on the staff.


class GraphicalNote(BoxLayout):
    def __init__(self, note, pixel_offset, width):
        super(GraphicalNote, self).__init__()
        self.pos = (pixel_offset, 40)
        with self.canvas:
            Color(0.5, 0, 0)
            self.ellipse = Ellipse(size=(width, width), pos=self.pos)

class HighScore(App):
    """
    The main game class
    """
    def __init__(self, level):
        super(HighScore, self).__init__()
        self.current_level = level

    def build(self):
        layout = FloatLayout()
        notes = self.current_level.score.notes
        self.width = 800
        curr_x = 0
        width = self.width / len(notes)
        for note in notes:
            layout.add_widget(GraphicalNote(note, curr_x, width))
            curr_x = curr_x + width
        return layout


def test_level():
    ode_to_joy = Score()
    melody = []
    melody.append(('B5', 1))
    melody.append(('B5', 1))
    melody.append(('C5', 1))
    melody.append(('D5', 1))
    melody.append(('D5', 1))
    melody.append(('C5', 1))
    melody.append(('B5', 1))
    melody.append(('A5', 1))
    melody.append(('G5', 1))
    melody.append(('G5', 1))
    melody.append(('A5', 1))
    melody.append(('B5', 1))
    melody.append(('B5', 1.5))
    melody.append(('A5', .5))
    melody.append(('A5', 2))
    ode_to_joy.notes = melody
    level1 = Level('/mp3s/odetojoy.mp3', ode_to_joy, "Ode to Joy")
    return level1


if __name__ == '__main__':
    # make it go stuff
    app = HighScore(test_level())
    app.run()
