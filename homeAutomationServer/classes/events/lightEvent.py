class LightEvent(ModuleEvent):
	"""
		class bringing all the information and functionality of an light event
			Parametters:
				module; module responsible for the event
				datetime: datetime of the event
				light state: state of the light
				event type: type of event

			Attributes:
				light state: state of the light

			property:

			method:
				str

	"""

	def __init__(self, moduleNode,datetime, bulbState, eventType = "light evenement"):
		pass


class LightOn(LightEvent):
	def __init__(self, moduleNode, datetime):
		pass

	def __str__(self):
		pass

class LightOff(LightEvent):
	def __init__(self, moduleNode, datetime):
		pass

	def __str__(self):
		pass
