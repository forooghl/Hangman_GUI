import turtle
import tkinter


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



main.mainloop()