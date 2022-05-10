from .room import *

class Kitchen(Room):
	'''
        class bringing all the information and functionality of an kitchen
			
			Parametters:
				id: identifiant of the room
				name: name of the room
				type: type of room(kitchen)
				automation network
    '''

	def __init__(self, id, name, Type, automationNetwork):
		Room.__init__(self, id, name, "kitchen", automationNetwork)
