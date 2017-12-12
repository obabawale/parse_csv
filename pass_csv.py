import csv
import os

the_dir = input("Enter the directory to work with.")
if not isinstance(the_dir, str):
	the_dir = str(the_dir)
res_partner_file = input("Enter the path to res_partner file.")
if not isinstance(res_partner_file, str):
	res_partner_file = str(res_partner_file)
os.chdir(the_dir)
source_dir = os.getcwd()
items = os.listdir(source_dir)
os.mkdir('New')
    
# Fields to be removed from the written csv
blacklist = [
    'partner_id',
    'create_uid', 
    'write_uid', 
    'enrolment_id',
    'id',
    'create_date',
    'write_date',
]        

# Method to pass-in and edit csv files for import into NACAPrEP Database. 
def make_new_file(working_directory, working_file, res_partner_file):
    """Method that passes in a direcory and file for creation of another csv file."""

    # Paths to the files to be read from/written to.
    in_path = str(working_directory) + "/" + str(working_file)
    partner_path = res_partner_file
    out_path = str(working_directory) + "/New/" + str(working_file) + "_new.csv"
    
    #Open respective files for reading/writing
    in_file = open(in_path, 'r')
    partner_file = open(partner_path, 'r')
    out_file = open(out_path, 'w')
    
    # Call csv reader function of the opened files
    reader1 = csv.reader(in_file, delimiter=';')
    reader2 = csv.reader(partner_file)
    writer = csv.writer(out_file)
    
    header1 = next(reader1)
    data1 = [row for row in reader1]
    
    header2 = next(reader2)
    data2 = [row for row in reader2]
    
    for row in data1:
        for item in row:
            if item == 'f':
                ind1 = row.index(item)
                row[ind1] = 'FALSE'
            elif item == 't':
                ind2 = row.index(item)
                row[ind2] = 'TRUE'
    
    for item in blacklist:
        if item in header1:
            item_index = header1.index(item)
            header1.pop(item_index)
            for row in data1:
                row.pop(item_index)
    
    a = header1.index('sceening_id')
    b = header2.index('name')
    
    header1.append('partner_id/id')
    writer.writerow(header1)
    
    for row1 in data1:
        for row2 in data2:
            if row1[a] == row2[b]:
                row1.append(row2[0])
                writer.writerow(row1)
            else:
                continue
                
    in_file.close()
    partner_file.close()
    out_file.close()
    
# Execute the code here
for item in items:
    make_new_file(source_dir, item, res_partner_file)