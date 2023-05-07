# Add parking floor method
# Id
# Name
# Address

class ParkingLot:
	__instance__ = None

	def __init__(self):
		self.id = None
		self.name = None
		self.address = None
		self.floors = []
		self.parking_rate = None

		if ParkingLot.__instance__ is None:
			ParkingLot.__instance__ = self
		else:
			raise Exception("Multiple Instance can not be created.")


	@staticmethod
	def get_instance():
		if not ParkingLot.__instance__:
			ParkingLot()
		return ParkingLot.__instance__

	def setId(self,id):
		self.id = id

	def getId(self):
		return self.id

	def setName(self,name):
		self.name = name

	def getName(self):
		return self.name

	def setAddress(self,address):
		self.address = address

	def getAddress(self):
		return self.address

	def setParkingRate(self, parking_rate):
		self.parking_rate = parking_rate

	def getParkingRate(self):
		return self.parking_rate

	def add_floors(self , floor):
		self.floors.append(floor)

	def park_vehicle(self, vehicle):
		for floor in self.floors:
			if vehicle.size == "compact":
				for spot in floor.compact_spots:
					if spot.is_empty:
						spot.is_empty = False
						spot.vehicle = vehicle
						return (floor.floor_number,spot.spot_number)
			elif vehicle.size == 'large':
				for spot in floor.large_spots:
					if spot.is_empty:
						spot.is_empty = False
						spot.vehicle = vehicle
						return (floor.floor_number,spot.spot_number)
			elif vehicle.size == 'disabled':
				for spot in floor.disabled_spots:
					if spot.is_empty:
						spot.is_empty = False
						spot.vehicle = vehicle
						return (floor.floor_number,spot.spot_number)
		return None

	def remove_vehicle(self, vehicle):
		for floor in self.floors:
			if vehicle.size == "compact":
				for spot in floor.compact_spots:
					if (not spot.is_empty) and spot.vehicle.license_plate == vehicle.license_plate:
						spot.is_empty = True
						spot.vehicle = None
						return True
			elif vehicle.size == 'large':
				for spot in floor.large_spots:
					if (not spot.is_empty) and spot.vehicle.license_plate == vehicle.license_plate:
						spot.is_empty = True
						spot.vehicle = None
						return True
			elif vehicle.size == 'disabled':
				for spot in floor.disabled_spots:
					if (not spot.is_empty) and spot.vehicle.license_plate == vehicle.license_plate:
						spot.is_empty = True
						spot.vehicle = None
						return True
		return None

	def calculate_parking_fee(self, checkin_time, checkout_time, vehicle_size):

		hourly_rate = self.parking_rate.get_hourly_rate(vehicle_size)
		daily_rate = self.parking_rate.get_daily_rate(vehicle_size)

		total_time = checkout_time - checkin_time

		# import pdb
		# pdb.set_trace()

		total_hours = total_time.seconds / 3600
		total_days = total_time.days

		if total_days > 0:
			return (total_days*daily_rate) + (total_hours*hourly_rate)

		if total_hours > 0:
			return (total_hours*hourly_rate)


































# class Vehicle:
#     def __init__(self, license_plate, size):
#         self.license_plate = license_plate
#         self.size = size

# class ParkingSpot:
#     def __init__(self, spot_number, spot_size, is_empty=True):
#         self.spot_number = spot_number
#         self.spot_size = spot_size
#         self.is_empty = is_empty
#         self.vehicle = None

# class ParkingFloor:
#     def __init__(self, floor_number, spots_per_size):
#         self.floor_number = floor_number
#         self.spots_per_size = spots_per_size
#         self.compact_spots = [ParkingSpot(i, 'compact') for i in range(1, spots_per_size+1)]
#         self.large_spots = [ParkingSpot(i, 'large') for i in range(spots_per_size+1, spots_per_size*2+1)]
#         self.disabled_spots = [ParkingSpot(i, 'disabled') for i in range(spots_per_size*2+1, spots_per_size*3+1)]

# class ParkingLot:
#     def __init__(self, num_floors, spots_per_size):
#         self.num_floors = num_floors
#         self.spots_per_size = spots_per_size
#         self.floors = [ParkingFloor(i+1, spots_per_size) for i in range(num_floors)]

#     def park_vehicle(self, vehicle):
#         for floor in self.floors:
#             if vehicle.size == 'compact':
#                 for spot in floor.compact_spots:
#                     if spot.is_empty:
#                         spot.is_empty = False
#                         spot.vehicle = vehicle
#                         return (floor.floor_number, spot.spot_number)
#             elif vehicle.size == 'large':
#                 for spot in floor.large_spots:
#                     if spot.is_empty:
#                         spot.is_empty = False
#                         spot.vehicle = vehicle
#                         return (floor.floor_number, spot.spot_number)
#             elif vehicle.size == 'disabled':
#                 for spot in floor.disabled_spots:
#                     if spot.is_empty:
#                         spot.is_empty = False
#                         spot.vehicle = vehicle
#                         return (floor.floor_number, spot.spot_number)
#         return None

#     def remove_vehicle(self, floor_number, spot_number):
#         floor = self.floors[floor_number-1]
#         spot = None
#         if spot_number <= self.spots_per_size:
#             spot = floor.compact_spots[spot_number-1]
#         elif spot_number <= self.spots_per_size*2:
#             spot = floor.large_spots[spot_number-self.spots_per_size-1]
#         elif spot_number <= self.spots_per_size*3:
#             spot = floor.disabled_spots[spot_number-self.spots_per_size*2-1]
#         if spot:
#             spot.is_empty = True
#             spot.vehicle = None

# # Example Usage:
# parking_lot = ParkingLot(num_floors=3, spots_per_size=20)
# vehicle1 = Vehicle(license_plate='ABC123', size='compact')
# vehicle2 = Vehicle(license_plate='DEF456', size='large')
# vehicle3 = Vehicle(license_plate='GHI789', size='disabled')
# spot1 = parking_lot.park_vehicle(vehicle1)
# spot2 = parking_lot.park_vehicle(vehicle2)
# spot3 = parking_lot.park_vehicle(vehicle3)
# print(spot1, spot2, spot3)
# parking_lot.remove_vehicle(spot1[0], spot1[1])