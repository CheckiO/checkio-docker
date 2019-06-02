class Container(object):
    def __init__(self, container, connection):
        self._container = container
        self._connection = connection

    @property
    def id(self):
        return self._container.id

    def start(self):
        self._container.start()

    def stop(self):
        self._container.stop()

    def remove(self):
        self._container.remove()

    def logs(self, stream=False, logs=False):
        return self._container.logs(stream=stream)