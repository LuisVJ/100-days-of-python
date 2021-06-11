from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
TOP_Y_LIMIT = 265
BOTTOM_Y_LIMIT = -230
CAR_NUMBER  = 20


class CarManager:
    
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def generate_cars(self):
        for _ in range(CAR_NUMBER):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(random.randint(-290, 330),
                        random.randint(BOTTOM_Y_LIMIT, TOP_Y_LIMIT))
            self.cars.append(new_car)
    
    def move_cars(self, player):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -300:
                car.goto(330, random.randint(BOTTOM_Y_LIMIT, TOP_Y_LIMIT))
                car.color(random.choice(COLORS))
            
            if self.detect_collision(car, player):
                return True 

    def detect_collision(self, car, player):
        x_distance = abs(car.xcor() - player.xcor())
        y_distance = abs(car.ycor() - player.ycor())
        return y_distance < 15  and x_distance < 20