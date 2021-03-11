# from __future__ import print_function
# import pickle
# import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
#
# # If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#
# # The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1TZHBYfwbXrFOCIVXUu_dwR38obeJpWjDzE8s0ern5Xg'
# SAMPLE_RANGE_NAME = 'Raid!A21:M'
#
#
# def main():
#     credentials = None
#     # The file token.pickle stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             credentials = pickle.load(token)
#     # If there are no (valid) credentials available, let the user log in.
#     if not credentials or not credentials.valid:
#         if credentials and credentials.expired and credentials.refresh_token:
#             credentials.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             credentials = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(credentials, token)
#
#     service = build('sheets', 'v4', credentials=credentials)
#
#     # Call the Sheets API
#     sheet = service.spreadsheets()
#     result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                 range=SAMPLE_RANGE_NAME).execute()
#     values = result.get('values', [])
#
#     if not values:
#         print('No data found.')
#     else:
#         print('Name, Major:')
#         for row in values:
#             # Print columns A and E, which correspond to indices 0 and 4.
#             print('%s, %s' % (row[1], row[2]))
#
#
# if __name__ == '__main__':
#     main()

# import sys
# import re
# import os
# import json
# import urllib.request
# from operator import itemgetter
# from collections import OrderedDict
#
# if len(sys.argv) != 4:
#     sys.exit(1)
#
# path = sys.argv[1]
# path_output = sys.argv[2]
# name = sys.argv[3]
#
# file_csv = open(path_output, "a")
#
# dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
# for directory in dirs:
#     print("Directory = " + directory)
#
#     file_combat = open(os.path.join(path, directory, "combat.log"), "r")
#     print(str(os.path.join(path, directory, "combat.log")))
#     text = file_combat.read()
#     regex_combat2 = re.compile(r"===== Gameplay 'Pve_([^L']+)' started, map '([a-zA-Z_]+)' ======"
#                                r"(.*?)"
#                                r"===== Gameplay finish", re.DOTALL)
#
#     regex_combat = re.compile(r"===== Gameplay 'Pve_([^L']+)' started, map '([a-zA-Z_]+)' ======[^=]*?"
#                               r"Active battle started\..*?"
#                               r"(([0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}\|\s+player\s+[0123], uid [0-9]+, party [0-9]+, "
#                               r"nickname: [a-zA-Z0-9_]+\s*, team: [0-9]+, bot: [0-9]+, ur: [0-9]+"
#                               r", mmHash: [a-z0-9]+\s)+)"
#                               r"(.*?)"
#                               r"===== Gameplay finish", re.DOTALL)
#
#     matches_combat2 = [m.groups() for m in regex_combat2.finditer(text)]
#     matches_combat = [m.groups() for m in regex_combat.finditer(text)]
#
#     print(str(len(matches_combat2)))
#     print(str(len(matches_combat)))
#
#     file_combat.close()
import sys
import re
import os
import json
import urllib.request
from operator import itemgetter
from collections import OrderedDict

if len(sys.argv) != 4:
    sys.exit(1)

path = sys.argv[1]
path_output = sys.argv[2]
name = sys.argv[3]

file_csv = open(path_output, "a")

dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
for directory in dirs:
    print("Directory = " + directory)
    file_game = open(os.path.join(path, directory, "game.log"), "r")

    text = file_game.read()
    regex_game = re.compile(r"\"queueTag\": MetaPve_([a-zA-Z0-9]+)[0-9]+.*?"
                            r"\"botlist\": ([a-zA-Z0-9]+).*?"
                            r"Combat: ===== Gameplay 'Pve_([a-zA-Z_]+)' started, map '([a-zA-Z_]+)'.*?win reason: "
                            r"OBJECTIVE_COMPLETE, battle time: ([0-9.]+) sec.*?"
                            r"(Plastic|Scrap_Epic|Scrap_Rare|Platinum|Scrap_Common|Accumulators) +([0-9]+).*?"
                            r"score ([0-9]+),", re.DOTALL)
    matches_game = [m.groups() for m in regex_game.finditer(text)]
    file_game.close()

    file_combat = open(os.path.join(path, directory, "combat.log"), "r")
    text = file_combat.read()
    regex_combat2 = re.compile(r"===== Gameplay 'Pve_([^L']+)' started, map '([a-zA-Z_]+)' ======"
                               r"(.*?)"
                               r"===== Gameplay finish", re.DOTALL)

    regex_combat = re.compile(r"===== Gameplay 'Pve_([^L']+)' started, map '([a-zA-Z_]+)' ======[^=]*?"
                              r"Active battle started\..*?"
                              r"(([0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}\|\s+player\s+[0123], uid [0-9]+, party [0-9]+, "
                              r"nickname: [a-zA-Z0-9_]+\s*, team: [0-9]+, bot: [0-9]+, ur: [0-9]+"
                              r", mmHash: [a-z0-9]+\s)+)"
                              r"(.*?)"
                              r"===== Gameplay finish", re.DOTALL)

    matches_combat2 = [m.groups() for m in regex_combat2.finditer(text)]
    matches_combat = [m.groups() for m in regex_combat.finditer(text)]

    file_combat.close()

    if len(matches_game) != len(matches_combat2):
        print("ERROR: number of matches differs between logs (bug or log file structure changed)")
        print(str(len(matches_game)) + " != " + str(len(matches_combat)))

    else:
        if len(matches_game) != len(matches_combat):
            print(str(len(matches_game)) + " != " + str(len(matches_combat)))
            for i in range(len(matches_combat2)):
                print(
                    "Missing info about players from combat log - sometimes this happens - skip some info from output.")
                print("===================================== Difficulty = " + matches_game[i][0] + ", Opponents = " +
                      matches_game[i][1] + ", Type = " + matches_game[i][2] + ", Map = " + matches_game[i][3] +
                      ", Time = " + matches_game[i][4] + ", Resource = " + matches_game[i][
                          5] + ", Gained resources = " +
                      matches_game[i][6] + ", Points = " + matches_game[i][7])
                file_csv.write(
                    directory + "," + matches_game[i][2] + "," + matches_game[i][0] + "," + matches_game[i][3] + "," +
                    matches_game[i][1] + "," + matches_game[i][5] + "," + matches_game[i][6] + "," +
                    matches_game[i][4] + "," + matches_game[i][7] + ",,,,," + '\n')
        else:
            for i in range(len(matches_combat)):
                print("===================================== Difficulty = " + matches_game[i][0] + ", Opponents = " +
                      matches_game[i][1] + ", Type = " + matches_game[i][2] + ", Map = " + matches_game[i][3] +
                      ", Time = " + matches_game[i][4] + ", Resource = " + matches_game[i][5] + ", Gained resources = " +
                      matches_game[i][6] + ", Points = " + matches_game[i][7])

                regex_players = re.compile(
                    r"player\s+([0123]), uid [0-9]+, party [0-9]+, nickname: ([a-zA-Z0-9_]+)\s*, "
                    r"team: [0-9]+, bot: [0-9]+, ur: ([0-9]+),")
                matches_players = re.findall(regex_players, matches_combat[i][2])

                regex_score = re.compile(r"Score:\s+player:\s+([0-9]+),\s+nick:\s+([a-zA-Z0-9_]+),\s+Got:\s+([0-9]+),")
                matches_score = re.findall(regex_score, matches_combat[i][4])
                player_points = [0, 0, 0, 0]
                for mmm in matches_score:
                    player_points[int(mmm[0])] = player_points[int(mmm[0])] + int(mmm[2])
                print("Score count = " + str(len(matches_score)) + ", Type = " + matches_combat[i][0] +
                      ", Map = " + matches_combat[i][1])
                all_PS = 0
                PS = 0
                all_points = 0
                standing = 0
                players = {}
                for mm in matches_players:
                    print("Player = " + mm[0] + ", name = " + mm[1] + ", PS = " + mm[2] +
                          ", points = " + str(player_points[int(mm[0])]))
                    players[mm[1]] = player_points[int(mm[0])]
                    if name and mm[1] == name:
                        PS = mm[2]
                    all_PS = all_PS + int(mm[2])
                    all_points = all_points + player_points[int(mm[0])]
                if name:
                    players_ordered = OrderedDict(sorted(players.items(), key=lambda t: t[1], reverse=True))
                    for p in players_ordered:
                        standing = standing + 1
                        if p == name:
                            break

                print("My PS = " + str(PS) + ", My points = " + str(matches_game[i][7]) + ", All PS = " + str(
                    all_PS) + ", all points = " + str(all_points) +
                      ", Standing = " + str(standing))
                file_csv.write(
                    directory + "," + matches_game[i][2] + "," + matches_game[i][0] + "," + matches_game[i][3] + "," +
                    matches_game[i][1] + "," + matches_game[i][5] + "," + matches_game[i][6] + "," +
                    matches_game[i][4] + "," + matches_game[i][7] + "," + str(PS) + "," + str(standing) + "," +
                    str(all_PS) + "," + str(all_points) + "," + '\n')
                print("===================================== Results count = " + str(len(matches_game)) + ", " +
                      str(len(matches_combat)))
file_csv.close()

# Remove duplicites
lines_seen = list()
for line in open(path_output, "r"):
    if line not in lines_seen:
        lines_seen.append(line)

# Remove old prices (lines beginning with letters)
with open(path_output, "w") as f:
    for line in lines_seen:
        if not line[0].isalpha():
            f.write(line)

file_csv = open(path_output, "a")
# Add current resource prices
data = urllib.request.urlopen("https://crossoutdb.com/api/v1/item/785").read()
output = json.loads(data)
file_csv.write("Plastic,Plastic," + output[0]["formatSellPrice"] + "," + output[0]["formatBuyPrice"] + "\n")

data = urllib.request.urlopen("https://crossoutdb.com/api/v1/item/201").read()
output = json.loads(data)
file_csv.write("Scrap_Epic,Electonics," + str(float(output[0]["formatSellPrice"]) * 10) + "," +
               str(float(output[0]["formatBuyPrice"]) * 10) + "\n")

data = urllib.request.urlopen("https://crossoutdb.com/api/v1/item/43").read()
output = json.loads(data)
file_csv.write("Platinum,Copper," + output[0]["formatSellPrice"] + "," + output[0]["formatBuyPrice"] + "\n")

data = urllib.request.urlopen("https://crossoutdb.com/api/v1/item/106").read()
output = json.loads(data)
file_csv.write("Fuel,Fuel," + output[0]["formatSellPrice"] + "," + output[0]["formatBuyPrice"] + "\n")

data = urllib.request.urlopen("https://crossoutdb.com/api/v1/item/783").read()
output = json.loads(data)
file_csv.write("Battery,," + str(float(output[0]["formatSellPrice"]) * 10) + "," +
               str(float(output[0]["formatBuyPrice"]) * 10) + "\n")

data = urllib.request.urlopen("https://crossoutdb.com/api/v1/item/53").read()
output = json.loads(data)
file_csv.write("Scrap,Scrap Metal," + output[0]["formatSellPrice"] + "," + output[0]["formatBuyPrice"] + "\n")

data = urllib.request.urlopen("https://crossoutdb.com/api/v1/item/85").read()
output = json.loads(data)
file_csv.write("Wires,," + output[0]["formatSellPrice"] + "," + output[0]["formatBuyPrice"] + "\n")
file_csv.close()

input("Press something to exit...")
