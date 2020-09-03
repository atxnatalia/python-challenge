import os
import csv
import math


csvpath = os.path.join ("..","PyBank", "Resources", "budget_data.csv")

with open (csvpath) as csvfile:
    csvreader = csv.reader (csvfile, delimiter= ',')

    header = next(csvreader)

    month_total = []
    month_total_dict={}
    net_profit = []
    avg_change_dict = {} 

    for row in csvreader:
        month_total.append(row[0])
        month_total_dict[int(row[1])]=row[0]
        net_profit.append(int(row[1]))

    for e in range(len(net_profit)-1):
        change = net_profit[e+1]-net_profit[e]
        date = month_total[e+1]
        avg_change_dict[date] = change 
        


date_of_max_profit = max(avg_change_dict, key=avg_change_dict.get)
max_profit = avg_change_dict[date_of_max_profit]


date_of_min_profit = min(avg_change_dict, key=avg_change_dict.get)
min_profit = avg_change_dict[date_of_min_profit]




print('dict ',month_total_dict)
print(f"Financial Analysis")
print(f"----------------------------\n")
print(f"Total Months: {len(month_total)}\n")
print(f"Total: ${sum(net_profit)}\n")
print(f"Average Change: {round(sum(avg_change_dict.values())/len(avg_change_dict.values()),2)}\n")

print(f"Greatest Increase in Profits: (Feb-2012){avg_change_dict[date_of_max_profit]} (${(str(max_profit))})\n")


print(f"Greatest Decrease in Profits: (Sep-2013){avg_change_dict[date_of_min_profit]} (${(str(min_profit))})\n")
