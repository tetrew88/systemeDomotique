class Door_WindowEvent(ModuleEvent):
	"""
		class bringing all the information and functionality of an door/windows event
			Parametters:
				module; module responsible for the event
				datetime: datetime of the event
				door/window state: state of the door/window
				event type: type of event

			Attributes:
				door/window state: state of the door/window

			property:

			method:
				str

	"""

	def __init__(self, module, datetime, door_windowState, eventType = "window/door event"):
		pass

	def __str__(self):
		pass


class Door_WindowOpening(Door_WindowEvent):

	def __init__(self, module, datetime):
		pass


	def __str__(self):
		pass


class Door_WindowClosing(Door_WindowEvent):
	def __init__(self, module, datetime):
		pass

	def __str__(self):
		pass