from datetime import datetime as dt

d = {}
with open("climate.csv") as file:
    #skipping the first line
    next(file)

    #Just to limite the dataset a bit
    n = 0
    
    
    #Reading each line in csv 
    for line in file:
        # data is formatted as [date, max temp(farenheit)]
        data = line.rstrip().split(",")[:2]
        temp = data[1]
        
        #Skip missing data
        if data[1].strip() != "M":
            date = data[0]
            date = dt.strptime(date, '%m/%d/%Y').timetuple().tm_yday
            # set value as list to append to each time with new temperatures
            if d.get(date) == None:
                d[date] = d.get(date, [temp])
            d.get(date).append(temp) 
        
        #Just to limit the dataset a bit
        n += 1
        if n == 1000:
            break

d = dict(sorted(d.items()))
print(d)

