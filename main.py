from turtle import Turtle,Screen

jack=Turtle()
screen=Screen()

def move_forward():
    jack.forward(100)

screen.listen()
screen.onkey(key="space",fun=move_forward)


screen.exitonclick()