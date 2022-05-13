import unittest

from homeAutomationServer.classes.homeAutomationSystem import *

from .fakeClasses.zwaves.fakeNode import *
from .fakeClasses.zwaves.fakeZwaveNetwork import *
from  .fakeClasses.zwaves.fakeController import *

class Test_HomeAutomationSystem(unittest.TestCase):
	"""
		testing class of the home automation system.

		tests list:
			ruuning attribute:
				
			start method:
			stop method:

			set running:

			get rooms list:
			get inhabitants list:
			get guests list:
			get profils list:
			get events list:
			get modules list

			get room:
			get inhabitant:
			get guest:
			get profil:
			get event:
			get module:
			get home:
			get home automation network

			add room:
			add inhabitant:
			add guest:
			add profil:
			add module:
			add event:

			del room:
			del inhabitant:
			del guest:
			del profil:
			del module:
			del event:

			set room name:
			set room type:
			set profil last name:
			set profil first name:
			set profil sexe
			set profil date of birth
			set inhabitant last name:
			set inhabitant first name:
			set inhabitant sexe
			set inhabitant date of birth
			set guest last name:
			set guest first name:
			set guest sexe
			set guest date of birth

			set module name:
			set module location:
			set automation network controller path:
			set automation network zwave config file
	"""


	def setUp(self):
		self.homeAutomationSystem = HomeAutomationSystem()
		self.goodZWaveNetwork = FakeZwaveNetwork(10, 10, True)
		self.badZWaveNetwork = FakeZwaveNetwork(10, 1, False)

		self.homeAutomationSystem.home.homeDatabase.databaseName = "TestHome"

	def test_running(self):
		"""
			test running property
		"""

		assert isinstance(self.homeAutomationSystem.running, bool)


	def test_set_running(self):
		"""
			test setting the running property
		"""
				
		assert self.homeAutomationSystem.set_running(True) is not False
		assert self.homeAutomationSystem.running == True

		assert self.homeAutomationSystem.set_running("True") is False


	def test_get_rooms_list(self):
		"""
			test getting room list
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		roomList = self.homeAutomationSystem.get_rooms_list()

		assert roomList is not False
		assert isinstance(roomList, list)

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.get_rooms_list() is False
			
	def test_get_inhabitants_list(self):
		"""
			test getting inhabitants list
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		inhabitantList = self.homeAutomationSystem.get_inhabitants_list()

		assert inhabitantList is not False
		assert isinstance(inhabitantList, list)

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.get_inhabitants_list() is False

	def test_get_guests_list(self):
		"""
			test guetting guest list
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		guestList = self.homeAutomationSystem.get_guests_list()

		assert guestList is not False
		assert isinstance(guestList, list)

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.get_guests_list() is False

	def test_get_profils_list(self):
		"""
			test getting profils list
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		profilList = self.homeAutomationSystem.get_profils_list()

		assert profilList is not False
		assert isinstance(profilList, list)

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.get_profils_list() is False

	def test_get_events_list(self):
		"""
			test getting events list
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		eventList = self.homeAutomationSystem.get_events_list()

		assert eventList is not False
		assert isinstance(eventList, list)

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.get_events_list() is False

	def test_get_modules_list(self):
		"""
			test getting modules list
		"""

		# test with zwaveNework corectly configured
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = self.goodZWaveNetwork
		moduleList = self.homeAutomationSystem.get_modules_list()
		assert moduleList is not False
		assert isinstance(moduleList, list)

		# test with zwaveNetwork uncorrectly configured
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = self.badZWaveNetwork
		assert self.homeAutomationSystem.get_modules_list() is False

		# test with failure zwaveNetwork
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = False
		assert self.homeAutomationSystem.get_modules_list() is False

	def test_get_room(self):
		"""
			test getting an specific room
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		room = self.homeAutomationSystem.get_room(1)
		assert room is not False
		assert isinstance(room, Room)

		#test with bad parametters
		assert self.homeAutomationSystem.get_room("1") is False


		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.get_room(1) is False

	def test_get_inhabitant(self):
		"""
			test getting an specific inhabitant
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		inhabitant = self.homeAutomationSystem.get_inhabitant(1)
		assert inhabitant is not False
		assert isinstance(inhabitant, Inhabitant)

		# test with bad parametters
		assert self.homeAutomationSystem.get_inhabitant("1") is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.get_inhabitant(1) is False

	def test_get_guest(self):
		"""
			test getting an specific guest
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		guest = self.homeAutomationSystem.get_guest(1)
		assert guest is not False
		assert isinstance(guest, Guest)

		# test with bad parametters
		assert self.homeAutomationSystem.get_guest("1") is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.get_guest(1) is False

	def test_get_profil(self):
		"""
			test getting an specific profil
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		profil = self.homeAutomationSystem.get_profil(1)
		assert profil is not False
		assert isinstance(profil, Profil)

		# test with bad parametters
		assert self.homeAutomationSystem.get_profil("1") is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.get_profil(1) is False

	def test_get_event(self):
		"""
			test getting an specific event
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		event = self.homeAutomationSystem.get_event(1)
		assert event is not False
		assert isinstance(event, Event)

		# test with bad parametters
		assert self.homeAutomationSystem.get_event("1") is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.get_event(1) is False

	def test_get_module(self):
		"""
			test getting an specific module
		"""

		# test with zwaveNework corectly configured
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = self.goodZWaveNetwork
		module = self.homeAutomationSystem.get_module(1)
		assert module is not False
		assert isinstance(module, Module)

		assert self.homeAutomationSystem.get_module("1") is False

		# test with zwaveNetwork uncorrectly configured
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = self.badZWaveNetwork
		assert self.homeAutomationSystem.get_module(1) is False

		# test with failure zwaveNetwork
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = False
		assert self.homeAutomationSystem.get_module(1) is False


	def test_add_room(self):
		"""
			test adding an room
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		roomId = self.homeAutomationSystem.add_room("test", 'bathroom')
		assert roomId is not False
		assert self.homeAutomationSystem.get_room(roomId).name == 'test'

		# test with bad parametters
		assert self.homeAutomationSystem.add_room(1, 'bathroom') is False
		assert self.homeAutomationSystem.add_room("test", 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.add_room("test", 'bathroom') is False

	def test_add_inhabitant(self):
		"""
			test adding an inhabitant
		"""
		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		inhabitantId = self.homeAutomationSystem.add_inhabitant("test2", "test2", "m", "10/10/2010")
		assert inhabitantId is not False
		assert self.homeAutomationSystem.get_inhabitant(inhabitantId).firstName == "test2"

		# test with bad parametters
		assert self.homeAutomationSystem.add_inhabitant(1, "test2", "m", "10/10/2010") is False
		assert self.homeAutomationSystem.add_inhabitant("test2", 1, "m", "10/10/2010") is False
		assert self.homeAutomationSystem.add_inhabitant("test2", "test2", 1, "10/10/2010") is False
		assert self.homeAutomationSystem.add_inhabitant("test2", "test2", "z", "10/10/2010") is False
		assert self.homeAutomationSystem.add_inhabitant("test2", "test2", "m", 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.add_inhabitant("test2", "test2", "m", "10/10/2010") is False
		
	def test_add_guest(self):
		"""
			test adding guest
		"""
		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		guestId = self.homeAutomationSystem.add_guest("test3", "test3", "m", "10/10/2010")
		assert guestId is not False
		assert self.homeAutomationSystem.get_guest(guestId).firstName == "test3"

		# test with bad parametters
		assert self.homeAutomationSystem.add_guest(1, "test3", "m", "10/10/2010") is False
		assert self.homeAutomationSystem.add_guest("test3", 1, "m", "10/10/2010") is False
		assert self.homeAutomationSystem.add_guest("test3", "test3", 1, "10/10/2010") is False
		assert self.homeAutomationSystem.add_guest("test3", "test3", "z", "10/10/2010") is False
		assert self.homeAutomationSystem.add_guest("test3", "test3", "m", 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.add_guest("test3", "test3", "m", "10/10/2010") is False

	def test_add_profil(self):
		"""
			test adding profil
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		profilId = self.homeAutomationSystem.add_profil("test4", "test4", "m", "10/10/2010")
		assert profilId is not False
		assert self.homeAutomationSystem.get_profil(profilId).firstName == "test4"

		# test with bad parametters
		assert self.homeAutomationSystem.add_profil(1, "test4", "m", "10/10/2010") is False
		assert self.homeAutomationSystem.add_profil("test4", 1, "m", "10/10/2010") is False
		assert self.homeAutomationSystem.add_profil("test4", "test4", 1, "10/10/2010") is False
		assert self.homeAutomationSystem.add_profil("test4", "test4", "z", "10/10/2010") is False
		assert self.homeAutomationSystem.add_profil("test4", "test4", "m", 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.add_profil("test4", "test4", "m", "10/10/2010") is False

	def test_add_module(self):
		"""
			test adding an module
		"""
		# test with zwaveNework corectly configured
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = self.goodZWaveNetwork
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork.controller.zwaveNetwork = self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork
		moduleId = self.homeAutomationSystem.add_module("test", 1)
		assert moduleId is not False
		assert self.homeAutomationSystem.get_module(moduleId).name == "test"

		# test with bad parametters
		assert self.homeAutomationSystem.add_module(1, 1) is False
		assert self.homeAutomationSystem.add_module("test", "1") is False

		# test with zwaveNetwork uncorrectly configured
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = self.badZWaveNetwork
		assert self.homeAutomationSystem.add_module("test", 1) is False

		# test with failure zwaveNetwork
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = False
		assert self.homeAutomationSystem.add_module("test", 1) is False

	def test_add_event(self):
		"""
			test with good parametters: test if the method works correctly
		"""

		"""
					test adding an event
				"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		eventId = self.homeAutomationSystem.add_event("motion detection", "10/10/2010 01:01:01", 1)
		assert eventId is not False
		assert self.homeAutomationSystem.get_event(eventId).type == "motion detection"

		# test with bad parametters
		assert self.homeAutomationSystem.add_event(1, "10/10/2010 01:01:01", 1) is False
		assert self.homeAutomationSystem.add_event("motion detection", 1, 1) is False
		assert self.homeAutomationSystem.add_event("motion detection", "10/10/2010 01:01:01", "1") is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.add_event("motion detection", "10/10/2010 01:01:01", 1) is False


	def test_del_room(self):
		"""
			test deleting an room
		"""
		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		roomId = self.homeAutomationSystem.add_room("testDel", "bathroom")
		assert self.homeAutomationSystem.del_room(roomId) is not False
		assert self.homeAutomationSystem.get_room(roomId) is False

		# test with bad parametters
		assert self.homeAutomationSystem.del_room('1') is False
		assert self.homeAutomationSystem.del_room(10000) is False


		# test with unconnected database
		roomId = self.homeAutomationSystem.add_room("testDel2", "bathroom")
		self.homeAutomationSystem.home.homeDatabase.disconnect()

		assert self.homeAutomationSystem.del_room(roomId) is False

	def test_del_inhabitant(self):
		"""
			test deleting an inhabitant
		"""
		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		inhabitantId = self.homeAutomationSystem.add_inhabitant("testDel", "testDel", "m", "10/10/2010")
		assert self.homeAutomationSystem.del_inhabitant(inhabitantId) is not False
		assert self.homeAutomationSystem.get_inhabitant(inhabitantId) is False

		# test with bad parametters
		assert self.homeAutomationSystem.del_inhabitant('1') is False
		assert self.homeAutomationSystem.del_inhabitant(10000) is False

		# test with unconnected database
		inhabitantId = self.homeAutomationSystem.add_inhabitant("testDel2", "testDel2", "m", "10/10/2010")

		self.homeAutomationSystem.home.homeDatabase.disconnect()

		assert self.homeAutomationSystem.del_inhabitant(inhabitantId) is False

	def test_del_guest(self):
		"""
			test deleting an guest
		"""
		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		guestId = self.homeAutomationSystem.add_guest("testDel", "testDel", "m", "10/10/2010")
		assert self.homeAutomationSystem.del_guest(guestId) is not False
		assert self.homeAutomationSystem.get_guest(guestId) is False

		# test with bad parametters
		assert self.homeAutomationSystem.del_guest('1') is False
		assert self.homeAutomationSystem.del_guest(10000) is False

		# test with unconnected database
		guestId = self.homeAutomationSystem.add_guest("testDel2", "testDel2", "m", "10/10/2010")

		self.homeAutomationSystem.home.homeDatabase.disconnect()

		assert self.homeAutomationSystem.del_guest(guestId) is False
		
	def test_del_profil(self):
		"""
			test deleting an profil
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		profilId = self.homeAutomationSystem.add_profil("testDel3", "testDel3", "m", "10/10/2010")
		assert self.homeAutomationSystem.del_profil(profilId) is not False
		assert self.homeAutomationSystem.get_profil(profilId) is False

		# test with bad parametters
		assert self.homeAutomationSystem.del_profil('1') is False
		assert self.homeAutomationSystem.del_profil(10000) is False

		# test with unconnected database
		profilId = self.homeAutomationSystem.add_profil("testDel3", "testDel3", "m", "10/10/2010")

		self.homeAutomationSystem.home.homeDatabase.disconnect()

		assert self.homeAutomationSystem.del_profil(profilId) is False

	def test_del_event(self):
		"""
			test deleting an event
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		eventId = self.homeAutomationSystem.add_event("motion detection", "10/10/2010", 1)
		assert self.homeAutomationSystem.del_event(eventId) is not False
		assert self.homeAutomationSystem.get_event(eventId) is False

		# test with bad parametters
		assert self.homeAutomationSystem.del_event('1') is False
		assert self.homeAutomationSystem.del_event(10000) is False

		# test with unconnected database
		eventId = self.homeAutomationSystem.add_event("motion detection", "10/10/2010", 1)

		self.homeAutomationSystem.home.homeDatabase.disconnect()

		assert self.homeAutomationSystem.del_event(eventId) is False
		

	def test_set_room_name(self):
		"""
			test setting an roomName
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_room_name(1, "testSetName") is not False
		assert self.homeAutomationSystem.get_room(1).name == "testSetName"

		# test with bad parametters
		assert self.homeAutomationSystem.set_room_name("1", "testSetName") is False
		assert self.homeAutomationSystem.set_room_name(1, 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_room_name(1, "testSetName") is False
		
	def test_set_room_type(self):
		"""
			test setting module location
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_room_type(1, "corridor") is not False
		assert self.homeAutomationSystem.get_room(1).type == "corridor"

		# test with bad parametters
		assert self.homeAutomationSystem.set_room_name("1", "corridor") is False
		assert self.homeAutomationSystem.set_room_name(1, 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_room_name(1, "corridor") is False

	def test_set_profil_last_name(self):
		"""
			test setting the last name of an profil
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_profil_last_name(1, "testSetLN") is not False
		assert self.homeAutomationSystem.get_profil(1).lastName == "testSetLN"

		# test with bad parametters
		assert self.homeAutomationSystem.set_profil_last_name("1", "testSetLN") is False
		assert self.homeAutomationSystem.set_profil_last_name(1, 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_profil_last_name(1, "testSetLN") is False

	def test_set_profil_first_name(self):
		"""
			test setting the first name of an profil
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_profil_first_name(1, "testSetFN") is not False
		assert self.homeAutomationSystem.get_profil(1).firstName == "testSetFN"

		# test with bad parametters
		assert self.homeAutomationSystem.set_profil_first_name("1", "testSetFN") is False
		assert self.homeAutomationSystem.set_profil_first_name(1, 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_profil_first_name(1, "testSetFN") is False

	def test_set_profil_sexe(self):
		"""
			test setting the sexe of an profil
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_profil_sexe(1, "f") is not False
		assert self.homeAutomationSystem.get_profil(1).sexe == "f"

		# test with bad parametters
		assert self.homeAutomationSystem.set_profil_sexe("1", "f") is False
		assert self.homeAutomationSystem.set_profil_sexe(1, 1) is False
		assert self.homeAutomationSystem.set_profil_sexe(1, "z") is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_profil_sexe(1, "f") is False

	def test_set_profil_date_of_birth(self):
		"""
			test setting the date of birth of an profil
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_profil_date_of_birth(1, "02/02/02") is not False
		assert self.homeAutomationSystem.get_profil(1).dateOfBirth == "02/02/02"

		# test with bad parametters
		assert self.homeAutomationSystem.set_profil_date_of_birth("1", "02/02/02") is False
		assert self.homeAutomationSystem.set_profil_date_of_birth(1, 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_profil_date_of_birth(1, "02/02/02") is False

	def test_set_inhabitant_last_name(self):
		"""
			test setting the last name of an inabitant
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_inhabitant_last_name(1, "testSetLN") is not False
		assert self.homeAutomationSystem.get_inhabitant(1).lastName == "testSetLN"

		# test with bad parametters
		assert self.homeAutomationSystem.set_inhabitant_last_name("1", "testSetLN") is False
		assert self.homeAutomationSystem.set_inhabitant_last_name(1, 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_inhabitant_last_name(1, "testSetLN") is False

	def test_set_inhabitant_first_name(self):
		"""
			test if the method works correctly
		"""

		"""
					test setting the first name of an inhabitant
				"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_inhabitant_first_name(1, "testSetFN") is not False
		assert self.homeAutomationSystem.get_inhabitant(1).firstName == "testSetFN"

		# test with bad parametters
		assert self.homeAutomationSystem.set_inhabitant_first_name("1", "testSetFN") is False
		assert self.homeAutomationSystem.set_inhabitant_first_name(1, 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_inhabitant_first_name(1, "testSetFN") is False

	def test_set_inhabitant_sexe(self):
		"""
			test setting the sexe of an inhabitant
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_inhabitant_sexe(1, "f") is not False
		assert self.homeAutomationSystem.get_inhabitant(1).sexe == "f"

		# test with bad parametters
		assert self.homeAutomationSystem.set_inhabitant_sexe("1", "f") is False
		assert self.homeAutomationSystem.set_inhabitant_sexe(1, 1) is False
		assert self.homeAutomationSystem.set_inhabitant_sexe(1, "z") is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_inhabitant_sexe(1, "f") is False

	def test_set_inhabitant_date_of_birth(self):
		"""
			test setting the date of birth of an inhabitant
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_inhabitant_date_of_birth(1, "02/02/02") is not False
		assert self.homeAutomationSystem.get_inhabitant(1).dateOfBirth == "02/02/02"

		# test with bad parametters
		assert self.homeAutomationSystem.set_inhabitant_date_of_birth("1", "02/02/02") is False
		assert self.homeAutomationSystem.set_inhabitant_date_of_birth(1, 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_inhabitant_date_of_birth(1, "02/02/02") is False

	def test_set_guest_last_name(self):
		"""
			test setting the last name of an guest
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_guest_last_name(1, "testSetLN") is not False
		assert self.homeAutomationSystem.get_guest(1).lastName == "testSetLN"

		# test with bad parametters
		assert self.homeAutomationSystem.set_guest_last_name("1", "testSetLN") is False
		assert self.homeAutomationSystem.set_guest_last_name(1, 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_guest_last_name(1, "testSetLN") is False

	def test_set_guest_first_name(self):
		"""
			test setting the first name of an guest
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_guest_first_name(1, "testSetFN") is not False
		assert self.homeAutomationSystem.get_guest(1).firstName == "testSetFN"

		# test with bad parametters
		assert self.homeAutomationSystem.set_guest_first_name("1", "testSetFN") is False
		assert self.homeAutomationSystem.set_guest_first_name(1, 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_guest_first_name(1, "testSetFN") is False

	def test_set_guest_sexe(self):
		"""
			test setting the sexe of an inhabitant
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_guest_sexe(1, "f") is not False
		assert self.homeAutomationSystem.get_guest(1).sexe == "f"

		# test with bad parametters
		assert self.homeAutomationSystem.set_guest_sexe("1", "f") is False
		assert self.homeAutomationSystem.set_guest_sexe(1, 1) is False
		assert self.homeAutomationSystem.set_guest_sexe(1, "z") is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_guest_sexe(1, "f") is False

	def test_set_guest_date_of_birth(self):
		"""
			test setting the date of birth of an guest
		"""

		self.homeAutomationSystem.home.homeDatabase.connect()

		# test with connected database
		# test with good parammeters
		assert self.homeAutomationSystem.set_guest_date_of_birth(1, "02/02/02") is not False
		assert self.homeAutomationSystem.get_guest(1).dateOfBirth == "02/02/02"

		# test with bad parametters
		assert self.homeAutomationSystem.set_guest_date_of_birth("1", "02/02/02") is False
		assert self.homeAutomationSystem.set_guest_date_of_birth(1, 1) is False

		# test with unconnected database
		self.homeAutomationSystem.home.homeDatabase.disconnect()
		assert self.homeAutomationSystem.set_guest_date_of_birth(1, "02/02/02") is False

	def test_set_module_name(self):
		"""
			test setting the name of an module
		"""

		# test with zwaveNework corectly configured
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = self.goodZWaveNetwork
		assert self.homeAutomationSystem.set_module_name(1, 'testSetName') is not False
		assert self.homeAutomationSystem.get_module(1).name == 'testSetName'

		# test with bad parametters
		assert self.homeAutomationSystem.set_module_name("1", 'testSetName') is False
		assert self.homeAutomationSystem.set_module_name(1, 1) is False

		# test with zwaveNetwork uncorrectly configured
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = self.badZWaveNetwork
		assert self.homeAutomationSystem.set_module_name(1, 'testSetName') is False

		# test with failure zwaveNetwork
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = False
		assert self.homeAutomationSystem.set_module_name(1, 'testSetName') is False

	def test_set_module_location(self):
		"""
			test setting the name of an module
		"""

		# test with zwaveNework corectly configured
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = self.goodZWaveNetwork
		assert self.homeAutomationSystem.set_module_location(1, 1) is not False
		assert self.homeAutomationSystem.get_module(1).location == 1

		# test with bad parametters
		assert self.homeAutomationSystem.set_module_location("1", 1) is False
		assert self.homeAutomationSystem.set_module_location(1, "1") is False

		# test with zwaveNetwork uncorrectly configured
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = self.badZWaveNetwork
		assert self.homeAutomationSystem.set_module_location(1, 1) is False

		# test with failure zwaveNetwork
		self.homeAutomationSystem.home.homeAutomationNetwork.zWaveNetwork = False
		assert self.homeAutomationSystem.set_module_location(1, 1) is False
'''
	def test_set_automation_network_controller_path(self):
		assert self.homeAutomationSystem.set_automation_network_controller_path("/test/") is not False
		assert self.homeAutomationSystem.home.homeAutomationNetwork.controllerPath == "/test/"

	def test_set_automation_network_Zwave_config_path(self):
		assert self.homeAutomationSystem.set_automation_network_Zwave_config_path("/test/") is not False
		assert self.homeAutomationSystem.home.homeAutomationNetwork.zwaveConfigPath == "/test/"
'''