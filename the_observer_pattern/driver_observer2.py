from the_observer_pattern.observer2 import Publisher, SubscriberOne, SubscriberTwo


pub = Publisher()

bob = SubscriberOne('Bob')
alice = SubscriberTwo('Alice')
john = SubscriberOne('John')

pub.register(bob)
pub.register(alice, alice.receive)
pub.register(john)

pub.dispatch("It's lunch time!!")

pub.unregister(john)

pub.dispatch("tTime for dinner!!")