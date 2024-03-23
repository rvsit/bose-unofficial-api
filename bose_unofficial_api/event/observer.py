from __future__ import annotations

from abc import abstractmethod


class Observer:
    """
    Observer class is used to listen for events from the speaker.
    """

    @abstractmethod
    def on_message(self, message):
        """
        This method is called when a message is received from the speaker.
        """
