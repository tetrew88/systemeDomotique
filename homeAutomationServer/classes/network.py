import openzwave
from openzwave.node import ZWaveNode
from openzwave.value import ZWaveValue
from openzwave.controller import ZWaveController
from openzwave.network import ZWaveNetwork
from openzwave.option import ZWaveOption

from pydispatch import dispatcher

import json
import os
import sys

import time
import datetime

from .modules import *
from.modules.networkController import *

from .modules.controller import *

from .modules.bulb import *
from .modules.rgbBulb import *

from .modules.sensors.sensor import *
from .modules.sensors.multiSensor import *

from .modules.sensors.motionSensor import *
from .modules.sensors.luminositySensor import *
from .modules.sensors.SeismicIntensitySensor import *
from .modules.sensors.temperatureSensor import *
from .modules.sensors.door_windowSensor import *

from .events.moduleEvent import *
from .events.motionDetection import *
from .events.door_windowEvent import *
from .events.lightEvent import *

from .homeDatabase import *


class Network:
	"""
		class bringing all the information and functionality of the automation network.

			Attributes:
				logFile: path to the network log file

			Property:
				homeId: identifiant of the home

				state: state of the network

				is ready: control booleans to know if the network is ready

				modules list: list of module contained in the network

				main controller: main controller of the network

				controllerPath: path to the zwave controller (ex: "/dev/ttyACM0")
				configPath: path to zwave config File

			Methods:
				load: load the network
				start: start the network
				stop: stop the network

				get module: allows to retrieve a specific module on the network

				add module: allows to add an module on the network

				del module:allows to del an module

				set automation network controller path: allows to set the path of the automation network controller)
				set zwave config directory path: allows to set the path of the zwave directory config

				set module name: allows to set the name of an module
				set module location: allows to set the location of an module

				heal network: allows to heal the automation network(zwave network)
				destroy network: allows to destroy the automation network
				save network: allows to save modification on the automation network

				serialize: allows to transform the class in dict for json use

			network interaction:
				network started
				network ready
				network awake
				module added
				value changed
	"""

	def __init__(self):
		self.logPath = "log.log"

		self.zWaveNetwork = False
		self.eventList = []

	@property
	def homeId(self):
		"""
			property representing the home identifier

				return: int
		"""

		if self.zWaveNetwork is not False:
			return int(self.zWaveNetwork.home_id)
		else:
			return False

	@property
	def state(self):
		"""
			property representing the state of the network

				return: int

				STATE_STOPPED = 0, 
				STATE_FAILED = 1, 
				STATE_RESETTED = 3, 
				STATE_STARTED = 5, 
				STATE_AWAKED = 7, 
				STATE_READY = 10
		"""

		if self.zWaveNetwork is not False:
			return int(self.zWaveNetwork.state)
		else:
			return False

	@property
	def isReady(self):
		"""
			property representing if the network is ready or not

				return: False/True
		"""

		if self.zWaveNetwork is not False:
			return self.zWaveNetwork.is_ready
		else:
			return False

	@property
	def modulesList(self):
		"""
			property representing list of modules contained on the network.

				functionning:
					asks the automation network to list the node contained in
						transtype each node to his associated class

				return:
					list of modules classe
		"""

		modules = []

		if self.state is not False and self.isReady:
			#add the main network controller to the list
			modules.append(NetworkController(self.mainController.node))

			#attributes each node at his personnal class thanks his device type
			for node in self.zWaveNetwork.nodes.values():
				#bulb section
				if 'bulb' in node.device_type.lower() or 'light' in node.device_type.lower():
					if "COMMAND_CLASS_COLOR" in node.command_classes_as_string:
						modules.append(RgbBulb(node))
					else:
						modules.append(Bulb(node))
				#sensor section
				elif 'sensor' in node.device_type.lower():
					if 'COMMAND_CLASS_SENSOR_MULTILEVEL' in node.command_classes_as_string:
						sensors = {}

						for element in node.get_sensors():
							if node.get_sensors()[
								element].label == 'Sensor' and 'motion sensor' in node.product_name.lower():
								sensors['motion sensor'] = MotionSensor(node)
							if node.get_sensors()[
								element].label == 'Sensor' and 'door' in node.product_name.lower() or 'window' in node.product_name.lower():
								sensors['door/window sensor'] = Door_WindowSensor(node)
							if node.get_sensors()[element].label == 'Temperature':
								sensors['temperature'] = TemperatureSensor(node)
							if node.get_sensors()[element].label == 'Luminance':
								sensors['luminosity'] = LuminositySensor(node)
							if node.get_sensors()[element].label == 'Seismic Intensity':
								sensors['seismic intensity'] = SeismicIntensitySensor(node)

						modules.append(MultiSensor(node, sensors))
					else:
						for element in node.get_sensors():
							if node.get_sensors()[
								element].label == 'Sensor' and 'motion sensor' in node.product_name.lower():
								modules.append(MotionSensor(node))
							elif node.get_sensors()[
								element].label == 'Sensor' and 'door' in node.product_name.lower() or 'window' in node.product_name.lower():
								modules.append(Door_WindowSensor(node))
							elif node.get_sensors()[element].label == 'Temperature':
								modules.append(TemperatureSensor(node))
							elif node.get_sensors()[element].label == 'Luminance':
								modules.append(LuminositySensor(node))
							elif node.get_sensors()[element].label == 'Seismic Intensity':
								modules.append(SeismicIntensitySensor(node))

				#controller section
				elif 'controller' in node.device_type.lower():
					modules.append(Controller(node))

				else:
					if node.node_id != self.mainController.node.node_id:
						modules.append(Module(node))
		else:
			return []

		return modules

		pass

	@property
	def mainController(self):
		"""
			property representing the main controller of the network.

				return:
					list of modules classes
		"""

		if self.zWaveNetwork is not False:
			return self.zWaveNetwork.controller
		else:
			return False

	@property
	def controllerPath(self):
		"""
			used for get the zwave controller path in the config file

				return:
					path of the controller
		"""

		configDirectoryPath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/config'

		try:
			with open(configDirectoryPath + "/networkConfiguration.json") as networkConfigurationFile:
				data = json.load(networkConfigurationFile)
				return data["controllerPath"]
		except:
			return False
	@property
	def zwaveConfigPath(self):
		configDirectoryPath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/config'

		try:
			with open(configDirectoryPath + "/networkConfiguration.json") as networkConfigurationFile:
				data = json.load(networkConfigurationFile)
				return data["zwaveConfigPath"]
		except:
			return False

	def load(self):
		dispatcher.connect(self.network_started, ZWaveNetwork.SIGNAL_NETWORK_STARTED)
		dispatcher.connect(self.network_ready, ZWaveNetwork.SIGNAL_NETWORK_READY)
		dispatcher.connect(self.network_awake, ZWaveNetwork.SIGNAL_NETWORK_AWAKED)
		dispatcher.connect(self.node_event, ZWaveNetwork.SIGNAL_NODE_EVENT)
		dispatcher.connect(self.scene_event, ZWaveNetwork.SIGNAL_SCENE_EVENT)
		dispatcher.connect(self.value_changed, ZWaveNetwork.SIGNAL_VALUE_CHANGED)
		dispatcher.connect(self.node_added, ZWaveNetwork.SIGNAL_NODE_ADDED)

	def start(self):
		"""
			method used for start the zwave network
		"""

		succes = False

		if self.controllerPath is not False and self.zwaveConfigPath is not False:
			device = self.controllerPath
			log = "Debug"

			# configuration og the logs
			options = ZWaveOption(device, self.zwaveConfigPath, user_path=".", cmd_line="")
			options.set_log_file(self.logPath)
			options.set_append_log_file(True)
			options.set_console_output(False)
			options.set_save_log_level(log)
			options.set_logging(True)
			options.lock()

			# Construction of the zwave network
			self.zWaveNetwork = ZWaveNetwork(options, autostart=False)

			if self.zWaveNetwork is not False:
				self.zWaveNetwork.start()

				print("Etablissement du serveur ZWave: ")

				if not self.isReady:
					for i in range(0, 300 * len(self.modulesList)):
						while not self.zWaveNetwork.state >= self.zWaveNetwork.STATE_AWAKED:
							if self.state >= self.zWaveNetwork.STATE_READY:
								print("Le serveur ZWave est prêt")

								succes = True
								break
							else:
								sys.stdout.write(".")
								sys.stdout.flush()
								time.sleep(1.0)
								succes = False
				else:
					succes = True
			else:
				succes = False
		else:
			succes = False

		# succes return
		return succes

	def stop(self):
		self.network.stop()

	def get_module(self, moduleId):
		"""
			method called for get an specific module on the network

				Parametters:
					moduleId: int

				functionning:
					- search for the module linked to the id
						if the module was found:
							return the module class
						else:
							return False

				return:
					module class/False
		"""

		selectedModule = False

		if isinstance(moduleId, int):
			for module in self.modulesList:
				if module.id == moduleId:
					selectedModule = module
					break
				else:
					selectedModule = False
		else:
			selectedModule = False

		return selectedModule


	def add_module(self, newModuleName, newModuleLocation):
		"""
			method called for adding an module on the network.

				Parametters:
					newModuleName: str
					newModuleLocation: int

				functionning::
					-list module already on the network
					ask to  add the module
					-check if a new module was added
						if succes:
							set the information
						else:
							return False

				return:
					succes (True/False)
		"""

		succes = False
		moduleIdList = []
		newModule = False

		if self.isReady:
			if isinstance(newModuleName, str) and isinstance(newModuleLocation, int):
				for module in self.modulesList:
					moduleIdList.append(module.id)

				self.mainController.add_node()

				print("Mettez le module en état d'inclusion")
				time.sleep(10)

				for module in self.modulesList:
					if module.id in moduleIdList:
						newModule = False
					else:
						newModule = module

				if newModule is not False:
					if newModule.set_name(newModuleName):
						succes = True
					else:
						succes = False

					if succes and newModule.set_location(newModuleLocation):
						succes = True
					else:
						succes = False

					self.save_modification()
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		if succes is not False:
			return newModule.id
		else:
			return False


	def del_module(self, moduleId):
		"""
			method called for del an specific module

				Parametters:
					moduleId: int

				functionning:
					-del the module associate to the id
						if the module was correctly deleted:
							return True
						else:
							return False

				return:
					succes: True/False
		"""
		succes = False

		beforeModuleIdList = afterModuleIdList = []

		if isinstance(moduleId, int):
			for module in self.modulesList:
				beforeModuleIdList.append(module.id)

			if moduleId in beforeModuleIdList:
				self.mainController.remove_node()
				print("Mettez le module en état d'exclusion")
				time.sleep(10)

				for module in self.modulesList:
					afterModuleIdList.append(module.id)

				if moduleId in afterModuleIdList:
					succes = False
				else:
					succes = True
			else:
				succes = False
		else:
			succes = False

		return succes


	def set_automation_network_controller_path(self, newPath):
		"""
			set the path of the automation network controller

				Parametters:
					newPath: str

				functionning:
					-modify the path in the network config file
						if the path was correctly modified:
							return True
						else:
							return False

				return:
					succes: True/False
		"""
		succes = False


		if isinstance(newPath, str):
			configDirectoryPath = os.path.dirname(
				os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/config'

			try:
				with open(configDirectoryPath + "/networkConfiguration.json") as networkConfigurationFile:
					data = json.load(networkConfigurationFile)
					data["controllerPath"] = newPath

				with open(configDirectoryPath + "/networkConfiguration.json", 'w') as networkConfigurationFile:
					json.dump(data, networkConfigurationFile)

				if self.controllerPath == newPath:
					succes = True
				else:
					succes = False
			except:
				succes = False
		else:
			succes = False

		return succes

	def set_Zwave_config_path(self, newPath):
		"""
			set the path of the automation network controller

				Parametters:
					newPath: str

				functionning:
					-set the automation network path in the config file
						if the path was correctly modified:
							return True
						else:
							return False

				return:
					succes: True/False
		"""

		succes = False

		if isinstance(newPath, str):
			configDirectoryPath = os.path.dirname(
				os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/config'

			try:
				with open(configDirectoryPath + "/networkConfiguration.json") as networkConfigurationFile:
					data = json.load(networkConfigurationFile)
					data["zwaveConfigPath"] = newPath

				with open(configDirectoryPath + "/networkConfiguration.json", 'w') as networkConfigurationFile:
					json.dump(data, networkConfigurationFile)

				if self.zwaveConfigPath == newPath:
					succes = True
				else:
					succes = False
			except:
				succes = False
		else:
			succes = False

		return succes

	def add_event(self, event):
		""" methode used for add an event in the home database"""

		homeDatabase = HomeDatabase()

		succes = False

		if isinstance(event, Event):
			if homeDatabase.connect():
				if homeDatabase.add_event(event.type, event.dateTime, int(event.location)):
					succes = True
				else:
					succes = False
			else:
				succes = False
		else:
			succes = False

		return succes

	def set_module_name(self, moduleId, newName):
		"""
	    	methods called for set an module's name.

	    		Parametters:
	    			moduleId: int
	    			newName: str

	    		functionning:
					-ask to the module to change is name
						if the module's name was correctly modified:
							return True
						else:
							return False

	    		return:
	    			succes: True/False
	    """

		selectedModule = False
		succes = False

		if self.isReady:
			for module in self.modulesList:
				if module.id == moduleId:
					selectedModule = module
					break
				else:
					selectedModule = False
		else:
			return False

		if selectedModule is not False:
			return selectedModule.set_name(newName)
		else:
			return False

	def set_module_location(self, moduleId, newLocation):
		"""
            methods called for set an module's location.

                Parametters:
                    moduleId: int
                    newLocation: int(roomId)

                functionning:
                    -ask to the module to change is location
                        if the module's location was correctly modified:
                            return True
                        else:
                            return False

                return:
                    succes: True/False
        """

		selectedModule = False
		succes = False

		if self.isReady:
			for module in self.modulesList:
				if module.id == moduleId:
					selectedModule = module
					break
				else:
					selectedModule = False
		else:
			return False

		if selectedModule is not False:
			return selectedModule.set_location(newLocation)
		else:
			return False


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

	def save_modification(self):
		self.zWaveNetwork.write_config()


	#network interaction
	def network_started(self, network):
		print("Hello from network : I'm started : homeid {:08x} – {} nodes were found.".format(network.home_id,
																							   network.nodes_count))

	def network_ready(self, network):
		print("Hello from network : I'm ready : {} nodes were found.".format(network.nodes_count))
		print("Hello from network : my controller is : {}".format(network.controller))

	def network_awake(self, network):
		print("Hello from network : I'm awake")

	def value_changed(self, node, value):
		module = event = False
		datetimeEvent = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

		print("####value changed######")
		print('{}: [{}: {}]'.format(node.name, value.label, value.data))

		if self.isReady:
			for element in self.modulesList:
				if element.id == node.node_id:
					module = element

			if isinstance(module, Sensor):
				if value.label == 'Access Control' and isinstance(module, Door_WindowSensor):
					if value.data == 22:
						event = Door_WindowOpening(node, datetimeEvent)
					elif value.data == 23:
						event = Door_WindowClosing(node, datetimeEvent)

				elif value.label == 'Access Control' and isinstance(module, MultiSensor):
					if 'door/window sensor' in module.sensorsList:
						if value.data == 22:
							event = Door_WindowOpening(node, datetimeEvent)
						elif value.data == 23:
							event = Door_WindowClosing(node, datetimeEvent)


				elif value.label == 'Sensor' and isinstance(module, MotionSensor):
					if value.data == True:
						event = MotionDetection(node, datetimeEvent)
				elif value.label == 'Sensor' and isinstance(module, MultiSensor):
					if 'motion sensor' in module.sensorsList:
						if value.data == True:
							event = MotionDetection(node, datetimeEvent)

			if isinstance(module, Bulb):
				if value.label == 'Level':
					if value.data > 0:
						event = LightOn(node, datetimeEvent)
					else:
						event = LightOff(node, datetimeEvent)

				elif isinstance(module, RgbBulb):
					if value.label == 'Color':
						pass

		if event != False:
			self.add_event(event)
		else:
			pass