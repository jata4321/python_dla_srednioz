class Car:

    car_list = list()

    def __init__(self, brand, model, paint, motor):
        self.brand = brand
        self.model = model
        self.paint = paint
        self.motor = motor
        self.__isOnSale = True

    def quality_check(self):
        return self.paint and self.motor

    def get_status(self):
        if self.motor:
            print(f'Motor of {self.model} is OK = {self.motor}')
        else:
            print("Motor is not OK")


car_1 = Car('Opel', 'Astra', True, True)

print(car_1.brand, car_1.model)
print(car_1.quality_check())

print(vars(car_1))

car_1.get_status()