class Module:
	'''
		class bringing all the information and functionality of an module

			Parametters:
				moduleNode; network node of the module
				
			attributes:
				moduleNode; network node of the module
				type: type of module (bulb, captor, ...)

			property:
				id: id of the module
				name: name of the element
				location: location of the element

				is awake: control boolean to know if the module is awake
				is failed: control boolean to know if the module is failed
				is ready: control boolean to know if the module is ready
				is sleeping: control boolean to know if the module is sleeping

				#manufacturer informations
					manufacturer name
					product name
					product type
					device type

			methods:
				set name: allows to modify the name of the element
				set location: allows to modify the location of the element

				heal: allows to heal the modules

				serialize (allows to transform the class in dict for json use)
	'''

	def __init__(self, moduleNode):
		self.moduleNode = moduleNode
		self.type = "module"


	@property
	def id(self):
		"""
			property representing the module identifier

				return: int
		"""
		return self.moduleNode.node_id

	@property
	def name(self):
		"""
			property representing the name of the module

				return: str
		"""

		return self.moduleNode.name

	@property
	def location(self):
		"""
			property representing the location of the module (room id)

				return: int
		"""

		location = 0

		try:
			location = int(self.moduleNode.location)
		except:
			location = 0

		return location

	@property
	def isAwake(self):
		"""
			property representing if the module is awake or not

				return: False/True
		"""

		pass

	@property
	def isFailed(self):
		"""
			property representing if the module is failed or not

				return: False/True
		"""

		pass

	@property
	def isReady(self):
		"""
			property representing if the module is ready or not

				return: False/True
		"""

		pass

	@property
	def isSleeping(self):
		"""
			property representing if the module is sleeping or not

				return: False/True
		"""

		pass

	@property
	def manufacturerName(self):
		"""
			property representing the manufacturer name of the module

				return: False/True
		"""

		pass

	@property
	def productName(self):
		"""
			property representing the product name of the module

				return: False/True
		"""

		pass

	@property
	def productType(self):
		"""
			property representing the product type of the module

				return: False/True
		"""

		pass

	@property
	def deviceType(self):
		"""
			property representing the device type of the module

				return: False/True
		"""

		pass


	def set_name(self, newName):
		"""
			methods called for set an module's name.

				Parametters:
					newName: str

				functionning:
					set the module's name
						if the module's name was correctly modified:
							return True
						else:
							return False

				return:
					succes: True/False
		"""
		succes = False

		if isinstance(newName, str):
			self.moduleNode.set_field('name', newName)
			succes = True
		else:
			succes = False

		if self.name == newName:
			succes = True
		else:
			succes = False

		return succes

	def set_location(self, newLocation):
		"""
			methods called for set an module's location.

				Parametters:
					moduleId: int
					newLocation: int(roomId)

				functionning:
					transtype location to str for compatiblities

					set the module's location
						if the module's location was correctly modified:
							return True
						else:
							return False

				return:
					succes: True/False
		"""
		succes = False

		if isinstance(newLocation, int):
			self.moduleNode.set_field('location', str(newLocation))
			succes = True
		else:
			succes = False

		if self.location == newLocation:
			succes = True
		else:
			succes = False

		return succes


	def heal(self):
		"""
			method call for heal the module
		"""

		pass


	def serialize(self):
		"""
			method called for seriallize data of the class
		"""

		pass