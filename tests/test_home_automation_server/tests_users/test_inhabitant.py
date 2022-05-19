import unittest

from homeAutomationServer.classes.users.inhabitant import *
from homeAutomationServer.classes.users.profil import *

class Test_Inhabitant(unittest.TestCase):
    """
		testing class of an inhabitant

		tests list:
			serialize:
				test if the data was conform
	"""

    def setUp(self):
        self.inhabitant = Inhabitant(1, Profil( 1, "test","test", "m", "01/01/01"))

    def test_serialize(self):
        """
            test if the data was conform
        """

        data = self.inhabitant.serialize()
        assert data is not False
        assert data["id"] == 1
        assert data["profilId"] == 1
        assert data["firstName"] == "test"
        assert data["lastName"] == "test"
        assert data["sexe"] == "m"
        assert data["dateOfBirth"] == "01/01/01"