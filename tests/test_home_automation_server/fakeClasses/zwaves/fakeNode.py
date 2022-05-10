class FakeNode:
	def __init__(self, id, deviceType, cmdClass):
		self.node_id = id
		self.device_type = deviceType
		self.command_classes_as_string = cmdClass
		self.name = ""
		self.location = ""

	def set_field(self, field, fieldData):
		if field == 'name':
			self.name = fieldData
		if field == 'location':
			self.location = fieldData