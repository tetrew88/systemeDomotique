import unittest

from homeAutomationServer.classes.homeDatabase import *

class Test_homeDatabase(unittest.TestCase):
	"""
		testing class of the home database.

		tests list:
			connect method:
				database connecting: check if the connection with database was esablished

			disconnect method:
				database disconnecting: check if the connection with database was disconnected

			get rooms list:
				check return: check if method return good type of data
			get inhabitants list:
				check return: check if method return good type of data
			get guests list:
				check return: check if method return good type of data
			get profils list:
				check return: check if method return good type of data
			get events list:
				check return: check if method return good type of data
			get room:
				check return: check if method return good type of data
			get inhabitant:
				check return: check if method return good type of data
			get guest:
				check return: check if method return good type of data
			get profil:
				check return: check if method return good type of data
			get event:
				check return: check if method return good type of data

			add room:
				test with good parametters: test if the method works correctly
				test with bad parametters: test if the method detect the bad parammeters 
			add inhabitant:
				test with good parametters: test if the method works correctly
				test with bad parametters: test if the method detect the bad parammeters 
			add guest:
				test with good parametters: test if the method works correctly
				test with bad parametters: test if the method detect the bad parammeters
			add profil:
				test with good parametters: test if the method works correctly
				test with bad parametters: test if the method detect the bad parammeters
			add event:
				test with good parametters: test if the method works correctly
				test with bad parametters: test if the method detect the bad parammeters

			del room:
				test with good parametters: test if the method works correctly
				test with bad parametters: test if the method detect the bad parammeters 
			del inhabitant:
				test with good parametters: test if the method works correctly
				test with bad parametters: test if the method detect the bad parammeters 
			del guest:
				test with good parametters: test if the method works correctly
				test with bad parametters: test if the method detect the bad parammeters
			del profil:
				test with good parametters: test if the method works correctly
				test with bad parametters: test if the method detect the bad parammeters
			del event:
				test with good parametters: test if the method works correctly
				test with bad parametters: test if the method detect the bad parammeters

			set room name:
				test with good parametters: test if the method works correctly
				test with bad room id parametters: test if the method detect the bad parammeters
				test with bad newName parametters: test if the method detect the bad parammeters
			set room type:
				test with good parametters: test if the method works correctly
				test with bad room id parametters: test if the method detect the bad parammeters
				test with bad newType parametters: test if the method detect the bad parammeters

			set profil last name:
				test with good parametters: test if the method works correctly
				test with bad profil id parametters: test if the method detect the bad parammeters
				test with bad newLastName parametters: test if the method detect the bad parammeters
			set profil first name:
				test with good parametters: test if the method works correctly
				test with bad profil id parametters: test if the method detect the bad parammeters
				test with bad newFirstName parametters: test if the method detect the bad parammeters

			set inhabitant last name:
				test with good parametters: test if the method works correctly
				test with bad inhabitant id parametters: test if the method detect the bad parammeters
				test with bad newLastName parametters: test if the method detect the bad parammeters
			set inhabitant first name:
				test with good parametters: test if the method works correctly
				test with bad inhabitant id parametters: test if the method detect the bad parammeters
				test with bad newFirstName parametters: test if the method detect the bad parammeters

			set guest last name:
				test with good parametters: test if the method works correctly
				test with bad guest id parametters: test if the method detect the bad parammeters
				test with bad newLastName parametters: test if the method detect the bad parammeters
			set guest first name:
				test with good parametters: test if the method works correctly
				test with bad guest id parametters: test if the method detect the bad parammeters
				test with bad newFirstName parametters: test if the method detect the bad parammeters
	"""

	def setUp(self):
		self.homeDatabase = HomeDatabase()


	def test_homeDatabaseConnection_established(self):
		"""
			test if the connection with the home database is established
		"""

		assert self.homeDatabase.connect() == True
		assert self.homeDatabase.db_connection is not False
		assert self.homeDatabase.db_cursor is not False


	def test_homeDatabaseConnection_disconnected(self):
		"""
			test if the connection with the home database is disconnect
		"""
		self.homeDatabase.connect()

		assert self.homeDatabase.disconnect() == True
		assert self.homeDatabase.db_connection is False
		assert self.homeDatabase.db_cursor is False


	def test_get_rooms_list(self):
		"""
			check if method return good type of data
		"""
		self.homeDatabase.connect()

		#test with connected database
		roomList = self.homeDatabase.get_rooms_list()
		assert isinstance(roomList, list)

		#test with unconnected database
		self.homeDatabase.disconnect()
		self.homeDatabase.get_rooms_list() == False

	def test_get_inhabitants_list(self):
		"""
			check if method return good type of data
		"""
		self.homeDatabase.connect()

		# test with connected database
		inhabitantList = self.homeDatabase.get_inhabitants_list()
		assert isinstance(inhabitantList, list)

		# test with unconnected database
		self.homeDatabase.disconnect()
		self.homeDatabase.get_inhabitants_list() == False

	def test_get_guests_list(self):
		"""
			check if method return good type of data
		"""

		self.homeDatabase.connect()

		# test with connected database
		guestList = self.homeDatabase.get_guests_list()
		assert isinstance(guestList, list)

		# test with unconnected database
		self.homeDatabase.disconnect()
		self.homeDatabase.get_guests_list() == False

	def test_get_profils_list(self):
		"""
			check if method return good type of data
		"""

		self.homeDatabase.connect()

		# test with connected database
		profilList = self.homeDatabase.get_profils_list()
		assert isinstance(profilList, list)

		# test with unconnected database
		self.homeDatabase.disconnect()
		self.homeDatabase.get_profils_list() == False

	def test_get_events_list(self):
		"""
			check if method return good type of data
		"""

		self.homeDatabase.connect()

		# test with connected database
		eventList = self.homeDatabase.get_events_list()
		assert isinstance(eventList, list)

		# test with unconnected database
		self.homeDatabase.disconnect()
		self.homeDatabase.get_events_list() == False

	def test_add_room_(self):
		"""
			test adding room in database
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		#test with good parammeters
		assert self.homeDatabase.add_room('roomTest', 'bathroom') is not False
		for room in self.homeDatabase.get_rooms_list():
			if room[1] == "roomTest" and room[2] == 'bathroom':
				succes = True
				break
			else:
				succes = False

		assert succes is True


		#test with bad parametters
		assert self.homeDatabase.add_room(1, 'bathroom') == False
		assert self.homeDatabase.add_room('roomTest2', 1) == False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.add_room('roomTest3', 'bathroom') == False

	def test_add_profil(self):
		"""
			test adding profil in database
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.add_profil("test1", "test1", "m", "10/10/2010") is not False
		for profil in self.homeDatabase.get_profils_list():
			if profil[1] == "test1" and profil[2] == "test1" \
				and profil[3] == "m" and profil[4] == "10/10/2010":
				succes = True
				break
			else:
				succes = False

		assert succes is True

		# test with bad parametters
		assert self.homeDatabase.add_profil(1, "test1", "m", "10/10/2010") is False
		assert self.homeDatabase.add_profil("test1", 1, "m", "10/10/2010") is False
		assert self.homeDatabase.add_profil("test1", "test1", "g", "10/10/2010") is False
		assert self.homeDatabase.add_profil("test1", "test1", 1, "10/10/2010") is False
		assert self.homeDatabase.add_profil("test1", "test1", "m", 1) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.add_profil("test1", "test1", "m", "10/10/2010") is False

	def test_add_inhabitant(self):
		"""
			test adding inhabitant in database
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		inhabitantId = self.homeDatabase.add_inhabitant("test2", "test2", "m", "10/10/2010")
		assert inhabitantId is not False

		profilId = self.homeDatabase.get_inhabitant(inhabitantId)[1]
		assert profilId is not False

		if profilId is not False:
			for profil in self.homeDatabase.get_profils_list():
				if profil[1] == "test2" and profil[2] == "test2" \
					and profil[3] == "m" and profil[4] == "10/10/2010":
					succes = True
					break
				else:
					succes = False
		else:
			succes = False

		assert succes is True

		# test with bad parametters
		assert self.homeDatabase.add_inhabitant(1, "test2", "m", "10/10/2010") is False
		assert self.homeDatabase.add_inhabitant("test2", 1, "m", "10/10/2010") is False
		assert self.homeDatabase.add_inhabitant("test2", "test2", "g", "10/10/2010") is False
		assert self.homeDatabase.add_inhabitant("test2", "test2", 1, "10/10/2010") is False
		assert self.homeDatabase.add_inhabitant("test2", "test2", "m", 1) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.add_inhabitant("test1", "test2", "m", "10/10/2010") is False

	def test_add_guest(self):
		"""
			testing add an guest in the database
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		guestId = self.homeDatabase.add_guest("test3", "test3", "m", "10/10/2010")
		assert guestId is not False

		profilId = self.homeDatabase.get_guest(guestId)[1]
		assert profilId is not False

		if profilId is not False:
			for profil in self.homeDatabase.get_profils_list():
				if profil[1] == "test3" and profil[2] == "test3" \
						and profil[3] == "m" and profil[4] == "10/10/2010":
					succes = True
					break
				else:
					succes = False
		else:
			succes = False

		assert succes is True

		# test with bad parametters
		assert self.homeDatabase.add_inhabitant(1, "test3", "m", "10/10/2010") is False
		assert self.homeDatabase.add_inhabitant("test3", 1, "m", "10/10/2010") is False
		assert self.homeDatabase.add_inhabitant("test3", "test3", "g", "10/10/2010") is False
		assert self.homeDatabase.add_inhabitant("test3", "test3", 1, "10/10/2010") is False
		assert self.homeDatabase.add_inhabitant("test3", "test3", "m", 1) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.add_inhabitant("test3", "test3", "m", "10/10/2010") is False

	def test_add_event(self):
		"""
			test adding an event in database
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.add_event("motion detection", "01/01/01 01:01:01", 1) is not False
		for event in self.homeDatabase.get_events_list():
			if event[1] == "motion detection" and event[2] == "01/01/01 01:01:01" \
				and event[3] == 1:
				succes = True
			else:
				succes = False

		assert succes is not False

		# test with bad parametters
		assert self.homeDatabase.add_event(1, "01/01/01 01:01:01", 1) is False
		assert self.homeDatabase.add_event("motion detection", 1, 1) is False
		assert self.homeDatabase.add_event("motion detection", "01/01/01 01:01:01", "1") is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.add_event("motion detection", "01/01/01 01:01:01", 1) is False

	def test_get_room(self):
		"""
			test getting an room in database
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.get_room(1) is not False

		room = self.homeDatabase.get_room(1)
		assert room[0] == 1

		for room in self.homeDatabase.get_rooms_list():
			if room[0] == 1:
				succes = True
				break
			else:
				succes = False
		assert succes is not False

		# test with bad parametters
		assert self.homeDatabase.get_room("1") is False
		assert self.homeDatabase.get_room(10000) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.get_room(1) is False
			
	def test_get_inhabitant(self):
		"""
			test getting an habitant in the database
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.get_inhabitant(1) is not False

		inhabitant = self.homeDatabase.get_inhabitant(1)
		assert inhabitant[0] == 1

		for inhabitant in self.homeDatabase.get_inhabitants_list():
			if inhabitant[0] == 1:
				succes = True
				break
			else:
				succes = False
		assert succes is not False

		# test with bad parametters
		assert self.homeDatabase.get_inhabitant("1") is False
		assert self.homeDatabase.get_inhabitant(10000) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.get_inhabitant(1) is False

	def test_get_guest(self):
		"""
			test getting an guest in the database
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.get_guest(1) is not False

		guest = self.homeDatabase.get_guest(1)
		assert guest[0] == 1

		for guest in self.homeDatabase.get_guests_list():
			if guest[0] == 1:
				succes = True
				break
			else:
				succes = False
		assert succes is not False

		# test with bad parametters
		assert self.homeDatabase.get_guest("1") is False
		assert self.homeDatabase.get_guest(10000) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.get_guest(1) is False

	def test_get_profil(self):
		"""
			test getting an profil in the database
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.get_profil(1) is not False

		profil = self.homeDatabase.get_profil(1)
		assert profil[0] == 1

		for profil in self.homeDatabase.get_profils_list():
			if profil[0] == 1:
				succes = True
				break
			else:
				succes = False
		assert succes is not False

		# test with bad parametters
		assert self.homeDatabase.get_profil("1") is False
		assert self.homeDatabase.get_profil(10000) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.get_profil(1) is False

	def test_get_event(self):
		"""
			test getting an event in the database
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.get_event(1) is not False

		event = self.homeDatabase.get_event(1)
		assert event[0] == 1

		for event in self.homeDatabase.get_events_list():
			if event[0] == 1:
				succes = True
				break
			else:
				succes = False
		assert succes is not False

		# test with bad parametters
		assert self.homeDatabase.get_event("1") is False
		assert self.homeDatabase.get_event(10000) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.get_event(1) is False


	def test_set_room_name(self):
		"""
			test changing name of an room in database
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_room_name(1, "testSetName") is True
		room = self.homeDatabase.get_room(1)
		if room[1] == "testSetName":
			succes = True
		else:
			succes = False

		assert succes is True

		#test with bad parametters
		assert self.homeDatabase.set_room_name("1", "testSetName") is False
		assert self.homeDatabase.set_room_name(1, 1) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_room_name(1, "testSetName") is False

	def test_set_room_type(self):
		"""
			test if the method detect the bad parametters
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_room_type(1, "testSetType") is True
		room = self.homeDatabase.get_room(1)
		if room[2] == "testSetType":
			succes = True
		else:
			succes = False

		assert succes is True

		# test with bad parametters
		assert self.homeDatabase.set_room_type("1", "testSetType") is False
		assert self.homeDatabase.set_room_type(1, 1) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_room_type(1, "testSetType") is False

	def test_set_profil_last_name(self):
		"""
			test if the method detect the bad parammeters
		"""

		pass

	def test_set_profil_first_name(self):
		"""
			test if the method detect the bad parammeters
		"""

		pass

	def test_set_inhabitant_last_name(self):
		"""
			test if the method detect the bad parammeters
		"""

		pass

	def test_set_inhabitant_first_name(self):
		"""
			test if the method detect the bad parammeters
		"""

		pass

	def test_set_guest_last_name(self):
		"""
			test if the method detect the bad parammeters
		"""

		pass

	def test_set_guest_first_name(self):
		"""
			test if the method works correctly
		"""

		pass


	def test_del_room(self):
		"""
			test with bad parametters: test if the method detect the bad parammeters
		"""

		pass

	def test_del_inhabitant(self):
		"""
			test with bad parametters: test if the method detect the bad parammeters
		"""

		pass

	def test_del_guest(self):
		pass

		"""
			test with bad parametters: test if the method detect the bad parammeters
		"""

		pass

	def test_del_profil(self):
		"""
			test with bad parametters: test if the method detect the bad parammeters
		"""

		pass

	def test_del_event(self):
		"""
			test with bad parametters: test if the method detect the bad parammeters
		"""
		pass
