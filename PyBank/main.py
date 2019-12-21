# You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

import os
import csv

#bring in the csv file
financialdata = os.path.join('budget_data.csv')

#create some variables.. lots of variables... might not need to formally define all of these
date = []
profit = []
change = []
AmountTotal = 0
valuechange = 0
valuesum = 0
maxvalue = 0
minvalue = 0
count = 0

#read through each line of the csv file
with open(financialdata, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #call out the header row
    csv_header = next(csvfile)
    #print(f'Header: {csv_header}')

    #when you go through each row, create a new list for the dates and the profits
    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])
        # The net total amount of "Profit/Losses" over the entire period
        AmountTotal = AmountTotal + int(row[1])

    # The total number of months included in the dataset
    MonthTotal = len(date)

    #print the results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {MonthTotal}")
    print(f"Total: {AmountTotal}")

    # The average of the changes in "Profit/Losses" over the entire period
    # loop through the list
    for i in range(len(profit)-1):
        #calculate the difference between the next value and the current value
        valuechange = int(profit[i+1]) - int(profit[i])
        #increase the count for each loop
        count += 1

        #find the max value in the valuechange list
        if valuechange > maxvalue:
            maxvalue = valuechange
            #set the count so I know where to call the matching result in the date list
            maxvaluecount = count
        #find the min value in the valuechange list
        if valuechange < minvalue:
            minvalue = valuechange
            #set the count so I know where to call the matching result in the data list
            minvaluecount = count

        #sum all of the values while looping through the list
        valuesum = valuesum + valuechange
        #then find the average by dividing by the length of the list
        valueaverage = valuesum/(len(profit)-1)

    #format the results and print them
    formataveragechange = '{:.2f}'.format(valueaverage)
    formatmax = '(${:})'.format(maxvalue)
    formatmin = '(${:})'.format(minvalue)
    print(f"Average Change: {formataveragechange}")
    print(f'Greatest Increase in Profits: {date[maxvaluecount]} {formatmax}')
    print(f'Greatest Decrease in Profits: {date[minvaluecount]} {formatmin}')

    #print all of this to a csv file
    with open("PyBank Results.csv", mode='w') as resultsFile:
        resultsWriter = csv.writer(resultsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        resultsWriter.writerow(["Financial Analysis"])
        resultsWriter.writerow(["Total Months:", MonthTotal])
        resultsWriter.writerow(["Total:", AmountTotal])
        resultsWriter.writerow(["Average Change:", formataveragechange])
        resultsWriter.writerow(["Greatest Increase in Profits:", date[maxvaluecount], formatmax])
        resultsWriter.writerow(["Greatest Decrease in Profits:", date[minvaluecount], formatmin])
