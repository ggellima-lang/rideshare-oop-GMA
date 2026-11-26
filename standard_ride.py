from base_ride import Base_Ride


class StandardRide(Base_Ride):

    def __init__(self, distanceKm: float):
        super().__init__(distanceKm)
        self.__base_rate = 5.00

    def calculateFare(self):
        return self.__base_rate + (self.distanceKm * 1.50)

    def startRide(self):
        print(f"Starting Standard Ride for {self.distanceKm} km.")

    def completeRide(self):
        self.isCompleted = True
        print(f"=== STANDARD RECEIPT ===\nFare: Php{self.calculateFare():.2f}")
