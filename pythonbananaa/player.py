from turtle import Turtle,Screen
import random
class Player(Turtle):
    def __init__(self):
        super().__init__()

        screen = Screen()
        screen.register_shape("zombie.gif")

        #banu = Turtle()
        self.shape("zombie.gif")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)

