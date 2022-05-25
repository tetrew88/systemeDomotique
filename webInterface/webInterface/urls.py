from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from homeManagement.views.roomListing import room_listing
from homeManagement.views.room import room

from homeManagement.views.profilListing import profil_listing
from homeManagement.views.profil import profil

from automationNetworkManagement.views.moduleListing import module_listing

from homeManagement.views.homeManagement import home_management
from homeManagement.views.addRoom import add_room
from homeManagement.views.addInhabitant import add_inhabitant
from homeManagement.views.addGuest import add_guest
from homeManagement.views.delRoom import del_room
from homeManagement.views.delInhabitant import del_inhabitant
from homeManagement.views.delGuest import del_guest

from automationNetworkManagement.views.automationNetworkManagement import automation_network_management
from automationNetworkManagement.views.addModule import add_module
from automationNetworkManagement.views.delModule import del_module

from automationNetworkManagement.views.module import module

urlpatterns = [
    url(r'^$', room_listing),
    path('admin/', admin.site.urls),
    path('/index', room_listing),
    path('roomListing/', room_listing),
    path('profilListing/', profil_listing),
    path('moduleListing/', module_listing),
    path('homeManagement/', home_management),
    path('automationNetworkManagement/', automation_network_management),
    path('room/<int:roomId>/', room),
    path('module/<int:moduleId>/', module),
    path('inhabitant/<int:profilId>/', profil),
    path('guest/<int:profilId>/', profil),
    path('addModule/', add_module),
    path("addRoom/", add_room),
    path("addInhabitant/", add_inhabitant),
    path("addGuest/", add_guest),
    path("delModule/", del_module),
    path("delRoom/", del_room),
    path('delInhabitant/', del_inhabitant),
    path('delGuest/', del_guest),
]
