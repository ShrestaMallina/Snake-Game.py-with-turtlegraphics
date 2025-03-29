
from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time



screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


screen.tracer(0)
Snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=Snake.up,key="Up")
screen.onkey(fun=Snake.down,key="Down")
screen.onkey(fun=Snake.left,key="Left")
screen.onkey(fun=Snake.right,key="Right")






game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    Snake.move()
    #detection with food
    if Snake.head.distance(food)<15:
       food.refresh()
       Snake.extend()
       scoreboard.score_inc()
    #detection collision with wall
    if Snake.head.xcor()>280 or Snake.head.xcor()<-280 or Snake.head.ycor()>280 or Snake.head.ycor()<-280:
       game_is_on = False
       scoreboard.game_over()

    #detection colision with tail
    for segment in Snake.segments[1:]:
        # if segment==Snake.head:
        #     pass

        if Snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()