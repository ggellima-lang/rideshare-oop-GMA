from base_ride import Base_Ride


class PremiumRide(Base_Ride):
    """Luxury ride subclass inheriting from Base_Ride."""

    def __init__(self, distanceKm: float, snack: str = "Bottled Water & Chips"):
        # Call parent Base_Ride initializer with distanceKm
        super().__init__(distanceKm)

        # Private attributes required by Member B specifications
        self.__premium_base_rate = 15.00
        self.__complimentary_snack = snack

    def calculateFare(self):
        # Required abstract method: luxury base rate + P3.00 per kilometer
        return self.__premium_base_rate + (self.distanceKm * 3.00)

    def calculate_fare(self):
        # Snake_case alias matching the handout text
        return self.calculateFare()

    def startRide(self):
        # Required abstract method from Base_Ride
        print("Starting VIP Premium Ride. Enjoy your snacks!")

    def start_ride(self):
        # Snake_case alias matching the handout text
        self.startRide()

    def completeRide(self):
        # Required abstract method from Base_Ride
        fare = self.calculateFare()
        self.isCompleted = True
        print("=== VIP RECEIPT ===")
        print(f"Fare: ₱{fare:.2f}")
        print(f"Complimentary Snack: {self.__complimentary_snack}")

    def complete_ride(self):
        # Snake_case alias matching the handout text
        self.completeRide()

    def get_snack(self):
        # Safe getter for private snack attribute
        return self.__complimentary_snack
