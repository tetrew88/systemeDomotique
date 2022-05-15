class FakeNode:
	def __init__(self, id, deviceType, cmdClass):
		self.node_id = id
		self.device_type = deviceType
		self.command_classes_as_string = cmdClass
		self.name = "test"
		self.location = 1
		self.is_awake = True
		self.is_failed = False
		self.is_ready = True
		self.is_sleeping = False
		self.manufacturer_name = "test"
		self.product_name = "test"
		self.product_type = "test"

	def set_field(self, field, fieldData):
		if field == 'name':
			self.name = fieldData
		if field == 'location':
			self.location = fieldData