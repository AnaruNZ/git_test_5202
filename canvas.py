import ttkbootstrap as ttk
import random

SIZE = 10
x_pos = 5
y_pos = 5

app = ttk.Window(themename="cosmo")
app.title("Canvas Example")

canvas = ttk.Canvas(app, width=400, height=400, bg="white")
canvas.pack()

colors = [
    "white",
    "black",
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "gray",
    "cyan",
    "magenta",
    "lightblue",
    "skyblue",
    "deepskyblue",
    "navy",
    "lightgreen",
    "limegreen",
    "forestgreen",
    "darkgreen",
    "gold",
    "goldenrod",
    "khaki",
    "salmon",
    "coral",
    "tomato",
    "plum",
    "orchid",
    "violet",
    "indigo",
    "beige",
    "ivory",
    "linen",
    "tan",
    "lightgray",
    "silver",
    "darkgray",
    "dimgray"
]

def get_random_color():
    return random.choice(colors)

    

def square_pattern_1():
    for row in range(10):
        for i in range (20):
            canvas.create_rectangle(x_pos,y_pos,x_pos + SIZE, y_pos + SIZE, fill=get_random_color())
            x_pos += 20

        x_pos = 5  
        y_pos += 20

def line_pattern():
    x1 = 10
    y1 = 10
    x2 = 300
    y2 = 10
    for i in range (10):
        canvas.create_line(x1, y1, x2, y2, fill=get_random_color())
        y1 += 5
        y2 += 5

line_pattern()

app.mainloop()