from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,270)
        self.color("white")

        self.score=0
        with open("../../../../OneDrive/Desktop/data.txt" , "r") as f:
            self.highscore=f.read()
        self.write(f"Your Score: {self.score}   High Score: {self.highscore}", font=('Arial', 20, "normal"),
                   align="center")
        self.hideturtle()
    def updatescores(self):
        self.clear()
        self.write(f"Your Score: {self.score} , High Score: {self.highscore}", font=('Arial', 20, "normal"),align="center")

    def gameover(self):
        self.clear()
        if self.score>int(self.highscore):
            self.highscore=self.score
        with open("../../../../OneDrive/Desktop/data.txt" , "w") as f:
            f.write(f"{self.highscore}")
        self.score=0
        self.pu()
        self.color("white")
        self.write(f"Your Score: {self.score} , High Score: {self.highscore}", font=('Arial', 20, "normal"), align="center")

