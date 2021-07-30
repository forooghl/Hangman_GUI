import turtle
import tkinter
from tkinter import *
import random
import re
import more_itertools as mit
from tkinter import messagebox

def DisButton():
    Q['state'] = DISABLED
    W['state'] = DISABLED
    E['state'] = DISABLED
    R['state'] = DISABLED
    T['state'] = DISABLED
    Y['state'] = DISABLED
    U['state'] = DISABLED
    I['state'] = DISABLED
    O['state'] = DISABLED
    P['state'] = DISABLED
    A['state'] = DISABLED
    S['state'] = DISABLED
    D['state'] = DISABLED
    F['state'] = DISABLED
    G['state'] = DISABLED
    H['state'] = DISABLED
    J['state'] = DISABLED
    K['state'] = DISABLED
    L['state'] = DISABLED
    Z['state'] = DISABLED
    X['state'] = DISABLED
    C['state'] = DISABLED
    V['state'] = DISABLED
    B['state'] = DISABLED
    N['state'] = DISABLED
    M['state'] = DISABLED

def EnButton():
    Q['state'] = NORMAL
    W['state'] = NORMAL
    E['state'] = NORMAL
    R['state'] = NORMAL
    T['state'] = NORMAL
    Y['state'] = NORMAL
    U['state'] = NORMAL
    I['state'] = NORMAL
    O['state'] = NORMAL
    P['state'] = NORMAL
    A['state'] = NORMAL
    S['state'] = NORMAL
    D['state'] = NORMAL
    F['state'] = NORMAL
    G['state'] = NORMAL
    H['state'] = NORMAL
    J['state'] = NORMAL
    K['state'] = NORMAL
    L['state'] = NORMAL
    Z['state'] = NORMAL
    X['state'] = NORMAL
    C['state'] = NORMAL
    V['state'] = NORMAL
    B['state'] = NORMAL
    N['state'] = NORMAL
    M['state'] = NORMAL

def hangman():
    DisButton()

    draw.speed(0)
    draw.pencolor("BLACK")
    draw.pensize(5) #pen size for draw gallows

    #set start position
    draw.penup()
    draw.goto(-30 , -105)
    draw.pendown()

    draw.forward(20)
    draw.backward(40)
    draw.forward(20)
    
    draw.left(90)
    draw.forward(180)

    draw.right(90)
    draw.forward(70)

    draw.pensize(3) #pen size for draw tanab ?!

    draw.right(90)
    draw.forward(50)

    draw.pensize(2) # pen size for draw a man
    draw.pencolor("#57291F")

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

    EnButton()

def KillHangman():
    global wrong

    draw.pencolor("#FFCD73")

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
        
        #call gameover function
        gameover()

def CharFound():
    global answer , answerText , answerLength
    
    #space
    charLocate = list(mit.locate(answer , lambda x : x == " "))
    answerText = answerLength*"_ "

    for i in charLocate:    
        answerText = answerText[:i*2] + " " + answerText[i*2 + 1 :]
    
    # '
    charLocate = list(mit.locate(answer , lambda x : x == "'"))

    for i in charLocate:    
        answerText = answerText[:i*2] + "'" + answerText[i*2 + 1 :]
    
    # -
    charLocate = list(mit.locate(answer , lambda x : x == "-"))

    for i in charLocate:    
        answerText = answerText[:i*2] + "-" + answerText[i*2 + 1 :]
    
    # .
        charLocate = list(mit.locate(answer , lambda x : x == "."))

    for i in charLocate:    
        answerText = answerText[:i*2] + "." + answerText[i*2 + 1 :]
    
    return answerText

def gameover():
    global answer , charLocate , lastAnswer

    messagebox.showinfo("Lose" , "Dead")
    playagain.place(x = 630 , y = 370)

    lastAnswer = answerLable['text']
    charLocate = list(mit.locate(lastAnswer , lambda x : x == "_"))
    
    for i in charLocate:    
        lastAnswer = lastAnswer[:i] + answer[int(i/2)] + lastAnswer[i + 1 :]
        answerLable.config(text = lastAnswer , fg = "#57291F")
    
def win():
    messagebox.showinfo("Win" , "Yohooo , you save him")
    playagain.place(x = 630 , y = 370)

def Playagain():
    global wrong , dice , answer , answerLength , lineCount , lastAnswer 

    dice = random.randint(0,lineCount - 1)
    hint.config(text = "(" + endFile[dice][0] + ")")
    answer = endFile[dice][1].lower()
    answerLength = len(endFile[dice][1])
    answerLable.config(text = CharFound() , fg = "black")
    lastAnswer = answerLable['text']

    canvas.delete("all")
    wrong = 0

    draw.home()
    hangman()
    playagain.place(x = 800 , y = 1)

