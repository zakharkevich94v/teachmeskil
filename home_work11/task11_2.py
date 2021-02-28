class Car:   

    def __init__(self, brand, model, year_issue, speed=0):       
        self.__brand = brand
        self.__model = model
        self.__year_issue = year_issue
        self.__speed = speed

    def speed_up(self):        
        self.__speed += 5

    def speed_down(self):        
        self.__speed -= 5

    def stop(self):        
        self.__speed *= 0

    @property
    def speed(self):        
        return self.__speed

    def turn(self):        
        self.__speed = -self.__speed


car_1 = Car('audi', 'q8', 2021)

car_1.speed_up()
print(car_1.speed)
car_1.turn()
print(car_1.speed)