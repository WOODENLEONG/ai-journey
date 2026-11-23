# 1. What is a class:
# A blueprint or mold that defines the attributes (data) and methods (behavior/ functions) common to a specific concept or object. It allows you to create multiple instances (objects) of that class, each with its own unique data but sharing the same methods.

# 2. What is self:
# When an instance menthod is called, Python automatically passes the instance itself as the first aurgument, conventionally named self. Inside the class methods, self.varible_name refers to the specific instance's data (known as instance vaiables)

# 3. One question I still have
# why do we need to use self in the method definition, but not when calling the method on an instance? For example, we define def min(self), but we call it as s.min() without passing self explicitly. How does Python know to pass the instance automatically?



import csv
import sys


class Sensor:

    def __init__(self, path):
        # 4. What is __init__:
        # __init__ is a special method in Python classes that is automatically called when a new
        
        # __init__ runs once, when the Sensor is created (like setup() on Arduino)
        self.temps = []
        with open(path) as f:
            for row in csv.DictReader(f):
                self.temps.append(float(row["temperature"]))  # Convert the temperature to float and store it in the temps list
    def min(self):
        return min(self.temps)
                
    def max(self):
        return max(self.temps)          
                
    def average(self):
        return sum(self.temps) / len(self.temps)    


s = Sensor(sys.argv[1])  # Create a Sensor object with the path to the CSV file provided as a command-line argument 
# Prediction: 10 (print(len(s.temps)) will print the number of temperature readings in the data.csv file, because the Sensor class reads the CSV file and stores the temperatures in the temps list.)
print(len(s.temps))

#Prediction (calculate by hand from data.csv first!)
#min: 25.1
#max: 29.0
#average: 26.93

print("min:", s.min())
print("max:", s.max())
print("average:", s.average())