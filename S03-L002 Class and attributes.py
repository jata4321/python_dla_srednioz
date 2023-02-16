class Car:
    def __init__(self, brand, model, isAirbagOk, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.airbag = isAirbagOk
        self.painting = isPaintingOK
        self.mechanic = isMechanicOK


car_01 = Car('Opel', 'Astra', True, True, True)

print(car_01.brand,
      car_01.model)
