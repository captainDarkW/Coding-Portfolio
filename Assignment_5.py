class Car:
    """A simple Car class with two attributes and two methods."""

    def __init__(self, make: str, speed: int):
        self.make = make          # attribute 1
        self.speed = speed        # attribute 2

    def display(self):
        """Method 1: Display the car's make and current speed."""
        print(f"Car make: {self.make}, Speed: {self.speed} km/h")

    def accelerate(self, increase: int):
        """Method 2: Increase the car's speed by a given amount."""
        self.speed += increase
        print(f"The car accelerates by {increase} km/h. New speed: {self.speed} km/h")


if __name__ == "__main__":
    # Create an instance of Car
    my_car = Car("Toyota", 60)

    # Read attributes
    print("Car make:", my_car.make)
    print("Current speed:", my_car.speed)

    # Call methods
    my_car.display()
    my_car.accelerate(20)  # Accelerate by 20 km/h
    my_car.display()
    my_car.accelerate(15)  # Accelerate by 15 km/h
    my_car.display()
