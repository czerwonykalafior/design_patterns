from the_observer_pattern.observer1 import Publisher, Subscriber


pub = Publisher()

bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

pub.register(bob)
pub.register(alice)
pub.register(john)

pub.dispatch("It's lunch time!!")

pub.unregister(john)

pub.dispatch("tTime for dinner!!")