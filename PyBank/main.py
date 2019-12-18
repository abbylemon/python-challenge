# You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

import os
import csv

financialdata = os.path.join('budget_data.csv')

date = []
profit = []
change = []
AmountTotal = 0
valuechange = 0
i = 0

with open(financialdata, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    print(f'Header: {csv_header}')

    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])
        # The net total amount of "Profit/Losses" over the entire period
        AmountTotal = AmountTotal + int(row[1])

# The total number of months included in the dataset

    MonthTotal = len(date)
    print(MonthTotal)

    print(AmountTotal)

# The average of the changes in "Profit/Losses" over the entire period

    for line in profit:
        valuechange = (profit[line+1]) - (profit[line])
        change.append(valuechange)
        i+=1
    print(change[0])
    #for i in profit:
        #non of this stuff worked
        #changevalue = int(profit[i+1]) - int(profit[i])
        #change.append(changevalue)
    #print(profit[1]-profit[0])
    #print(change[0])


# The greatest increase in profits (date and amount) over the entire period

    #Need to do this function on the change in profit[]
    #GreatestIncrease = max(profit)
    #print(GreatestIncrease)

# The greatest decrease in losses (date and amount) over the entire period
