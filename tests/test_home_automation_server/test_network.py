import unittest

from homeAutomationServer.classes.network import *
from homeAutomationServer.classes.events.event import *

class FakeNode:
	def __init__(self, id, deviceType, cmdClass):
		self.node_id = id
		self.device_type = deviceType
		self.command_classes_as_string = cmdClass
		self.name = ""
		self.location = ""

	def set_field(self, field, fieldData):
		if field == 'name':
			self.name = fieldData
		if field == 'location':
			self.location = fieldData


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


class FakeController():
	def __init__(self, node):
		self.node = node
		self.id = self.node.node_id
		self.zwaveNetwork = False

	def add_node(self):
		key = len(self.zwaveNetwork.nodes) + 2
		self.zwaveNetwork.nodes[key] = FakeNode(key, "bulb", "light système")

	def remove_node(self):
		self.zwaveNetwork.nodes.pop('0001')


class Test_Network(unittest.TestCase):
	"""
		testing class of the network.

		tests list:
			home id property:
				check return: check if method return good type of data
			state property:
				check return: check if method return good type of data
			isReady property:
				check return: check if method return good type of data
			module list property:
				check return: check if method return good type of data
			main controller property:
				check return: check if method return good type of data
			controller list property:
				check return: check if method return good type of data

			start method:
				home automation network Starting: test if the home automation network was started

			stop method:
				home automation network Stop: test if the home automation network was stoped

			get module:
				check return: check if method return good type of data

			add module:
				test with good parametters: test if the method works correctly
				test with bad name: test if the method detect the bad parammeters
				test with bad location: test if the method detect the bad parammeters

			del module:
				test with good parametters: test if the method works correctly
				test with bad parametters: test if the method detect the bad parammeters

			set module name:
				test with good parametters: test if the method works correctly
				test with bad module id parametters: test if the method detect the bad parammeters
				test with bad module Name parametters: test if the method detect the bad parammeters
			set module location:
				test with good parametters: test if the method works correctly
				test with bad module id parametters: test if the method detect the bad parammeters
				test with bad module location parametters: test if the method detect the bad parammeters

			serialize:
				test if the data was conform
	"""

	def setUp(self):
		self.network = Network()
		self.goodZWaveNetwork = FakeZwaveNetwork(10, 10, True)
		self.badZWaveNetwork = FakeZwaveNetwork(10, 1, False)

	def test_homeId_property(self):
		"""
			check if method return good type of data
		"""
		#test with zwaveNework corectly configured
		self.network.zWaveNetwork = self.goodZWaveNetwork
		assert isinstance(self.network.homeId, int)
		assert self.network.homeId == 10

		#test with zwaveNetwork uncorrectly configured
		self.network.zWaveNetwork = self.badZWaveNetwork
		assert isinstance(self.network.homeId, int)
		assert self.network.homeId == 10

		#test with failure zwaveNetwork
		self.network.zWaveNetwork = False
		assert isinstance(self.network.homeId, bool)
		assert self.network.homeId is False

	def test_state_property(self):
		"""
			check if method return good type of data
		"""

		# test with zwaveNework corectly configured
		self.network.zWaveNetwork = self.goodZWaveNetwork
		assert isinstance(self.network.state, int)
		assert self.network.state == 10

		# test with zwaveNetwork uncorrectly configured
		self.network.zWaveNetwork = self.badZWaveNetwork
		assert isinstance(self.network.state, int)
		assert self.network.state == 1

		# test with failure zwaveNetwork
		self.network.zWaveNetwork = False
		assert isinstance(self.network.state, bool)
		assert self.network.state is False

	def test_isReady_property(self):
		"""
			check if method return good type of data
		"""

		# test with zwaveNework corectly configured
		self.network.zWaveNetwork = self.goodZWaveNetwork
		assert isinstance(self.network.isReady, bool)
		assert self.network.isReady is True

		# test with zwaveNetwork uncorrectly configured
		self.network.zWaveNetwork = self.badZWaveNetwork
		assert isinstance(self.network.isReady, bool)
		assert self.network.isReady is False

		# test with failure zwaveNetwork
		self.network.zWaveNetwork = False
		assert isinstance(self.network.isReady, bool)
		assert self.network.isReady is False

	def test_modules_list_property(self):
		"""
			check if method return good type of data
		"""
		# test with zwaveNework corectly configured
		self.network.zWaveNetwork = self.goodZWaveNetwork
		moduleList = self.network.modulesList
		assert len(moduleList) == 3

		# test with zwaveNetwork uncorrectly configured
		self.network.zWaveNetwork = self.badZWaveNetwork
		moduleList = self.network.modulesList
		assert len(moduleList) == 0

		# test with failure zwaveNetwork
		self.network.zWaveNetwork = False
		moduleList = self.network.modulesList
		assert len(moduleList) == 0

	def test_mainController_property(self):
		"""
			check if method return good type of data
		"""
		# test with zwaveNework corectly configured
		self.network.zWaveNetwork = self.goodZWaveNetwork
		assert isinstance(self.network.mainController, FakeController)

		# test with zwaveNetwork uncorrectly configured
		self.network.zWaveNetwork = self.badZWaveNetwork
		assert isinstance(self.network.mainController, FakeController)

		# test with failure zwaveNetwork
		self.network.zWaveNetwork = False
		assert self.network.mainController is False

	def test_get_controller_path(self):
		assert isinstance(self.network.controllerPath, str)

	def test_get_Zwave_config_path(self):
		assert isinstance(self.network.zwaveConfigPath, str)


	def test_get_module(self):
		"""
			check if method return good type of data
		"""
		self.network.zWaveNetwork = self.goodZWaveNetwork

		#test with good Id
		assert self.network.get_module(1).id == 1

		#test with bad Id
		assert self.network.get_module(4) is False

		# test with zwaveNetwork uncorrectly configured
		self.network.zWaveNetwork = self.badZWaveNetwork
		assert self.network.get_module(1) is False

		#test with failure zwaveNetwork
		self.network.zWaveNetwork = False
		assert self.network.get_module(1) is False

	def test_add_module(self):
		#test with good parametters and zwaveNetwork: test if the method works correctly
		self.network.zWaveNetwork = self.goodZWaveNetwork
		self.network.zWaveNetwork.controller.zwaveNetwork = self.network.zWaveNetwork

		assert self.network.add_module("test1", 1) is True

		succes = False

		for module in self.network.modulesList:
			if module.name == "test1":
				succes = True
				break
			else:
				succes = False

		assert succes is True

		#test with bad name
		assert self.network.add_module(int(1), 1) is False

		# test with bad location
		assert self.network.add_module("test2", "1") is False

		# test with zwaveNetwork uncorrectly configured
		self.network.zWaveNetwork = self.badZWaveNetwork
		assert self.network.add_module("test3", 1) is False

		# test with failure zwaveNetwork
		self.network.zWaveNetwork = False
		assert self.network.add_module("test4", 1) is False

	def test_add_event(self):
		self.network.zWaveNetwork = self.goodZWaveNetwork

		#test with good parametters
		assert self.network.add_event(Event("test1", "01/01/01 01:01:01", 1)) == True

		#test with bad parametters
		assert self.network.add_event(1) == False
		assert self.network.add_event(Event(1, "01/01/01 01:01:01", 1)) == False
		assert self.network.add_event(Event("test2", 1, 1)) == False
		assert self.network.add_event(Event("test3", "01/01/01 01:01:01", 100000)) == False

'''
	def test_set_automation_network_controller_path(self):
		# test with good parametter
		self.network.zWaveNetwork = self.goodZWaveNetwork
		assert self.network.set_automation_network_controller_path('/dev/test1') == True

		# test with bad parametter
		assert self.network.set_automation_network_controller_path(1) == False

	def test_set_Zwave_config_path(self):
		# test with good parametter
		self.network.zWaveNetwork = self.goodZWaveNetwork
		assert self.network.set_Zwave_config_path('/dev/test2') == True
		
		# test with bad parametter
		assert self.network.set_Zwave_config_path(2) == False
'''

'''
	def test_del_module(self):
		#test with good parameters and good zwaveNetwork
		self.network.zWaveNetwork = self.goodZWaveNetwork
		self.network.zWaveNetwork.controller.zwaveNetwork = self.network.zWaveNetwork

		assert self.network.del_module(1) == True
'''
