class Sensor():
    def __init__(self):
        self.engine_list = []
        self.active = False
        self.pin = 0

    def subscribe(self, engine):
        self.engine_list.append(engine)

    def unscribe(self, engine):
        self.engine_list.remove(engine)

    def notify(self):
        for engine in self.engine_list:
            engine.update()