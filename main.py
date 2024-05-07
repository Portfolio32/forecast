from datetime import datetime as dt
from datetime import date
import matplotlib.pyplot as plt
import torch

d = {}
with open("climate.csv") as file:
    #skipping the first line
    next(file)


    #Reading each line in csv 
    for line in file:
        # data is formatted as [date, max temp(farenheit)]
        data = line.rstrip().split(",")[:2]
        temp = data[1]
        
        #Skip missing data
        if data[1].strip() != "M":
            time = data[0]
            time = dt.strptime(time, '%m/%d/%Y').timetuple().tm_yday
            # set value as list to append to each time with new temperatures
            if d.get(time) == None:
                d[time] = d.get(time, [temp])
            d.get(time).append(temp) 
       


# key is 1 to 365, value is list of temperatures 
d = dict(sorted(d.items()))
T = torch.zeros((1, 366), dtype=torch.int32)
for day, temperatures in d.items():
    average_temp = round(sum([int(temperature) for temperature in temperatures])/len(temperatures))
    # it starts indexed at zero, 0-365, but has the len is 366
    T[0, day - 1] = average_temp

current = date.today().timetuple().tm_yday
today_temperature = T[0, current-1].item()
print(today_temperature)