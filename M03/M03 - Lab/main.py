# Alexander L
# M03 - Lab, main.py
# Allows user to enter details about a car

class Vehicle:
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

if __name__ == '__main__':
    userInputs = []

    userInput = input("Enter vehicle type: ")
    userInputs.append(userInput)
    userInput = input("Enter vehicle year: ")
    userInputs.append(userInput)
    userInput = input("Enter vehicle make: ")
    userInputs.append(userInput)
    userInput = input("Enter vehicle model: ")
    userInputs.append(userInput)
    userInput = input("Enter vehicle number of doors: ")
    while True:
        if userInput == "2" or userInput == "4":
            break
        else:
            userInput = input("Enter vehicle number of doors(2 or 4 only): ")
    userInputs.append(userInput)
    userInput = input("Enter vehicle type of roof: ")
    
    while True:
        if userInput.upper() == "SUN ROOF" or userInput.upper() == "SOLID":
            break
        else:
            userInput = input("Enter vehicle type of roof(solid or sun roof only): ")
    userInputs.append(userInput)

    userCar = Automobile(type=userInputs[0], year=userInputs[1], make=userInputs[2], model=userInputs[3], doors=userInputs[4], roof=userInputs[5])

    print("Vehicle type: " + userCar.type)
    print("Year: " + userCar.year)
    print("Make: " + userCar.make)
    print("Model: " + userCar.model)
    print("Number of doors: " + userCar.doors)
    print("Type of roof: " + userCar.roof)
