import mysql.connector

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
		self.username = "HomeAutomatisationSystem"
		self.host = "localHost"
		self.databaseName = "Home"
		self.databasePassword = "0000"

		self.db_connection = False
		self.db_cursor = False


	def connect(self):
		"""
			method called for establish connection with the home database
		"""
		succes = False

		self.db_connection = mysql.connector.connect(
			host=self.host,
			user=self.username,
			passwd=self.databasePassword,
			database=self.databaseName,
			connection_timeout=10000
		)
		self.db_cursor = self.db_connection.cursor(buffered=True)

		if self.db_connection == False or self.db_cursor == False:
			succes = False
		else:
			succes = True

		return succes

	def disconnect(self):
		"""
			method called for disconnect the connection with the home database
		"""

		succes = False

		if self.db_connection is not False:
			try:
				self.db_connection.close()
				self.db_cursor = False
				self.db_connection = False
				succes = True
			except:
				succes = False

		return succes



	def commit_change(self):
		"""
			method called for commit change to the database
		"""

		if self.db_connection != False:
			self.db_connection.commit()


	def get_rooms_list(self):
		"""
    		Method called for get an list of the rooms

    			return:
    				list of room classes
    	"""

		request = """SELECT * FROM Rooms"""

		if self.db_connection is not False and self.db_cursor is not False:
			try:
				self.db_cursor.execute(request)
			except:
				return False

			rooms = self.db_cursor.fetchall()

			return rooms
		else:
			return False

	def get_inhabitants_list(self):
		"""
    		Method called for get an list of the inhabitants

    			return:
    				list of inhabitant classes
    	"""
		request = """SELECT * FROM Inhabitants"""

		if self.db_connection is not False and self.db_cursor is not False:
			try:
				self.db_cursor.execute(request)
			except:
				return False

			inhabitants = self.db_cursor.fetchall()

			return inhabitants
		else:
			return False

	def get_guests_list(self):
		"""
    		method called for get an list of guests

    			return:
    				list of guests class
    	"""

		request = """SELECT * FROM Guests"""

		if self.db_connection is not False and self.db_cursor is not False:
			try:
				self.db_cursor.execute(request)
			except:
				return False

			guests = self.db_cursor.fetchall()

			return guests
		else:
			return False

	def get_profils_list(self):
		"""
    		method called for get an list of profil

    			return:
    				list of profil class
    	"""

		request = """SELECT * FROM Profils"""

		if self.db_connection is not False and self.db_cursor is not False:
			try:
				self.db_cursor.execute(request)
			except:
				return False

			profils = self.db_cursor.fetchall()

			return profils
		else:
			return False

	def get_events_list(self):
		"""
    		method called for get an list of events
    			return:
    				list of events class
    	"""
		request = """SELECT * FROM Events"""

		if self.db_connection is not False and self.db_cursor is not False:
			try:
				self.db_cursor.execute(request)
			except:
				return False

			events = self.db_cursor.fetchall()

			return events
		else:
			return False

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

		room = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(roomId, int):
				request = "SELECT * FROM Rooms WHERE id = {}".format(roomId)

				try:
					self.db_cursor.execute(request)
				except:
					return False

				room = self.db_cursor.fetchall()

				if len(room) > 0:
					return room[0]
				else:
					return False
			else:
				return False
		else:
			return False
	
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

		inhabitant = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(inhabitantId, int):
				request = "SELECT * FROM Inhabitants WHERE id = {}".format(inhabitantId)
				
				try:
					self.db_cursor.execute(request)
				except:
					return False

				inhabitant = self.db_cursor.fetchall()

				if len(inhabitant) > 0:
					return inhabitant[0]
				else:
					return False
			else:
				return False
		else:
			return False

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

		guest = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(guestId, int):
				request = "SELECT * FROM Guests WHERE id = {}".format(guestId)
				
				try:
					self.db_cursor.execute(request)
				except:
					return False

				guest = self.db_cursor.fetchall()

				if len(guest) > 0:
					return guest[0]
				else:
					return False
			else:
				return False
		else:
			return False

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

		profil = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(profilId, int):
				request = "SELECT * FROM Profils WHERE id = {}".format(profilId)
				
				try:
					self.db_cursor.execute(request)
				except:
					return False

				profil = self.db_cursor.fetchall()

				if len(profil) > 0:
					return profil[0]
				else:
					return False
			else:
				return False
		else:
			return False

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

		event = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(eventId, int):
				request = "SELECT * FROM Events WHERE id = {}".format(eventId)
				
				try:
					self.db_cursor.execute(request)
				except:
					return False

				event = self.db_cursor.fetchall()

				if len(event) > 0:
					return event[0]
				else:
					return False
			else:
				return False
		else:
			return False

	def add_room(self, roomName, roomType):
		"""
    		method called for adding an room.

    			Parametters:
    				newRoom: room class

    			functionning:
    				check parametters
    				adding the room
    					if succes:
    						return True
    					else:
    						return False

    			return:
    				succes (True/False)
    	"""

		succes = False
		roomId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(roomName, str) and isinstance(roomType, str):
				request = "INSERT INTO Rooms(name, type) VALUES ('{}', '{}')".format(roomName, roomType)
				try:
					self.db_cursor.execute(request)
				except:
					return False

				self.commit_change()
				roomId = self.db_cursor.lastrowid

				for room in self.get_rooms_list():
					if room[0] == roomId \
							and room[1] == roomName \
							and room[2] == roomType:
						succes = True
						break
					else:
						succes = False
			else:
				succes = False
		else:
			succes = False

		if succes:
			return roomId
		else:
			return False

	def add_inhabitant(self, firstName, lastName, sexe, dateOfBirth):
		"""
    		method called for adding an inhabitant

    			Parametters:
    				newInhabitant: inhabitant class

    			functionning:
    				adding the inhabitant
    					if succes:
    						return True
    					else:
    						return False

    			return:
    				succes (True/False)
    	"""

		succes = False
		profilId = inhabitantId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(firstName, str) \
				and isinstance(lastName, str) \
				and sexe == "f" or sexe == "m" \
				and isinstance(dateOfBirth, str):

				profilId = self.add_profil(firstName, lastName, sexe, dateOfBirth)
				if profilId is not False:
					request = "INSERT INTO Inhabitants(fk_profil_id) VALUES ({})".format(profilId)

					try:
						self.db_cursor.execute(request)
					except:
						return False

					self.commit_change()

					inhabitantId = self.db_cursor.lastrowid

					for inhabitant in self.get_inhabitants_list():
						if inhabitant[0] == inhabitantId and inhabitant[1] == profilId:
							succes = True
						else:
							succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		if succes:
			return inhabitantId
		else:
			return False
		
	def add_guest(self, firstName, lastName, sexe, dateOfBirth):
		"""
    		method called for adding an guest

    			Parametters:
    				newGuest: guest class

    			functionning:
    				check parametters
    				adding the guest
    					if succes:
    						return True
    					else:
    						return False

    			return:
    				succes (True/False)
    	"""

		succes = False
		profilId = guestId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(firstName, str) \
				and isinstance(lastName, str) \
				and sexe == "f" or sexe == "m" \
				and isinstance(dateOfBirth, str):

				profilId = self.add_profil(firstName, lastName, sexe, dateOfBirth)
				if profilId is not False:
					request = "INSERT INTO Guests(fk_profil_id) VALUES ({})".format(profilId)

					try:
						self.db_cursor.execute(request)
					except:
						return False

					self.commit_change()

					guestId = self.db_cursor.lastrowid

					for guest in self.get_guests_list():
						if guest[0] == guestId and guest[1] == profilId:
							succes = True
						else:
							succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		if succes:
			return guestId
		else:
			return False
		
	def add_profil(self, firstName, lastName, sexe, dateOfBirth):
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

		succes = profilId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(firstName, str) \
				and isinstance(lastName, str) \
				and sexe == "f" or sexe == "m" \
				and isinstance(dateOfBirth, str):

				request = "INSERT INTO Profils(first_name, last_name, sexe, date_of_birth) VALUES\
				('{}', '{}', '{}', '{}')".format(firstName, lastName, sexe, dateOfBirth)

				try:
					self.db_cursor.execute(request)
				except:
					return False

				self.commit_change()

				profilId = self.db_cursor.lastrowid

				for profil in self.get_profils_list():
					if profil[0] == profilId \
						and profil[1] == firstName \
						and profil[2] == lastName \
						and profil[3] == sexe \
						and profil[4] == dateOfBirth:

						succes = True
						break
					else:
						succes = False
			else:
				succes = False
		else:
			succes = False

		if succes:
			return profilId
		else:
			return False

	def add_event(self, eventType, eventDatetime, eventLocation):
		"""
    		method called for adding an event

    			Parametters:
    				newEvent: event class

    			functionning:
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
		succes = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(eventType, str) and isinstance(eventDatetime, str):
				if isinstance(eventLocation, int):
					request = "INSERT INTO Events(type, datetime, fk_room_id) VALUES \
							('{}', '{}', {})".format(eventType,
													 eventDatetime,
													 eventLocation)

					try:
						self.db_cursor.execute(request)
						self.commit_change()
					except:
						return False

					eventId = self.db_cursor.lastrowid

					for event in self.get_events_list():
						if event[0] == eventId\
								and event[1] == eventType \
								and event[2] == eventDatetime \
								and event[3] == eventLocation:
							succes = True
							break
						else:
							succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		if succes:
			return eventId
		else:
			return False


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

		succes = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(roomId, int):
				request = "DELETE FROM Rooms WHERE id = {}".format(roomId)

				if self.get_room(roomId) is not False:
					eventList = self.get_events_list()
					if eventList is not False:
						for event in eventList:
							if event[3] == roomId:
								self.del_event(event[0])
					else:
						return False

					try:
						self.db_cursor.execute(request)
					except:
						return False

					self.commit_change()

					if self.get_room(roomId) is False:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

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

		succes = False
		profilId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(inhabitantId, int):
				request = "DELETE FROM Inhabitants WHERE id = {}".format(inhabitantId)

				inhabitant = self.get_inhabitant(inhabitantId)
				if inhabitant is not False:
					profilId = inhabitant[1]

					try:
						self.db_cursor.execute(request)
					except:
						return False

					self.commit_change()

					if self.get_inhabitant(inhabitantId) is False:
						if self.del_profil(profilId):
							if self.get_profil(profilId) is False:
								succes = True
							else:
								succes = False
						else:
							succes = False
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

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

		succes = False
		profilId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(guestId, int):
				request = "DELETE FROM Guests WHERE id = {}".format(guestId)

				guest = self.get_guest(guestId)
				if guest is not False:
					profilId = guest[1]
					try:
						self.db_cursor.execute(request)
					except:
						return False

					self.commit_change()

					if self.get_guest(guestId) is False:
						if self.del_profil(profilId):
							if self.get_profil(profilId) is False:
								succes = True
							else:
								succes = False
						else:
							succes = False
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes
	
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
		succes = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(profilId, int):
				request = "DELETE FROM Profils WHERE id = {}".format(profilId)
				
				if self.get_profil(profilId) is not False:
					try:
						self.db_cursor.execute(request)
					except:
						return False

					self.commit_change()

					if self.get_profil(profilId) is False:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

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

		succes = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(eventId, int):
				request = "DELETE FROM Events WHERE id = {}".format(eventId)
				
				if self.get_event(eventId) is not False:
					try:
						self.db_cursor.execute(request)
					except:
						return False

					self.commit_change()

					if self.get_event(eventId) is False:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes


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

		succes = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(roomId, int) and isinstance(newName, str):
				request = """UPDATE Rooms SET name = '{}' where id = {}""".format(newName, roomId)

				self.db_cursor.execute(request)


				self.commit_change()

				room = self.get_room(roomId)

				if room is not False:
					if room[1] == newName:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

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

		succes = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(roomId, int) and isinstance(newType, str):
				request = """UPDATE Rooms SET type = '{}' where id = {}""".format(newType, roomId)

				try:
					self.db_cursor.execute(request)
				except:
					return False

				self.commit_change()

				room = self.get_room(roomId)

				if room is not False:
					if room[2] == newType:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes


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

		succes = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(profilId, int) and isinstance(newLastName, str):
				request = """UPDATE Profils SET last_name = '{}' where id = {}""".format(newLastName, profilId)

				try:
					self.db_cursor.execute(request)
				except:
					return False

				self.commit_change()

				profil = self.get_profil(profilId)

				if profil is not False:
					if profil[2] == newLastName:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

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

		succes = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(profilId, int) and isinstance(newFirstName, str):
				request = """UPDATE Profils SET first_name = '{}' where id = {}""".format(newFirstName, profilId)

				try:
					self.db_cursor.execute(request)
				except:
					return False

				self.commit_change()

				profil = self.get_profil(profilId)

				if profil is not False:
					if profil[1] == newFirstName:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

	def set_profil_sexe(self, profilId, newSexe):
		"""
		    methods called for set an profil's sexe.

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

		succes = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(profilId, int) and isinstance(newSexe, str) \
					and newSexe is 'f' or newSexe is 'm':
				request = """UPDATE Profils SET sexe = '{}' where id = {}""".format(newSexe, profilId)

				try:
					self.db_cursor.execute(request)
				except:
					return False

				self.commit_change()

				profil = self.get_profil(profilId)

				if profil is not False:
					if profil[3] == newSexe:
						succes = True
					else:
						succes = False
				else:
					succes = False

			else:
				succes = False
		else:
			succes = False

		return succes

	def set_profil_date_of_birth(self, profilId, newDateOfBirth):
		succes = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(profilId, int) and isinstance(newDateOfBirth, str):
				request = """UPDATE Profils SET date_of_birth = '{}' where id = {}""".format(newDateOfBirth, profilId)

				try:
					self.db_cursor.execute(request)
				except:
					return False

				self.commit_change()

				profil = self.get_profil(profilId)

				if profil is not False:
					if profil[4] == newDateOfBirth:
						succes = True
					else:
						succes = False
				else:
					succes = False

			else:
				succes = False
		else:
			succes = False

		return succes

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

		succes = profilId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(inhabitantId, int) and isinstance(newLastName, str):
				inhabitant = self.get_inhabitant(inhabitantId)
				if inhabitant is not False:
					profilId = inhabitant[1]

				if profilId is not False:
					self.set_profil_last_name(profilId, newLastName)

					profil =  self.get_profil(profilId)

					if profil[2] == newLastName:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

	def set_inhabitant_first_name(self, inhabitantId, newFirstName):
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

		succes = profilId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(inhabitantId, int) and isinstance(newFirstName, str):
				inhabitant = self.get_inhabitant(inhabitantId)
				if inhabitant is not False:
					profilId = inhabitant[1]

				if profilId is not False:
					self.set_profil_first_name(profilId, newFirstName)

					profil = self.get_profil(profilId)

					if profil[1] == newFirstName:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

	def set_inhabitant_sexe(self, inhabitantId, newSexe):
		succes = profilId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(inhabitantId, int) and isinstance(newSexe, str) \
					and newSexe == "f" or newSexe == "m":
				inhabitant = self.get_inhabitant(inhabitantId)
				if inhabitant is not False:
					profilId = inhabitant[1]

				if profilId is not False:
					self.set_profil_sexe(profilId, newSexe)

					profil = self.get_profil(profilId)

					if profil[3] == newSexe:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

	def set_inhabitant_date_of_birth(self, inhabitantId, newDateOfBirth):
		succes = profilId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(inhabitantId, int) and isinstance(newDateOfBirth, str):
				inhabitant = self.get_inhabitant(inhabitantId)
				if inhabitant is not False:
					profilId = inhabitant[1]

				if profilId is not False:
					self.set_profil_date_of_birth(profilId, newDateOfBirth)

					profil = self.get_profil(profilId)

					if profil[4] == newDateOfBirth:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

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

		succes = profilId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(guestId, int) and isinstance(newLastName, str):
				guest = self.get_guest(guestId)
				if guest is not False:
					profilId = guest[1]

				if profilId is not False:
					self.set_profil_last_name(profilId, newLastName)

					profil = self.get_profil(profilId)

					if profil[2] == newLastName:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

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

		succes = profilId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(guestId, int) and isinstance(newFirstName, str):
				guest = self.get_guest(guestId)
				if guest is not False:
					profilId = guest[1]

				if profilId is not False:
					self.set_profil_first_name(profilId, newFirstName)

					profil = self.get_profil(profilId)

					if profil[1] == newFirstName:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

	def set_guest_sexe(self, guestId, newSexe):
		succes = profilId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(guestId, int) and isinstance(newSexe, str) \
					and newSexe == "f" or newSexe == "m":
				guest = self.get_guest(guestId)
				if guest is not False:
					profilId = guest[1]

				if profilId is not False:
					self.set_profil_sexe(profilId, newSexe)

					profil = self.get_profil(profilId)

					if profil[3] == newSexe:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

	def set_guest_date_of_birth(self, guestId, newDateOfBirth):
		succes = profilId = False

		if self.db_connection is not False and self.db_cursor is not False:
			if isinstance(guestId, int) and isinstance(newDateOfBirth, str):
				guest = self.get_guest(guestId)
				if guest is not False:
					profilId = guest[1]

				if profilId is not False:
					self.set_profil_date_of_birth(profilId, newDateOfBirth)

					profil = self.get_profil(profilId)

					if profil[4] == newDateOfBirth:
						succes = True
					else:
						succes = False
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes