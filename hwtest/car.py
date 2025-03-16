from hw_2.base import Vehicle
from hw_2.engine import Engine


class Car(Vehicle):
    def __init__(self, engine=6, weight=15, started=False, fuel=98, fuel_consumption=5):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine = engine

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        if issubclass(type(value), Engine):
            self._engine = value
        else:
            raise TypeError("Engine must be Engine Class.")

    def set_engine(self, new_engine):
        #new_engine = Engine(volume=1.0, pistons=2)
        return new_engine
