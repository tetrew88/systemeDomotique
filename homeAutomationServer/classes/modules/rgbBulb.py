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
		Bulb.__init__(self, moduleNode)
		self.colorPalette = [Color("rouge", '#FF0000', '#FF00000000'),
							 Color("blanc", '#FFFFFF', '#FFFFFF0000'),
							 Color("bleu", "#0000FF", '#0000FF0000'),
							 Color("vert", "#008000", "#0080000000")]
		self.type = 'rgb bulb'


	@property
	def color(self):
		"""
			property representing the color of the light

				return: False/True
		"""

		for values in self.moduleNode.get_rgbbulbs().values():
			if values.label == 'Color':
				for element in self.colorPalette:
					if values.data == element.rgbwValue:
						return element


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

		valuesId = ""

		for values in self.moduleNode.get_rgbbulbs().values():
			if values.label == 'Color':
				valueId = values.value_id

		self.moduleNode.set_rgbw(valueId, newColor.rgbwValue)

		if self.color.name == newColor.name:
			return True
		else:
			return False


	def serialize(self):
		"""
			method called for seriallize data of the class
		"""

		data = {}

		colorPalette = []

		for color in self.colorPalette:
			colorPalette.append(color.serialize())

		data = {'id': self.id,
				'name': self.name,
				'location': self.location,
				"awake": self.isAwake,
				"disfunctionnement": self.isFailed,
				"ready": self.isReady,
				"sleep": self.isSleeping,
				"manufacturer name": self.manufacturerName,
				"product name": self.productName,
				"product type": self.productType,
				"system type": self.deviceType,
				"type": self.type,
				"lightUp": self.lightUp,
				"intensity": self.intensity,
				"color": self.color.serialize(),
				"color palette": colorPalette
				}

		return data
