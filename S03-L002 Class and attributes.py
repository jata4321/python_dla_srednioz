class Car:
    def __init__(self, brand, model, is_airbag_ok, is_painting_ok, is_mechanic_ok):
        self.brand = brand
        self.model = model
        self.airbag = is_airbag_ok
        self.painting = is_painting_ok
        self.mechanic = is_mechanic_ok

    def is_damaged(self):
        return not (self.airbag, self.painting, self.mechanic)


car_01 = Car('Opel', 'Astra', True, True, True)
car_02 = Car('Seat', 'Ibiza', True, False, True)

print(car_01.brand, car_01.model, car_01.is_damaged())
print(car_02.brand, car_02.model, car_02.is_damaged())

print(car_01.brand, car_01.model)
print(car_02.brand, car_02.model)


def is_car_damaged(some_car):
    return not (some_car.airbag, some_car.painting, some_car.mechanic)


print(is_car_damaged(car_01))
