from .fakeNode import *
from .fakeController import *

class FakeZwaveNetwork:
	def __init__(self, homeId, state, ready):
		"""
			class created for substitute the zwaveNetwork class
			during the test
		"""
		self.home_id = homeId
		self.state = state
		self.is_ready = ready
		self.nodes = {'0001': FakeNode(1, "bulb", "bulb"), '002': FakeNode(2, "light", "bulb")}
		self.controller = FakeController(FakeNode(3, "main controller","controller"))

	def write_config(self):
		pass
