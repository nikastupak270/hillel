class Vehicle:
    def __init__(self, brand: str, model: str ):
        self.brand = brand
        self.model = model

    def info(self):
        print(f'Я авто марки {self.brand}, модель {self.model}')


class Car(Vehicle):
    def __init__(self, brand: str, model: str, num_doors: int):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def info(self):
        print(f'Я авто марки {self.brand}, модель {self.model} і у мене є  {self.num_doors} дверей')


class Bike(Vehicle):
    def __init__(self, brand: str, model: str, type: str):
        super().__init__(brand, model)
        self.type = type

    def info(self):
        print(f'Я {self.type} велосипед марки {self.brand}, модель {self.model}')


class Truck(Vehicle):
    def __init__(self, brand: str, model: str, capacity: int):
        super().__init__(brand, model)
        self.capacity = capacity

    def info(self):
        print(f'Я вантажівка марки {self.brand}, модель {self.model} і я можу перевезти {self.capacity} тон')


car_fiat = Car('Fiat','Tipo', num_doors=2)
car_volvo = Car('Volvo','XC60', num_doors=5)
car_nissan = Car('Nissan','Juke', num_doors=4)
bike_formula = Bike('Formula','F-1', type='гірський')
bike_xtreme = Bike('X-Treme','Rider', type='міський')
truck_volvo = Truck('Volvo','FH16', capacity=16)
truck_daf = Truck('DAF','CF', capacity=11)

car_fiat.info()
car_volvo.info()
bike_formula.info()
bike_xtreme.info()
truck_volvo.info()
truck_daf.info()
