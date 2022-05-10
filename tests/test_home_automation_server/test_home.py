import unittest

from homeAutomationServer.classes.home import *

from .fakeClasses.zwaves.fakeNode import *
from .fakeClasses.zwaves.fakeZwaveNetwork import *
from  .fakeClasses.zwaves.fakeController import *


class Test_HomeAutomationSystem(unittest.TestCase):
	"""
		testing class of the home.

		tests List:
			home database attribute:
				check return: check if method return good type of data

			home automationNetwork attribute:
				check return: check if method return good type of data

			rooms list property:
		 		check return: check if method return good type of data
			inhabitants list property:
				check return: check if method return good type of data
			guests list property:
				check return: check if method return good type of data
			profils list property:
				check return: check if method return good type of data
			events list property:
				check return: check if method return good type of data
			modules list property:
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
			get module:
				check return: check if method return good type of data

			set inhabitants first name
			set inhabitants last name
			set inhabitants sexe
			set inhabitants date of birth

			set guest first name
			set guest last name
			set guest sexe
			set guest date of birth

			set profil first name
			set profil last name
			set profil sexe
			set profil date of birth

			set module name
			set module location
	"""

	def setUp(self):
		self.home = Home()
		self.goodZWaveNetwork = FakeZwaveNetwork(10, 10, True)
		self.badZWaveNetwork = FakeZwaveNetwork(10, 1, False)

		self.home.homeDatabase.databaseName = "TestHome"


	def test_home_id_property(self):
		"""
			test getting home id
		"""

		# test with zwaveNework corectly configured
		self.home.homeAutomationNetwork.zWaveNetwork = self.goodZWaveNetwork
		assert isinstance(self.home.homeAutomationNetwork.homeId, int)
		assert self.home.homeAutomationNetwork.homeId == 10

		# test with zwaveNetwork uncorrectly configured
		self.home.homeAutomationNetwork.zWaveNetwork = self.badZWaveNetwork
		assert isinstance(self.home.homeAutomationNetwork.homeId, int)
		assert self.home.homeAutomationNetwork.homeId == 10

		# test with failure zwaveNetwork
		self.home.homeAutomationNetwork.zWaveNetwork = False
		assert isinstance(self.home.homeAutomationNetwork.homeId, bool)
		assert self.home.homeAutomationNetwork.homeId is False



	def test_rooms_list_property(self):
		"""
			test get rooms list
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		roomList = self.home.roomsList

		assert roomList is not False
		assert isinstance(roomList, list)

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.roomsList is False
			
	def test_inhabitants_list_property(self):
		"""
			test getting the inhabitant list
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		inhabitantList = self.home.inhabitantsList

		assert inhabitantList is not False
		assert isinstance(inhabitantList, list)

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.inhabitantsList is False

	def test_guests_list_property(self):
		"""
			test getting guests list
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		guestList = self.home.guestsList

		assert guestList is not False
		assert isinstance(guestList, list)

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.guestsList is False

	def test_profils_list_property(self):
		"""
			test getting profils list
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		profilList = self.home.profilsList

		assert profilList is not False
		assert isinstance(profilList, list)

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.profilsList is False

	def test_events_list_property(self):
		"""
			test getting events list
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		eventList = self.home.eventsList

		assert eventList is not False
		assert isinstance(eventList, list)

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.eventsList is False

	def test_modules_list_property(self):
		"""
			test getting modules list
		"""

		# test with zwaveNework corectly configured
		self.home.homeAutomationNetwork.zWaveNetwork = self.goodZWaveNetwork
		moduleList = self.home.modulesList
		assert moduleList is not False
		assert isinstance(moduleList, list)

		# test with zwaveNetwork uncorrectly configured
		self.home.homeAutomationNetwork.zWaveNetwork = self.badZWaveNetwork
		assert self.home.modulesList is False

		# test with failure zwaveNetwork
		self.home.homeAutomationNetwork.zWaveNetwork = False
		assert self.home.modulesList is False


	def test_get_room(self):
		"""
			test getting an specific room
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		room = self.home.get_room(1)
		assert room is not False
		assert isinstance(room, Room)

		#test with bad parametters
		room = self.home.get_room("1")
		assert room is False


		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.get_room(1) is False
			
	def test_get_inhabitant(self):
		"""
			test getting and specific inhabitant
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		inhabitant = self.home.get_inhabitant(1)
		assert inhabitant is not False
		assert isinstance(inhabitant, Inhabitant)

		# test with bad parametters
		inhabitant = self.home.get_inhabitant("1")
		assert inhabitant is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.get_inhabitant(1) is False

	def test_get_guest(self):
		"""
			test getting an specific guest
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		guest = self.home.get_guest(1)
		assert guest is not False
		assert isinstance(guest, Guest)

		# test with bad parametters
		guest = self.home.get_guest("1")
		assert guest is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.get_guest(1) is False

	def test_get_profil(self):
		"""
			check if method return good type of data
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		profil = self.home.get_profil(1)
		assert profil is not False
		assert isinstance(profil, Profil)

		# test with bad parametters
		profil = self.home.get_profil("1")
		assert profil is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.get_profil(1) is False

	def test_get_event(self):
		"""
			check if method return good type of data
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		event = self.home.get_event(1)
		assert event is not False
		assert isinstance(event, Event)

		# test with bad parametters
		event = self.home.get_event("1")
		assert event is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.get_event(1) is False

	def test_get_module(self):
		"""
			check if method return good type of data
		"""

		# test with zwaveNework corectly configured
		self.home.homeAutomationNetwork.zWaveNetwork = self.goodZWaveNetwork
		module = self.home.get_module(1)
		assert module is not False
		assert isinstance(module, Module)

		#test with bad parametters
		assert self.home.get_module("1") is False

		# test with zwaveNetwork uncorrectly configured
		self.home.homeAutomationNetwork.zWaveNetwork = self.badZWaveNetwork
		assert self.home.get_module(1) is False

		# test with failure zwaveNetwork
		self.home.homeAutomationNetwork.zWaveNetwork = False
		assert self.home.get_module(1) is False


	def test_add_room(self):
		"""
			test adding an room
		"""
		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		roomId = self.home.add_room("test", 'bathroom')
		assert roomId is not False
		assert self.home.get_room(roomId).name == 'test'

		# test with bad parametters
		assert self.home.add_room(1, 'bathroom') is False
		assert self.home.add_room("test", 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.add_room("test", 'bathroom') is False

	def test_add_inhabitant(self):
		"""
			test adding an inhabitant
		"""
		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		inhabitantId = self.home.add_inhabitant("test2", "test2", "m", "10/10/2010")
		assert inhabitantId is not False
		assert self.home.get_inhabitant(inhabitantId).firstName == "test2"

		# test with bad parametters
		assert self.home.add_inhabitant(1, "test2", "m", "10/10/2010") is False
		assert self.home.add_inhabitant("test2", 1, "m", "10/10/2010") is False
		assert self.home.add_inhabitant("test2", "test2", 1, "10/10/2010") is False
		assert self.home.add_inhabitant("test2", "test2", "z", "10/10/2010") is False
		assert self.home.add_inhabitant("test2", "test2", "m", 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.add_inhabitant("test2", "test2", "m", "10/10/2010") is False

	def test_add_guest(self):
		"""
			test adding guest
		"""
		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		guestId = self.home.add_guest("test3", "test3", "m", "10/10/2010")
		assert guestId is not False
		assert self.home.get_guest(guestId).firstName == "test3"

		# test with bad parametters
		assert self.home.add_guest(1, "test3", "m", "10/10/2010") is False
		assert self.home.add_guest("test3", 1, "m", "10/10/2010") is False
		assert self.home.add_guest("test3", "test3", 1, "10/10/2010") is False
		assert self.home.add_guest("test3", "test3", "z", "10/10/2010") is False
		assert self.home.add_guest("test3", "test3", "m", 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.add_guest("test3", "test3", "m", "10/10/2010") is False

	def test_add_profil(self):
		"""
			test adding profil
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		profilId = self.home.add_profil("test4", "test4", "m", "10/10/2010")
		assert profilId is not False
		assert self.home.get_profil(profilId).firstName == "test4"

		# test with bad parametters
		assert self.home.add_profil(1, "test4", "m", "10/10/2010") is False
		assert self.home.add_profil("test4", 1, "m", "10/10/2010") is False
		assert self.home.add_profil("test4", "test4", 1, "10/10/2010") is False
		assert self.home.add_profil("test4", "test4", "z", "10/10/2010") is False
		assert self.home.add_profil("test4", "test4", "m", 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.add_profil("test4", "test4", "m", "10/10/2010") is False

	def test_add_event(self):
		"""
			test adding an event
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		eventId = self.home.add_event("motion detection", "10/10/2010 01:01:01", 1)
		assert eventId is not False
		assert self.home.get_event(eventId).type == "motion detection"

		# test with bad parametters
		assert self.home.add_event(1, "10/10/2010 01:01:01", 1) is False
		assert self.home.add_event("motion detection", 1, 1) is False
		assert self.home.add_event("motion detection", "10/10/2010 01:01:01", "1") is False


		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.add_event("motion detection", "10/10/2010 01:01:01", 1) is False


	def test_add_module(self):
		"""
			test adding an module
		"""
		# test with zwaveNework corectly configured
		self.home.homeAutomationNetwork.zWaveNetwork = self.goodZWaveNetwork
		self.home.homeAutomationNetwork.zWaveNetwork.controller.zwaveNetwork = self.home.homeAutomationNetwork.zWaveNetwork
		moduleId = self.home.add_module("test", 1)
		assert moduleId is not False
		assert self.home.get_module(moduleId).name == "test"

		# test with bad parametters
		assert self.home.add_module(1, 1) is False
		assert self.home.add_module("test", "1") is False

		# test with zwaveNetwork uncorrectly configured
		self.home.homeAutomationNetwork.zWaveNetwork = self.badZWaveNetwork
		assert self.home.add_module("test", 1) is False

		# test with failure zwaveNetwork
		self.home.homeAutomationNetwork.zWaveNetwork = False
		assert self.home.add_module("test", 1) is False


	def test_del_room(self):
		"""
			test deleting an room
		"""
		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		roomId = self.home.add_room("testDel", "bathroom")
		assert self.home.del_room(roomId) is not False
		assert self.home.get_room(roomId) is False

		# test with bad parametters
		assert self.home.del_room('1') is False
		assert self.home.del_room(10000) is False


		# test with unconnected database
		roomId = self.home.add_room("testDel2", "bathroom")
		self.home.homeDatabase.disconnect()

		assert self.home.del_room(roomId) is False

	def test_del_inhabitant(self):
		"""
			test deleting an inhabitant
		"""
		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		inhabitantId = self.home.add_inhabitant("testDel", "testDel", "m", "10/10/2010")
		assert self.home.del_inhabitant(inhabitantId) is not False
		assert self.home.get_inhabitant(inhabitantId) is False

		# test with bad parametters
		assert self.home.del_inhabitant('1') is False
		assert self.home.del_inhabitant(10000) is False

		# test with unconnected database
		inhabitantId = self.home.add_inhabitant("testDel2", "testDel2", "m", "10/10/2010")

		self.home.homeDatabase.disconnect()

		assert self.home.del_inhabitant(inhabitantId) is False

	def test_del_guest(self):
		"""
			test deleting an guest
		"""
		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		guestId = self.home.add_guest("testDel", "testDel", "m", "10/10/2010")
		assert self.home.del_guest(guestId) is not False
		assert self.home.get_guest(guestId) is False

		# test with bad parametters
		assert self.home.del_guest('1') is False
		assert self.home.del_guest(10000) is False

		# test with unconnected database
		guestId = self.home.add_guest("testDel2", "testDel2", "m", "10/10/2010")

		self.home.homeDatabase.disconnect()

		assert self.home.del_guest(guestId) is False

	def test_del_profil(self):
		"""
			test deleting an profil
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		profilId = self.home.add_profil("testDel3", "testDel3", "m", "10/10/2010")
		assert self.home.del_profil(profilId) is not False
		assert self.home.get_profil(profilId) is False

		# test with bad parametters
		assert self.home.del_profil('1') is False
		assert self.home.del_profil(10000) is False

		# test with unconnected database
		profilId = self.home.add_profil("testDel3", "testDel3", "m", "10/10/2010")

		self.home.homeDatabase.disconnect()

		assert self.home.del_profil(profilId) is False

	def test_del_event(self):
		"""
			test deleting an event
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		eventId = self.home.add_event("motion detection", "10/10/2010", 1)
		assert self.home.del_event(eventId) is not False
		assert self.home.get_event(eventId) is False

		# test with bad parametters
		assert self.home.del_event('1') is False
		assert self.home.del_event(10000) is False

		# test with unconnected database
		eventId = self.home.add_event("motion detection", "10/10/2010", 1)

		self.home.homeDatabase.disconnect()

		assert self.home.del_event(eventId) is False

	def test_set_room_name(self):
		"""
			test setting an roomName
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_room_name(1, "testSetName") is not False
		assert self.home.get_room(1).name == "testSetName"

		# test with bad parametters
		assert self.home.set_room_name("1", "testSetName") is False
		assert self.home.set_room_name(1, 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_room_name(1, "testSetName") is False

	def test_set_room_type(self):
		"""
			test setting module location
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_room_type(1, "corridor") is not False
		assert self.home.get_room(1).type == "corridor"

		# test with bad parametters
		assert self.home.set_room_name("1", "corridor") is False
		assert self.home.set_room_name(1, 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_room_name(1, "corridor") is False

	def test_set_profil_last_name(self):
		"""
			test setting the last name of an profil
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_profil_last_name(1, "testSetLN") is not False
		assert self.home.get_profil(1).lastName == "testSetLN"

		# test with bad parametters
		assert self.home.set_profil_last_name("1", "testSetLN") is False
		assert self.home.set_profil_last_name(1, 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_profil_last_name(1, "testSetLN") is False

	def test_set_profil_first_name(self):
		"""
			test setting the first name of an profil
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_profil_first_name(1, "testSetFN") is not False
		assert self.home.get_profil(1).firstName == "testSetFN"

		# test with bad parametters
		assert self.home.set_profil_first_name("1", "testSetFN") is False
		assert self.home.set_profil_first_name(1, 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_profil_first_name(1, "testSetFN") is False

	def test_set_profil_sexe(self):
		"""
			test setting the sexe of an profil
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_profil_sexe(1, "f") is not False
		assert self.home.get_profil(1).sexe == "f"

		# test with bad parametters
		assert self.home.set_profil_sexe("1", "f") is False
		assert self.home.set_profil_sexe(1, 1) is False
		assert self.home.set_profil_sexe(1, "z") is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_profil_sexe(1, "f") is False

	def test_set_profil_date_of_birth(self):
		"""
			test setting the date of birth of an profil
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_profil_date_of_birth(1, "02/02/02") is not False
		assert self.home.get_profil(1).dateOfBirth == "02/02/02"

		# test with bad parametters
		assert self.home.set_profil_date_of_birth("1", "02/02/02") is False
		assert self.home.set_profil_date_of_birth(1, 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_profil_date_of_birth(1, "02/02/02") is False

	def test_set_inhabitant_last_name(self):
		"""
			test setting the last name of an inabitant
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_inhabitant_last_name(1, "testSetLN") is not False
		assert self.home.get_inhabitant(1).lastName == "testSetLN"

		# test with bad parametters
		assert self.home.set_inhabitant_last_name("1", "testSetLN") is False
		assert self.home.set_inhabitant_last_name(1, 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_inhabitant_last_name(1, "testSetLN") is False

	def test_set_inhabitant_first_name(self):
		"""
			test setting the first name of an inhabitant
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_inhabitant_first_name(1, "testSetFN") is not False
		assert self.home.get_inhabitant(1).firstName == "testSetFN"

		# test with bad parametters
		assert self.home.set_inhabitant_first_name("1", "testSetFN") is False
		assert self.home.set_inhabitant_first_name(1, 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_inhabitant_first_name(1, "testSetFN") is False

	def test_set_inhabitant_sexe(self):
		"""
			test setting the sexe of an inhabitant
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_inhabitant_sexe(1, "f") is not False
		assert self.home.get_inhabitant(1).sexe == "f"

		# test with bad parametters
		assert self.home.set_inhabitant_sexe("1", "f") is False
		assert self.home.set_inhabitant_sexe(1, 1) is False
		assert self.home.set_inhabitant_sexe(1, "z") is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_inhabitant_sexe(1, "f") is False

	def test_set_inhabitant_date_of_birth(self):
		"""
			test setting the date of birth of an inhabitant
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_inhabitant_date_of_birth(1, "02/02/02") is not False
		assert self.home.get_inhabitant(1).dateOfBirth == "02/02/02"

		# test with bad parametters
		assert self.home.set_inhabitant_date_of_birth("1", "02/02/02") is False
		assert self.home.set_inhabitant_date_of_birth(1, 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_inhabitant_date_of_birth(1, "02/02/02") is False

	def test_set_guest_last_name(self):
		"""
			test setting the last name of an guest
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_guest_last_name(1, "testSetLN") is not False
		assert self.home.get_guest(1).lastName == "testSetLN"

		# test with bad parametters
		assert self.home.set_guest_last_name("1", "testSetLN") is False
		assert self.home.set_guest_last_name(1, 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_guest_last_name(1, "testSetLN") is False

	def test_set_guest_first_name(self):
		"""
			test setting the first name of an guest
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_guest_first_name(1, "testSetFN") is not False
		assert self.home.get_guest(1).firstName == "testSetFN"

		# test with bad parametters
		assert self.home.set_guest_first_name("1", "testSetFN") is False
		assert self.home.set_guest_first_name(1, 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_guest_first_name(1, "testSetFN") is False

	def test_set_guest_sexe(self):
		"""
			test setting the sexe of an inhabitant
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_guest_sexe(1, "f") is not False
		assert self.home.get_guest(1).sexe == "f"

		# test with bad parametters
		assert self.home.set_guest_sexe("1", "f") is False
		assert self.home.set_guest_sexe(1, 1) is False
		assert self.home.set_guest_sexe(1, "z") is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_guest_sexe(1, "f") is False

	def test_set_guest_date_of_birth(self):
		"""
			test setting the date of birth of an guest
		"""

		self.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.home.set_guest_date_of_birth(1, "02/02/02") is not False
		assert self.home.get_guest(1).dateOfBirth == "02/02/02"

		# test with bad parametters
		assert self.home.set_guest_date_of_birth("1", "02/02/02") is False
		assert self.home.set_guest_date_of_birth(1, 1) is False

		# test with unconnected database
		self.home.homeDatabase.disconnect()
		assert self.home.set_guest_date_of_birth(1, "02/02/02") is False


	def test_set_module_name(self):
		"""
			test setting the name of an module
		"""

		# test with zwaveNework corectly configured
		self.home.homeAutomationNetwork.zWaveNetwork = self.goodZWaveNetwork
		assert self.home.set_module_name(1, 'testSetName') is not False
		assert self.home.get_module(1).name == 'testSetName'

		# test with bad parametters
		assert self.home.set_module_name("1", 'testSetName') is False
		assert self.home.set_module_name(1, 1) is False

		# test with zwaveNetwork uncorrectly configured
		self.home.homeAutomationNetwork.zWaveNetwork = self.badZWaveNetwork
		assert self.home.set_module_name(1, 'testSetName') is False

		# test with failure zwaveNetwork
		self.home.homeAutomationNetwork.zWaveNetwork = False
		assert self.home.set_module_name(1, 'testSetName') is False

	def test_set_module_location(self):
		"""
			test setting the name of an module
		"""

		# test with zwaveNework corectly configured
		self.home.homeAutomationNetwork.zWaveNetwork = self.goodZWaveNetwork
		assert self.home.set_module_location(1, 1) is not False
		assert self.home.get_module(1).location == 1

		# test with bad parametters
		assert self.home.set_module_location("1", 1) is False
		assert self.home.set_module_location(1, "1") is False

		# test with zwaveNetwork uncorrectly configured
		self.home.homeAutomationNetwork.zWaveNetwork = self.badZWaveNetwork
		assert self.home.set_module_location(1, 1) is False

		# test with failure zwaveNetwork
		self.home.homeAutomationNetwork.zWaveNetwork = False
		assert self.home.set_module_location(1, 1) is False

"""
	def test_del_module(self):
		pass
"""