from .module import *
from .bulb import *
from .color import *

class RgbBulb(Bulb):
	"""
		class bringing all the information and functionality of an rbgBulb.

			Parammetters:
				module node: network node of the module

			Attributes:
				type: type of module (rbgBulb)
				color palette: list of color class

			Propertys:
				color: allow to know the actual color of the light

			Methods:
				set color: allow to set the color of the light 
				serialize (allows to transform the class in dict for json use)
	"""

	def __init__(self, moduleNode):
		pass


	@property
	def color(self):
		"""
			property representing the color of the light

				return: False/True
		"""

		pass


	def set_color(self, newColor):
		"""
			Method called for set the color light.

			Parametters:
				newColor: color class

			functionning:
				check if newColor is color instance
					if it is:
						ask to node change the color
		"""

		pass


	def serialize(self):
		"""
			method called for seriallize data of the class
		"""

		pass
