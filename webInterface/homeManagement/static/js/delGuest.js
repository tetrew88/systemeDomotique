let loadingScreen = document.getElementById("loadingScreen");
let pageContent = document.getElementById("pageContent");

socket.emit('get_guests_list', '');
socket.on('post_guests_list', data=>{
  let guestInput = document.getElementById("guest");
  guestInput.innerHTML = "";

  let optionList = [];

  data = data["data"];
  for (const element of data)
  {
    let option = document.createElement('option');

    option.text = element['firstName'] + " " + element['lastName'];
    option.value = element['id'];

    optionList.push(option);
  }

  for (const element of optionList)
  {
    guestInput.appendChild(element);
  }
})


async function del_guest()
{
  let guestInput = document.getElementById("guest");

  let newGuestList = [];

  let data = {};
  let succes = false

  data['guestId'] = guestInput.value;

  socket.emit('del_guest', data);

  pageContent.style.display = "none";
  loadingScreen.style.display = "block";

  await pause(10000);

  socket.emit('get_guests_list', '');
  socket.on('post_guests_list', guestData=>{
    newGuestList = guestData["data"];
  })

  await pause(2500);

  pageContent.style.display = "block";
  loadingScreen.style.display = "none";

  if (newGuestList.lenght > 0)
  {
      for (const element of newGuestList)
      {
        if(element["id"] == data['guestId'])
        {
          succes = false;
          break;
        }
        else
        {
          succes = true;
        }
      }
  }
  else
  {
    succes = true;
  }

  if(succes == true)
  {
    document.location.href = '/profilListing'
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