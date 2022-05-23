from .module import *


class Bulb(Module):
	"""
		class bringing all the information and functionality of an bulb.

			Parammetters:
				module node: network node of the module

			Attributes:
				type: type of module (bulb)

			Propertys:
				light up: control booléean for know if the light is on
				intensity: intensity level of the light

			Methods:
				on: allow to light up the bulb
				off: allow to light down the bulb

				set intensity: allows to set the intensity of the light

				serialize (allows to transform the class in dict for json use)
    """

	def __init__(self, moduleNode):
		Module.__init__(self, moduleNode)
		self.type = 'bulb'

	@property
	def lightUp(self):
		"""
			property representing if the light is on or not

				return: False/True
		"""

		if self.intensity > 0:
			return True
		else:
			return False

	@property
	def intensity(self):
		"""
			property representing the light intensity level

				return: int
		"""

		for values in self.moduleNode.get_dimmers().values():
			if values.label == 'Level':
				return values.data


	def on(self, intensity = 50):
		"""
			method called for light up the bulb
		"""

		self.set_intensity(intensity)

	def off(self):
		"""
			method called for light down the bulb
		"""

		self.set_intensity(0)

	def set_intensity(self, newIntensity):
		"""
			Method called for set the light intensity level.

			Parametters:
				newIntensity: int

			functionning:
				check if newIntensity is int type
					if it is:
						ask to node change the intensity value
		"""

		if isinstance(newIntensity, int):
			for values in self.moduleNode.get_dimmers().values():
				if values.label == 'Level':
					valueId = values.value_id
					break

			self.moduleNode.set_dimmer(valueId, newIntensity)
			return True
		else:
			return False


	def serialize(self):
		"""
			method called for seriallize data of the class
		"""

		data = {}

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
				"intensity": self.intensity
				}

		return data