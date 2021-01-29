import csv


fh = open('Csvs\example.csv', newline='')

fr = csv.reader(fh, quoting=csv.QUOTE_MINIMAL)
fl = list[fr]

dr = csv.DictReader(fh)

fo = open('Csvs\examples.csv', 'w', newline='')
fieldnames = ['Man', 'Woman', 'Boy', 'Girl']
s = [{i:len(i)+k for i in fieldnames} for k in range(10)]

dw = csv.DictWriter(fo, fieldnames, extrasaction='ignore')
dw.writeheader()
dw.writerow(s[0])
dw.writerows(s[1:])