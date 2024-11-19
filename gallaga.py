import pgzrun
import random

WIDTH=400
HEIGHT=700

ship=Actor("ship")
ship.x=WIDTH//2


bullets=[]
enimies=[]
score=0

#Draw the score
def drawScore():
    screen.draw.text(str(score),(50,50),color="blue")


def draw():
    screen.fill("light green")
    drawScore()


def update():
    pass






















pgzrun.go()