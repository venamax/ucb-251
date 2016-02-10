import zipfile
import sys
import csv
from csv import reader

csv.field_size_limit(sys.maxsize)

test_keyword = "!"
test_file_zip = 'googlebooks-eng-us-all-2gram-20090715-2.csv.zip'




def find_ngrams(file_zip, keyword):
    current_word = None
    count = 0
    pairs = {}
    myzip = zipfile.ZipFile(file_zip, 'r')
    if zipfile.is_zipfile(file_zip):
        filename = myzip.namelist()[0]

    with myzip.open(filename) as myfile:
        for line in myfile:
            line = myfile.readline()
            line = line.split()
            if len(line) == 6:
                try:
                    word = line[0]
                except ValueError:
                    continue
                if word == keyword:
                    if current_word == line[1]:
                        count += int(line[3])
                    else:
                        pairs.update({current_word:count})
                        current_word = line[1]
                        count = int(line[3])

        pairs.update({current_word:count})
        return pairs
pairs = find_ngrams(test_file_zip,test_keyword)

print pairs

        
