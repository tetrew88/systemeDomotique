class Color:
	"""
		class bringing all the information and functionality of an color.

			Parammetters:
				name: name of the color
				rgb value: rgb code of the color
				rgbw value: rgbw code of the color

			Attributes:
				name: name of the color
				rgb value: rgb code of the color
				rgbw value: rgbw code of the color

			Method:
				serialize (allows to transform the class in dict for json use)
	"""

	def __init__(self, name, rgbValue, rgbwValue):
		self.name = name
		self.rgbValue = rgbValue
		self.rgbwValue = rgbwValue


	def serialize(self):
		"""
			method called for seriallize data of the class
		"""

		data = {}

		data = {'name': self.name,
				'rgbValue': self.rgbValue,
				'rgbwValue': self.rgbwValue}

		return data