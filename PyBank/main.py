import csv

total = 0.0
rows = 0
previous_profit_loss = 0.0
total_change = 0.0
greatest_increase_month = ""
greatest_increase_amount = 0.0
greatest_decrease_month = ""
greatest_decrease_amount = 0.0
current_change = 0.0 

with open("C:\\Users\\Sweety\\Documents\\GitHub\\python-challenge\\PyBank\\Resources\\budget_data.csv") as infile,\
        open ("C:\\Users\\Sweety\\Documents\\GitHub\\python-challenge\\PyBank\\Analysis\\result.txt","w") as outfile:
   reader = csv.reader(infile)

   next(reader, None)  # skip the headers
   #print(len(list(reader)))
   for row in reader:
       total += float(row[1])
       if rows > 0:
           current_change = float(row[1]) - previous_profit_loss
           if greatest_increase_amount < current_change and current_change > 0:
               greatest_increase_month = row[0]
               greatest_increase_amount = current_change
           if greatest_decrease_amount >  current_change and current_change < 0:
               greatest_decrease_month = row[0]
               greatest_decrease_amount = current_change
       total_change += current_change           
       previous_profit_loss = float(row[1])  
       rows += 1 

   result = '''   Financial Analysis
   -----------------------------------
   Total Months: {}    
   Total: ${}
   Average  Change: ${:.2f}
   Greatest Increase in Profits: {}(${})
   Greatest Decrease in Profits: {}(${})''' \
   .format(rows,total.__round__(),total_change/(rows-1).__round__(),greatest_increase_month,greatest_increase_amount.__round__(),\
       greatest_decrease_month,greatest_decrease_amount.__round__())

   outfile.write(result)    

print(result)