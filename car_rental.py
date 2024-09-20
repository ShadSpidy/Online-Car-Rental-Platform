import datetime

class CarRental:
    def __init__(self, inventory):
        self.inventory = inventory
        self.rented_cars = {}
        self.hourly_rate = 100
        self.daily_rate = 1000
        self.weekly_rate = 5000

    # Display available cars
    def display_available_cars(self):
        return self.inventory

    # Rent cars on an hourly basis
    def rent_hourly(self, num_cars):
        if 1 <= num_cars <= len(self.inventory):
            now = datetime.datetime.now()
            rented_cars = []
            for i in range(num_cars):
                car = self.inventory.pop()
                self.rented_cars[car] = now
                rented_cars.append(car)  # Keep track of rented cars
            return rented_cars  # Return list of rented cars
        else:
            return False

    # Rent cars on a daily basis
    def rent_daily(self, num_cars):
        if 1 <= num_cars <= len(self.inventory):
            now = datetime.datetime.now()
            rented_cars = []
            for i in range(num_cars):
                car = self.inventory.pop()
                self.rented_cars[car] = now
                rented_cars.append(car)  # Keep track of rented cars
            return rented_cars  # Return list of rented cars
        else:
            return False

    # Rent cars on a weekly basis
    def rent_weekly(self, num_cars):
        if 1 <= num_cars <= len(self.inventory):
            now = datetime.datetime.now()
            rented_cars = []
            for i in range(num_cars):
                car = self.inventory.pop()
                self.rented_cars[car] = now
                rented_cars.append(car)  # Keep track of rented cars
            return rented_cars  # Return list of rented cars
        else:
            return False

    # Return cars and calculate the bill
    def return_cars(self, rented_cars, rental_mode):
        if rented_cars:
            now = datetime.datetime.now()
            total_bill = 0
            for car in rented_cars:
                rent_start_time = self.rented_cars[car]
                rent_duration = (now - rent_start_time).total_seconds() / 3600

                # Calculate bill based on rental mode
                if rental_mode == "hourly":
                    bill = rent_duration * self.hourly_rate
                elif rental_mode == "daily":
                    bill = (rent_duration / 24) * self.daily_rate
                elif rental_mode == "weekly":
                    bill = (rent_duration / (24 * 7)) * self.weekly_rate
                else:
                    return None

                total_bill += bill
                self.inventory.append(car)  # Return car to the inventory
                del self.rented_cars[car]  # Remove car from rented records
            return total_bill
        else:
            return None


class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_cars = {}  # Keeps track of rented cars by this customer

    # Method for requesting cars
    def request_cars(self, rental_service, num_cars, rental_mode):
        # Check if the request is valid (positive number of cars and sufficient inventory)
        if num_cars > 0 and num_cars <= len(rental_service.inventory):
            # Choose the rental mode
            if rental_mode == "hourly":
                rented_cars = rental_service.rent_hourly(num_cars)
            elif rental_mode == "daily":
                rented_cars = rental_service.rent_daily(num_cars)
            elif rental_mode == "weekly":
                rented_cars = rental_service.rent_weekly(num_cars)
            else:
                return "Invalid rental mode"

            # If rental successful, update customer's rented cars
            if isinstance(rented_cars, list):
                self.rented_cars.update({car: rental_service.rented_cars[car] for car in rented_cars})  # Update rented cars
                return rented_cars  # Return the list of rented cars
            else:
                return "Not enough cars available"
        else:
            return "Invalid request: Please check the number of cars or availability"

    # Method for returning cars
    def return_cars(self, rental_service, rental_mode):
        # Attempt to return the cars and calculate the bill
        bill = rental_service.return_cars(list(self.rented_cars.keys()), rental_mode)

        if bill is not None:
            self.rented_cars.clear()  # Clear the customer's record of rented cars
            return f"Total bill for {rental_mode} rental: ${bill:.2f}"
        else:
            # More detailed error message for invalid return request
            if not self.rented_cars:
                return "No cars to return"
            return "Invalid return request"
