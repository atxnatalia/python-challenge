import os
import csv
import math

csv_path = os.path.join ("PyBank", "Resources", "budget_data.csv")

with open (csv_path) as csvfile
    csvreader = csv.reader (csvfile, delimiter= ',')

    header = next(csvreader)

    month_total = []
    net_profit = []
    avg_change_profit = []

    for row in csvreader
        month_total.append(row[0])
        net_profit.append(int(row[1]))

    for e in range(len(net_profit)-1)
        avg_change_profit.append(net_profit[e+1]-net_profit[e])

greatist_profit = max(avg_change_profit)
greatist_loss = min(avg_change_profit)

date_loss = avg_change_profit(max(avg_change_profit))
date_profit = avg_change_profit(min(avg_change_profit))

print(f"Financial Analysis")
print(f"----------------------------\n")
print(f"Total Months: {len(month_total)}\n")
print(f"Total: ${sum(net_profit)}\n")
print(f"Average Change: {round(sum(avg_change_profit)/len(avg_change_profit),2)}\n")
print(f"Greatest Increase in Profits: {month_total[date_profit]} (${(str(most_profit))})\n")
print(f"Greatest Decrease in Profits: {month_count[date_loss]} (${[str(most_loss)]}))\n")
