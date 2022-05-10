from .room import *

class Corridor(Room):
	'''
        class bringing all the information and functionality of an corridor
			
			Parametters:
				id: identifiant of the room
				name: name of the room
				type: type of room(corridor)
				automation network
    '''

	def __init__(self, id, name, Type, automationNetwork):
		Room.__init__(self, id, name, "corridor", automationNetwork)
