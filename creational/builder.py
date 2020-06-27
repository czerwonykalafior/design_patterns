from abc import ABC, abstractmethod
from collections import namedtuple


class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        # First goes the body
        body = self.__builder.get_body()
        car.set_body(body)

        # Then engine
        engine = self.__builder.get_engine()
        car.set_engine(engine)

        # And four wheels
        for wheel in range(4):
            wheel = self.__builder.get_wheel()
            car.attach_wheel(wheel)

        car.model = self.__builder.get_model()

        return car

    def get_no_wheeled_car(self):
        car = Car()
        # First goes the body
        body = self.__builder.get_body()
        car.set_body(body)

        # Then engine
        engine = self.__builder.get_engine()
        car.set_engine(engine)

        return car


# The whole product
class Car:
    def __init__(self):
        self.__model = None
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    def set_body(self, body):
        self.__body = body

    def attach_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print("\nModel:: %s" % self.model)
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d\'" % self.__wheels[3].size)


class Builder(ABC):
    @abstractmethod
    def get_wheel(self): pass

    @abstractmethod
    def get_engine(self): pass

    @abstractmethod
    def get_body(self): pass

    @abstractmethod
    def get_model(self): pass


class JeepBuilder(Builder):

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def get_body(self):
        body = Body()
        body.shape = "SUV"
        return body

    def get_model(self):
        return 'Jeep'


class MonsterTruckBuilder(Builder):

    def get_wheel(self):
        wheel = TrackWheel()
        return wheel

    def get_engine(self):
        engine = RocketFuelEngine()
        return engine

    def get_body(self):
        body = HardSteelBody()
        body.shape = "Rainbow"
        return body

    def get_model(self):
        return 'Monster Truck'


class ToyCarBuilder(Builder):

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 1
        return wheel

    def get_engine(self):
        engine = Engine15V()
        return engine

    def get_body(self):
        body = PlasticBody()
        body.shape = "Viper"
        return body

    def get_model(self):
        return 'Toy Car'


# Car parts

@dataclass
class Wheel:
    size = None


class TrackWheel(Wheel):
    size = 1000


class Engine:
    horsepower = None


class RocketFuelEngine(Engine):
    horsepower = 999999


class Engine15V(Engine):
    horsepower = 0.1


class Body:
    shape = None


class HardSteelBody(Body):
    material = 'Steel'


class PlasticBody(Body):
    kids_safe = True


def main():
    director = Director()

    for builder in JeepBuilder(), MonsterTruckBuilder(), ToyCarBuilder():
        director.set_builder(builder)
        car = director.get_car()
        car.specification()

    director.set_builder(MonsterTruckBuilder())
    my_car = director.get_no_wheeled_car()

    my_own_awesome_wheels_i_got_from_black_market = namedtuple('Wheel', ['size'])
    for wheel in range(4):
        my_car.attach_wheel(my_own_awesome_wheels_i_got_from_black_market)

    my_car.specification()


if __name__ == "__main__":
    main()
