let profilId = document.getElementById("profilId").value;

socket.emit('get_profil', profilId)
socket.on('post_profil', data=>{
	lastNameInput = document.getElementById('lastNameInput');
	firstNameInput = document.getElementById('firstNameInput');
	let sexeInput = document.getElementById("sexe");
	let dateOfBirthInput = document.getElementById("dateOfBirth");

	data = data["data"];

	firstNameInput.value = data["firstName"];
	lastNameInput.value = data["lastName"];
	if(data['sexe'] == 'f')
	{
	    sexeInput.value = 'f';
	    sexeInput.inneHTML = "Femme";
	}
	else
	{
	    sexeInput.value = 'm';
	    sexeInput.inneHTML = "Homme";
	}
	dateOfBirthInput.value = data["dateOfBirth"]
})

function set_profil_lastName()
{
	let profilId = document.getElementById("profilId").value;
	let lastName = document.getElementById('lastNameInput').value;


	socket.emit('set_profil_last_name', {"profilId": profilId, "lastName": lastName});
}


function set_profil_firstName()
{
	let profilId = document.getElementById("profilId").value;
	firstName = document.getElementById('firstNameInput').value;

	socket.emit('set_profil_first_name', {"profilId": profilId, "firstName": firstName});
}

function set_profil_sexe()
{
	let profilId = document.getElementById("profilId").value;
	let sexe = document.getElementById('sexe').value;


	socket.emit('set_profil_sexe', {"profilId": profilId, "sexe": sexe});
}

function set_profil_date_of_birth()
{
	let profilId = document.getElementById("profilId").value;
	let dateOfBirth = document.getElementById('dateOfBirth').value;


	socket.emit('set_profil_date_of_birth', {"profilId": profilId, "dateOfBirth": dateOfBirth});
}