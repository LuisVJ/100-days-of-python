from turtle import Turtle


FONT = ("Courier", 16, "normal")
POSITION = (-290, 260)


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)