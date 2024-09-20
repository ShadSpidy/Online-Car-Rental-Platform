import car_rental

def main():
    # Initialize car inventory
    inventory = ["Car1", "Car2", "Car3", "Car4"]

    # Create car rental service
    rental_service = car_rental.CarRental(inventory)

    # Create a dictionary to store customers
    customers = {}

    while True:
        print("\nMenu:")
        print("1. Display available cars")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. View rented cars")
        print("5. Quit")
        choice = input("Select an option (1/2/3/4/5): ")

        if choice == "1":
            # Display available cars
            print("Available cars:", rental_service.display_available_cars())
        elif choice == "2":
            # Rent a car
            customer_name = input("Enter customer name: ")
            if customer_name not in customers:
                customers[customer_name] = car_rental.Customer(customer_name)
            customer = customers[customer_name]

            num_cars = int(input("Enter the number of cars to rent: "))
            rental_mode = input("Enter rental mode (hourly/daily/weekly): ")
            rented_cars = customer.request_cars(rental_service, num_cars, rental_mode)

            if isinstance(rented_cars, list):
                print(f"Rented cars: {', '.join(rented_cars)}")
            else:
                print(rented_cars)  # Display error message
        elif choice == "3":
            # Return a car
            customer_name = input("Enter customer name: ")
            if customer_name in customers:
                customer = customers[customer_name]
                rental_mode = input("Enter rental mode (hourly/daily/weekly): ")
                print(customer.return_cars(rental_service, rental_mode))
            else:
                print("Customer not found.")
        elif choice == "4":
            # View rented cars
            print("Rented Cars:")
            for customer_name, customer in customers.items():
                if customer.rented_cars:
                    print(f"{customer_name} has rented: {', '.join(customer.rented_cars.keys())}")
                else:
                    print(f"{customer_name} has no rented cars.")
        elif choice == "5":
            # Quit
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
