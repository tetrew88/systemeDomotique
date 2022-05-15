import unittest

from homeAutomationServer.classes.modules.module import *
from ..fakeClasses.zwaves.fakeNode import *

class Test_Module(unittest.TestCase):
	"""
        testing class of an event

    """

	def setUp(self):
		self.module = Module(FakeNode(1, "test", "test"))


	def test_serialize(self):
		data = self.module.serialize()
		assert data is not False
		assert data['id'] == 1
		assert data['name'] == 'test'
		assert data['location'] == 1
		assert data["awake"] == True
		assert data["disfunctionnement"] == False
		assert data["ready"] == True
		assert data["sleep"] ==  False
		assert data["manufacturer name"] ==  "test"
		assert data["product name"] == "test"
		assert data["product type"] == "test"
		assert data["system type"] ==  "test"
		assert data["type"] ==  "module"