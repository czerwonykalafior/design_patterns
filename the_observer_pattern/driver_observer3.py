from the_observer_pattern.observer3 import Publisher, Subscriber


pub = Publisher(['lunch', 'diner'])

bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

pub.register('lunch', bob)
pub.register('diner', alice)
pub.register('lunch', john)
pub.register('diner', john)

pub.dispatch('lunch', "It's lunch time!!")

pub.unregister('diner', john)

pub.dispatch('diner', "Time for dinner!!")