import turtle


screen = turtle.Screen()
screen.title("Interactive Turtle Pattern Generator")
screen.setup(width=800, height=600)
screen.bgcolor("#101820")


pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()


def draw_spiral():
    colors = ["#FFB000", "#00D4FF", "#F5F5F5"]
    for step in range(120):
        pen.pencolor(colors[step % len(colors)])
        pen.forward(step * 2)
        pen.right(91)


def koch_curve(length, depth):
    if depth == 0:
        pen.forward(length)
    else:
        koch_curve(length / 3, depth - 1)
        pen.left(60)
        koch_curve(length / 3, depth - 1)
        pen.right(120)
        koch_curve(length / 3, depth - 1)
        pen.left(60)


def draw_snowflake():
    pen.pencolor("#00D4FF")
    pen.penup()
    pen.goto(-180, 100)
    pen.pendown()

    for side in range(3):
        koch_curve(360, 3)
        pen.right(120)


choice = input("Choose pattern (1 = Spiral, 2 = Koch Snowflake): ")

if choice == "1":
    draw_spiral()
elif choice == "2":
    draw_snowflake()
else:
    print("Invalid choice. Drawing Koch Snowflake.")
    draw_snowflake()

screen.exitonclick()
