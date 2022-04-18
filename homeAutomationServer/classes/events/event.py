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

	def __init__(self):
		pass


	def serialize(self):
    	"""
    		method called for seriallize data of the class
    	"""

    	pass