class ParkingRate:

	def __init__(self):
		
		self.compact_hourly_rate = None
		self.compact_daily_rate = None
		self.large_hourly_rate = None
		self.large_daily_rate = None
		self.disabled_hourly_rate = None
		self.disabled_daily_rate = None


	def get_hourly_rate(self, vehicle_size):
		
		if vehicle_size == 'compact':
			return self.compact_hourly_rate
		elif vehicle_size == 'large':
			return self.large_hourly_rate
		elif vehicle_size == 'disabled':
			return self.disabled_hourly_rate

	def get_daily_rate(self, vehicle_size):

		if vehicle_size == 'compact':
			return self.compact_daily_rate
		elif vehicle_size == 'large':
			return self.large_daily_rate
		elif vehicle_size == 'disabled':
			return self.disabled_daily_rate 

	


class ParkingRateBuilder:
	''' I added builder pattern because May be we will have different charging parameter in future'''

	def __init__(self , parking_rate = ParkingRate()):

		self.parking_rate = parking_rate

	def set_compact_hourly_rate(self, rate):

		self.parking_rate.compact_hourly_rate = rate
		return self

	def set_compact_daily_rate(self, rate):

		self.parking_rate.compact_daily_rate = rate
		return self

	def set_large_hourly_rate(self, rate):

		self.parking_rate.large_hourly_rate = rate
		return self

	def set_large_daily_rate(self, rate):

		self.parking_rate.large_daily_rate = rate
		return self

	def set_disabled_hourly_rate(self, rate):

		self.parking_rate.disabled_hourly_rate = rate
		return self

	def set_disabled_daily_rate(self, rate):

		self.parking_rate.disabled_daily_rate = rate
		return self

	def build(self):

		return self.parking_rate


# builder = ParkingRateBuilder()
# parking_rate = builder.set_compact_hourly_rate(2)\
#                     .set_compact_daily_rate(20)\
#                     .set_large_hourly_rate(3)\
#                     .set_large_daily_rate(25)\
#                     .set_disabled_hourly_rate(1)\
#                     .set_disabled_daily_rate(15)\
#                     .build()




