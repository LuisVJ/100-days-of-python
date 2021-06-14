import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")

t = turtle.Turtle()
t.hideturtle()
t.penup()

correct = []
correct_n = 0
while True:
    # prompt
    answer_state = screen.textinput(title= f"{correct_n}/50 States Correct",
                    prompt="What's another state's name?").title()

    if answer_state in data.state.values:
        # Check if already answered that state
        if answer_state in correct:
            continue
        correct.append(answer_state)
        correct_n = len(correct)
        # get position
        position = data[data.state == answer_state]
        t.goto(position.x.values[0], position.y.values[0])
        t.write(answer_state, align="center")

    if correct == 50 or answer_state == "End":
        break

turtle.mainloop()