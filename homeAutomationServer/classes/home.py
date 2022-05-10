from .network import *

from .homeDatabase import *

from .events.event import *
from .events.motionDetection import *

from .rooms.room import *
from .rooms.bedroom import *
from .rooms.kitchen import *
from .rooms.bathroom import *
from .rooms.livingroom import *
from .rooms.corridor import *

from .users.profil import *
from .users.inhabitant import *
from .users.guest import *


class Home:
	"""
		class bringing all the information and functionality of the home.

			Parammetters:

			Attributes:
				home database (database containing home information)
                home automation network (z-wave network)

			Propertys:
				id (id of the home)

                rooms list (list of room contained in the home database)
                inhabitants list (list of inhabitant contained in the home database)
                guests list (list of guest contained in the home database)
                profils list (list of profil contained in the home database)
                events list (list of events contained in the home database)

                modules list (list of module contained in the automation network)

			Methods:
				get room (allows to retrieve a specific room in the home database)

				get inhabitant (allows to retrieve a specific inhabitant in the home database)
				get guest (allows to retrieve a specific guest in the home database)
				get profil (allows to retrieve a specific profil in the home database)

				get automation network (allows to retrieve the home automation network class (zwave network))
				get module (allows to retrieve a specific module on the network)

				get event (allows to retrieve a specific event)
	"""

	def __init__(self):
		self.homeDatabase = HomeDatabase()
		self.homeAutomationNetwork = Network()


	@property
	def id(self):
		"""
			property representing the home identifier

				return: int
		"""

		if self.homeAutomationNetwork != False and self.homeAutomationNetwork.isReady:
			return self.homeAutomationNetwork.homeId
		else:
			return False

	@property
	def roomsList(self):
		"""
    		property representing list of rooms contained in the home.

				functionning:
					asks the database to list the rooms

    			return:
    				list of room classes
    	"""

		tmpRooms = rooms = []
		if self.homeDatabase.db_connection is not False:
			tmpRooms = self.homeDatabase.get_rooms_list()

			if tmpRooms is not False:
				for room in tmpRooms:
					if room[2].lower() == "bathroom":
						tmpRoom = Bathroom(room[0], room[1], room[2], self.homeAutomationNetwork)
					elif room[2].lower() == "bedroom":
						tmpRoom = Bedroom(room[0], room[1], room[2], self.homeAutomationNetwork)
					elif room[2].lower() == "kitchen":
						tmpRoom = Kitchen(room[0], room[1], room[2], self.homeAutomationNetwork)
					elif room[2].lower() == "livingroom":
						tmpRoom = Livingroom(room[0], room[1], room[2], self.homeAutomationNetwork)
					elif room[2].lower() == "corridor":
						tmpRoom = Corridor(room[0], room[1], room[2], self.homeAutomationNetwork)
					else:
						tmpRoom = Room(room[0], room[1], room[2], self.homeAutomationNetwork)

					rooms.append(tmpRoom)
			else:
				return False
		else:
			return False

		return rooms

	@property
	def inhabitantsList(self):
		"""
    		property representing list of inhabitants contained in the home.

				functionning:
					asks the database to list the inhabitants

    			return:
    				list of inhabitants classes
    	"""

		tmpInhabitants = inhabitants = []

		if self.homeDatabase.db_connection is not False:
			tmpInhabitants = self.homeDatabase.get_inhabitants_list()

			if tmpInhabitants is not False:
				for inhabitant in tmpInhabitants:
					tmpProfil = self.homeDatabase.get_profil(inhabitant[1])

					profil = Profil(tmpProfil[0], tmpProfil[1], tmpProfil[2], tmpProfil[3], tmpProfil[4])

					tmpInhabitant = Inhabitant(inhabitant[0], profil)

					inhabitants.append(tmpInhabitant)
			else:
				return False
		else:
			return False

		return inhabitants

	@property
	def guestsList(self):
		"""
    		property representing list of guests contained in the home.

				functionning:
					asks the database to list the guests

    			return:
    				list of guests classes
    	"""

		tmpGuests = guests = []

		if self.homeDatabase.db_connection is not False:
			tmpGuests = self.homeDatabase.get_guests_list()

			if tmpGuests is not False:
				for guest in tmpGuests:
					tmpProfil = self.homeDatabase.get_profil(guest[1])

					profil = Profil(tmpProfil[0], tmpProfil[1], tmpProfil[2], tmpProfil[3], tmpProfil[4])

					tmpGuest = Guest(guest[0], profil)

					guests.append(tmpGuest)
			else:
				return False
		else:
			return False

		return guests

	@property
	def profilsList(self):
		"""
    		property representing list of profils contained in the home.

				functionning:
					asks the database to list the profils

    			return:
    				list of profils classes
    	"""

		tmpProfils = profils = []

		if self.homeDatabase.db_connection is not False:
			tmpProfils = self.homeDatabase.get_profils_list()

			if tmpProfils is not False:
				for profil in tmpProfils:

					profil = Profil(profil[0], profil[1], profil[2], profil[3], profil[4])
					profils.append(profil)
			else:
				return False
		else:
			return False

		return profils

	@property
	def eventsList(self):
		"""
    		property representing list of events contained in the home.

				functionning:
					asks the database to list the events

    			return:
    				list of events classes
    	"""

		tmpEvents = events = []

		if self.homeDatabase.db_connection is not False:
			tmpEvents = self.homeDatabase.get_events_list()

			if tmpEvents is not False:
				for event in tmpEvents:
					event = Event(event[1], event[2], event[3], event[0])
					events.append(event)
			else:
				return False
		else:
			return False

		return events

	@property
	def modulesList(self):
		"""
    		property representing list of modules contained in the home.

				functionning:
					asks the automation network to list the module

    			return:
    				list of modules classes
    	"""

		tmpModules = modules = []

		if self.homeAutomationNetwork.isReady:
			tmpModules = self.homeAutomationNetwork.modulesList

			return tmpModules
		else:
			return False


	def get_room(self, roomId):
		"""
    		Method called for get an specific room contains in the home.

				Parametters:
					roomId: int

				functionning:
					-asks the home database to search for the room linked to the id
						if the room was found:
							return the room class
						else:
							return False
    			return:
    				room classes/False
    	"""

		room = False


		if self.homeDatabase.db_connection is not False:
			tmpRoom = self.homeDatabase.get_room(roomId)

			if tmpRoom is not False:
				if tmpRoom[2].lower() == "bathroom":
					room = Bathroom(tmpRoom[0], tmpRoom[1], tmpRoom[2], self.homeAutomationNetwork)
				elif tmpRoom[2].lower() == "bedroom":
					room = Bedroom(tmpRoom[0], tmpRoom[1], tmpRoom[2], self.homeAutomationNetwork)
				elif tmpRoom[2].lower() == "kitchen":
					room = Kitchen(tmpRoom[0], tmpRoom[1], tmpRoom[2], self.homeAutomationNetwork)
				elif tmpRoom[2].lower() == "livingroom":
					room = Livingroom(tmpRoom[0], tmpRoom[1], tmpRoom[2], self.homeAutomationNetwork)
				elif tmpRoom[2].lower() == "corridor":
					room = Corridor(tmpRoom[0], tmpRoom[1], tmpRoom[2], self.homeAutomationNetwork)
				else:
					room = Room(tmpRoom[0], tmpRoom[1], tmpRoom[2], self.homeAutomationNetwork)
			else:
				return False
		else:
			return False

		return room

	def get_inhabitant(self, inhabitantId):
		"""
    		Method called for get an specific inhabitant in the home

    			Parametters:
					inhabitantId: int

				functionning:
					-asks the homeDatabase to search for the inhabitant linked to the id
						if the inhabitant was found:
							return the inhabitant class
						else:
							return False

    			return:
    				inhabitant class/False
    	"""

		inhabitant = profil = False

		if self.homeDatabase.db_connection is not False:
			tmpInhabitant = self.homeDatabase.get_inhabitant(inhabitantId)

			if tmpInhabitant is not False:
				tmpProfil = self.homeDatabase.get_profil(tmpInhabitant[1])

				if tmpProfil is not False:
					profil = Profil(tmpProfil[0], tmpProfil[1],
									tmpProfil[2], tmpProfil[3], tmpProfil[4])

					inhabitant = Inhabitant(tmpInhabitant[0], profil)
				else:
					return False
			else:
				return False
		else:
			return False

		return inhabitant

	def get_guest(self, guestId):
		"""
    		method called for get an specific guest in the home

    			Parametters:
					guestId: int

				functionning:
					-asks the home database to search for the guest linked to the id
						if the guest was found:
							return the guest class
						else:
							return False

    			return:
    				guests class/False
    	"""

		guest = profil = False

		if self.homeDatabase.db_connection is not False:
			tmpGuest = self.homeDatabase.get_guest(guestId)

			if tmpGuest is not False:
				tmpProfil = self.homeDatabase.get_profil(tmpGuest[1])

				if tmpProfil is not False:
					profil = Profil(tmpProfil[0], tmpProfil[1],
									tmpProfil[2], tmpProfil[3], tmpProfil[4])

					guest = Guest(tmpGuest[0], profil)
				else:
					return False
			else:
				return False
		else:
			return False

		return guest

	def get_profil(self, profilId):
		"""
    		method called for get an specific profil in the home

    			Parametters:
					profilId: int

				functionning:
					-asks the home database to search for the profil linked to the id
						if the profil was found:
							return the profil class
						else:
							return False

    			return:
    				profil class/False
    	"""

		profil = False

		if self.homeDatabase.db_connection is not False:
			tmpProfil = self.homeDatabase.get_profil(profilId)

			if tmpProfil is not False:
				profil = Profil(tmpProfil[0], tmpProfil[1],
								tmpProfil[2], tmpProfil[3], tmpProfil[4])
		else:
			return False

		return profil

	def get_module(self, moduleId):
		"""
    		method called for get an specific module on the network

    			Parametters:
					moduleId: int

				functionning:
					-asks the automation network to search for the module linked to the id
						if the module was found:
							return the module class
						else:
							return False

    			return:
    				module class/False
    	"""

		if self.homeAutomationNetwork.isReady:
			return self.homeAutomationNetwork.get_module(moduleId)
		else:
			return False

	def get_event(self, eventId):
		"""
    		method called for get an specific event

    			Parametters:
					eventId: int

				functionning:
					-asks the home database to search for the event linked to the id
						if the event was found:
							return the event class
						else:
							return False

    			return:
    				event class/False
    	"""

		event = False

		if self.homeDatabase.db_connection is not False:
			tmpEvent = self.homeDatabase.get_event(eventId)

			if tmpEvent is not False:
				event = Event(tmpEvent[1], tmpEvent[2], tmpEvent[3])
				print(event)
			else:
				return False
		else:
			return False

		return event


	def add_room(self, roomName, roomType):
		"""
    		method called for adding an room in the home.

    			Parametters:
    				roomName,
    				roomType

    			functionning:
    				asks the home database to add the room
    					if succes:
    						return True
    					else:
    						return False

    			return:
    				succes room id
    				failes: False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.add_room(roomName, roomType)
		else:
			return False

	def add_inhabitant(self, firstName, lastName, sexe, dateOfBirth):
		"""
    		method called for adding an inhabitant in the home.

    			Parametters:
    				firstName
    				lastName
    				sexe
    				dateOfBirth

    			functionning:
    				asks the homeDatabase to add the inhabitant
    					if succes:
    						return True
    					else:
    						return False

    			return:
    				succes inhabitant id
    				failed: False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.add_inhabitant(firstName, lastName, sexe, dateOfBirth)
		else:
			return False

	def add_guest(self, firstName, lastName, sexe, dateOfBirth):
		"""
    		method called for adding an guest in the home.

    			Parametters:
    				firstName
    				lastName
    				sexe
    				dateOfBirth

    			functionning:
    				asks the homeDatabase to add the guest
    					if succes:
    						return True
    					else:
    						return False

    			return:
    				succes guest id
    				failed: False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.add_guest(firstName, lastName, sexe, dateOfBirth)
		else:
			return False

	def add_profil(self, firstName, lastName, sexe, dateOfBirth):
		"""
    		method called for adding an profil in the home.

    			Parametters:
    				firstName
    				lastName
    				sexe
    				dateOfBirth

    			functionning:
    				asks the homeDatabase to add the profil
    					if succes:
    						return True
    					else:
    						return False

    			return:
    				succes profil id
    				failed: False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.add_profil(firstName, lastName, sexe, dateOfBirth)
		else:
			return False

	def add_module(self, newModuleName, newModuleLocation):
		"""
    		method called for adding an module on the network.

    			Parametters:
    				newModuleName: str
    				newModuleLocation: int

    			functionning:
    				ask to automation network adding the module
    					if succes:
    						return True
    					else:
    						return False

    			return:
    				succes (True/False)
    	"""

		if self.homeAutomationNetwork is not False:
			if self.homeAutomationNetwork.isReady:
				moduleId = self.homeAutomationNetwork.add_module(newModuleName, newModuleLocation)
			else:
				return False
		else:
			return False

		return moduleId

	def add_event(self, eventType, eventDatetime, eventLocation):
		"""
    		method called for adding an event in the home.

    			Parametters:
    				eventType
    				eventDatetime
    				eventLocation

    			functionning:
    				asks the home database to add the event
    					if succes:
    						return True
    					else:
    						return False

    			return:
    				succes event id
    				failed: False
    	"""

		if self.homeDatabase.db_connection is not False:
			eventId = self.homeDatabase.add_event(eventType, eventDatetime, eventLocation)
		else:
			return False

		return eventId


	def del_room(self, roomId):
		"""
    		method called for del an specific room

    			Parametters:
					roomId: int

				functionning:
					-ask the home database for del an specific room
						if the room was correctly deleted:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.del_room(roomId)
		else:
			return False

	def del_inhabitant(self, inhabitantId):
		"""
    		method called for del an specific inhabitant

    			Parametters:
					inhabitantId: int

				functionning:
					-ask the home database for del an specific inhabitant
						if the inhabitant was correctly deleted:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.del_inhabitant(inhabitantId)
		else:
			return False



	def del_guest(self, guestId):
		"""
    		method called for del an specific guest

    			Parametters:
					guestId: int

				functionning:
					-ask the home database for del an specific guest
						if the guest was correctly deleted:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.del_guest(guestId)
		else:
			return False

	def del_profil(self, profilId):
		"""
    		method called for del an specific profil

    			Parametters:
					profilId: int

				functionning:
					-ask the home database for del an specific profil
						if the profil was correctly deleted:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.del_profil(profilId)
		else:
			return False

	def del_module(self, moduleId):
		"""
    		method called for del an specific module

    			Parametters:
					moduleId: int

				functionning:
					-ask the automation network for del an specific module
						if the module was correctly deleted:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeAutomationNetwork.isReady():
			return self.homeAutomationNetwork.del_module(moduleId)
		else:
			return False

	def del_event(self, eventId):
		"""
    		method called for del an specific event

    			Parametters:
					eventId: int

				functionning:
					-ask the home database for del an specific event
						if the event was correctly deleted:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.del_event(eventId)
		else:
			return False


	def set_room_name(self, roomId, newName):
		"""
    		methods called for set an room's name.

    			Parametters:
    				roomId: int
    				newName: str

    			functionning:
					-ask the home database for set an room's name
						if the room was correctly renamed:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_room_name(roomId, newName)
		else:
			return False

	def set_room_type(self, roomId, newType):
		"""
    		methods called for set an room's type.

    			Parametters:
    				roomId: int
    				newType: str

    			functionning:
					-ask the home database for set an room's name
						if the room was correctly 'transtyped':
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_room_type(roomId, newType)
		else:
			return False

	def set_profil_last_name(self, profilId, newLastName):
		"""
    		methods called for set an profil's last name.

    			Parametters:
    				profilId: int
    				newLastName: str

    			functionning:
					-ask the home database for set an profils's last name
						if the profils last name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_profil_last_name(profilId, newLastName)
		else:
			return False

	def set_profil_first_name(self, profilId, newFirstName):
		"""
    		methods called for set an profil's first name.

    			Parametters:
    				profilId: int
    				newFirstName: str

    			functionning:
					-ask the home database for set an profils's first name
						if the profils first name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_profil_first_name(profilId, newFirstName)
		else:
			return False

	def set_profil_sexe(self, profilId, newSexe):
		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_profil_sexe(profilId, newSexe)
		else:
			return False

	def set_profil_date_of_birth(self, profilId, newDateOfBirth):
		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_profil_date_of_birth(profilId, newDateOfBirth)
		else:
			return False

	def set_inhabitant_last_name(self, inhabitantId, newLastName):
		"""
    		methods called for set an inhabitant's last name.

    			Parametters:
    				inhabitantId: int
    				newLastName: str

    			functionning:
					-ask the home database for set an inhabitant's last name
						if the inhabitant's last name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_inhabitant_last_name(inhabitantId, newLastName)
		else:
			return False

	def set_inhabitant_first_name(self, inhabitantId, newFirstName):
		"""
    		methods called for set an inhabitant's first name.

    			Parametters:
    				inhabitantId: int
    				newFirstName: str

    			functionning:
					-ask the home database for set an inhabitant's first name
						if the inhabitant's first name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_inhabitant_first_name(inhabitantId, newFirstName)
		else:
			return False

	def set_inhabitant_sexe(self, inhabitantId, newSexe):
		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_inhabitant_sexe(inhabitantId, newSexe)
		else:
			return False

	def set_inhabitant_date_of_birth(self, inhabitantId, newDateOfBirth):
		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_inhabitant_date_of_birth(inhabitantId, newDateOfBirth)
		else:
			return False

	def set_guest_last_name(self, guestId, newLastName):
		"""
    		methods called for set an guest's last name.

    			Parametters:
    				guestId: int
    				newNLastame: str

    			functionning:
					-ask the home database for set an guest's last name
						if the guest's last name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""


		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_guest_last_name(guestId, newLastName)
		else:
			return False

	def set_guest_first_name(self, guestId, newFirstName):
		"""
    		methods called for set an guest's first name.

    			Parametters:
    				guestId: int
    				newFirstName: str

    			functionning:
					-ask the home database for set an guest's first name
						if the guest's first name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""


		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_guest_first_name(guestId, newFirstName)
		else:
			return False

	def set_guest_sexe(self, guestId, newSexe):
		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_guest_sexe(guestId, newSexe)
		else:
			return False

	def set_guest_date_of_birth(self, guestId, newDateOfBirth):
		if self.homeDatabase.db_connection is not False:
			return self.homeDatabase.set_guest_date_of_birth(guestId, newDateOfBirth)
		else:
			return False

	def set_module_name(self, moduleId, newName):
		"""
    		methods called for set an module's name.

    			Parametters:
    				moduleId: int
    				newName: str

    			functionning:
					-ask the automation network for set an module's name
						if the module's name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeAutomationNetwork.isReady:
			return self.homeAutomationNetwork.set_module_name(moduleId, newName)
		else:
			return False

	def set_module_location(self, moduleId, newLocation):
		"""
    		methods called for set an module's location.

    			Parametters:
    				moduleId: int
    				newLocation: int(roomId)

    			functionning:
					-ask the automation network for set an module's location
						if the module's location was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.homeAutomationNetwork.isReady:
			return self.homeAutomationNetwork.set_module_location(moduleId, newLocation)
			return self.homeAutomationNetwork.set_module_location(moduleId, newLocation)
		else:
			return False