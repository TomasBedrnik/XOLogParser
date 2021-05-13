import read_write_Google
import parse_PVE
import parse_XCODB
import os


path = "/path/to/data/log"
name = "YourIngameName"
SPREADSHEET_ID = 'yourGoogleSpreadSheetsCopyOfTableIDIDIDIDID0'

# Read previous data from google sheet
data = read_write_Google.read_google_sheet(spreadsheet_id=SPREADSHEET_ID)

# Read new data from logs
dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
for directory in dirs:
    print("__________")
    print("Directory = " + directory)
    path_game_log = os.path.join(path, directory, "game.log")
    path_combat_log = os.path.join(path, directory, "combat.log")

    data_game = parse_PVE.parse_PVE_game_log(path_game_log)
    data_combat = parse_PVE.parse_PVE_combat_log(path_combat_log, name)
    for time in data_game:
        print("Time = " + time, end=", ")
        print("Difficulty = " + data_game[time][0], end=", ")
        print("Opponents = " + data_game[time][1], end=", ")
        print("Type = " + data_game[time][2], end=", ")
        print("Map = " + data_game[time][3], end=", ")
        print("Time [s] = " + data_game[time][4], end=", ")
        print("Resource type = " + data_game[time][5], end=", ")
        print("Gained resources = " + data_game[time][6], end=", ")
        print("Points = " + data_game[time][7], end=", ")
        if time in data_combat.keys():
            print("Type = " + data_combat[time][0], end=", ")
            print("Map = " + data_combat[time][1], end=", ")
            print("All PS = " + str(data_combat[time][2]), end=", ")
            print("My PS = " + str(data_combat[time][3]), end=", ")
            print("all points = " + str(data_combat[time][4]), end=", ")
            print("Standing = " + str(data_combat[time][5]), end=", ")
            print(" ")
            print("               Players:", end=" ")
            for player in data_combat[time][6]:
                print(player[0]+"[" + player[1] + "]: "+str(player[2]), end=" ")
            data.append([directory[0:11]+time, data_game[time][2], data_game[time][0], data_game[time][3], data_game[time][1],
                        data_game[time][5], data_game[time][6], data_game[time][4], data_game[time][7],
                        data_combat[time][3], data_combat[time][5], data_combat[time][2], data_combat[time][4]])
        else:

            data.append([directory[0:11]+time, data_game[time][2], data_game[time][0], data_game[time][3], data_game[time][1],
                        data_game[time][5], data_game[time][6], data_game[time][4], data_game[time][7]])
        print(" ")

# Make everything string for proper sorting
if not data:
    print('No data found.')
else:
    print(type(data))
    for i in range(len(data)):
        for y in range(len(data[i])):
            # print(data[i][y], end=", ")
            data[i][y] = str(data[i][y])
        # print(" ")


# Sort by first element (time) descending
data_sorted = sorted(data, reverse=True)

# Write to google docs
read_write_Google.write_google_sheet(spreadsheet_id=SPREADSHEET_ID, data=data_sorted)

print("_____________________________")
print("Plastic: ", parse_XCODB.read_price("Plastic")[0], ", ", parse_XCODB.read_price("Plastic")[1])
print("Electonics: ", parse_XCODB.read_price("Electonics")[0], ", ", parse_XCODB.read_price("Electonics")[1])
print("Copper: ", parse_XCODB.read_price("Copper")[0], ", ", parse_XCODB.read_price("Copper")[1])
print("Fuel: ", parse_XCODB.read_price("Fuel")[0], ", ", parse_XCODB.read_price("Fuel")[1])
print("Battery: ", parse_XCODB.read_price("Battery")[0], ", ", parse_XCODB.read_price("Battery")[1])
print("Scrap Metal: ", parse_XCODB.read_price("Scrap Metal")[0], ", ", parse_XCODB.read_price("Scrap Metal")[1])
print("Wires: ", parse_XCODB.read_price("Wires")[0], ", ", parse_XCODB.read_price("Wires")[1])

data_price = [
    [parse_XCODB.read_price("Plastic")[0], parse_XCODB.read_price("Plastic")[1]],
    [parse_XCODB.read_price("Electonics")[0], parse_XCODB.read_price("Electonics")[1]],
    [parse_XCODB.read_price("Copper")[0], parse_XCODB.read_price("Copper")[1]],
    [parse_XCODB.read_price("Fuel")[0], parse_XCODB.read_price("Fuel")[1]],
    [parse_XCODB.read_price("Battery")[0], parse_XCODB.read_price("Battery")[1]],
    [parse_XCODB.read_price("Scrap Metal")[0], parse_XCODB.read_price("Scrap Metal")[1]],
    [parse_XCODB.read_price("Wires")[0], parse_XCODB.read_price("Wires")[1]]
]

read_write_Google.write_google_sheet_price(spreadsheet_id=SPREADSHEET_ID, data=data_price)

# input("Press anything to exit...")
