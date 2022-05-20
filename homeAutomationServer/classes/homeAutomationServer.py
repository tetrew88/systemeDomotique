import eventlet
import socketio

import json

from classes.homeAutomationSystem import *

socketIoServer = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(socketIoServer, object)


class HomeAutomationServer(socketio.Namespace):
    """
        class representing the home automation server:

            attributes:
                home automation système

            property:

            methods:
                start
                stop

                set home automation system

            server event:
                connection
                get
    """

    homeAutomationSystem = False

    def __init__(self):
        socketio.Namespace.__init__(self, '/HomeAutomationServer')

    def start(self):
        """
            method called for start the home automation system and the server
        """
        HomeAutomationServer.homeAutomationSystem.start()
        eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

    def stop(self):
        """
            method called for stop the home automation system and server
        """
        socketIoServer.stop()
        homeAutomationSystem.stop()

    @staticmethod
    def set_home_automation_system(homeAutomationSystem):
        """
            method called for attribute the home automation server to the server
        """
        HomeAutomationServer.homeAutomationSystem = homeAutomationSystem

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def connect(sid, environ, auth):
        print('connect ', sid)

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_rooms_list(sid, data):
        """
            method called when an client claim the rooms list
        """

        rooms = []
        for room in HomeAutomationServer.homeAutomationSystem.get_rooms_list():
            rooms.append(room.serialize())

        socketIoServer.emit('post_rooms_list', {'data': rooms}, namespace='/HomeAutomationServer')

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_inhabitants_list(sid, data):
        """
            method called when an client claim the inhabitant list
        """

        inhabitants = []

        for inhabitant in HomeAutomationServer.homeAutomationSystem.get_inhabitants_list():
            inhabitants.append(inhabitant.serialize())

        socketIoServer.emit('post_inhabitants_list', {"data": inhabitants}, namespace='/HomeAutomationServer')

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_guests_list(sid, data):
        """
            method called when an client claim the guest list
        """

        guests = []

        for guest in HomeAutomationServer.homeAutomationSystem.get_guests_list():
            guests.append(guest.serialize())

        socketIoServer.emit('post_guests_list', {"data": guests}, namespace='/HomeAutomationServer')

    def get_profils_list(sid, data):
        """
            method called when an client claim the profil list
        """
        profils = []

        for profil in HomeAutomationServer.homeAutomationSystem.get_profils_list():
            profils.append(profil.serialize())

        socketIoServer.emit('post_profils_list', {"data": profils}, namespace='/HomeAutomationServer')

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_modules_list(sid, data):
        """
            method called when an client claim the module list
        """

        modules = []

        for element in HomeAutomationServer.homeAutomationSystem.get_modules_list():
            modules.append(element.serialize())

        socketIoServer.emit('post_modules_list', {"data": modules}, namespace='/HomeAutomationServer')

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_events_list(sid, data):
        """
            method called when an client claim the event list
        """

        eventList = []

        for element in HomeAutomationServer.homeAutomationSystem.get_events_list():
            eventList.append(element.serialize())

        socketIoServer.emit('post_events_list', {"data": eventList}, namespace='/HomeAutomationServer')


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_room(sid, data):
        """
            method called when an client claim an specific room
        """

        room = HomeAutomationServer.homeAutomationSystem.get_room(data)
        room = room.serialize()

        socketIoServer.emit('post_room', {"data": room}, namespace='/HomeAutomationServer')

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_room_content(sid, data):
        """
            method called when an client claim the content of an room
        """

        tmpContent = False
        content = []

        room = HomeAutomationServer.homeAutomationSystem.get_room(data)

        tmpContent = HomeAutomationServer.homeAutomationSystem.get_room_content(data)
        for element in tmpContent:
            content.append(element.serialize())

        socketIoServer.emit('post_room_content', {"data": content, "roomId": room.id},
                            namespace='/HomeAutomationServer')

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_room_events(sid, data):
        """
            method called when an client claim the events associated to an room
        """

        room = False
        events = []

        room = HomeAutomationServer.homeAutomationSystem.get_room(data)

        eventList = HomeAutomationServer.homeAutomationSystem.get_room_event(data)
        for event in eventList:
            events.append(event.serialize())

        socketIoServer.emit('post_room_events', {"data": events, "roomId": room.id}, namespace='/HomeAutomationServer')

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_module(sid, data):
        """
            method called when an client claim an specific module
        """

        module = HomeAutomationServer.homeAutomationSystem.get_module(data)
        module = module.serialize()

        socketIoServer.emit('post_module', {"data": module}, namespace='/HomeAutomationServer')

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_profil(sid, data):
        profil = HomeAutomationServer.homeAutomationSystem.get_profil(data).serialize()

        socketIoServer.emit('post_profil', {"data": profil}, namespace='/HomeAutomationServer')

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_homeId(sid, data):
        homeId = HomeAutomationServer.homeAutomationSystem.get_homeId()

        socketIoServer.emit('post_homeId', {"data": homeId}, namespace='/HomeAutomationServer')

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def get_network_state(sid, data):
        networkState = HomeAutomationServer.homeAutomationSystem.get_network_state()

        socketIoServer.emit('post_network_state', {"data": networkState}, namespace='/HomeAutomationServer')

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def switch_light(sid, data):
        HomeAutomationServer.homeAutomationSystem.switch_light(data)

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_rbgBulb_color(sid, data):
        HomeAutomationServer.homeAutomationSystem.set_rbgBulb_color(data['moduleId'], data["colorName"])

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_bulb_intensity(sid, data):
        HomeAutomationServer.homeAutomationSystem.set_bulb_intensity(data['moduleId'], int(data['intensity']))


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_module_name(sid, data):
        HomeAutomationServer.homeAutomationSystem.set_module_name(data['moduleId'], data['name'])

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_module_location(sid, data):
        HomeAutomationServer.homeAutomationSystem.set_module_location(data['moduleId'], data['location'])
        ########
    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_profil_last_name(sid, data):
        HomeAutomationServer.homeAutomationSystem.set_profil_last_name(data['profilId'], data["lastName"])

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_profil_first_name(sid, data):
        HomeAutomationServer.homeAutomationSystem.set_profil_first_name(data['profilId'], data["firstName"])

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_profil_sexe(sid, data):
        HomeAutomationServer.homeAutomationSystem.set_profil_sexe(data['profilId'], data["sexe"])

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def set_profil_date_of_birth(sid, data):
        HomeAutomationServer.homeAutomationSystem.set_profil_date_of_birth(data['profilId'], data['dateOfBirth'])

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def add_module(sid, data):
        HomeAutomationServer.homeAutomationSystem.add_module(data["moduleName"], int(data["roomId"]))

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def add_room(sid, data):
        HomeAutomationServer.homeAutomationSystem.add_room(data["roomName"], data["roomType"])

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def add_inhabitant(sid, data):
        HomeAutomationServer.homeAutomationSystem.add_inhabitant(data["firstName"], data["lastName"], data["sexe"], data["dateOfBirth"])

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def add_guest(sid, data):
        HomeAutomationServer.homeAutomationSystem.add_guest(data["firstName"], data["lastName"], data["sexe"], data["dateOfBirth"])


    @socketIoServer.event(namespace='/HomeAutomationServer')
    def del_module(sid, data):
        HomeAutomationServer.homeAutomationSystem.del_module()

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def del_room(sid, data):
        HomeAutomationServer.homeAutomationSystem.del_room(int(data['roomId']))

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def del_inhabitant(sid, data):
        HomeAutomationServer.homeAutomationSystem.del_inhabitant(int(data['inhabitantId']))

    @socketIoServer.event(namespace='/HomeAutomationServer')
    def del_guest(sid, data):
        HomeAutomationServer.homeAutomationSystem.del_guest(int(data['guestId']))


socketIoServer.register_namespace(HomeAutomationServer())