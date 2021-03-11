import json
import urllib.request


def read_price(item):
    table_data = {
       "Plastic": 785,
       "Electonics": 201,
       "Copper": 43,
       "Fuel": 106,
       "Battery": 783,
       "Scrap Metal": 53,
       "Wires": 85
    }
    table_multiplier = {
       "Plastic": 1,
       "Electonics": 10,
       "Copper": 1,
       "Fuel": 1,
       "Battery": 1,
       "Scrap Metal": 1,
       "Wires": 1
    }

    if item in table_multiplier.keys() and item in table_data.keys():
        url = "https://crossoutdb.com/api/v1/item/"+str(table_data[item])
        data = urllib.request.urlopen(url).read()
        output = json.loads(data)
        if len(output) > 0 and "formatBuyPrice" in output[0].keys():
            return float(output[0]["formatSellPrice"]) * table_multiplier[item], \
                   float(output[0]["formatBuyPrice"]) * table_multiplier[item]
        else:
            return 0, 0
    else:
        return 0, 0
