from .moduleEvent import *


class MotionDetection(ModuleEvent):
    """
        class bringing all the information and functionality of an motion detection
            Parametters:
                module; module responsible for the event
                datetime: datetime of the event
                event type: type of event

            Attributes:

            property:
            method:
                str

    """

    def __init__(self, moduleNode, datetime):
        ModuleEvent.__init__(self, moduleNode, "motion detection", datetime)

    def __str__(self):
        return "[{}]: un mouvement as été détécter".format(self.dateTime)