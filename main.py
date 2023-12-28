from turtle import Turtle, Screen
import random

is_raceon=False
screen=Screen()
screen.setup(400,400)
bet=screen.textinput(title="Make your bet for the best turtle:",prompt="Which turtle win the race?")
colors=["red","orange","yellow","green","blue","purple"]
y_position=[-70,-40,-10,20,50,80]

all_turtles=[]
for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-180,y=y_position[turtle_index])
    all_turtles.append(new_turtle)
if bet:
    is_raceon=True


while is_raceon:
    for turtle in all_turtles:
        if turtle.xcor()>180:
            is_raceon=False
            winning_color=turtle.pencolor()
            if winning_color == bet :
                print(f"You have win .The {winning_color} is the turtle winner of the race.")
            else:
                print(f"You have lost .The {winning_color} is the turtle winner of the race.")


        random_distance=random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()