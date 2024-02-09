import csv

file = open("prefs.csv", "r")
prefs = list(csv.reader(file, delimiter=","))
file.close()

pre = [row[0] for row in prefs]
prefixes = tuple(pre)

file = open("cdrs.csv", "r")
cdrs = list(csv.reader(file, delimiter=","))
file.close()

from_numbers = [row[0] for row in cdrs]

count=0
for i in from_numbers:
    if i.startswith(prefixes):
        print(i)
        count += 1

print("Total prefixes found",count)






