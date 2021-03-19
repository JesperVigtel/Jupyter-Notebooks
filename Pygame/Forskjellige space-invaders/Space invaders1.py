# Write your code here :-)
import turtle
import os

#Skjermen:

Vindu = turtle.Screen()
Vindu.bgcolor("black")
Vindu.title("Space invaders")





#Kanten:
kant_tegner = turtle.Turtle()
kant_tegner.speed(0)
kant_tegner.color("White")
kant_tegner.penup()
kant_tegner.setposition(-300,-300)
kant_tegner.pendown()
kant_tegner.pensize(3)

for side in range(4):
    kant_tegner.fd(600)
    kant_tegner.lt(90)
kant_tegner.hideturtle()

#Lage spiller
spiller = turtle.Turtle()
spiller.color("blue")
spiller.shape("triangle")
spiller.penup()
spiller.speed(0)
spiller.setposition(0,-200)
spiller.setheading(90)

#Bevegelser for spiller
spillerfart = 15

#Fiende
fiende = turtle.Turtle()
fiende.color("red")
fiende.shape("circle")
fiende.penup()
fiende.speed(0)
fiende.setposition(-200,250)

fiendefart = 2




#For høyre og vestre
def venstre ():
    x = spiller.xcor()
    x -= spillerfart
    if x < -280:
        x = -280
    spiller.setx(x)
def høyre ():
    x = spiller.xcor()
    x += spillerfart
    if x > 280:
        x = 280
    spiller.setx(x)

#For tastaturet
turtle.listen()
turtle.onkey(venstre, "Left")
turtle.onkey(høyre, "Right")

