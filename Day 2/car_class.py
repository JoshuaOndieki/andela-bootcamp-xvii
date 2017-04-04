#car class lab

class Car(object):
    speed = 0

    def __init__(self, name="General", model="GM", car_type=None):
        self.name = name
        self.model = model
        self.car_type = car_type

        if self.name == "Porshe":
            self.num_of_doors = 2
        elif self.name == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.car_type != 'trailer':
            self.num_of_wheels = 4
        else:
            self.num_of_wheels = 8

    def is_saloon(self):
        if self.car_type is not 'trailer':
            self.car_type = 'saloon'
            return True
        return False

    def drive(self, moving_speed):
        self.speed = 0
        if self.car_type is not "trailer":
            self.speed = 10 ** moving_speed
        else:
            self.speed = 77

        return self

