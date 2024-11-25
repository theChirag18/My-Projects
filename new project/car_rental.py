import datetime


class CarRental:
    def __init__(self, stock=0):
        self.stock = stock

    def displayStock(self):
        """Display the number of cars available."""
        print(f"Currently, {self.stock} car(s) are available for rent.")
        return self.stock

    def rentCarOnHourlyBasis(self, numOfCars):
        """Rent cars on an hourly basis."""
        if numOfCars <= 0:
            print("Number of cars should be positive!")
            return None
        elif numOfCars > self.stock:
            print(f"Sorry, only {self.stock} car(s) are available.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You rented {numOfCars} car(s) on an hourly basis at {now}.")
            self.stock -= numOfCars
            return now

    def rentCarOnDailyBasis(self, numOfCars):
        """Rent cars on a daily basis."""
        if numOfCars <= 0:
            print("Number of cars should be positive!")
            return None
        elif numOfCars > self.stock:
            print(f"Sorry, only {self.stock} car(s) are available.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You rented {numOfCars} car(s) on a daily basis at {now}.")
            self.stock -= numOfCars
            return now

    def rentCarOnWeeklyBasis(self, numOfCars):
        """Rent cars on a weekly basis."""
        if numOfCars <= 0:
            print("Number of cars should be positive!")
            return None
        elif numOfCars > self.stock:
            print(f"Sorry, only {self.stock} car(s) are available.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You rented {numOfCars} car(s) on a weekly basis at {now}.")
            self.stock -= numOfCars
            return now

    def returnCar(self, request):
        """Calculate the bill and update stock."""
        rentalTime, rentalBasis, numOfCars = request
        bill = 0

        if rentalTime and rentalBasis and numOfCars:
            self.stock += numOfCars
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            if rentalBasis == 1:  # Hourly
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfCars
            elif rentalBasis == 2:  # Daily
                bill = rentalPeriod.days * 120 * numOfCars
            elif rentalBasis == 3:  # Weekly
                bill = (rentalPeriod.days // 7) * 360 * numOfCars

            if numOfCars >= 2:
                print("You earned a 20% discount for renting multiple cars!")
                bill *= 0.8

            print(f"Thanks for returning the car(s). Your total bill is ${bill:.2f}.")
            return bill
        else:
            print("No valid rental data provided.")
            return None


class Customer:
    def __init__(self):
        self.cars = 0
        self.rentalBasis = 0
        self.rentalTime = 0

    def requestCar(self):
        """Request a specific number of cars."""
        try:
            numOfCars = int(input("How many cars would you like to rent? "))
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            return None

        if numOfCars < 1:
            print("Number of cars should be greater than zero!")
            return None
        else:
            self.cars = numOfCars
            return self.cars

    def returnCar(self):
        """Return rented cars."""
        if self.rentalTime and self.rentalBasis and self.cars:
            return self.rentalTime, self.rentalBasis, self.cars
        else:
            return None, None, None
