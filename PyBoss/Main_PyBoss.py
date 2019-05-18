#State Dictionary for passing through St abbrevations
states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


#Emp ID	Name	DOB	SSN	State

      
import csv
import re
import datetime
first_name = ""
last_name = ""
full_name=""
output = []
#Declare variables




#Create List for Tabulation

with open('employee_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    line_count = 0
    with open("PyBoss.csv", "w", newline='') as out_file:
        csvwriter = csv.writer(out_file, delimiter=',')
        csvwriter.writerow(['Emp ID','Name','DOB','SSN','State'])
#         # Write the first row (column headers)
        
#         # Write the second row
         #csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])

        for row in csv_reader:
            #namesplit = re.split(" ", row[1])
            namesplit = row[1].split(" ")
            first_name = namesplit[0]
            last_name = namesplit[1]
            #datesplit = re.split("-", row[2])
            datesplit = row[2].split("-")
            year = datesplit[0]
            month = datesplit[1]
            day = datesplit[2]
            ssn = '***-**-' + row[3][-4:]
            vState = states[row[4]]
            csvwriter.writerow([row[0],first_name,last_name,(str(month)+"/"+str(day)+"/"+str(year)),ssn,vState])
            print((row[0]+", "+first_name + ", " + last_name + ", " + (str(month)+"/"+str(day)+"/"+str(year))+", "+ssn+", "+vState))
        
        
#        
#f = open("PyBoss.txt", "w")
#
#f.write(
#    

#    
#    
#   )
#f.close()         

    


