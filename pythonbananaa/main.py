
#current
from turtle import Screen
from zomn1 import Zomn
from player import Player
from followers import Followers
import time

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("green")
screen.title("Conga, Conga, Conga")

zomn1 = Zomn()
player = Player()
followers = Followers()

screen.listen()
screen.onkey(zomn1.move_forward, "Down")
screen.onkey(zomn1.move_backward, "Up")
screen.onkey(zomn1.move_right, "Left")
screen.onkey(zomn1.move_left, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    zomn1.move()

    #meeting new friends
    if zomn1.banu.distance(player) < 50:
        print("nom nom nom")
        player.refresh()
        followers.increase_score()
    if zomn1.check_collision(player):
        followers.increase_score()

    #collision with wall
    if (
            zomn1.banu.xcor() > screen.window_width() / 2
            or zomn1.banu.xcor() < -screen.window_width() / 2
            or zomn1.banu.ycor() > screen.window_height() / 2
            or zomn1.banu.ycor() < -screen.window_height() / 2
    ):
        game_is_on = False
        followers.game_over()



screen.exitonclick()




