class HomeDatabase:
	"""
		class bringing all the information and functionality of the home database.

			Attributes:
				username: username used for database connection
                host: host of the database
                database name: name of the database
                database password: password for the database

                db_connection
                db_cursor

			Property:

			Methods:
				connect: allows to connect to the database
				disconnect: allows to disconnect to the database
				commit change: commit change to the database

				get rooms list (list of room contained in the home database)
                get inhabitants list (list of inhabitant contained in the home database)
                get guests list (list of guest contained in the home database)
                get profils list (list of profil contained in the home database)
                get events list (list of events contained in the home database)

				get room (allows to retrieve a specific room in the home database)
                get inhabitant (allows to retrieve a specific inhabitant in the home database)
				get guest (allows to retrieve a specific guest in the home database)
				get profil (allows to retrieve a specific profil in the home database)
				get event (allows to retrieve a specific event)

                add room (allows to add an room in the house)
				add inhabitant (allows to add an inhabitant in the house)
				add guest (allows to add an guest in the house)
				add profil (allows to add an profil in the house)
				add event (allows to add an event in the home database)

                del room (allows to delete an room in the home database)	
                del inhabitant (allows to delete an inhabitant in the home database)
                del guest (allows to delete an guest in the home database)
                del profil (allows to del an profil in the home database)
                del event (allows to del an event in the home database)

                set room name (allows to set the name of an room)
				set room type (allows to set the type of an room)
				set profil last name (allows to set the last name of an profil)
				set profil first name (allows to set the first name of an profil)
				set inhabitant last name (allows to set the last name of an inhabitant)
				set inhabitant first name (allows to set the first name of an inhabitant)
				set guest last name (allows to set the last name of an guest)
				set guest first name (allows to set the first name of an inhabitant)
	"""

	def __init__(self):
		pass


	def connect(self):
		"""
			method called for establish connection with the home database
		"""

		pass

	def disconnect(self):
		"""
			method called for disconnect the connection with the home database
		"""

		pass

	def commit_change(self):
		"""
			method called for commit change to the database
		"""

		pass


	def get_rooms_list(self):
    	"""
    		Method called for get an list of the rooms

    			return:
    				list of room classes
    	"""

    	pass

    def get_inhabitants_list(self):
    	"""
    		Method called for get an list of the inhabitants

    			return:
    				list of inhabitant classes
    	"""

    	pass

    def get_guests_list(self):
    	"""
    		method called for get an list of guests

    			return:
    				list of guests class
    	"""

    	pass

    def get_profils_list(self):
    	"""
    		method called for get an list of profil

    			return:
    				list of profil class
    	"""

    	pass

    def get_events_list(self):
    	"""
    		method called for get an list of events
    			return:
    				list of events class
    	"""

    	pass

    def get_room(self, roomId):
    	"""
    		Method called for get an specific room

				Parametters:
					roomId: int

				functionning:
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
    		Method called for get an specific inhabitant

    			Parametters:
					inhabitantId: int

				functionning:
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
    		method called for get an specific guest

    			Parametters:
					guestId: int

				functionning:
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
    		method called for get an specific profil

    			Parametters:
					profilId: int

				functionning:
					if the profil was found:
						return the profil class
					else:
						return False

    			return:
    				profil class/False
    	"""

    	pass

    def get_event(self, eventId):
    	"""
    		method called for get an specific event

    			Parametters:
					eventId: int

				functionning:
					if the event was found:
						return the event class
					else:
						return False

    			return:
    				event class/False
    	"""

    	pass


    def add_room(self, newRoom):
    	"""
    		method called for adding an room.

    			Parametters:
    				newRoom: room class

    			functionning:
    				- check if new room is an instance of room class
    					if it is:
    						adding the room
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
    		method called for adding an inhabitant

    			Parametters:
    				newInhabitant: inhabitant class

    			functionning:
    				- check if newInhabitant is an instance of inhabitant class
    					if it is:
    						adding the inhabitant
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
    		method called for adding an guest

    			Parametters:
    				newGuest: guest class

    			functionning:
    				- check if newGuest is an instance of guest class
    					if it is:
    						adding the guest
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
    		method called for adding an profil

    			Parametters:
    				newProfil: profil class

    			functionning:
    				- check if newProfil is an instance of profil class
    					if it is:
    						adding the profil
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

    def add_event(self, newEvent):
    	"""
    		method called for adding an event

    			Parametters:
    				newEvent: event class

    			functionning:
    				- check if newEvent is an instance of event class
    					if it is:
    						adding the event
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
					del specific room
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
					del specific inhabitant
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
					del specific guest
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
					del specific profil
						if the profil was correctly deleted:
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
					del specific event
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
					set the room's name
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
					set the room's name
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
					set the profils's last name
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
					set the profils's first name
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
					set the inhabitant's last name
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
					set the inhabitant's first name
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
					set the guest's last name
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
					set the guest's first name
						if the guest's first name was correctly modified:
							return True
						else:
							return False

    			return:
    				succes: True/False
    	"""
    	pass