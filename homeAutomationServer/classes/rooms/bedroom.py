from .room import *

class Bedroom(Room):
	'''
        class bringing all the information and functionality of an bedroom
			
			Parametters:
				id: identifiant of the room
				name: name of the room
				type: type of room(bedroom)
				automation network
    '''

	def __init__(self, id, name, Type, automationNetwork):
		Room.__init__(self, id, name, "bedroom", automationNetwork)
