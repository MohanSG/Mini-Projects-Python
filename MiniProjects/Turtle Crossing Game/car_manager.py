from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        
    def spawn_car(self):
        random_y = random.randint(-300, 300)
        
        car = Turtle()
        car.penup()
        car.shape('square')
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.setheading(180)
        car.color(random.choice(COLORS))
        car.goto(340, random_y)
        
        self.cars.append(car)
    
    def move_cars(self):
        for car in self.cars:
            car.forward(10)