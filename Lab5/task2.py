class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_perimeter(self):
        return 2*3.14*float(self.radius)

circle = Circle(input("Введите радиус круга:\n"))
print(f"Текцщий радиус круга: {circle.get_radius()}")

circle.set_radius(input("Введите новое значение радиуса:\n"))
print(f"Обновлённое значение радиуса: {circle.get_radius()}")

print(circle.get_perimeter())