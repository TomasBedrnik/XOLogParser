import parse_PVE
import parse_XCODB
import csv

# Mind the slashes - you have to use forward slash or two backslashes
path = "C:/Users/John/Documents/My Games/Crossout/logs/"
name = "YourIngameName"
csv_file = 'C:\\Users\\John\\Desktop\\test.csv'

data = []
# Read data from logs
data_updated = parse_PVE.read(path, name, data)

# Read prices from https://crossoutdb.com/
data_price = parse_XCODB.read()

with open(csv_file, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(data_price)
    writer.writerows(data_updated)

input("Press anything to exit...")
