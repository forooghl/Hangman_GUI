import turtle
import tkinter
from tkinter import *
import random
import re
import more_itertools as mit
from tkinter import messagebox

def hangman():
    draw.speed(0)
    draw.pencolor("black")
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
    global wrong

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
        draw.lt(90)

        #set playagain button on screen and show message when gameover
        messagebox.showinfo("Lose" , "Dead")
        playagain.place(x = 630 , y = 370)

def Playagain():
    global wrong , dice , answer , answerLength

    dice = random.randint(0,2636)
    hint.config(text = endFile[dice][0])
    answer = endFile[dice][1].lower()
    answerLength = len(endFile[dice][1])
    answerLable.config(text = answerLength*"_ ")
    canvas.delete("all")
    wrong = 0

    hangman()
    playagain.place(x = 800 , y = 1)

def Keyword(key):
    global answer , answerLength , charLocate , lastAnswer , wrong
    
    if answer.count(key) != 0:
        charLocate = list(mit.locate(answer , lambda x : x == key))
        lastAnswer = answerLable['text']
        
        for i in charLocate:    
            lastAnswer = lastAnswer[:i*2] + key + lastAnswer[i*2 + 1 :]
            answerLable.config(text = lastAnswer)
    else:
        wrong += 1
        KillHangman()

#main game
main = tkinter.Tk()
main.title("Hangman")
main.geometry("700x400")
main.resizable(width = False , height = False)
main['bg'] = 'white'

#connect tkinter and turtle
canvas = tkinter.Canvas(master = main , width = 150 , height = 280)
canvas.pack(fill = tkinter.Y , side = "left")
draw = turtle.RawTurtle(canvas , visible = False)

#variable
wrong = 0
dice = random.randint(0,2636)
charLocate = list()
lastAnswer = ""

#database
endFile = list()
with open("D:\Work\Pythonexe\Project\Hangman\database.txt" , "r") as ReadMode:
        File =  ReadMode.readlines()
        for line in File :
            line = re.sub(r"\n" , "" , line)
            endFile.append(line.split(" : "))

#hint lable
hint = Label(main , text = endFile[dice][0] , font = 'arial')
hint.pack()
hint.place(x = 400 , y = 10)
hint['bg'] = 'white'

#answer lable
answer = endFile[dice][1].lower()
answerLength = len(endFile[dice][1])
answerLable = Label(main , text = answerLength*"_ " , font = 'arial')
answerLable.pack()
answerLable.place(x = 400 - answerLength*2 , y = 70)
answerLable['bg'] = 'white'

#Alphabet Keyboard
Q = Button(main , width = 4 , text = "Q" , command = lambda key = 'q' : Keyword(key))
Q.pack()
Q.place(x = 225 , y = 250)

W = Button(main , width = 4 , text = "W" , command = lambda key = 'w' : Keyword(key))
W.pack()
W.place(x = 270 , y = 250)

E = Button(main , width = 4 , text = "E" , command = lambda key = 'e' : Keyword(key))
E.pack()
E.place(x = 315 , y = 250)

R = Button(main , width = 4 , text = "R" , command = lambda key = 'r' : Keyword(key))
R.pack() 
R.place(x = 360 , y = 250)

T = Button(main , width = 4 , text = "T" , command = lambda key = 't' : Keyword(key))
T.pack()
T.place(x = 405 , y = 250)

Y = Button(main , width = 4 , text = "Y" , command = lambda key = 'y' : Keyword(key))
Y.pack()
Y.place(x = 450 , y = 250)

U = Button(main , width = 4 , text = "U" , command = lambda key = 'u' : Keyword(key))
U.pack()
U.place(x = 495 , y = 250)

I = Button(main , width = 4 , text = "I" , command = lambda key = 'i' : Keyword(key))
I.pack() 
I.place(x = 540 , y = 250)

O = Button(main , width = 4 , text = "O" , command = lambda key = 'o' : Keyword(key))
O.pack()
O.place(x = 585 , y = 250)

P = Button(main , width = 4 , text = "P" , command = lambda key = 'p' : Keyword(key))
P.pack()
P.place(x = 630 , y = 250)

A = Button(main , width = 4 , text = "A" , command = lambda key = 'a' : Keyword(key))
A.pack() 
A.place(x = 240 , y = 280)

S = Button(main , width = 4 , text = "S" , command = lambda key = 's' : Keyword(key))
S.pack() 
S.place(x = 285 , y = 280)

D = Button(main , width = 4 , text = "D" , command = lambda key = 'd' : Keyword(key))
D.pack() 
D.place(x = 330 , y = 280)

F = Button(main , width = 4 , text = "F" , command = lambda key = 'f' : Keyword(key))
F.pack() 
F.place(x = 375 , y = 280)

G = Button(main , width = 4 , text = "G" , command = lambda key = 'g' : Keyword(key))
G.pack() 
G.place(x = 420 , y = 280)

H = Button(main , width = 4 , text = "H" , command = lambda key = 'h' : Keyword(key))
H.pack() 
H.place(x = 465 , y = 280)

J = Button(main , width = 4 , text = "J" , command = lambda key = 'j' : Keyword(key))
J.pack() 
J.place(x = 510 , y = 280)

K = Button(main , width = 4 , text = "K" , command = lambda key = 'k' : Keyword(key))
K.pack()  
K.place(x = 555 , y = 280)

L = Button(main , width = 4 , text = "L" , command = lambda key = 'l' : Keyword(key))
L.pack() 
L.place(x = 600 , y = 280)

Z = Button(main , width = 4 , text = "Z" , command = lambda key = 'z' : Keyword(key))
Z.pack()  
Z.place(x = 255 , y = 310)

X = Button(main , width = 4 , text = "X" , command = lambda key = 'x' : Keyword(key))
X.pack() 
X.place(x = 300 , y = 310)

C = Button(main , width = 4 , text = "C" , command = lambda key = 'c' : Keyword(key))
C.pack() 
C.place(x = 345 , y = 310)

V = Button(main , width = 4 , text = "V" , command = lambda key = 'v' : Keyword(key))
V.pack() 
V.place(x = 390 , y = 310)

B = Button(main , width = 4 , text = "B" , command = lambda key = 'b' : Keyword(key))
B.pack() 
B.place(x = 435 , y = 310)

N = Button(main , width = 4 , text = "N" , command = lambda key = 'n' : Keyword(key))
N.pack() 
N.place(x = 480 , y = 310)

M = Button(main , width = 4 , text = "M" , command = lambda key = 'm' : Keyword(key))
M.pack()
M.place(x = 525 , y = 310)

#play again button
playagain = Button(main , text = "playagain" , fg = "red" , command = Playagain)
playagain.pack()
playagain.place(x = 800 , y = 1)

hangman()
KillHangman()

main.mainloop()