from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.speed(0)
        self.goto(x=randint(-270, 270), y=randint(-270, 270))
    def refresh(self):
        self.goto(x=randint(-270, 270), y=randint(-270, 270))
