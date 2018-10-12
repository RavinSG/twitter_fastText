import csv


output = open('word_set.csv', 'w', newline='')


def make_word_set(file_list):
    for file in file_list:
        with open(file, 'r') as csv_file:
            in_file = csv.reader(csv_file)
            csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in in_file:
                csv_writer.writerow(row[:3])
                print(row[:3])

files = ['set1.csv', 'set2.csv']

make_word_set(files)

