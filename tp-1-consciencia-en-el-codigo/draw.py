import turtle
from turtle import *
import time

def dibujar_espiral():
    turtle.title("Espiral arcoiris")
    speed(15)
    bgcolor("black")
    r,g,b=255,0,0

    for i in range(255*2):
        colormode(255)
        if i<255//3:
            g+=3
        elif i<255*2//3:
            r-=3
        elif i<255:
            b+=3
        elif i<255*4//3:
            g-=3
        elif i<255*5//3:
            r+=3
        else:
            b-=3
        fd(50+i)
        rt(91)
        pencolor(r,g,b)
    
    time.sleep(1)
    turtle.bye()
    

if __name__ == "__main__":
    dibujar_espiral()