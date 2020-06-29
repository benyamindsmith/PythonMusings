from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from random import randint

#Load Sounds

#Choose appropriate path
boop = SoundLoader.load("C:\\Users\\Smith\\PycharmProjects\\Kivy Tutorial\\Boop.mp3")
ehhh = SoundLoader.load("C:\\Users\\Smith\\PycharmProjects\\Kivy Tutorial\\Ehhh.mp3")
bounce = SoundLoader.load("C:\\Users\\Smith\\PycharmProjects\\Kivy Tutorial\\ping-pong-ball-single-bounce-sound-effect-34008790.mp3")
win =SoundLoader.load("C:\\Users\\Smith\\PycharmProjects\\Kivy Tutorial\\Win.wav")
music = SoundLoader.load("C:\\Users\\Smith\\PycharmProjects\\Kivy Tutorial\\Music.mp3")

class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1
            boop.play()
class Opponent(Widget):
    score = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1
            boop.play()

    def move(self):
            self.pos = Vector(*self.velocity) + self.pos



class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Latest Position = Current Velocity + Current Position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos



# Update- Moving the ball by calling the move function
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(6, 0).rotate(randint(0, 360))

    def opp_move(self):
        self.player2.velocity = Vector(3, 0).rotate(90)


    def update(self, dt):
        self.ball.move()
        self.player2.move()

        # Bounce off top and bottom

        if (self.ball.y < 0) or (self.ball.y > self.height - 50):
            self.ball.velocity_y *= -1
            bounce.play()
        # Bounce off left and right, increase player scores

        if (self.ball.x < 0) or (self.ball.x > self.width - 50):

            if (self.ball.x > self.width - 50):
                self.ball.velocity_x *= -1
                self.player1.score += 1
                win.play()


            if (self.ball.x < self.width - 50):
                self.ball.velocity_x *= -1
                self.player2.score += 1
                ehhh.play()

        #Keep opponent's paddle on screen

        if (self.ball.y < 0) or (self.ball.y > self.height-50) or (self.player2.y < 0) or (self.player2.y > self.height-50):
            self.player2.velocity_y *= -1


        # Contact with paddles

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

    def on_touch_move(self, touch):
        if touch.x < self.width / 1 / 4:
            self.player1.center_y = touch.y


class PongApp(App):
    def build(self):

        music.play()

        game = PongGame()
        game.serve_ball()
        game.opp_move()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


PongApp().run()
