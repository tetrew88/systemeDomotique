#!/usr/bin/python3

from classes.homeAutomationServer import *
from classes.homeAutomationSystem import *

def main():
	homeAutomationSystem = HomeAutomationSystem()

	homeAutomationServer = HomeAutomationServer()
	homeAutomationServer.set_home_automation_system(homeAutomationSystem)

	homeAutomationServer.start()