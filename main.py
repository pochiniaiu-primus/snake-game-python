from turtle import Screen, Turtle

# x_position = [0, -20, -40]
# y_positions = [0, 0, 0]
# all_turtles = []

# for turtle_index in range(0, 3):
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.penup()
#     new_turtle.goto(x=x_position[turtle_index], y=y_positions[turtle_index])
#     all_turtles.append(new_turtle)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")























screen.exitonclick()