

class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print('{} got message "{}"'.format(self.name, msg))


class Publisher:
    def __init__(self, events):
        self.subscribers = {event: dict()
                            for event in events}

    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')

        self.subscribers[event][who] = callback

    def unregister(self, event, who):
        del self.subscribers[event][who]

    def dispatch(self, event, msg):
        for subscriber, callback in self.subscribers[event].items():
            callback(msg)
