import csv


class Sensor:
    def __init__(self, path):
        # __init__ runs once, when the Sensor is created (like setup() on Arduino)
        self.temps = []
        with open(path) as f:
            for row in csv.DictReader(f):
                self.temps.append(float(row["temperature"]))


s = Sensor("data.csv")
# Prediction: print(len(s.temps)) will print the number of temperature readings in the data.csv file, because the Sensor class reads the CSV file and stores the temperatures in the temps list.
print(len(s.temps))