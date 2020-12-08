import os
from shutil import copyfile
import csv

OLD_DIR = r'../data/Random Sample'
NEW_DIR = r'../data/Random Sample Named'
MAP = r'../data/0_10000MLFiles.csv'

#rename files of random sampling so no overwriting
def rename():
    for filename in os.listdir(OLD_DIR):
        # print(filename)
        ml_num = filename[0:filename.index('.')]
        ext = filename[filename.index('.'):]
        with open(MAP, 'r') as legend:
            # ln = 0
            reader = csv.reader(legend, delimiter=',')
            for row in reader:
                if str(row[0]) == str(ml_num):
                    new_name = str(row[3]) + ext
                    if '/' in new_name:
                        new_name = new_name.replace('/', ' ', 3)
                    src = OLD_DIR + '/' + filename
                    dest = NEW_DIR + '/' + new_name
                    copyfile(src, dest)
                    break


rename()
