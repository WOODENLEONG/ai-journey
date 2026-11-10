# Warm-up 1: a list = many values in order (like a sample buffer)
temps = [25.1,26.0,24.8]
#Prediction: temps[0] = 25.1, temps[1] = 26.0, temps[2] = 24.8 , len(temps) = 3  
print(temps)
print(temps[0])
print(temps[1])
print(temps[2])
print(len(temps))

#Warm-up: a dict = values with names (like a sample with labels)
reading = {"time":0, "temperature":25.1, "humidity":0.5 }
#Prediction: reading["time"] = 0, reading["temperature"] = 25.1, reading["humidity"] = 0.5
print(reading)
print(reading["time"])
print(reading["temperature"])
print(reading["humidity"])

import csv

rows = [] # empty list = empty sample buffer

with open("data.csv") as f: # open the file it closes by itself at the end
    reader = csv.DictReader(f) # read each line as a dict, using the header as keys
    for row in reader: # one loop = one sample
        rows.append(row) # add the sample to the buffer

#Prediction: len(rows)= 10, rows[0]={'time'='0','temperature'='25.1'}
print(len(rows))
print(rows[0])

temps = [] # empty list = empty sample buffer
for row in rows: # one loop = one sample
    temps.append(float(row["temperature"])) # add the sample to the buffer, converting the string to a float    

    #Prediction: temps = [25.1, 26.0, 24.8, 25.5, 26.2, 25.9, 24.7, 25.3, 26.1, 25.4]
    print(temps)


#Problem:
## FileNotFoundError: open() looks in the terminal's current folder, not the .py file's folder