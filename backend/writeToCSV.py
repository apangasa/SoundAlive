import csv

def to_csv(animal, list1, list2):
    row = [animal] + list1 + list2
    with open(r'../data/test_results.csv', 'a') as file:
        addRow = csv.writer(file)
        addRow.writerow(row)
    return

