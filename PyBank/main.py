import os
import csv

months = 0
total = 0
avgchange = 0
i = 0
profitchange = []

#finding the csv
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #check that it's pulling the correct csv
    # csvheader = next(csvreader)
    # print(csvheader)

    for row in csvreader:

        #get total profit
        if row[1] != "Profit/Losses":
            total += int(row[1])
            profitchange.append(int(row[1]))

        #get total number of months
        if row[0] != "Date":
            #count months
            months += 1
    
    print(months)
    print(total)


    avgchange = [profitchange[i + 1] - profitchange[i] for i in range(len(profitchange)-1)]

    avgchange = sum(avgchange)
    
    print(avgchange)