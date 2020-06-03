import os
import csv

#set variables
months = 0
total_profit = 0
monthly_avg = 0
profitchange = []
new_start_row = []
profit_change_list = []
month_of_change = []

#greatest incrase var
greatest_increase_month = ""
greatest_increase_amount = 0

#decrease var
greatest_decrease_month = ""
greatest_decrease_amount = 0



#finding the orginial csv
csv_org = os.path.join("Resources", "budget_data.csv")
#output txt
txt_output = os.path.join("Analysis", "analysis.txt")


with open(csv_org, 'r') as csv_org_file:
    csvreader = csv.reader(csv_org_file, delimiter =',')
    
    #check that it's pulling the correct csv
    # csvheader = next(csvreader)
    # print(csvheader)

    #store headers
    headers = next(csvreader)

    #start at row after header row
    new_start_row = next(csvreader) 
    months += 1
    total_profit += int(new_start_row[1])
    prev_profit = int(new_start_row[1])

    for row in csvreader:

        #get total profit & months
        months += 1
        total_profit += int(row[1])

        #profit change
        profit_change = int(row[1]) - prev_profit
        prev_profit = int(row[1])
        profit_change_list += [profit_change]
        month_of_change += [row[0]]

        #greatest increase
        if profit_change > greatest_increase_amount:
            greatest_increase_month = row[0]
            greatest_increase_amount = profit_change
        
        #greatest decrease
        if profit_change < greatest_decrease_amount:
            greatest_decrease_month = row[0]
            greatest_decrease_amount = profit_change


#avg
monthly_avg = sum(profit_change_list) / len(profit_change_list)

#formatting output
print("Financial Analysis")
print("")
print(f"Total Months: {months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${monthly_avg:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})")


#\n = newline
combined_output = (
    f"Financial Analysis\n"
    f""
    f"Total Months: {months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})\n"
)

with open(txt_output, "w") as txt_analysis:
    txt_analysis.write(combined_output)