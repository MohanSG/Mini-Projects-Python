from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkeypress(snake.up, "Up") 
screen.onkeypress(snake.down, "Down") 
screen.onkeypress(snake.left, "Left") 
screen.onkeypress(snake.right, "Right")  

is_playing = True

while is_playing:
    screen.update()
    time.sleep(0.1)
    
    snake.move_forward()
    
screen.exitonclick()