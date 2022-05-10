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

        pass

    @property
    def temperature(self):
        """
            property representing the temperature of the room

                return: float
        """

        pass

    @property
    def luminosity(self):
        """
            property representing the luminosity of the room

                return: int
        """

        pass


    def serialize(self):
        """
            method called for seriallize data of the class
        """

        pass