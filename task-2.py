import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def koch_curve_part(t, order, size):
    for part in range(3):
        koch_curve(t, order, size)
        t.left(-120)
    

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    koch_curve_part(t, order, size)

    window.mainloop()

# Виклик функції
draw_koch_curve(5)
