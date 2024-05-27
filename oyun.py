import turtle
import os
import random

def clear():
    os.system("clear")
    
def main_text():
    turtle.penup()
    turtle.color("dark blue")
    turtle.setposition(0,360)
    turtle.write(arg="Catch the Turtle", align="center", font=('verdana',17,'normal'))

def programmer_name():
    turtle.penup()
    turtle.color("dark blue")
    turtle.setposition(0,340)
    turtle.write(arg="Programming by cpu-astatine", align="center",font=('verdana',17,'normal'))

clear()
print("Game is running...")
turtle.title("Catch the Turtle")
turtle.bgcolor("light blue")
turtle.shape("turtle")
turtle.color("green")
main_text()
programmer_name()
turtle.home()

def get_lost(x,y):
    x = random.randint(-350,350)
    y = random.randint(-350,350)
    turtle.penup()
    turtle.hideturtle()
    turtle.setposition(x,y)
    turtle.showturtle()

turtle.onclick(get_lost)
turtle.mainloop()
print("Game is stopped.")
