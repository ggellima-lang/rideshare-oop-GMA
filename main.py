from driver import DriverAccount
from passenger import PassengerAccount
from standard_ride import StandardRide
from premium_ride import PremiumRide
from dispatcher import RideDispatcher

print("=== PRACTICAL 1: DATA INTEGRITY TEST ===")
driver = DriverAccount("Juan Dela Cruz", "ABC-1234")
driver.add_rating(4.5)
print("Valid rating added:", driver.get_rating_info())

try:
    driver.add_rating(10.0)
except ValueError as e:
    print(f"PASS - Driver rejected 10-star rating: {e}")

passenger = PassengerAccount("Maria Clara")
try:
    passenger.top_up_wallet(-50.0)
except ValueError as e:
    print(f"PASS - Passenger blocked negative top-up: {e}")

try:
    passenger.pay_for_ride(500.0)
except ValueError as e:
    print(f"PASS - Passenger blocked payment without enough funds: {e}")

passenger.top_up_wallet(200.0)
passenger.pay_for_ride(120.0)

print("\n=== PRACTICAL 2: POLYMORPHISM INTEGRATION TEST ===")
ride_queue = [
    StandardRide(5.0),
    PremiumRide(10.0),
    StandardRide(2.5),
]

dispatcher = RideDispatcher()
dispatcher.process_ride_queue(ride_queue)
