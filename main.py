from datetime import datetime as dt

d = {}
with open("climate.csv") as file:
    n = 0
    next(file)
    for line in file:
        # data is formatted as date : max temp(farenheit)
        data = line.rstrip().split(",")[:2]
        if data[1].strip() != "M":
            date = data[0]
            date = dt.strptime(date, '%m/%d/%Y')
            for month,day in zip(date.month,date.day):
                
            #d[date] = data[1]      
        n += 1
        if n == 100:
            break

