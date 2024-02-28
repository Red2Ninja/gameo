'''from turtle import Turtle,Screen
class Zomn:
    def __init__(self):
        self.create_zomn()

    def create_zomn(self):
        screen = Screen()
        screen.register_shape("zombie.gif")
        banu = Turtle()
        banu.shape("zombie.gif")
        banu.penup()
        banu.speed("slow")

    def move(self):
        self.backward(50)


    def move_forward(self):
        self.setheading(90)
        self.forward(10)

    def move_backward(self):
        self.setheading(270)
        self.forward(10)

    def move_right(self):
        self.setheading(0)
        self.forward(10)

    def move_left(self):
        self.setheading(180)
        self.forward(10)'''


'''from turtle import Turtle, Screen

class Zomn:
    def __init__(self):
        self.banu = Turtle()
        self.create_zomn()

    def create_zomn(self):
        screen = Screen()
        screen.register_shape("zombie.gif")
        self.banu.shape("zombie.gif")
        self.banu.penup()
        self.banu.speed("slow")

    def move(self):
        self.banu.backward(50)

    def move_forward(self):
        self.banu.setheading(90)
        self.banu.forward(10)

    def move_backward(self):
        self.banu.setheading(270)
        self.banu.forward(10)

    def move_right(self):
        self.banu.setheading(0)
        self.banu.forward(10)

    def move_left(self):
        self.banu.setheading(180)
        self.banu.forward(10)'''


#current
from turtle import Turtle, Screen

class Zomn:
    def __init__(self):
        self.banu = Turtle()
        self.zombies = []
        self.create_zomn()

    def create_zomn(self):
        screen = Screen()
        screen.register_shape("zombie.gif")
        self.banu.shape("zombie.gif")
        self.banu.penup()
        self.banu.speed("slow")
        self.zombies.append(self.banu)

    def add_zomn(self):
        screen = Screen()
        screen.register_shape("zombie.gif")
        self.banu.shape("zombie.gif")
        self.banu.penup()
        self


    def move(self):
        for zombie in self.zombies:
            zombie.backward(50)

    def move_forward(self):
        for zombie in self.zombies:
            zombie.setheading(90)
            zombie.forward(10)

    def move_backward(self):
        for zombie in self.zombies:
            zombie.setheading(270)
            zombie.forward(10)

    def move_right(self):
        for zombie in self.zombies:
            zombie.setheading(0)
            zombie.forward(10)

    def move_left(self):
        for zombie in self.zombies:
            zombie.setheading(180)
            zombie.forward(10)

    def add_zombie(self):
        new_zombie = Turtle()
        new_zombie.shape("zombie.gif")
        new_zombie.penup()
        new_zombie.speed("fastest")
        self.zombies.append(new_zombie)

    def check_collision(self, player):
        for zombie in self.zombies:
            if zombie.distance(player) < 25:
                self.add_zombie()
                player.refresh()
                return True
        return False


