class Engine:
    def __init__(self):
        pass
    
    def start(self):
        return f"Engine is starting"
    
class Car:
    def __init__(self, engine):
        self.engine = engine
        
    def drive(self):
        return f"Car is driving."
    
engine = Engine()

car = Car(engine)
print(car.drive())
print(car.engine.start())