class Car:
    def __init__(self, year: int, make: str, model: str, fuel_cons: float):
        self.year = year
        self.make = make
        self.model = model
        self.fuel_cons = fuel_cons
        self.mileage = 0

    def drive(self):
        print(f'Я авто марки {self.model}, їду по справам господаря')

    @property
    def cost_of_service(self):
        return self.mileage * 7.6


car_fiat = Car(2010,'Fiat','Tipo', fuel_cons=5.6)
car_volvo = Car(2021,'Volvo','XC60', fuel_cons=9.1)
car_nissan = Car(2021,'Nissan','Juke', fuel_cons=6.7)
car_toyota = Car(2015,'Toyota','Yaris', fuel_cons=7.3)
car_opel = Car(2019,'Opel', 'Astra', fuel_cons=8.1)

car_fiat.mileage = 65000
print(car_fiat.mileage)
print(car_volvo.cost_of_service)
car_toyota.drive()
