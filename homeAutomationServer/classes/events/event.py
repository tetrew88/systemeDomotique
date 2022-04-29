class Event:
	"""
		class bringing all the information and functionality of an event

			Parametters:
				type: type of event (motion detection, light on, ...) (str)
				datetime: datetime of the event (str)
				location: location of the event

			Attributes:
				type: type of event (motion detection, light on, ...) (str)
				datetime: datetime of the event (str)
				location: location of the event

			methods:
				serialize (allows to transform the class in dict for json use)
	"""

	def __init__(self, Type, dateTime, location, id=0):
		self.id = id
		self.type = Type
		self.dateTime = dateTime
		self.location = location


	def serialize(self):
		"""
    		method called for seriallize data of the class
    	"""

		data = {}

		data = {'type': self.type,
        'dateTime': self.dateTime,
        'location': self.location,
        'str': self.__str__()
        }

		return data

	def __str__(self):
		return "[{}]: {}".format(self.dateTime, self.type)