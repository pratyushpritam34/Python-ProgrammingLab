class Car:
    car_count = 0  
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        Car.car_count += 1

    def start(self):
        return f"{self.color} {self.model} is starting."

    def stop(self):
        return f"{self.color} {self.model} is stopping."

    def accelerate(self):
        return f"{self.color} {self.model} is accelerating."

    @staticmethod
    def count_cars():
        return f"Total cars created: {Car.car_count}"



num_car = int(input("Enter the number of car: "))
for i in range(num_car):
    model_name = input(f"Enter the name of car: ")
    color = input(f"Enter the colour of car : ")
    price = float(input(f"Enter the price of car : "))
    car = Car(model_name, color, price)


print(car.start())
print(car.accelerate())
print(car.stop())


print(Car.count_cars())
