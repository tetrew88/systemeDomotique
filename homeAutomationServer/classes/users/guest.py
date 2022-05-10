class Guest:
    '''
        class bringing all the information and functionality of an guest
			
			Parametters:
				id: identifiant of the room
				profil: profil of the guest

            attributes:
            	id: identifiant of the room
				profil: profil of the guest

            property:

            methods:
            	serialize (allows to transform the class in dict for json use)
    '''

    def __init__(self, Id, profil):
        self.id = Id
        self.profil = profil

    @property
    def lastName(self):
        return self.profil.lastName

    @property
    def firstName(self):
        return self.profil.firstName

    @property
    def sexe(self):
        return self.profil.sexe

    @property
    def dateOfBirth(self):
        return self.profil.dateOfBirth

    def serialize(self):
        data = {}

        data = {'id': self.id,
                'profil': self.profil.serialize()
                }

        return data