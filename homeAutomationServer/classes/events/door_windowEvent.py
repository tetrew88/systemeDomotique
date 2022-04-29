from .moduleEvent import *


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

	def __init__(self, moduleNode, datetime, door_windowState, eventType="window/door event"):
		ModuleEvent.__init__(self, moduleNode, eventType, datetime)
		self.door_windowState = door_windowState

	def __str__(self):
		return "[{}]: {}".format(self.dateTime, self.type)


class Door_WindowOpening(Door_WindowEvent):

	def __init__(self, moduleNode, datetime):
		Door_WindowEvent.__init__(self, moduleNode, datetime, 'open', "door/window opening")

	def __str__(self):
		return "[{}]: la porte/fenètre n°{} a été ouverte".format(self.dateTime, self.moduleNode.node_id)


class Door_WindowClosing(Door_WindowEvent):
	def __init__(self, moduleNode, datetime):
		Door_WindowEvent.__init__(self, moduleNode, datetime, 'closed', "door/window closing")

	def __str__(self):
		return "[{}]: la porte/fenètre n°{} a été fermé".format(self.dateTime, self.moduleNode.node_id)