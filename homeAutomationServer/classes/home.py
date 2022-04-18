class Home:
	"""
		class bringing all the information and functionality of the home.

			Parammetters:
				controllerPath: path to the zwave controller (ex: "/dev/ttyACM0")

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
				start database (allows to establish connection with the home database)
				start automation network (allows to start the automation network)

				stop database (allows to close the connection with the home database)
				stop automation network (allows to stop the automation network)

				get room (allows to retrieve a specific room in the home database)

				get inhabitant (allows to retrieve a specific inhabitant in the home database)
				get guest (allows to retrieve a specific guest in the home database)
				get profil (allows to retrieve a specific profil in the home database)

				get automation network (allows to retrieve the home automation network class (zwave network))
				get module (allows to retrieve a specific module on the network)

				get event (allows to retrieve a specific event)

				add room (allows to add an room in the house)

				add inhabitant (allows to add an inhabitant in the house)
				add guest (allows to add an guest in the house)
				add profil (allows to add an profil in the house)

				add module (allows to add an module on the network)

				add event (allows to add an event in the home database)

				del room (allows to delete an room in the home database)
				
                del inhabitant (allows to delete an inhabitant in the home database)
                del guest (allows to delete an guest in the home database)
                del profil (allows to del an profil in the home database)

                del module (allows to del an module)

                del event (allows to del an event in the home database)

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

	def __init__(self, controllerPath):
		pass


	@property
	def id(self):
		"""
			property representing the home identifier

				return: int
		"""

		pass

	@property
	def roomsList:
		"""
    		property representing list of rooms contained in the home.

				functionning:
					asks the database to list the rooms

    			return:
    				list of room classes
    	"""

    	pass

    @property
    def inhabitantsList(self):
    	"""
    		property representing list of inhabitants contained in the home.

				functionning:
					asks the database to list the inhabitants

    			return:
    				list of inhabitants classes
    	"""
    
    	pass

    @property
    def guestsList(self):
    	"""
    		property representing list of guests contained in the home.

				functionning:
					asks the database to list the guests

    			return:
    				list of guests classes
    	"""

    	pass

    @property
    def profilsList(self):
    	"""
    		property representing list of profils contained in the home.

				functionning:
					asks the database to list the profils

    			return:
    				list of profils classes
    	"""

    	pass

    @property
    def eventsList(self):
    	"""
    		property representing list of events contained in the home.

				functionning:
					asks the database to list the events

    			return:
    				list of events classes
    	"""

    	pass

    @property
    def modulesList(self):
    	"""
    		property representing list of modules contained in the home.

				functionning:
					asks the automation network to list the module

    			return:
    				list of modules classes
    	"""

    	pass


    def start_database(self):
    	"""
    		Method call for start the home database connection.

    			return:
    				succes: True/False
    	"""

    	pass

    def start_automation_network(self):
    	"""
    		method call for start the automation network

    			return:
    				succes: True/False
    	"""

    	pass

    def stop_database(self):
    	"""
    		Method call for stop the home database connection.

    			return:
    				succes: True/False
    	"""

    	pass

    def stop_automation_network(self):
    	"""
    		method call for stop the automation network

    			return:
    				succes: True/False
    	"""
    	pass


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

    	pass

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

    	pass

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

    	pass

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

    	pass

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

    	pass

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

    	pass

    def get_automation_network(self):
    	"""
    		method called get the home automation network.

    			return:
    				home automation network class
    	"""

    	pass


    def add_room(self, newRoom):
    	"""
    		method called for adding an room in the home.

    			Parametters:
    				newRoom: room class

    			functionning:
    				- check if new room is an instance of room class
    					if it is:
    						asks the home database to add the room
    							if succes:
    								return True
    							else:
    								return False
    					else:
    						return False

    			return:
    				succes (True/False)
    	"""

    	pass

    def add_inhabitant(self, newInhabitant):
    	"""
    		method called for adding an inhabitant in the home.

    			Parametters:
    				newInhabitant: inhabitant class

    			functionning:
    				- check if newInhabitant is an instance of inhabitant class
    					if it is:
    						asks the homeDatabase to add the inhabitant
    							if succes:
    								return True
    							else:
    								return False
    					else:
    						return False

    			return:
    				succes (True/False)
    	"""

    	pass

    def add_guest(self, newGuest):
    	"""
    		method called for adding an guest in the home.

    			Parametters:
    				newGuest: guest class

    			functionning:
    				- check if newGuest is an instance of guest class
    					if it is:
    						asks the home database to add the guest
    							if succes:
    								return True
    							else:
    								return False
    					else:
    						return False

    			return:
    				succes (True/False)
    	"""

    	pass

    def add_profil(self, newProfil):
    	"""
    		method called for adding an profil in the home.

    			Parametters:
    				newProfil: profil class

    			functionning:
    				- check if newProfil is an instance of profil class
    					if it is:
    						asks the home database to add the profil
    							if succes:
    								return True
    							else:
    								return False
    					else:
    						return False

    			return:
    				succes (True/False)
    	"""

    	pass

    def add_module(self, newModuleName, newModuleLocation):
    	"""
    		method called for adding an module on the network.

    			Parametters:
    				newModuleName: str
    				newModuleLocation: int

    			functionning:
    				- check if newModuleName  is instance str
    					if it is:
    						pass
    					else:
    						return False
    				- check if newModuleLocation is instance int
    					if it is:
    						pass
    					else:
    						return false

    				if all the parameters are of good type:
    					ask to home add the module
    						if succes:
    							return True
    						else:
    							return False

    			return:
    				succes (True/False)
    	"""

    	pass

    def add_event(self, newEvent):
    	"""
    		method called for adding an event in the home.

    			Parametters:
    				newEvent: event class

    			functionning:
    				- check if newEvent is an instance of event class
    					if it is:
    						asks the home database to add the event
    							if succes:
    								return True
    							else:
    								return False
    					else:
    						return False

    			return:
    				succes (True/False)
    	"""

    	pass


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

    	pass

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

    	pass



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

    	pass

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

    	pass

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

    	pass

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

    	pass


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

    	pass

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

    	pass

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

    	pass

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
    	pass

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
    	pass

    def inhabitant_first_name(self, inhabitantId, newFirstName):
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
    	pass

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

    	pass

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

    	pass

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

    	pass

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

    	pass

    def set_automation_network_controller_path(self, newPath):
    	"""
    		set the path of the automation network controller

    			Parametters:
    				newPath: str

    			functionning:
					-ask the automation server for set the automation network controller path
						if the path was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""


    def heal_network(self):
    	"""
    		Method called for heal automation network
    	"""

    	pass

    def destroy_network(self):
    	"""
    		Method called for destroy the automation network
    	"""

    	pass

    def save_network(self):
    	"""
    		Method called for save modification effectuate on the automation network
    	"""

    	pass


    def serialize(self):
    	"""
    		method called for seriallize data of the class
    	"""

    	pass