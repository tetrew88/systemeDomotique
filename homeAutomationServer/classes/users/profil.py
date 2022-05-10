class Profil:
    """
        class representing an profil

            Attributes:
                id
                first name
                lastname
                sexe
                date of birth

            Property:

            method:
    """

    def __init__(self, Id, firstName, lastName, sexe, dateOfBirth):
        self.id = Id
        self.firstName = firstName
        self.lastName = lastName
        self.sexe = sexe
        self.dateOfBirth = dateOfBirth

    def serialize(self):
        data = {}

        data = {"id": self.id,
        'firstName': self.firstName,
        'lastName': self.lastName
        }

        return data