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
			get inhabitants list:
			get guests list:
			get profils list:
			get events list:
			get room:
			get inhabitant:
			get guest:
			get profil:
			get event:

			add room:
			add inhabitant:
			add guest:
			add profil:
			add event:


			del room:
			del inhabitant:
			del guest:
			del profil:
			del event:

			set room name:
			set room type:
			set profil last name:
			set profil first name:

			set inhabitant last name:
			set inhabitant first name:
			set guest last name:
			set guest first name:
	"""

	def setUp(self):
		self.homeDatabase = HomeDatabase()
		self.homeDatabase.databaseName = "TestHome"


	def test_homeDatabaseConnection_established(self):
		"""
			test if the connection with the home database is established
		"""

		assert self.homeDatabase.connect() is not False
		assert self.homeDatabase.db_connection is not False
		assert self.homeDatabase.db_cursor is not False


	def test_homeDatabaseConnection_disconnected(self):
		"""
			test if the connection with the home database is disconnect
		"""
		self.homeDatabase.connect()

		assert self.homeDatabase.disconnect() is not False
		assert self.homeDatabase.db_connection is False
		assert self.homeDatabase.db_cursor is False


	def test_add_room_(self):
		"""
			test adding room in database
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.add_room('roomTest', 'bathroom') is not False
		for room in self.homeDatabase.get_rooms_list():
			if room[1] == "roomTest" and room[2] == 'bathroom':
				succes = True
				break
			else:
				succes = False

		assert succes is True

		# test with bad parametters
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


	def test_get_rooms_list(self):
		"""
			check if method return good type of data
		"""
		self.homeDatabase.connect()

		#test with connected database
		roomList = self.homeDatabase.get_rooms_list()
		assert roomList is not False
		assert isinstance(roomList, list)

		#test with unconnected database
		self.homeDatabase.disconnect()
		self.homeDatabase.get_rooms_list() is False

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
			test changing the type of the room
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
			test changing the last name of an profil
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_profil_last_name(1, "testSetProfilLN") is True
		assert self.homeDatabase.get_profil(1)[2] == "testSetProfilLN"

		#test with bad parametters
		assert self.homeDatabase.set_profil_last_name("1", "testSetProfilLN") is False
		assert self.homeDatabase.set_profil_last_name(1, 1) is False
		assert self.homeDatabase.set_profil_last_name(10000, "testSetProfilLN") is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_profil_last_name(1, "testSetProfilLN") is False

	def test_set_profil_first_name(self):
		"""
			test changing the last name of an profil
		"""

		succes = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_profil_first_name(1, "testSetProfilFN") is True
		assert self.homeDatabase.get_profil(1)[1] == "testSetProfilFN"

		# test with bad parametters
		assert self.homeDatabase.set_profil_first_name("1", "testSetProfilFN") is False
		assert self.homeDatabase.set_profil_first_name(1, 1) is False
		assert self.homeDatabase.set_profil_first_name(10000, "testSetProfilFN") is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_profil_first_name(1, "testSetProfilFN") is False

	def test_set_profil_sexe(self):
		"""
			test changing the sexe of an profil
		"""
		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_profil_sexe(1, "f") is True
		assert self.homeDatabase.get_profil(1)[3] == "f"

		# test with bad parametters
		assert self.homeDatabase.set_profil_sexe("1", "f") is False
		assert self.homeDatabase.set_profil_sexe(1, 1) is False
		assert self.homeDatabase.set_profil_sexe(10000, "f") is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_profil_sexe(1, "f") is False

	def test_set_profil_date_of_birth(self):
		"""
			test changing the date of birth of an profil
		"""
		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_profil_date_of_birth(1, "02/02/2002") is True
		assert self.homeDatabase.get_profil(1)[4] == "02/02/2002"

		# test with bad parametters
		assert self.homeDatabase.set_profil_date_of_birth("1", "02/02/2002") is False
		assert self.homeDatabase.set_profil_date_of_birth(1, 1) is False
		assert self.homeDatabase.set_profil_date_of_birth(10000, "02/02/2002") is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_profil_date_of_birth(1, "02/02/2002") is False

	def test_set_inhabitant_last_name(self):
		"""
			test changing inhabitant last name
		"""

		succes = profil = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_inhabitant_last_name(1, "testSetInhabitantLN") is True

		profilId = self.homeDatabase.get_inhabitant(1)[1]

		assert self.homeDatabase.get_profil(profilId)[2] == "testSetInhabitantLN"

		#test with bad parametters
		assert self.homeDatabase.set_inhabitant_last_name("1", "testSetInhabitantLN") is False
		assert self.homeDatabase.set_inhabitant_last_name(1, 1) is False
		assert self.homeDatabase.set_inhabitant_last_name(1000, "testSetInhabitantLN") is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_inhabitant_last_name(1, "testSetInhabitantLN") is False


	def test_set_inhabitant_first_name(self):
		"""
			test changing inhabitant first name
		"""

		succes = profil = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_inhabitant_first_name(1, "testSetInhabitantFN") is True

		profilId = self.homeDatabase.get_inhabitant(1)[1]

		assert self.homeDatabase.get_profil(profilId)[1] == "testSetInhabitantFN"

		# test with bad parametters
		assert self.homeDatabase.set_inhabitant_first_name("1", "testSetIFN") is False
		assert self.homeDatabase.set_inhabitant_first_name(1, 1) is False
		assert self.homeDatabase.set_inhabitant_first_name(1000, "testSetIFN") is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_inhabitant_first_name(1, "testSetInhabitantFN") is False


	def test_set_inhabitant_sexe(self):
		"""
			test changing the sexe of an inhabitant
		"""

		succes = profil = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_inhabitant_sexe(1, "f") is True

		profilId = self.homeDatabase.get_inhabitant(1)[1]

		assert self.homeDatabase.get_profil(profilId)[3] == "f"

		# test with bad parametters
		assert self.homeDatabase.set_inhabitant_sexe("1", "f") is False
		assert self.homeDatabase.set_inhabitant_sexe(1, "g") is False
		assert self.homeDatabase.set_inhabitant_sexe(1, 1) is False
		assert self.homeDatabase.set_inhabitant_sexe(1000, "testSetIFN") is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_inhabitant_sexe(1, "f") is False


	def test_set_inhabitant_date_of_birth(self):
		"""
			test changin the date of birth of an inhabitant
		"""

		succes = profil = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_inhabitant_date_of_birth(1, "03/03/03") is True

		profilId = self.homeDatabase.get_inhabitant(1)[1]

		assert self.homeDatabase.get_profil(profilId)[4] == "03/03/03"

		# test with bad parametters
		assert self.homeDatabase.set_inhabitant_sexe("1", "03/03/03") is False
		assert self.homeDatabase.set_inhabitant_sexe(1, 1) is False
		assert self.homeDatabase.set_inhabitant_sexe(1000, "03/03/03") is False

		print('1')

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_inhabitant_date_of_birth(1, "03/03/03") is False


	def test_set_guest_last_name(self):
		"""
			test if the method detect the bad parammeters
		"""

		print("2")

		succes = profil = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_guest_last_name(1, "testSetGuestLN") is True

		profilId = self.homeDatabase.get_guest(1)[1]

		assert self.homeDatabase.get_profil(profilId)[2] == "testSetGuestLN"

		# test with bad parametters
		assert self.homeDatabase.set_guest_last_name("1", "testSetGuestLN") is False
		assert self.homeDatabase.set_guest_last_name(1, 1) is False
		assert self.homeDatabase.set_guest_last_name(1000, "testSetGuestLN") is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_guest_last_name(1, "testSetGuestLN") is False

	def test_set_guest_first_name(self):
		"""
			test if the method works correctly
		"""

		succes = profil = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_guest_first_name(1, "testSetGuestFN") is True

		profilId = self.homeDatabase.get_guest(1)[1]

		assert self.homeDatabase.get_profil(profilId)[1] == "testSetGuestFN"

		# test with bad parametters
		assert self.homeDatabase.set_guest_first_name("1", "testSetGuestFN") is False
		assert self.homeDatabase.set_guest_first_name(1, 1) is False
		assert self.homeDatabase.set_guest_first_name(1000, "testSetGuestFN") is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_guest_first_name(1, "testSetGuestFN") is False

	def test_set_guest_sexe(self):
		"""
			test changing the sexe of an guest
		"""

		succes = profil = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_guest_sexe(1, "f") is True

		profilId = self.homeDatabase.get_guest(1)[1]

		assert self.homeDatabase.get_profil(profilId)[3] == "f"

		# test with bad parametters
		assert self.homeDatabase.set_guest_sexe("1", "f") is False
		assert self.homeDatabase.set_guest_sexe(1, 1) is False
		assert self.homeDatabase.set_guest_sexe("1", "g") is False
		assert self.homeDatabase.set_guest_sexe(1000, "f") is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_guest_sexe(1, "f") is False

	def test_set_guest_date_of_birth(self):
		"""
			test changin the date of birth of an guest
		"""

		succes = profil = False

		self.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeDatabase.set_guest_date_of_birth(1, "04/04/04") is True

		profilId = self.homeDatabase.get_guest(1)[1]

		assert self.homeDatabase.get_profil(profilId)[4] == "04/04/04"

		# test with bad parametters
		assert self.homeDatabase.set_guest_date_of_birth("1", "04/04/04") is False
		assert self.homeDatabase.set_guest_date_of_birth(1, 1) is False
		assert self.homeDatabase.set_guest_date_of_birth(1000, "04/04/04") is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.set_guest_date_of_birth(1, "04/04/04") is False


	def test_del_room(self):
		"""
			test deleting an room in the database
		"""

		self.homeDatabase.connect()

		roomId = self.homeDatabase.add_room("testDel", "testDel")

		# test with connected database
		# test with good parametters
		assert self.homeDatabase.del_room(roomId) is True
		assert self.homeDatabase.get_room(roomId) is False

		# test with bad parametters
		assert self.homeDatabase.del_room("1") is False
		assert self.homeDatabase.del_room(10000) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.del_room(2) is False

	def test_del_inhabitant(self):
		"""
			test deleting an inhabitant in the database
		"""

		self.homeDatabase.connect()

		inhabitantId = self.homeDatabase.add_inhabitant("testDel", "testDel", "m", "0/0/0")

		# test with connected database
		# test with good parametters
		assert self.homeDatabase.del_inhabitant(inhabitantId) is True
		assert self.homeDatabase.get_inhabitant(inhabitantId) is False
		# ajouter verif profil

		# test with bad parametters
		assert self.homeDatabase.del_inhabitant("1") is False
		assert self.homeDatabase.del_inhabitant(10000) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.del_inhabitant(1) is False

	def test_del_guest(self):

		"""
			test deleting an guest in the database
		"""

		self.homeDatabase.connect()

		guestId = self.homeDatabase.add_guest("testDel", "testDel", "m", "0/0/0")

		# test with connected database
		# test with good parametters
		assert self.homeDatabase.del_guest(guestId) is True
		assert self.homeDatabase.get_guest(guestId) is False
		#ajouter verif profil

		# test with bad parametters
		assert self.homeDatabase.del_guest("1") is False
		assert self.homeDatabase.del_guest(10000) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.del_guest(1) is False

	def test_del_profil(self):
		"""
			test with bad parametters: test if the method detect the bad parammeters
		"""

		self.homeDatabase.connect()

		guestId = self.homeDatabase.add_profil("testDel", "testDel", "m", "0/0/0")

		# test with connected database
		# test with good parametters
		assert self.homeDatabase.del_profil(guestId) is True
		assert self.homeDatabase.get_profil(guestId) is False

		# test with bad parametters
		assert self.homeDatabase.del_profil("1") is False
		assert self.homeDatabase.del_profil(10000) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.del_profil(1) is False

	def test_del_event(self):
		"""
			test with bad parametters: test if the method detect the bad parammeters
		"""
		self.homeDatabase.connect()

		eventId = self.homeDatabase.add_event("testDel", "test", 1)

		# test with connected database
		# test with good parametters
		assert self.homeDatabase.del_event(eventId) is True
		assert self.homeDatabase.get_event(eventId) is False

		# test with bad parametters
		assert self.homeDatabase.del_event("1") is False
		assert self.homeDatabase.del_event(10000) is False

		# test with unconnected database
		self.homeDatabase.disconnect()
		assert self.homeDatabase.del_event(1) is False
