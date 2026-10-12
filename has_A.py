class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self):
        self.engine = Engine()   # Has-A relationship

    def drive(self):
        self.engine.start()
        print("Car is Moving")

# Create object
c = Car()

# Call method
c.drive()