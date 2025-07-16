import csv
data = []
temperatures = []

with open("./weather_data.csv", "r") as file:
#    for row in file.readlines():
#       data.append(row)
    data = csv.reader(file)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    
print(temperatures)