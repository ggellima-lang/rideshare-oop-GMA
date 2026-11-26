class RideDispatcher:
    def process_ride_queue(self, ride_list):
        print("--- Dispatching Ride Queue ---")
        total_revenue = 0.0

        for ride in ride_list:
            ride.startRide()
            total_revenue += ride.calculateFare()
            ride.completeRide()

        print(f"\nTotal Revenue for this batch: php{total_revenue:.2f}")
