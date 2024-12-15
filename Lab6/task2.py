class Vehile:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return f'Марка: { self.make }\n Модель: {self.model}'


class Car(Vehile):
    def __init__(self, make, model, fuel):
        super().__init__(make, model)
        self.fuel = fuel

    def get_info(self):
        return super().get_info()+ f'Топливо: { self.fuel }'
    

new_car = Car("Daewoo", "Matizik", "Plov")
print(new_car.get_info())