def Keyword(key):
    global answer , answerLength , charLocate , lastAnswer , wrong
    
    #disable a button after click
    if key == 'q' :
        Q['state'] = DISABLED
    elif key == 'w' :
        W['state'] = DISABLED
    elif key == 'e' :    
        E['state'] = DISABLED
    elif key == 'r' :
        R['state'] = DISABLED
    elif key == 't' :    
        T['state'] = DISABLED
    elif key == 'y' :
        Y['state'] = DISABLED
    elif key == 'u' :
        U['state'] = DISABLED
    elif key == 'i' :
        I['state'] = DISABLED
    elif key == 'o' :
        O['state'] = DISABLED
    elif key == 'p' :
        P['state'] = DISABLED
    elif key == 'a' :
        A['state'] = DISABLED
    elif key == 's' :
        S['state'] = DISABLED
    elif key == 'd' :
        D['state'] = DISABLED
    elif key == 'f' :
        F['state'] = DISABLED
    elif key == 'g' :
        G['state'] = DISABLED
    elif key == 'h' :
        H['state'] = DISABLED
    elif key == 'j' :
        J['state'] = DISABLED
    elif key == 'k' :
        K['state'] = DISABLED
    elif key == 'l' :
        L['state'] = DISABLED
    elif key == 'z' :
        Z['state'] = DISABLED
    elif key == 'x' :
        X['state'] = DISABLED
    elif key == 'c' :
        C['state'] = DISABLED
    elif key == 'v' :
        V['state'] = DISABLED
    elif key == 'b' :
        B['state'] = DISABLED
    elif key == 'n' :
        N['state'] = DISABLED
    elif key == 'm' :
        M['state'] = DISABLED

    #config answer lable after click alphabet button 
    if answer.count(key) != 0:
        charLocate = list(mit.locate(answer , lambda x : x == key))
        lastAnswer = answerLable['text']
        for i in charLocate:    
            lastAnswer = lastAnswer[:i*2] + key + lastAnswer[i*2 + 1 :]
            answerLable.config(text = lastAnswer)
    else:
        wrong += 1
        KillHangman()

    #check if win end game..
    if lastAnswer.count("_") == 0 and wrong < 6:
        win()

#main game
main = tkinter.Tk()
main.title("Hangman")
main.geometry("700x400")
main.resizable(width = False , height = False)
main['bg'] = '#FFCD73'

#connect tkinter and turtle
canvas = tkinter.Canvas(master = main , width = 150 , height = 280 )
canvas.pack(fill = tkinter.Y , side = "left")

turtle_screen = turtle.TurtleScreen(canvas)
turtle_screen.bgcolor("#FFCD73")
canvas.pack()
draw = turtle.RawTurtle(turtle_screen , visible = False)

#variable
wrong = 0
charLocate = list()
lastAnswer = ""
lineCount = 0
answerText = ""

#database
endFile = list()
with open("D:\Work\Pythonexe\Project\Hangman\database.txt" , "r") as ReadMode:
        File =  ReadMode.readlines()
        for line in File :
            lineCount += 1
            line = re.sub(r"\n" , "" , line)
            endFile.append(line.split(" : "))

dice = random.randint(0,lineCount-1)

#hint lable
hint = Label(main , text = "(" +endFile[dice][0] + ")", font = 'arial')
hint.pack()
hint.place(x = 180 , y = 10)
hint['bg'] = '#FFCD73'

#answer lable
answer = endFile[dice][1].lower()
answerLength = len(endFile[dice][1])
answerLable = Label(main , text = CharFound() , font = 'arial')
answerLable.pack()
answerLable.place(x = 290 , y = 70)
answerLable['bg'] = '#FFCD73'
lastAnswer = answerLable["text"]

#Alphabet Keyboard
Q = Button(main , width = 4 , text = "Q" , command = lambda key = 'q' : Keyword(key))
Q.pack()
Q.place(x = 225 , y = 250)
Q['bg'] = "#FF9200"

W = Button(main , width = 4 , text = "W" , command = lambda key = 'w' : Keyword(key))
W.pack()
W.place(x = 270 , y = 250)
W['bg'] = "#FF9200"

E = Button(main , width = 4 , text = "E" , command = lambda key = 'e' : Keyword(key))
E.pack()
E.place(x = 315 , y = 250)
E['bg'] = "#FF9200"

R = Button(main , width = 4 , text = "R" , command = lambda key = 'r' : Keyword(key))
R.pack() 
R.place(x = 360 , y = 250)
R['bg'] = "#FF9200"

