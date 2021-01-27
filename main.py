from turtle import Turtle, Screen

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

def up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
