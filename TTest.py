import csv

with open('CP3_csv.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            row.replace("\uFEFF", "")
            print('Column names are ', (", ".join(row)))
            line_count += 1
        else:
            print('\t',row[0],' like ',row[1],' and favorite pet is ',row[2],'.')
            line_count += 1
    print(f'Processed {line_count} {row[0]} lines.')
