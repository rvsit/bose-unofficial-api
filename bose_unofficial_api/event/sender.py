from .observer import Observer


class Sender:
    """
    Class to send NOTIFY events to the event listeners
    """

    _observers: list[Observer] = []

    def add_observer(self, observer: Observer):
        """
        Add an observer to the list of observers
        """
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        """
        Remove an observer from the list of observers
        """
        self._observers.remove(observer)

    def send_message(self, message):
        """
        Send a message to all observers
        """
        for observer in self._observers:
            observer.on_message(message)
