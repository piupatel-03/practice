#Vehicle Hierarchy: Create a Vehicle base class with Car, Bike, and Truck subclasses. Each
#overrides a fuel_cost(distance) method with different rates.input by user .

class Vehicle:
    def fuel_cost(self, distance):
        raise NotImplementedError("Subclasses must implement this method")
    
class Car(Vehicle):
    def fuel_cost(self, distance):
        input_rate = input("Enter the fuel rate per mile for Car: ")
        try:
            rate_per_mile = float(input_rate)
        except ValueError:
            print("Invalid input. Using default rate of 0.12 per mile.")
            rate_per_mile = 0.12  # Default rate for a car
        return distance * rate_per_mile
    

    
       
    
class Bike(Vehicle):
    def fuel_cost(self, distance):
        input_rate = input("Enter the fuel rate per mile for Bike: ")
        try:
            rate_per_mile = float(input_rate)
        except ValueError:
            print("Invalid input. Using default rate of 0.05 per mile.")
            rate_per_mile = 0.05  # Default rate for a bike
        
        return distance * rate_per_mile
    
class Truck(Vehicle):
    def fuel_cost(self, distance):
        input_rate = input("Enter the fuel rate per mile for Truck: ")
        try:
            rate_per_mile = float(input_rate)
        except ValueError:
            print("Invalid input. Using default rate of 0.20 per mile.")
            rate_per_mile = 0.20  # Example rate for a truck

        return distance * rate_per_mile
        
       
    
# Example usage:
if __name__ == "__main__":
    distance = 100  # Example distance in miles
    
    car = Car()
    bike = Bike()
    truck = Truck()
    
    print(f"Car fuel cost for {distance} miles: ${car.fuel_cost(distance):.2f}")
    print(f"Bike fuel cost for {distance} miles: ${bike.fuel_cost(distance):.2f}")
    print(f"Truck fuel cost for {distance} miles: ${truck.fuel_cost(distance):.2f}")

    