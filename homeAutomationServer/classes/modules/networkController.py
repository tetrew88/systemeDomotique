from .module import *


class NetworkController(Module):
	"""
		class bringing all the information and functionality of an network controller.

			Parammetters:
				module node: network node of the module

			Attributes:
				type: type of module (networkController)

			Propertys:

			Methods:
				hard reset: allows to hard reset the controller
				soft reset: allows to soft reset the controller

				add node: allows to add node (start inclusion mode)
				remove node: allows to remove node (start exclusion mode)

				serialize (allows to transform the class in dict for json use)
	"""

	def __init__(self, moduleNode):
		Module.__init__(self, moduleNode)
		self.type = 'network controller'


	def hard_reset(self):
		"""
			method called for hard reset the controller
		"""

		pass


	def soft_reset(self):
		"""
			Method called for soft reset the controller
		"""

		pass


	def add_node(self):
		"""
			method called to put the controller into inclusion mode
		"""

		self.moduleNode.add_node()

	def remove_node(self):
		self.moduleNode.remove_node()