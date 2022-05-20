let loadingScreen = document.getElementById("loadingScreen");
let pageContent = document.getElementById("pageContent");

socket.emit('get_modules_list', '');
socket.on('post_modules_list', data=>{
	let moduleInput = document.getElementById("module");

	moduleInput.innerHTML = "";

	let optionList = [];

	data = data["data"];
	for (const element of data)
	{
		let option = document.createElement('option');

		option.text = element['name']
		option.value = element['id']

		optionList.push(option);
	}

	for (const element of optionList)
	{
		moduleInput.appendChild(element);
	}
})


async function del_module()
{
	let moduleInput = document.getElementById("module");

	let newModuleList = [];

	let data = {};
	let succes = false

	data['moduleId'] = moduleInput.value;

	socket.emit('del_module', data);

	pageContent.style.display = "none";
	loadingScreen.style.display = "block";

	await pause(10000);

	socket.emit('get_modules_list', '');
	socket.on('post_modules_list', data=>{
		newModuleList = data["data"];
	})

	await pause(2500);

	pageContent.style.display = "block";
	loadingScreen.style.display = "none";

	for (const element of newModuleList)
	{
		if(element["id"] == data['moduleId'])
		{
			succes = false;
			break;
		}
		else
		{
			succes = true;
		}
	}

	if(succes == true)
	{
		document.location.href = '/moduleListing'
	}
	else
	{
		if(!document.getElementById('notif'))
		{
  			// on ajoute la div
			let notif = document.createElement('div');
			let message = document.createElement("h2");

			notif.classList.add("row", "text-center");
			notif.id = "notif"

			message.classList.add("alertNotif");

			message.textContent = 'Erreur';

			notif.appendChild(message);

			pageContent.appendChild(notif);
		}
	}


}