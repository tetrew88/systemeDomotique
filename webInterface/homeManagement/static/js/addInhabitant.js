let loadingScreen = document.getElementById("loadingScreen");
let pageContent = document.getElementById("pageContent");

async function add_inhabitant()
{
	let firstNameInput = document.getElementById("firstName");
	let lastNameInput = document.getElementById("lastName");
	let sexeInput = document.getElementById("sexe");
	let dateOfBirthInput = document.getElementById("dateOfBirth");

	let newInhabitantList = [];

	let data = {};
	let succes = false

	data['firstName'] = firstNameInput.value;
	data['lastName'] = lastNameInput.value;
	data['sexe'] = sexeInput.value;
	data['dateOfBirth'] = dateOfBirthInput.value;

	socket.emit('add_inhabitant', data);

	pageContent.style.display = "none";
	loadingScreen.style.display = "block";

	await pause(2500);

	socket.emit('get_inhabitants_list', '');
	socket.on('post_inhabitants_list', inhabitantData=>{
		newInhabitantList = inhabitantData["data"];
	})

	await pause(2500);

	pageContent.style.display = "block";
	loadingScreen.style.display = "none";

	for (const element of newInhabitantList)
	{
		if(element["firstName"] == data['firstName'])
		{
			if(element['lastName'] == data['lastName'])
			{
			    if(element['sexe'] == data['sexe'])
			    {
			        if(element['dateOfBirth'] == data['dateOfBirth'])
			        {
                        succes = true;
                        break;
                    }
                }
			}
			else
			{
				succes = false;
			}
		}
		else
		{
			succes = false
		}
	}


	if(succes == true)
	{
		document.location.href = '/profilListing'
	}
	else
	{
		if(!document.getElementById('notif'))
		{
			let notif = document.createElement('div');
			let message = document.createElement("h2");

			notif.classList.add("row", "text-center");
			notif.id = "notif";
			message.classList.add("alertNotif");

			message.textContent = 'Erreur';

			notif.appendChild(message);

			pageContent.appendChild(notif);
		}
	}


}add