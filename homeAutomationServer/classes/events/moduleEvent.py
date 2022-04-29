from .event import *

class ModuleEvent(Event):
    """
        class bringing all the information and functionality of an module event
            Parametters:
                module; module responsible for the event
                datetime: datetime of the event
                event type: type of event

            Attributes:
                module: module responsible for the event
            property:
                
            method:
                str

    """

    def __init__(self, moduleNode, Type, dateTime):
        Event.__init__(self, Type, dateTime, moduleNode.location)
        self.moduleNode = moduleNode