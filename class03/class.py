class Car:
    def __init__(self,name,speed):
        self.name= name
        self.speed=speed


def get_car():
    name= "Palio"
    speed= 100
    car = Car(name,speed)
    return car


def main():
    car = get_car()
    print(car.name)

main()
