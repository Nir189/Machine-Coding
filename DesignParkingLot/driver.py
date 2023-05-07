import os
import sys
from datetime import datetime, timedelta
sys.path.append('/home/isha/Documents/A/P/R/CodingPractice26Jan/CodingPractice/system_design/Machine-Coding')

from DesignParkingLot.models.parking_floor import ParkingFloor
from DesignParkingLot.models.parking_lot import ParkingLot
from DesignParkingLot.models.vehicle import Vehicle
from DesignParkingLot.models.parking_rate import ParkingRateBuilder

parking_floor1 = ParkingFloor(1)
parking_floor1.add_spots(5 , 'compact')
parking_floor1.add_spots(5 , 'large')
parking_floor1.add_spots(5 , 'disabled')
parking_floor2 = ParkingFloor(2)
parking_floor2.add_spots(5 , 'compact')
parking_floor2.add_spots(5 , 'large')
parking_floor2.add_spots(5 , 'disabled')

parking_lot = ParkingLot()
parking_lot.setId('DEO12345')
parking_lot.setName('HariHar Parking Lot')
parking_lot.address('Deoria')
parking_lot.add_floors(parking_floor1)
parking_lot.add_floors(parking_floor2)

vehicle1 = Vehicle('TT1234IO','compact')
tmp1 = parking_lot.park_vehicle(vehicle1)

vehicle2 = Vehicle('TT1234I1','large')
tmp2 = parking_lot.park_vehicle(vehicle2)

vehicle3 = Vehicle('TT1234IL','disabled')
tmp3 = parking_lot.park_vehicle(vehicle3)


tmp4 = parking_lot.remove_vehicle(vehicle1)

parking_rate_builder = ParkingRateBuilder()
parking_rate = parking_rate_builder.set_compact_hourly_rate(2)\
				.set_compact_daily_rate(20)\
				.set_large_hourly_rate(3)\
				.set_large_daily_rate(25)\
				.set_disabled_hourly_rate(1)\
				.set_disabled_daily_rate(15)\
				.build()
					
parking_lot.setParkingRate(parking_rate)
checkin_time = datetime.now() - timedelta(days=1,hours=2)
checkout_time = datetime.now()
parking_fee = parking_lot.calculate_parking_fee(checkin_time, checkout_time, 'compact')
print(checkin_time)
print(checkout_time)
print("parking_fee******",parking_fee)



# print(tmp1)
# print(tmp2)
# print(tmp3)
# print(tmp4)
# for spot in parking_floor.compact_spots:
# 	print(spot.spot_number)

# for spot in parking_floor.large_spots:
# 	print(spot.spot_number)

# for spot in parking_floor.disabled_spots:
# 	print(spot.spot_number)
# print(parking_floor.compact_spots
# print(parking_floor.large_spots)
# print(parking_floor.disabled_spots)

# cwd = os.getcwd()
# print(cwd)