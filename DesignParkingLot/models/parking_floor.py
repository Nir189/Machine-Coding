# Add parking spot method
# I have to import ParkingSpot class here
from DesignParkingLot.models.parking_spot import ParkingSpot
class ParkingFloor:
	def __init__(self , floor_number=None):
		self.floor_number = floor_number
		self.compact_spots = []
		self.large_spots = []
		self.disabled_spots = []

	def setFloorNumber(self , number):
		self.floor_number = number

	def add_spots(self, number_of_spot, spot_size):
		occupied_spot = len(self.compact_spots) + len(self.large_spots) + len(self.disabled_spots)
		if spot_size == 'compact':
			# create compact spot
			for i in range(occupied_spot+1 , occupied_spot+number_of_spot+1):
				self.compact_spots.append(ParkingSpot(i , 'compact'))

		elif spot_size == 'large':
			# create large spot
			for i in range(occupied_spot+1 , occupied_spot+number_of_spot+1):
				self.large_spots.append(ParkingSpot(i , 'large'))

		elif spot_size == 'disabled':
			# create disabled spot
			for i in range(occupied_spot+1 , occupied_spot+number_of_spot+1):
				self.disabled_spots.append(ParkingSpot(i , 'disabled'))








