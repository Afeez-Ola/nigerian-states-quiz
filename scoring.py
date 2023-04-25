from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.state_len = 36
        self.result = f"0/{self.state_len} states correct"
        self.color("black")

    def update_score(self):
        self.result = f"{int(self.result.split('/')[0]) + 1}/{self.state_len}  correct"
        return self.result

    def score_board(self):
        return self.result

    def final_score(self):
        score_turtle = Turtle()
        score_turtle.hideturtle()
        score_turtle.penup()
        score_turtle.write(self.result, align="center", font=("Calibri", 24, "bold"))
