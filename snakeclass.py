from turtle import Turtle,Screen
import time

coordinates = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.turtles=[]
        self.createsnake()
        self.coordinates = [(0, 0), (-20, 0), (-40, 0)]
    def createsnake(self):
        self.turtles = []
        for c in coordinates:
            newturtle = Turtle(shape="square")
            newturtle.goto(c)
            newturtle.color("green")
            newturtle.pu()
            self.turtles.append(newturtle)
    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            p1 = self.turtles[i - 1].position()
            self.turtles[i].goto(p1)
        self.turtles[0].forward(20)
    def up(self):
        if self.turtles[0].heading()!=270:
            self.turtles[0].setheading(90)
    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)
    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)
    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)
    def extend(self):
        newturtle=Turtle()
        self.coordinates.append(self.turtles[-1].position())
        newturtle = Turtle(shape="square")
        newturtle.goto(coordinates[-1])
        newturtle.color("green")
        newturtle.pu()
        self.turtles.append(newturtle)
    def gameoversn(self):
        for i in self.turtles:
            i.hideturtle()
        self.turtles.clear()
        self.createsnake()
