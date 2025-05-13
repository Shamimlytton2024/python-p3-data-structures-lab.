class Plane:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

    def fly(self):
        return f"The plane {self.model} is flying with a capacity of {self.capacity} passengers."


class Train:
    def __init__(self, train_type, number_of_cars):
        self.train_type = train_type
        self.number_of_cars = number_of_cars

    def depart(self):
        return f"The {self.train_type} train with {self.number_of_cars} cars is departing."


class Motorbike:
    def __init__(self, brand, engine_capacity):
        self.brand = brand
        self.engine_capacity = engine_capacity

    def ride(self):
        return f"The motorbike {self.brand} with {self.engine_capacity}cc engine is being ridden."


# Creating instances of each class
plane_instance = Plane("Boeing 747", 416)
train_instance = Train("Freight", 20)
motorbike_instance = Motorbike("Yamaha", 600)

# Example usage prints
print(plane_instance.fly())
print(train_instance.depart())
print(motorbike_instance.ride())
