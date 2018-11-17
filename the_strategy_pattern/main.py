from the_strategy_pattern.strategy import LoudQuackStrategy
from the_strategy_pattern.strategy import GentleQuackStrategy
from the_strategy_pattern.strategy import OnForTenSecStrategy


loud_quack = LoudQuackStrategy()
gentle_quack = GentleQuackStrategy()
ten_sec = OnForTenSecStrategy()


class Duck(object):
    def __init__(self, quack_strategy, light_strategy):
        self._quack_strategy = quack_strategy
        self._light_strategy = light_strategy

    def quack(self):
        self._quack_strategy.quack()

    def lights_on(self):
        self._light_strategy.lights_on()


# Po o te wszystkie dzedziczenia? z go_home() mozna trzebaby tez robic strategy i przy tworzeniu instancji Duck podawac
# rozne abstracty. Zobacz line 52.
class VillageDuck(Duck):
    def __init__(self):
        super(VillageDuck, self).__init__(loud_quack, None)

    def go_home(self):
        print("Going to the river")


class ToyDuck(Duck):
    def __init__(self):
        super(ToyDuck, self).__init__(gentle_quack, ten_sec)


class CityDuck(Duck):
    def __init__(self):
        super(CityDuck, self).__init__(gentle_quack, None)

    def go_home(self):
        print("Going to the Central Park pond")


class RobotDuck(Duck):
    def __init__(self):
        super(RobotDuck, self).__init__(loud_quack, ten_sec)


def main():
    robot = Duck(loud_quack, ten_sec)
    # robot = RobotDuck()
    robot.quack()
    robot.lights_on()


if __name__ == '__main__':
    main()
