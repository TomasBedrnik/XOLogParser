import parse_PVE
import parse_XCODB
import csv

path = "/path/to/data/log"
name = "YourIngameName"
csv_file = '/tmp/test.csv'

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
