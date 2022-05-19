class Inhabitant:
    '''
        class bringing all the information and functionality of an inhabitant
			
			Parametters:
				id: identifiant of the room
				profil: profil of the inhabitant

            attributes:
            	id: identifiant of the room
				profil: profil of the inhabitant

            property:
                lastname: lastname of the inhabitant
                firstname: firstname of the inhabitant
                sexe: sexe of the inhabitant
                date of birth: date of birth of the inhabitant

            methods:
            	serialize (allows to transform the class in dict for json use)
    '''

    def __init__(self, Id, profil):
        self.id = Id
        self.profil = profil

    @property
    def profilId(self):
        return self.profil.id

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
                'profilId': self.profilId,
                'firstName': self.firstName,
                'lastName': self.lastName,
                'sexe': self.sexe,
                'dateOfBirth': self.dateOfBirth
                }

        return data