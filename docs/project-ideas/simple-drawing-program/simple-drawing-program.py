import turtle
from turtle import Screen, Turtle
import tkinter as tk
from tkinter import simpledialog, messagebox

def set_color():
    # Vælg farve
    color = simpledialog.askstring("Indtast", "Hvilken farve vil du gerne have? (f.eks., 'rød', 'blå', 'grøn')")
    turtle.color(str(color))

def draw_shape():
    # Tegn form
    shape = simpledialog.askstring("Indtast", "Hvilken form vil du gerne tegne? (cirkel, firkant, trekant)")
    
    if shape == "cirkel":
        radius = simpledialog.askfloat("Indtast", "Indtast radius for cirklen:")
        turtle.circle(radius)
    
    elif shape == "firkant":
        side = simpledialog.askfloat("Indtast", "Indtast sidelængde for firkanten:")
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)
    
    elif shape == "trekant":
        side = simpledialog.askfloat("Indtast", "Indtast sidelængde for trekanten:")
        for _ in range(3):
            turtle.forward(side)
            turtle.left(120)
    
    else:
        messagebox.showerror("Fejl", "Form ikke genkendt!")

def save_drawing():
    # Gem tegning
    cvs = turtle.getcanvas()
    cvs.postscript(file="tegning.eps", colormode='color')
    messagebox.showinfo("Info", "Tegningen gemt som 'tegning.eps'")

def main():
    screen = Screen()
    screen.title("Simpelt tegneprogram")

    screen.setup(width=800, height=600)

    screen.onkey(set_color, "c")
    screen.onkey(draw_shape, "s")
    screen.onkey(save_drawing, "d")
    screen.onkey(turtle.clear, "r")

    screen.listen()
    messagebox.showinfo("Instruktioner", 
                        "Tryk på 'c' for at vælge farve.\n"
                        "Tryk på 's' for at tegne en form.\n"
                        "Tryk på 'd' for at gemme tegningen.\n"
                        "Tryk på 'r' for at nulstille tegningen.\n"
                        "Luk vinduet for at afslutte.")
    screen.mainloop()

# Indgangspunkt for applikationen 
if __name__ == "__main__": # Hvis main findes
    main() # Så kør main