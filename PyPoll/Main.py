      
import csv
#Declare variables

kcount = 0
ccount = 0
lcount = 0
ocount = 0
winner = str
Total = 0



#Create List for Tabulation

with open('Election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row[2]=="Khan":
            kcount+=1
        elif row[2]=="Correy":
            ccount+=1
        elif row[2]=="Li":
            lcount+=1
        else:
            ocount+=1

if kcount>ccount and kcount>lcount and kcount>ocount:
    winner="Khan"
elif ccount>kcount and ccount>lcount and ccount>ocount:
    winner="Correy"
elif ocount>kcount and ocount>lcount and ocount>ccount:     
    winner="O'Tooley"
else:
    winner="Li"
    
Total = (kcount+lcount+ocount+ccount)
    


print("")    
print("")    

print('Election result' )
print('-------------------------------------------------------------')
print ('Total Votes: ' + str(Total))
   # print (Candidate)
print('-------------------------------------------------------------')
print("Khan: " + str(round((kcount/Total)*100,3)) +'% '+ '('+str(kcount)+')')
print("Correy: " + str(round((ccount/Total)*100,3)) +'% '+ '('+str(ccount)+')')
print("Li: " + str(round((lcount/Total)*100,3)) +'% '+'('+str(lcount)+')')
print("O'Tooley: " + str(round((ocount/Total)*100,3)) +'% '+ '('+str(ocount)+')')
print('-------------------------------------------------------------')
print('Winner: ' + str(winner) )
print('-------------------------------------------------------------')
    
f = open("PyPoll.txt", "w")

f.write(
    
'Election result\n' 
'-------------------------------------------------------------\n'
'Total Votes: ' + str(Total) + '\n'
'-------------------------------------------------------------\n'
"Khan: " + str(round((kcount/Total)*100,3)) +'% '+ '('+str(kcount)+')' + '\n'
"Correy: " + str(round((ccount/Total)*100,3)) +'% '+ '('+str(ccount)+')' + '\n'
"Li: " + str(round((lcount/Total)*100,3)) +'% '+'('+str(lcount)+')' + '\n'
"O'Tooley: " + str(round((ocount/Total)*100,3)) +'% '+ '('+str(ocount)+')' + '\n'
'-------------------------------------------------------------\n'
'Winner: ' + str(winner)  + '\n'
'-------------------------------------------------------------'

    
    
    
   )
f.close()         

    

