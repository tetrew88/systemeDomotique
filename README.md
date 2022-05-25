# systemeDomotique
système permettant de gérer son installation z-wave et permettant l'interaction avec les autres systeme hestiaDomotics


Ce système domotique as pour but de simplifier la vie des utilisateurs en leurs permettant de gérer leurs domicile via divers support, ainsi que recevoir des notification d'événement, ... .

quatre grand point sont a l'oeuvre dans ce projet:
  - le système domotique
  - l'interface web
  - la base de donnée du domicile
  - le reseau domotique(zwave)

Installation:(installer a venir)

	- installer les dépendances
	- modifier le chemin du controlleur réseau et du fichier de config dans le dossier config
	- configurer nginx:
		créer un nouveau fichier dans sites-available ;
		(sudo touch sites-available/homeAutomationSystem)

		ajouter un lien symbolique dans sites-enabled grâce à la commande ln
		(sudo ln -s /etc/nginx/sites-available/homeAutomationSystem /etc/nginx/sites-enabled)


		Ouvrez le document etc/nginx/sites-available/homeAutomationSystem via sudo a cause des restriction

		entrer le code suivant:
			server { 
				
			    listen 80; server_name IP_DU_RPI; 
			    root /home/pi/Desktop/hestiaDomotics/systemeDomotique/webInterface/;
				
			    location / {
				proxy_set_header Host $http_host;
				proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
				proxy_redirect off;
				proxy_pass http://127.0.0.1:8000;
			    }
				
			}

		-configurer supervisor/gunicorn:
			Supervisor lance des services et les redémarre ce qui permettra de démarrer l'appli au démarrage du rpi

			créer un fichier de configuration pour supervisor:
			(sudo touch /etc/supervisor/conf.d/homeAutomationSystem.conf)

			ouvrez le doc et entrer la commande suivante:
				[program:homeAutomationSystem]
				command = python3 manage.py runserver
				user = pi
				directory = /home/pi/Desktop/hestiaDomotics/systemeDomotique/webInterface
				autostart = true
				autorestart = true
			
			créer un nouveau fichier de configuration pour supervisor:
			(sudo touch /etc/supervisor/conf.d/automationServer.conf)

			ouvrez le doc et entrer la commande suivante:
				[program:homeAutomationSystem]
				command = python3 main.py
				user = pi
				directory = /home/pi/Desktop/hestiaDomotics/homeAutomationServer
				autostart = true
				autorestart = true

			(bien penser a réveiller vos nos endormis au redémarrage (necessaire au démarrage du système))
			




lien hestiaDomotics: 
  - git: https://github.com/tetrew88/hestiaDomotic
  - fb: a venir
