import unittest

from homeAutomationServer.classes.rooms.room import *
from ..fakeClasses.zwaves.fakeZwaveNetwork import *

class Test_Room(unittest.TestCase):
	"""
		testing class of an room.

		tests list:
			serialize:
				test if the data was conform
	"""

	def setUp(self):
		self.room = Room(1, "test", "bedroom", FakeZwaveNetwork(1, True, True))



	def test_serialize(self):
		"""
			test if the data was conform
		"""

		data = self.room.serialize()
		assert data is not False
		assert data["id"] == 1
		assert data["name"] == "test"
		assert data["type"] ==  "bedroom"
		assert isinstance(data["content"], list)
		assert data["temperature"] == "NULL"
		assert data["luminosity"] == "NULL"