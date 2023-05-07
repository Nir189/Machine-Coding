class ParkingSpot:
	def __init__(self, spot_number, spot_size, is_empty=True):
		self.spot_number = spot_number
		self.spot_size = spot_size
		self.vehicle = None
		self.is_empty = is_empty

