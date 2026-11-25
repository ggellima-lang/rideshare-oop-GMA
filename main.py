from driver import DriverAccount
from passenger import PassengerAccount

print("=== PRACTICAL 1: DATA INTEGRITY TEST ===")

# 1. Prove the driver rejects a 10-star rating
driver = DriverAccount("Juan Dela Cruz", "ABC-1234")
driver.add_rating(4.5)
print("Valid rating added:", driver.get_rating_info())

try:
    driver.add_rating(10.0)
except ValueError as e:
    print(f"PASS - Driver rejected 10-star rating: {e}")

# 2. Prove the passenger cannot top up negative money or pay without funds
passenger = PassengerAccount("Maria Clara")

try:
    passenger.top_up_wallet(-50.0)
except ValueError as e:
    print(f"PASS - Passenger blocked negative top-up: {e}")

try:
    passenger.pay_for_ride(500.0)
except ValueError as e:
    print(f"PASS - Passenger blocked payment without enough funds: {e}")

# Bonus check: verify valid top-up and payment work properly
passenger.top_up_wallet(200.0)
passenger.pay_for_ride(120.0)