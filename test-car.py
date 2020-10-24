# test-car.py
# practicing OOP and classes in python - Create a car class with attributes:
# attributes: age, color, number_of_seats, off-road (boolean)

class Car:
    make = "Jeep"

    def __init__(self, color, age, number_of_seats, miles):
        self.color = color
        self.age = age
        self.number_of_seats = number_of_seats
        self.miles = miles

    # Instance method (I know it's obvious, I'm practicing)
    def __str__(self):
        return f"The {self.color} {Car.make} is {self.age} years old and has {self.number_of_seats} seats and {self.miles} miles"

    #another instance method
    def speak(self, sound):
        return f"{self.color} {Car.make} says {sound}"

#betty = Car("Blue", 9, 4, 1000)
#print("")
#print(betty)
#print("")
#beep = betty.speak("Vroom vroom")
#print(beep)

# create cars
silver_car = Car("Silver", 1, 6, 100)
red_car = Car("Red", 2, 2, 3500)
# loop thru print with a tuple
for car in (silver_car, red_car):
    print(f"The {car.color} car has {car.miles:,} miles")