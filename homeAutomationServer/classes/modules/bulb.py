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
    	pass


    @property
    def lightUp(self):
    	"""
			property representing if the light is on or not

				return: False/True
		"""

		pass

	@property
	def intensity(self):
		"""
			property representing the light intensity level

				return: int
		"""

		pass


	def on(self):
		"""
			method called for light up the bulb
		"""

		pass

	def off(self):
		"""
			method called for light down the bulb
		"""

		pass

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

		pass


	def serialize(self):
    	"""
    		method called for seriallize data of the class
    	"""

    	pass