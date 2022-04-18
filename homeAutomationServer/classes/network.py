class Network:
	"""
		class bringing all the information and functionality of the automation network.

			Parammetters:
				controllerPath: path to the zwave controller (ex: "/dev/ttyACM0")

			Attributes:
				controllerPath: path to the zwave controller (ex: "/dev/ttyACM0")
				configPath: path to zwave config File
				logFile: path to the network log file

			Property:
				homeId: identifiant of the home

				state: state of the network

				is ready: control booleans to know if the network is ready

				modules list: list of module contained in the network

				main controller: main controller of the network
				controllersList: list of controllers of the network

			Methods:
				load: load the network
                start: start the network
                stop: stop the network

                get module: allows to retrieve a specific module on the network

                add module: allows to add an module on the network

                del module:allows to del an module

                set module name: allows to set the name of an module
				set module location: allows to set the location of an module)

				set automation network controller path: allows to set the path of the automation network controller)

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

	def __init__(self, controllerPath):
		pass


	@property
	def homeId(self):
		"""
			property representing the home identifier

				return: int
		"""

		pass

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

		pass

	@property
	def isReady(self):
		"""
			property representing if the network is ready or not

				return: False/True
		"""

		pass

	@property
    def modulesList(self):
    	"""
    		property representing list of modules contained on the network.

				functionning:
					asks the automation network to list the node contained in
						transtype each node to his associated class

    			return:
    				list of modules classes
    	"""

    	pass

   	@property
   	def mainController(self):
   		"""
    		property representing the main controller of the network.

    			return:
    				list of modules classes
    	"""

    	pass

    @property
    def controllerList(self):
    	"""
    		property representing the list of network controller.

    			return:
    				list of modules classes
    	"""
    	
    	pass


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
    					transtype newModule location to str for compatibilities
    					ask to  add the module
    						if succes:
    							return True
    						else:
    							return False

    			return:
    				succes (True/False)
    	"""

    	pass


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

    	pass


    def set_module_name(self, moduleId, newName):
    	"""
    		methods called for set an module's name.

    			Parametters:
    				moduleId: int
    				newName: str

    			functionning:
					-set the name of the module associate to the id
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
					-set the location of the module associate to the id
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
					-set the automation network path
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
    		Method called for save modification effectuate on the network
    	"""

    	pass


    def serialize(self):
    	"""
    		method called for seriallize data of the class
    	"""

    	pass