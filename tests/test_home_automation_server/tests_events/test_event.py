import unittest

from homeAutomationServer.classes.events.event import *

class Test_event(unittest.TestCase):
    """
        testing class of an event

            test list:

    """

    def setUp(self):
        self.event = Event("motion detection", "01/01/01", 1)

    def test_serialize(self):
        data = self.event.serialize()
        assert data is not False
        assert isinstance(data, dict)
        assert data["type"] == 'motion detection'
        assert data["dateTime"] == '01/01/01'
        assert data["location"] == 1