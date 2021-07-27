import turtle
import tkinter

def hangman():
    draw.pensize(5) #pen size for draw gallows

    #set start position
    draw.penup()
    draw.goto(-30 , -105)
    draw.pendown()

    draw.forward(20)
    draw.backward(40)
    draw.forward(20)
    
    draw.left(90)
    draw.forward(240)

    draw.right(90)
    draw.forward(70)

    draw.pensize(3) #pen size for draw tanab ?!

    draw.right(90)
    draw.forward(50)

    draw.pensize(2) # pen size for draw a man

    draw.penup()
    draw.left(90)
    draw.backward(14)
    draw.right(90)
    draw.forward(15)
    draw.pendown()

    draw.circle(14)

    draw.penup()
    draw.left(90)
    draw.forward(14)
    draw.right(90)
    draw.forward(15)
    draw.right(45)
    draw.pendown()

    draw.forward(20)

    draw.penup()
    draw.backward(20)
    draw.left(90)
    draw.pendown()

    draw.forward(20)

    draw.penup()
    draw.backward(20)
    draw.right(45)
    draw.pendown()

    draw.forward(40)

    draw.penup()
    draw.right(45)
    draw.pendown()

    draw.forward(20)

    draw.penup()
    draw.backward(20)
    draw.left(90)
    draw.pendown()

    draw.forward(20)

def KillHangman():
    draw.pencolor("white")

    if wrong == 1:
        draw.bk(20) # right leg
        draw.rt(90)
    elif wrong == 2:
        draw.fd(20) # left leg
        draw.bk(20)
        draw.left(45)
    elif wrong == 3:
        draw.bk(40) # body
        draw.lt(45)
    elif wrong == 4:
        draw.fd(20) # right hand
        draw.bk(20)
        draw.rt(90)
    elif wrong == 5:
        draw.fd(20) # left hand
        draw.bk(20)

    elif wrong == 6:
        draw.penup()
        draw.lt(45)
        draw.bk(15)
        draw.rt(90)
        draw.fd(14)
        draw.lt(90)
        draw.pendown()

        draw.circle(14) # Head

#main game
main = tkinter.Tk()
main.title("Hangman")
main.geometry("700x400")
main.resizable(width = False , height = False)
main['bg'] = 'white'

#connect tkinter and turtle
canvas = tkinter.Canvas(master = main , width = 150 , height = 280)
canvas.grid(row = 0 , column = 0)
draw = turtle.RawTurtle(canvas , visible = False)

#variable
wrong = 0

hangman()
KillHangman()

main.mainloop()