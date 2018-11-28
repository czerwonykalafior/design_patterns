

class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print('{} got message "{}"'.format(self.name, msg))


class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, msg):
        for subscriber in self.subscribers:
            subscriber.update(msg)
