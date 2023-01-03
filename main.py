from turtle import Turtle,Screen
import time
from food import Food
from snakeclass import Snake
from random import randint
from scoreboard import ScoreBoard
s1=Screen()
s1.setup(600,600)
s1.bgcolor("black")
s1.title("Snake Game")
s1.tracer(0)
sn1=Snake()
board1=ScoreBoard()
s1.listen()
s1.onkey(sn1.up,"Up")
s1.onkey(sn1.down,"Down")
s1.onkey(sn1.right,"Right")
s1.onkey(sn1.left,"Left")
food1=Food()
game_on = True
while game_on:
    s1.update()
    time.sleep(0.1)

    sn1.move()
    if  sn1.turtles[0].position()[0]<-300 or sn1.turtles[0].position()[0]>300 or sn1.turtles[0].position()[1]<-300 or sn1.turtles[0].position()[1]>300 :
        board1.gameover()
        sn1.gameoversn()

    if sn1.turtles[0].distance(food1)<15:
        food1.refresh()
        board1.score+=1
        board1.updatescores()
        sn1.extend()
    for i in sn1.turtles:
        if i==sn1.turtles[0]:
            pass
        elif sn1.turtles[0].distance(i)<9:
            board1.gameover()
            sn1.gameoversn()


s1.exitonclick()