import csv
import os
def to_csv(animal, list1, list2):
    row = [animal] + list1 + list2
    with open(r'../data/test_results.csv', 'a') as file:
        addRow = csv.writer(file)
        #https://stackoverflow.com/questions/42537194/how-to-check-if-xls-and-csv-files-are-empty#:~:text=import%20pandas%20as%20pd%20df,empty%20or%20False%20if%20not.
        if os.stat(r'../data/test_results.csv').st_size == 0:
            header = ['Animal', 'B #1', 'B #2', 'B #3', 'Splay #1', 'Splay #2', 'Splay #3']
            addRow.writerow(header)
        addRow.writerow(row)
    return
