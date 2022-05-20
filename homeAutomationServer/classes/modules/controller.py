from .module import *


class Controller(Module):
	"""
		class bringing all the information and functionality of an controller.

			Parammetters:
				module node: network node of the module

			Attributes:
				type: type of module (controller)

			Propertys:

			Methods:
				serialize (allows to transform the class in dict for json use)
	"""

	def __init_(self, moduleNode):
		Module.__init__(self, moduleNode)
		self.type = "controller"