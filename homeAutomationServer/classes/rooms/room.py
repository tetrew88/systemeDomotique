class Room:
    """
        class bringing all the information and functionality of an module
			
			Parametters:
				id: identifiant of the room
				name: name of the room
				type: type of room(bedroom, lounge, bathroom)

				automation network

            attributes:
            	id: identifiant of the room
				name: name of the room
				type: type of room(bedroom, lounge, bathroom)

				automation network

            property:
            	content: list of module contained in the room
            	
            	temperature: temperature of the room
            	luminosity: luminosity of the room

            methods:
            	serialize (allows to transform the class in dict for json use)
    """

    def __init__(self, id, name, Type, automationNetwork):
        self.id = int(id)
        self.name = name
        self.type = Type

        self.automationNetwork = automationNetwork


    @property
    def content(self):
        """
            property representing the module list contained in the room

                return: list of module class
        """

        modules = []

        for module in self.automationNetwork.modulesList:
            if module.location != '':
                if int(module.location) == self.id:
                    modules.append(module)
                else:
                    pass
            else:
                pass

        return modules

    @property
    def temperature(self):
        """
            property representing the temperature of the room

                return: float
        """

        temperatureSensor = False

        temperature = 'NULL'

        for module in self.content:
            if isinstance(module, TemperatureSensor):
                temperature = module.temperature
                break
            elif isinstance(module, MultiSensor):
                if 'temperature' in module.sensors.keys():
                    temperatureSensor = module.sensors['temperature']
                    temperature = temperatureSensor.temperature
                    break
            else:
                pass

        return temperature

    @property
    def luminosity(self):
        """
            property representing the luminosity of the room

                return: int
        """

        luminositySensor = False
        luminosity = 'NULL'

        for module in self.content:
            if isinstance(module, LuminositySensor):
                luminosity = module.luminosity
                break
            elif isinstance(module, MultiSensor):
                if 'luminosity' in module.sensors.keys():
                    luminositySensor = module.sensors['luminosity']
                    luminosity = luminositySensor.luminosity
                    break
            else:
                pass

        return luminosity


    def serialize(self):
        """
            method called for seriallize data of the class
        """

        data = {}

        data = {"id": self.id,
                "name": self.name,
                "type": self.type,
                "content": [],
                "temperature": self.temperature,
                "luminosity": self.luminosity,
                "events": []
                }

        content = []
        for element in self.content:
            tmp = element.serialize()
            content.append(tmp)
        data['content'] = content

        return data