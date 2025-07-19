from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
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
    
    if snake.first_bit.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.add_snake_bit()
    
    if snake.first_bit.xcor() > 280 or snake.first_bit.xcor() < -280 or snake.first_bit.ycor() > 280 or snake.first_bit.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        
    for bit in snake.snake_bits[1:]:
        if snake.first_bit.distance(bit) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()