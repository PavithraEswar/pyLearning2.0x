class Car:
    name = None
    make = None
    model = None

    def __init__(self, x_name, x_make, x_model):
        self.name = x_name
        self.make = x_make
        self.model = x_model

    def start_engine(self):
        print("start a car with name ", self.name)
        print("start a car with make ", self.make)
        print("start a car with model ", self.model)

scoda = Car(x_name="scoda", x_make="India", x_model="2017")
scoda.start_engine()