T = Button(main , width = 4 , text = "T" , command = lambda key = 't' : Keyword(key))
T.pack()
T.place(x = 405 , y = 250)
T['bg'] = "#FF9200"

Y = Button(main , width = 4 , text = "Y" , command = lambda key = 'y' : Keyword(key))
Y.pack()
Y.place(x = 450 , y = 250)
Y['bg'] = "#FF9200"

U = Button(main , width = 4 , text = "U" , command = lambda key = 'u' : Keyword(key))
U.pack()
U.place(x = 495 , y = 250)
U['bg'] = "#FF9200"

I = Button(main , width = 4 , text = "I" , command = lambda key = 'i' : Keyword(key))
I.pack() 
I.place(x = 540 , y = 250)
I['bg'] = "#FF9200"

O = Button(main , width = 4 , text = "O" , command = lambda key = 'o' : Keyword(key))
O.pack()
O.place(x = 585 , y = 250)
O['bg'] = "#FF9200"

P = Button(main , width = 4 , text = "P" , command = lambda key = 'p' : Keyword(key))
P.pack()
P.place(x = 630 , y = 250)
P['bg'] = "#FF9200"

A = Button(main , width = 4 , text = "A" , command = lambda key = 'a' : Keyword(key))
A.pack() 
A.place(x = 240 , y = 280)
A['bg'] = "#FF9200"

S = Button(main , width = 4 , text = "S" , command = lambda key = 's' : Keyword(key))
S.pack() 
S.place(x = 285 , y = 280)
S['bg'] = "#FF9200"

D = Button(main , width = 4 , text = "D" , command = lambda key = 'd' : Keyword(key))
D.pack() 
D.place(x = 330 , y = 280)
D['bg'] = "#FF9200"

F = Button(main , width = 4 , text = "F" , command = lambda key = 'f' : Keyword(key))
F.pack() 
F.place(x = 375 , y = 280)
F['bg'] = "#FF9200"

G = Button(main , width = 4 , text = "G" , command = lambda key = 'g' : Keyword(key))
G.pack() 
G.place(x = 420 , y = 280)
G['bg'] = "#FF9200"

H = Button(main , width = 4 , text = "H" , command = lambda key = 'h' : Keyword(key))
H.pack() 
H.place(x = 465 , y = 280)
H['bg'] = "#FF9200"

J = Button(main , width = 4 , text = "J" , command = lambda key = 'j' : Keyword(key))
J.pack() 
J.place(x = 510 , y = 280)
J['bg'] = "#FF9200"

K = Button(main , width = 4 , text = "K" , command = lambda key = 'k' : Keyword(key))
K.pack()  
K.place(x = 555 , y = 280)
K['bg'] = "#FF9200"

L = Button(main , width = 4 , text = "L" , command = lambda key = 'l' : Keyword(key))
L.pack() 
L.place(x = 600 , y = 280)
L['bg'] = "#FF9200"

Z = Button(main , width = 4 , text = "Z" , command = lambda key = 'z' : Keyword(key))
Z.pack()  
Z.place(x = 255 , y = 310)
Z['bg'] = "#FF9200"

X = Button(main , width = 4 , text = "X" , command = lambda key = 'x' : Keyword(key))
X.pack() 
X.place(x = 300 , y = 310)
X['bg'] = "#FF9200"

C = Button(main , width = 4 , text = "C" , command = lambda key = 'c' : Keyword(key))
C.pack() 
C.place(x = 345 , y = 310)
C['bg'] = "#FF9200"

V = Button(main , width = 4 , text = "V" , command = lambda key = 'v' : Keyword(key))
V.pack() 
V.place(x = 390 , y = 310)
V['bg'] = "#FF9200"

B = Button(main , width = 4 , text = "B" , command = lambda key = 'b' : Keyword(key))
B.pack() 
B.place(x = 435 , y = 310)
B['bg'] = "#FF9200"

N = Button(main , width = 4 , text = "N" , command = lambda key = 'n' : Keyword(key))
N.pack() 
N.place(x = 480 , y = 310)
N['bg'] = "#FF9200"

M = Button(main , width = 4 , text = "M" , command = lambda key = 'm' : Keyword(key))
M.pack()
M.place(x = 525 , y = 310)
M['bg'] = "#FF9200"

#play again button
playagain = Button(main , text = "playagain" , fg = "#57291F" , command = Playagain)
playagain.pack()
playagain.place(x = 800 , y = 1)
playagain['bg'] = "#D77B5F"

hangman()
KillHangman()

main.mainloop()