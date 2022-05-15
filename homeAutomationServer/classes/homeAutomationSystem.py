from .home import *


class HomeAutomationSystem:
	"""
		class bringing all the information and functionality of the system.

			Attributes:
				running (control boolean to know if the system is in working order)
				home (class bringing all the information of the home)

			Propertys:

			Methods:
				start (allows to start the system)
				stop (allows to stop the system)

				set running (allows to set the running parametters)

				get home (allows you to retrieve the linked home class)
				get rooms list (allows to retrieve the list of rooms in the home)
				get events list (allows to retrieve the list of events in the home)

				get inhabitants list (allows to retrieve the list of inhabitants in the home)
				get guests list (allows to retrieve the list of guests in the home)
				get profil list (allows to retrieve the list of guest in the home)

				get room (allows to retrieve a specific room in the home)

				get inhabitant (allows to retrieve a specific inhabitant in the home)
				get guest (allows to retrieve a specific guest in the home)
				get profil (allows to retrieve a specific profil in the home)

				get automation network (allows to retrieve the home automation network class (zwave network))
				get modules list (allows to retrieve the list of module on the network)
				get module (allows to retrieve a specific module on the network)

				get event list (allows to retrive the list of event)
				get event (allows to retrieve a specific event)

				add room (allows to add an room in the home)

				add inhabitant (allows to add an inhabitant in the home)
				add guest (allows to add an guest in the home)
				add profil (allows to add an profil in the home)

				add module (allows to add an module on the network)

				add event (allows to add an event in the home)

				del room (allows to delete an room in the home)

				del inhabitant (allows to delete an inhabitant in the home)
                del guest (allows to delete an guest in the home)
                del profil (allows to del an profil in the home)

                del module (allows to delete an module on the network)

                del event (allows to delete an event in the home)

                set room name (allows to set the name of an room)
				set room type (allows to set the type of an room)

				set profil last name (allows to set the last name of an profil)
				set profil first name (allows to set the first name of an profil)

				set inhabitant last name (allows to set the last name of an inhabitant)
				set inhabitant first name (allows to set the first name of an inhabitant)

				set guest last name (allows to set the last name of an guest)
				set guest first name (allows to set the first name of an inhabitant)

				set module name (allows to set the name of an module)
				set module location (allows to set the location of an module)

				set automation network controller path (allows to set the path of the automation network controller)

				heal network (allows to heal the automation network(zwave network))
				destroy network (allows to destroy the automation network)
				save network (allows to save modification on the automation network)

				serialize (allows to transform the class in dict for json use)
    """

	def __init__(self):
		self.running = False
		self.home = Home()


	def start(self):
		"""
			Method called for start the system.

				functioning:
					- establish connection with the home database
					- start the home automation network
					- set working on True
					- return the succes

				return:
					succes (True/False)
		"""

		if self.home.homeDatabase.connect() is True:
			if self.home.homeAutomationNetwork.start() is True:
				self.set_running(True)
			else:
				return False
		else:
			return False

		if self.running is True:
			return True
		else:
			return False

	def stop(self):
		"""
    		Method called for stop the system.

    			functionning:
    				- stop the connection with the home database
    				- stop the home automation network
    				- set running on False
    				- return succes

    			return:
    				succes (True/False)
    	"""

		if self.home.homeDatabase.disconnect():
			if self.home.homeAutomationNetwork.stop():
				self.set_running(False)
			else:
				return False
		else:
			return False
		if self.running is False:
			return True
		else:
			return False

	def set_running(self, value):
		"""
    		Method called for set the running parametters.

    			Parametters:
    				value: booléen

    			fuctionning:
    				- checks if the value is an Booléan
    					if it is:
    						set the parametters with the value
    						return True
    					else:
    						return False

    			return:
    				succes (True/False)
    	"""

		if isinstance(value, bool):
			self.running = value
		else:
			return False

		if self.running == value:
			return True
		else:
			return False


	def get_rooms_list(self):
		"""
    		Method called for get an list of the room contains in the home.

				functionning:
					ask to home list his rooms
    			return:
    				list of room classes
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.roomsList
		else:
			return False

	def get_inhabitants_list(self):
		"""
    		Method called for get an list of the inhabitants in the home

				functionning:
					ask to home list his inhabitants
    			return:
    				list of inhabitant classes
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.inhabitantsList
		else:
			return False

	def get_guests_list(self):
		"""
    		method called for get an list of guests in the home

				functionning:
					ask to home list his guests
    			return:
    				list of guests class
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.guestsList
		else:
			return False

	def get_profils_list(self):
		"""
    		method called for get an list of profil in the home

				functionning:
					ask to home list his profils
    			return:
    				list of profil class
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.guestsList
		else:
			return False

	def get_events_list(self):
		"""
    		method called for get an list of events in the home

				functionning:
					ask to home list his events
    			return:
    				list of events class
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.eventsList
		else:
			return False

	def get_modules_list(self):
		"""
			method called for get an list of module on the network

				return:
					list of module class
		"""

		if self.home.homeAutomationNetwork.isReady:
			return self.home.homeAutomationNetwork.modulesList
		else:
			return False


	def get_room(self, roomId):
		"""
    		Method called for get an specific room contains in the home.

				Parametters:
					roomId: int

				functionning:
					-asks the home to search for the room linked to the id
						if the room was found:
							return the room class
						else:
							return False
    			return:
    				room classes/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.get_room(roomId)
		else:
			return False

	def get_inhabitant(self, inhabitantId):
		"""
    		Method called for get an specific inhabitant in the home

    			Parametters:
					inhabitantId: int

				functionning:
					-asks the home to search for the inhabitant linked to the id
						if the inhabitant was found:
							return the inhabitant class
						else:
							return False

    			return:
    				inhabitant class/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.get_inhabitant(inhabitantId)
		else:
			return False

	def get_guest(self, guestId):
		"""
    		method called for get an specific guest in the home

    			Parametters:
					guestId: int

				functionning:
					--asks the home to search for the guest linked to the id
						if the guest was found:
							return the guest class
						else:
							return False

    			return:
    				guests class/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.get_guest(guestId)
		else:
			return False

	def get_profil(self, profilId):
		"""
    		method called for get an specific profil in the home

    			Parametters:
					profilId: int

				functionning:
					-asks the home to search for the profil linked to the id
						if the profil was found:
							return the profil class
						else:
							return False

    			return:
    				profil class/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.get_profil(profilId)
		else:
			return False

	def get_module(self, moduleId):
		"""
    		method called for get an specific module on the network

    			Parametters:
					moduleId: int

				functionning:
					--asks the home to search for the module linked to the id
						if the module was found:
							return the module class
						else:
							return False

    			return:
    				module class/False
    	"""

		if self.home.homeAutomationNetwork.isReady:
			return self.home.homeAutomationNetwork.get_module(moduleId)
		else:
			return False

	def get_event(self, eventId):
		"""
    		method called for get an specific event

    			Parametters:
					eventId: int

				functionning:
					-asks the home to search for the event linked to the id
						if the event was found:
							return the event class
						else:
							return False

    			return:
    				event class/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.get_event(eventId)
		else:
			return False


	def add_room(self, roomName, roomType):
		"""
    		method called for adding an room in the home.

    			Parametters:
    				roomName: name of the room
    				roomType: type of the room (bathroom, corridor, ...)

    			functionning:
    				asks to the home to add the room
    					if succes:
    						return id of the room
    					else:
    						return False

    			return:
    				succes id of the room
    				failed False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.add_room(roomName, roomType)
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
    				asks the home to add the inhabitant
    					if succes:
    						return inhabitant id
    					else:
    						return False

    			return:
    				succes inhabitant id
    				failed False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.add_inhabitant(firstName, lastName, sexe, dateOfBirth)
		else:
			return False

	def add_guest(self,firstName, lastName, sexe, dateOfBirth):
		"""
    		method called for adding an guest in the home.

    			Parametters:
    				firstName
    				lastName
    				sexe
    				dateOfBirth

    			functionning:
    				asks the home to add the guest
    					if succes:
    						return True
    					else:
    						return False

    			return:
    				succes guest id
    				failed False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.add_guest(firstName, lastName, sexe, dateOfBirth)
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
    				asks the home to add the profil
    					if succes:
    						return True
    					else:
    						return False

    			return:
    				succes profil id
    				failed False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.add_profil(firstName, lastName, sexe, dateOfBirth)
		else:
			return False

	def add_module(self, newModuleName, newModuleLocation):
		"""
    		method called for adding an module on the network.

    			Parametters:
    				newModuleName: str
    				newModuleLocation: int

    			functionning:
    				ask to home add the module
    					if succes:
    						return True
    					else:
    						return False

    			return:
    				succes module id
    				failed False
    	"""

		if self.home.homeAutomationNetwork.isReady:
			return self.home.add_module(newModuleName, newModuleLocation)
		else:
			return False

	def add_event(self, eventType, eventDatetime, eventLocation):
		"""
    		method called for adding an event in the home.

    			Parametters:
    				newEvent: event class

    			functionning:
    				asks the home to add the event
    					if succes:
    						return True
    					else:
    						return False

    			return:
    				succes event id
    				failed False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.add_event(eventType, eventDatetime, eventLocation)
		else:
			return False


	def del_room(self, roomId):
		"""
    		method called for del an specific room

    			Parametters:
					roomId: int

				functionning:
					-ask the home for del an specific room
						if the room was correctly deleted:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.del_room(roomId)
		else:
			return False

	def del_inhabitant(self, inhabitantId):
		"""
    		method called for del an specific inhabitant

    			Parametters:
					inhabitantId: int

				functionning:
					-ask the home for del an specific inhabitant
						if the inhabitant was correctly deleted:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.del_inhabitant(inhabitantId)
		else:
			return False

	def del_guest(self, guestId):
		"""
    		method called for del an specific guest

    			Parametters:
					guestId: int

				functionning:
					-ask the home for del an specific guest
						if the guest was correctly deleted:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.del_guest(guestId)
		else:
			return False

	def del_profil(self, profilId):
		"""
    		method called for del an specific profil

    			Parametters:
					profilId: int

				functionning:
					-ask the home for del an specific profil
						if the profil was correctly deleted:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.del_profil(profilId)
		else:
			return False

	def del_module(self, moduleId):
		"""
    		method called for del an specific module

    			Parametters:
					moduleId: int

				functionning:
					-ask the home for del an specific module
						if the module was correctly deleted:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeAutomationNetwork.isReady:
			return self.home.del_module(moduleId)
		else:
			return False

	def del_event(self, eventId):
		"""
    		method called for del an specific event

    			Parametters:
					eventId: int

				functionning:
					-ask the home for del an specific event
						if the event was correctly deleted:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.del_event(eventId)
		else:
			return False


	def set_room_name(self, roomId, newName):
		"""
    		methods called for set an room's name.

    			Parametters:
    				roomId: int
    				newName: str

    			functionning:
					-ask the home for set an room's name
						if the room was correctly renamed:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_room_name(roomId, newName)
		else:
			return False

	def set_room_type(self, roomId, newType):
		"""
    		methods called for set an room's type.

    			Parametters:
    				roomId: int
    				newType: str

    			functionning:
					-ask the home for set an room's name
						if the room was correctly 'transtyped':
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_room_type(roomId, newType)
		else:
			return False

	def set_profil_last_name(self, profilId, newLastName):
		"""
    		methods called for set an profil's last name.

    			Parametters:
    				profilId: int
    				newLastName: str

    			functionning:
					-ask the home for set an profils's last name
						if the profils last name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_profil_last_name(profilId, newLastName)
		else:
			return False

	def set_profil_first_name(self, profilId, newFirstName):
		"""
    		methods called for set an profil's first name.

    			Parametters:
    				profilId: int
    				newFirstName: str

    			functionning:
					-ask the home for set an profils's first name
						if the profils first name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_profil_first_name(profilId, newFirstName)
		else:
			return False

	def set_profil_sexe(self, profilId, newSexe):
		"""
	    	methods called for set an profil's sexe.

	    		Parametters:
	    			profilId: int
	    			newSexe: str(m/f)

	    		functionning:
					-ask the home for set an profils's sexe
						if the profils sexe was correctly modified:
							return True
						else:
							return False

	    		return:
	    			succes: True/False
	    """

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_profil_sexe(profilId, newSexe)
		else:
			return False

	def set_profil_date_of_birth(self, profilId, newDateOfBirth):
		"""
	    	methods called for set an profil's date of birth

	    		Parametters:
	    			profilId: int
	    			new date of birth: str

	    		functionning:
					-ask the home for set an profils's date of birth
						if the profils date of birth was correctly modified:
							return True
						else:
							return False

	    		return:
	    			succes: True/False
	    """

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_profil_date_of_birth(profilId, newDateOfBirth)
		else:
			return False

	def set_inhabitant_last_name(self, inhabitantId, newLastName):
		"""
    		methods called for set an inhabitant's last name.

    			Parametters:
    				inhabitantId: int
    				newLastName: str

    			functionning:
					-ask the home for set an inhabitant's last name
						if the inhabitant's last name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_inhabitant_last_name(inhabitantId, newLastName)
		else:
			return False

	def set_inhabitant_first_name(self, inhabitantId, newFirstName):
		"""
    		methods called for set an inhabitant's first name.

    			Parametters:
    				inhabitantId: int
    				newFirstName: str

    			functionning:
					-ask the home for set an inhabitant's first name
						if the inhabitant's first name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_inhabitant_first_name(inhabitantId, newFirstName)
		else:
			return False

	def set_inhabitant_sexe(self, inhabitantId, newSexe):
		"""
	    	methods called for set an inhabitant's sexe.

	    		Parametters:
	    			inhabitantId: int
	    			newSexe: str(m/f)

	    		functionning:
					-ask the home for set an inhabitant's sexe
						if the inhabitant sexe was correctly modified:
							return True
						else:
							return False

	    		return:
	    			succes: True/False
	    """

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_inhabitant_sexe(inhabitantId, newSexe)
		else:
			return False

	def set_inhabitant_date_of_birth(self, inhabitantId, newDateOfBirth):
		"""
	    	methods called for set an inhabitant's date of birth

	    		Parametters:
	    			inhabitantId: int
	    			new date of birth: str

	    		functionning:
					-ask the home for set an inhabitant's date of birth
						if the inhabitant date of birth was correctly modified:
							return True
						else:
							return False

	    		return:
	    			succes: True/False
	    """

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_inhabitant_date_of_birth(inhabitantId, newDateOfBirth)
		else:
			return False

	def set_guest_last_name(self, guestId, newLastName):
		"""
    		methods called for set an guest's last name.

    			Parametters:
    				guestId: int
    				newNLastame: str

    			functionning:
					-ask the home for set an guest's last name
						if the guest's last name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_guest_last_name(guestId, newLastName)
		else:
			return False

	def set_guest_first_name(self, guestId, newFirstName):
		"""
    		methods called for set an guest's first name.

    			Parametters:
    				guestId: int
    				newFirstName: str

    			functionning:
					-ask the home for set an guest's first name
						if the guest's first name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_guest_first_name(guestId, newFirstName)
		else:
			return False

	def set_guest_sexe(self, guestId, newSexe):
		"""
	    	methods called for set an guest sexe.

	    		Parametters:
	    			guestId: int
	    			newSexe: str(m/f)

	    		functionning:
					-ask the home for set an guest sexe
						if the guest sexe was correctly modified:
							return True
						else:
							return False

	    		return:
	    			succes: True/False
	    """

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_guest_sexe(guestId, newSexe)
		else:
			return False

	def set_guest_date_of_birth(self, guestId, newDateOfBirth):
		"""
	    	methods called for set an guest date of birth

	    		Parametters:
	    			guestId: int
	    			new date of birth: str

	    		functionning:
					-ask the home for set an guest date of birth
						if the guest date of birth was correctly modified:
							return True
						else:
							return False

	    		return:
	    			succes: True/False
	    """

		if self.home.homeDatabase.db_connection is not False:
			return self.home.set_guest_date_of_birth(guestId, newDateOfBirth)
		else:
			return False

	def set_module_name(self, moduleId, newName):
		"""
    		methods called for set an module's name.

    			Parametters:
    				moduleId: int
    				newName: str

    			functionning:
					-ask the home for set an module's name
						if the module's name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeAutomationNetwork.isReady:
			return self.home.set_module_name(moduleId, newName)
		else:
			return False

	def set_module_location(self, moduleId, newLocation):
		"""
    		methods called for set an module's location.

    			Parametters:
    				moduleId: int
    				newLocation: int(roomId)

    			functionning:
					-ask the home for set an module's location
						if the module's location was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		if self.home.homeAutomationNetwork.isReady:
			return self.home.set_module_location(moduleId, newLocation)
		else:
			return False

	def set_automation_network_controller_path(self, newPath):
		"""
    		set the path of the automation network controller

    			Parametters:
    				newPath: str

    			functionning:
					-ask the home for set the automation network controller path
						if the path was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		return self.home.homeAutomationNetwork.set_automation_network_controller_path(newPath)

	def set_automation_network_Zwave_config_path(self, newPath):
		"""
    		set the path of the automation network controller

    			Parametters:
    				newPath: str

    			functionning:
					-ask the home for set the automation network controller path
						if the path was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""

		return self.home.homeAutomationNetwork.set_Zwave_config_path(newPath)

	def heal_network(self):
		"""
    		Method called for heal automation network
    	"""

		return self.home.homeAutomationNetwork.heal_network()

	def destroy_network(self):
		"""
    		Method called for destroy the automation network
    	"""

		return self.home.homeAutomationNetwork.destroy_network()

	def save_network(self):
		"""
    		Method called for save modification effectuate on the automation network
    	"""

		return self.home.homeAutomationNetwork.save_modification()