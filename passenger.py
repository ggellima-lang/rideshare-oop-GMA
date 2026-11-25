class PassengerAccount:
    def __init__(self, name, initial_balance=0.0):
        if initial_balance < 0:
            raise ValueError("Initial wallet balance cannot be negative.")

        self.name = name
        self.__wallet_balance = float(initial_balance)

    def top_up(self, amount):
        if amount < 0:
            raise ValueError("Cannot add negative money to wallet.")

        self.__wallet_balance += amount

    def top_up_wallet(self, amount):
        self.top_up(amount)

    def pay_fare(self, fare_amount):
        if self.__wallet_balance < fare_amount:
            raise ValueError("Insufficient funds! Please top up.")

        self.__wallet_balance -= fare_amount
        print(f"Remaining balance: {self.__wallet_balance}")

    def pay_for_ride(self, fare_amount):
        self.pay_fare(fare_amount)

    def get_balance(self):
        return self.__wallet_balance
