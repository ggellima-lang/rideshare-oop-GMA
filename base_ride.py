from abc import ABC, abstractmethod

class Base_Ride(ABC):
    def __init__(self, distanceKm: float):
        self.distanceKm = distanceKm
        self.isCompleted = False

    @abstractmethod
    def calculateFare(self):
        pass
    @abstractmethod
    def startRide(self):
        pass
    @abstractmethod
    def completeRide(self):
        pass































