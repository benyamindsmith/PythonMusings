from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Ellipse, Color, Line
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import random

# Music- Adjust for your directory

music = SoundLoader.load("C:\\Users\\Smith\\PycharmProjects\\PaintApp\\Relaxation Music.mp3")

# RGBA= Red, Green, Blue, Transparency

Window.clearcolor = (1, 1, 1, 1)


class PaintWindow(Widget):

    def on_touch_down(self, touch):
        colorR = random.randint(0, 255)
        colorG = random.randint(0, 255)
        colorB = random.randint(0, 255)
        self.canvas.add(Color(rgb=(colorR / 255.0, colorG / 255.0, colorB / 255.0, 1)))
        d = 30

        self.canvas.add(Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d)))

        touch.ud['line'] = Line(points=(touch.x, touch.y), length=30, width=30)

        self.canvas.add(touch.ud['line'])

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


# Root Window = Paint Window + Button

class PaintApp(App):

    #Deal with music

    def check_sound(self, dt=None):
        music.play()

    def build(self):
        music.play()
        Clock.schedule_interval(self.check_sound, 1)
        rootWindow = Widget()
        self.painter = PaintWindow()
        clearButton = Button(text='Erase All')
        clearButton.bind(on_release=self.clear_canvas)
        rootWindow.add_widget(self.painter)
        rootWindow.add_widget(clearButton)
        return rootWindow

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


PaintApp().run()
