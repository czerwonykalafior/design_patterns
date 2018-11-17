import abc


class QuackStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def quack(self):
        pass


class LoudQuackStrategy(QuackStrategyAbstract):
    def quack(self):
        print("QUACK! QUACK!")


class GentleQuackStrategy(QuackStrategyAbstract):
    def quack(self):
        print("quack...")


class LightStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def light_on(self):
        pass


class OnForTenSecStrategy(LightStrategyAbstract):
    def lights_on(self):
        print("Lights on fo 10 sec . . .")
