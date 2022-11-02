from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('black')
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.penup()
        self.goto(-230, 270)
        self.write(f'Level: {self.score}', align='center', font=FONT)

    def get_point(self):
        self.clear()
        self.score += 1
        self.update_score_board()

    def end_game(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)

