import turtle
import time

#create screen

sc = turtle.Screen()
sc.title("Ping Pong")
sc.bgcolor("black")
sc.cv._rootwindow.resizable(False,False)


#left player
left_pl = turtle.Turtle()
left_pl.shape("square")
left_pl.color("white")
left_pl.speed(0)
left_pl.penup()
left_pl.shapesize(stretch_wid=6,stretch_len=2)
left_pl.goto(-250,0)

#right player

right_pl=turtle.Turtle()
right_pl.shape("square")
right_pl.color("white")
right_pl.speed(0)
right_pl.penup()
right_pl.shapesize(stretch_wid=6,stretch_len=2)
right_pl.goto(250,0)

#ball
ball = turtle.Turtle()
ball.speed(3)
ball.shape("circle")
ball.color("red")
ball.goto(0,0)
ball.dx=5
ball.dy=-5

player1=0
player2=0

#score
word = turtle.Turtle()
word.speed(0)
word.color("blue")
word.penup()
word.goto(0,260)
word.write("Player_L : 0    Player_R : 0",align = "center" , font=("Ariel",24))


#motion

def playerL_up():
    y = left_pl.ycor()
    if y < 260:
        y+=20
        left_pl.sety(y)

def playerR_up():
    y = right_pl.ycor()
    if y < 260:
        y+=20
        right_pl.sety(y)

def playerL_down():
    y = left_pl.ycor()
    if y > -240:
        y-=20
        left_pl.sety(y)


def playerR_down():
    y = right_pl.ycor()
    if y > -240:
        y-=20
        right_pl.sety(y)

sc.listen()
sc.onkeypress(playerR_up, "Up")
sc.onkeypress(playerR_down, "Down")
sc.onkeypress(playerL_up,"w")
sc.onkeypress(playerL_down,"s")


        
        
    
    
    





















