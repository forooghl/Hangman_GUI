import turtle
import tkinter

def hangman():
    draw.speed(0)
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

def Keyword(key):
    print(key)

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

#Alphabet Keyboard
Q = tkinter.Button(main , width = 4 , text = "Q" , command = lambda key = 'Q' : Keyword(key))
Q.grid(row = 1 , column = 3) 

W = tkinter.Button(main , width = 4 , text = "W" , command = lambda key = 'W' : Keyword(key))
W.grid(row = 1 , column = 4)

E = tkinter.Button(main , width = 4 , text = "E" , command = lambda key = 'E' : Keyword(key))
E.grid(row = 1 , column = 5) 

R = tkinter.Button(main , width = 4 , text = "R" , command = lambda key = 'R' : Keyword(key))
R.grid(row = 1 , column = 6) 

T = tkinter.Button(main , width = 4 , text = "T" , command = lambda key = 'T' : Keyword(key))
T.grid(row = 1 , column = 7) 

Y = tkinter.Button(main , width = 4 , text = "Y" , command = lambda key = 'Y' : Keyword(key))
Y.grid(row = 1 , column = 8)

U = tkinter.Button(main , width = 4 , text = "U" , command = lambda key = 'U' : Keyword(key))
U.grid(row = 1 , column = 9) 

I = tkinter.Button(main , width = 4 , text = "I" , command = lambda key = 'I' : Keyword(key))
I.grid(row = 1 , column = 10) 

O = tkinter.Button(main , width = 4 , text = "O" , command = lambda key = 'O' : Keyword(key))
O.grid(row = 1 , column = 11) 

P = tkinter.Button(main , width = 4 , text = "P" , command = lambda key = 'P' : Keyword(key))
P.grid(row = 1 , column = 12) 

A = tkinter.Button(main , width = 4 , text = "A" , command = lambda key = 'A' : Keyword(key))
A.grid(row = 2 , column = 3)  

S = tkinter.Button(main , width = 4 , text = "S" , command = lambda key = 'S' : Keyword(key))
S.grid(row = 2 , column = 4)

D = tkinter.Button(main , width = 4 , text = "D" , command = lambda key = 'D' : Keyword(key))
D.grid(row = 2 , column = 5) 

F = tkinter.Button(main , width = 4 , text = "F" , command = lambda key = 'F' : Keyword(key))
F.grid(row = 2 , column = 6)

G = tkinter.Button(main , width = 4 , text = "G" , command = lambda key = 'G' : Keyword(key))
G.grid(row = 2 , column = 7) 

H = tkinter.Button(main , width = 4 , text = "H" , command = lambda key = 'H' : Keyword(key))
H.grid(row = 2 , column = 8)

J = tkinter.Button(main , width = 4 , text = "J" , command = lambda key = 'J' : Keyword(key))
J.grid(row = 2 , column = 9) 

K = tkinter.Button(main , width = 4 , text = "K" , command = lambda key = 'K' : Keyword(key))
K.grid(row = 2 , column = 10) 

L = tkinter.Button(main , width = 4 , text = "L" , command = lambda key = 'L' : Keyword(key))
L.grid(row = 2 , column = 11) 

Z = tkinter.Button(main , width = 4 , text = "Z" , command = lambda key = 'Z' : Keyword(key))
Z.grid(row = 3 , column = 3) 

X = tkinter.Button(main , width = 4 , text = "X" , command = lambda key = 'X' : Keyword(key))
X.grid(row = 3 , column = 4) 

C = tkinter.Button(main , width = 4 , text = "C" , command = lambda key = 'C' : Keyword(key))
C.grid(row = 3 , column = 5) 

V = tkinter.Button(main , width = 4 , text = "V" , command = lambda key = 'V' : Keyword(key))
V.grid(row = 3 , column = 6)

B = tkinter.Button(main , width = 4 , text = "B" , command = lambda key = 'B' : Keyword(key))
B.grid(row = 3 , column = 7) 

N = tkinter.Button(main , width = 4 , text = "N" , command = lambda key = 'N' : Keyword(key))
N.grid(row = 3 , column = 8) 

M = tkinter.Button(main , width = 4 , text = "M" , command = lambda key = 'M' : Keyword(key))
M.grid(row = 3 , column = 9) 

#enter and delete
enter = tkinter.Button(main , width = 4 , text = "Enter" , command = lambda key = "enter" : Keyword(key))
enter.grid(row = 2 , column = 12)

Delete = tkinter.Button(main , width = 4 , text = "Del" , command = lambda key = "delete" : Keyword(key))
Delete.grid(row = 3 , column = 10)



hangman()
KillHangman()

main.mainloop()