import csv
dates = []
value = []

with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
    #        print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif len(row) != 0:
            dates.append(row[0])
            value.append(int(row[1]))
            line_count+=1

change = []

for i in range(len(value)-1):
    change.append (value[i+1]-value[i])
    
   
Min = min(change)
Max = max(change)
date_min = dates[change.index(Min)+1]
date_max = dates[change.index(Max)+1]
avg_change = sum(change)/len(change)

    



    #print(f'Processed {line_count} lines.')
print ('Financial Analysis')
print('-----------------------------------------')
print ('Total Months ' + str(len(dates)))
print ('Total ' + '$'+str(sum(value)))
print ('Average Change ' + '$'+str(round(avg_change,2)))
print ('Greatest Increase in Profits ' + date_max + ' $'+str(Max))
print ("Greatest Decrease in Profits " + date_min + ' ($'+str(abs(Min))+')' )
    
f = open("PyBank.txt", "w")

f.write(
     "Financial Analysis\n"   +
     "Total Months "  + str(len(dates))+ '\n' +
     "Total " + str(sum(value)) + '\n' +
    "Average Change $" +str(round(sum(change)/len(change))) +'\n'+
    "Greatest Increase in Profits $" +str(max(value)) +'\n' +
    "Greatest Decrease in Profits " + '($'+str(abs(Min))+')' 
   )
f.close()         




