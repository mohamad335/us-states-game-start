from turtle import *
import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
shape = "blank_states_img.gif"
screen.addshape(shape)
turtle.shape(shape)
data = pandas.read_csv("50_states.csv")
states_name = data["state"].to_list()
screen.tracer(0)
number_of_states = 50
count = 0
tim = Turtle()
tim.color("black")
tim.hideturtle()
tim.penup()
game_on = True
guess = screen.textinput("Guess a State", "What's another State's name?").title()
while game_on:
    if guess == "exit" or count == number_of_states:
        game_on = False
    for i in states_name:
        new_data = pandas.DataFrame(states_name)
        new_data.to_csv("missing_states")
        if i == guess:
            count += 1
            screen.update()
            location = data[data.state == i]
            x_location = location.x
            y_location = location.y
            tim.goto(int(x_location), int(y_location))
            tim.write(i)
            states_name.remove(i)
    guess = screen.textinput(f"{count}/{number_of_states} states correct", "what's another state's name?").title()
screen.mainloop()

