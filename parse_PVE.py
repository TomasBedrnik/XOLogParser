import re
from collections import OrderedDict


def parse_PVE_game_log(path):
    data = dict()
    file = open(path, "r")
    text = file.read()
    regex = re.compile(r"====== starting level.*?"
                       r"\{.*?"
                       r"\"queueTag\": MetaPve_([a-zA-Z0-9]+)[0-9]+.*?"
                       r"\"botlist\": ([a-zA-Z0-9]+).*?"
                       r"\}.*?"
                       r"([0-9]+:[0-9]+:[0-9]+\.[0-9]+)         \| Combat: ===== Gameplay 'Pve_([a-zA-Z_]+)' started, "
                       r"map '([a-zA-Z_]+)'.*?"
                       r"Combat: ===== Gameplay finish, reason: (.*?),.*?battle time: ([0-9.]+) sec.*?"
                       r"Gameplay statistic. gameResult '(.*?)'.*?"
                       r"(Plastic|Scrap_Epic|Scrap_Rare|Platinum|Scrap_Common|Accumulators) +([0-9]+).*?"
                       r"score ([0-9]+),", re.DOTALL)

    # split first to speed up the regex
    parts = text.split("====== starting level")
    for p in parts:
        p = "====== starting level" + p
        matches = [m.groups() for m in regex.finditer(p)]
        # print(type(matches))
        for m in matches:
            # print(type(m))
            # print("Time = " + m[2], end=", ")
            # print("Difficulty = " + m[0], end=", ")
            # print("Opponents = " + m[1], end=", ")
            # print("Type = " + m[3], end=", ")
            # print("Map = " + m[4], end=", ")
            # print("Finish reason = " + m[5], end=", ")
            # print("Time [s] = " + m[6], end=", ")
            # print("Result = " + m[7], end=", ")
            # print("Resource type = " + m[8], end=", ")
            # print("Gained resources = " + m[9], end=", ")
            # print("Points = " + m[10], end=", ")
            # print(" ")
            if m[7] == "victory":
                data[m[2]] = (m[0], m[1], m[3], m[4], m[6], m[8], m[9], m[10])
    return data
    file.close()


def parse_PVE_combat_log(path, name):
    data = dict()
    file = open(path, "r")
    text = file.read()
    regex = re.compile(r"([0-9]+:[0-9]+:[0-9]+\.[0-9]+)\| ===== Gameplay 'Pve_([^L']+)' started, "
                       r"map '([a-zA-Z_]+)' ======[^=]*?"
                       r"Active battle started\.[^=]*?"
                       r"(([0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}\|\s+player\s+[0123], uid [0-9]+, party [0-9]+, "
                       r"nickname: [a-zA-Z0-9_]+\s*, team: [0-9]+, bot: [0-9]+, ur: [0-9]+"
                       r", mmHash: [a-z0-9]+\s)+)"
                       r"([^=]*?)"
                       r"===== Gameplay finish", re.DOTALL)
    matches = [m.groups() for m in regex.finditer(text)]

    regex_players = re.compile(
        r"player\s+([0123]), uid [0-9]+, party [0-9]+, nickname: ([a-zA-Z0-9_]+)\s*, "
        r"team: [0-9]+, bot: [0-9]+, ur: ([0-9]+),")

    # print(type(matches))
    for m in matches:
        matches_players = re.findall(regex_players, m[3])

        regex_score = re.compile(r"Score:\s+player:\s+([0-9]+),\s+nick:\s+([a-zA-Z0-9_]+),\s+Got:\s+([0-9]+),")
        matches_score = re.findall(regex_score, m[5])
        player_points = [0, 0, 0, 0]
        for mmm in matches_score:
            player_points[int(mmm[0])] = player_points[int(mmm[0])] + int(mmm[2])
        # print("Score count = " + str(len(matches_score)) + ", Type = " + m[1] +
        #       ", Map = " + m[2])
        all_PS = 0
        PS = 0
        all_points = 0
        standing = 0
        players = {}
        for mm in matches_players:
            # print("Player = " + mm[0] + ", name = " + mm[1] + ", PS = " + mm[2] +
            #       ", points = " + str(player_points[int(mm[0])]))
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

        # print(len(m))
        # print("Time = " + m[0], end=", ")
        # print("Type = " + m[1], end=", ")
        # print("Map = " + m[2], end=", ")
        # print("All PS = " + str(all_PS), end=", ")
        # print("My PS = " + str(PS), end=", ")
        # print("all points = " + str(all_points), end=", ")
        # print("Standing = " + str(standing), end=", ")
        # print("Players:", end=" ")
        data_players = list()
        for p in matches_players:
            # print(p[1] + "[" + p[2] + "]: " + str(player_points[int(p[0])]), end=", ")
            data_players.append((p[1], p[2], player_points[int(p[0])]))
        # print(" ")
        data[m[0]] = (m[1], m[2], all_PS, PS, all_points, standing, data_players)
    return data
    file.close()
