import csv 
fields = ['Name', 'Branch', 'Year', 'CGPA']  		
rows = [ ['Nikhil', 'COE', '2', '9.0'],['Sanchit', 'COE', '2', '9.1'], ['Aditya', 'IT', '2', '9.3'], ['Sagar', 'SE', '1', '9.5'], ['Prateek', 'MCE', '3', '7.8'], ['Sahil', 'EP', '2', '9.1'] ] 
filename = "university_records.csv"			
with open(filename, 'w',newline='') as csvfile:
	csvwriter = csv.writer(csvfile)   			  
	csvwriter.writerow(fields)				
	csvwriter.writerows(rows)				
with open(filename, 'r') as readFile:
          reader = csv.reader(readFile)
          print (reader)
          lines = list(reader)
for row in lines: 
    for col in row: 
        print(col,end="\t")
    print('\n')


