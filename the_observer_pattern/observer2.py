

class SubscriberOne:
    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print('{} got message "{}"'.format(self.name, msg))


class SubscriberTwo:
    def __init__(self, name):
        self.name = name

    def receive(self, msg):
        print('{} got message "{}"'.format(self.name, msg))


class Publisher:
    def __init__(self):
        self.subscribers = dict()

    def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')

        self.subscribers[who] = callback

    def unregister(self, who):
        del self.subscribers[who]

    def dispatch(self, msg):
        for subscriber, callback in self.subscribers.items():
            callback(msg)
