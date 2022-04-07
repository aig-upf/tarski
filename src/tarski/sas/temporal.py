"""
    Temporal (durative) actions for SAS+
"""
from tarski.sas import Action


class TemporalAction:
    """
    Temporal action where events are given as SAS+ actions
    """
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.events = []
        self.deltas = []

        for delta, evt in kwargs.get('events', []):
            self.events += [evt]
            self.deltas += [delta]

    @property
    def start(self) -> Action:
        """
            First event in temporal action
        """
        return self.events[0]

    @property
    def end(self) -> Action:
        """
            Last event in temporal action
        :return:
        """
        return self.events[-1]

    @property
    def duration(self):
        """
        Duration of the temporal action
        :return:
        """
        return sum(self.deltas)

    def add_event(self, d: float, evt: Action) -> None:
        """
        Adds new event to temporal action
        :return:
        """
        self.deltas += [d]
        self.events += [evt]
