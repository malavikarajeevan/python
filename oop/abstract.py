from abc import ABC,abstractmethod
class vehicle(ABC):
    def engine(self):
        print("engine provaide")
    @abstractmethod
    def gear(self):
        pass
class car(vehicle):
    def gear(self):
        print("automatic gear")
class truck(vehicle):
    def wheel(self):
        print("heavy")
    def gear(self):
        print("manual gear")
c=car()
c.gear()
t=truck()