import logging

from lxml import etree


def boardgame_parse(game):
    tree_root = etree.XML(game)

    game_info = {"id": tree_root[0].get("id"), "Mechanics": [], "Designers": [], "Artists": [], "Publishers": []}

    for item in tree_root[0]:
        match (str(item.tag)):
            case "name":
                if item.attrib["type"] == "primary":
                    game_info['Name'] = item.attrib["value"]
            case "image":
                game_info['Image_Link'] = item  # TODO Retrieve image
            case "yearpublished":
                game_info['PublicationYear'] = item.attrib["value"]
            case "statistics":
                game_info['BGG_Score'] = round(float(item[0][1].get("value")), 1)
                try:
                    currentmax = 0
                    for element in item.iter("rank"):
                        if int(element.attrib["value"]) > currentmax and element.attrib["type"] == "family":
                            currentmax = int(element.attrib["value"])
                            game_info['Category'] = element.attrib["name"]
                except:
                    logging.debug(f"missing current category max value far {game_info['Name']}")
            case "minplayers":
                game_info['MinPlayers'] = item.attrib["value"]
            case "maxplayers":
                game_info['MaxPlayers'] = item.attrib["value"]
            case "playingtime":
                game_info['PlayingTime'] = item.attrib["value"]
            case "minage":
                game_info['MinAge'] = item.attrib["value"]
            case "link":
                if item.attrib["type"] == "boardgamemechanic":
                    game_info['Mechanics'].append(item.attrib["value"])
                if item.attrib["type"] == "boardgamedesigner":
                    game_info['Designers'].append(item.attrib["value"])
                if item.attrib["type"] == "boardgameartist":
                    game_info['Artists'].append(item.attrib["value"])
                if item.attrib["type"] == "boardgamepublisher":
                    game_info['Publishers'].append(item.attrib["value"])

    return game_info


def boardgame_parse2(game):

    tree_root = etree.XML(game)

    game_info = {"Name": "N/A",
                 "id": "N/A",
                 "Image_Link": "N/A",
                 "PublicationYear": "N/A",
                 "BGG_Score": "N/A",
                 "Category": "N/A",
                 "MinPlayers": "N/A",
                 "MaxPlayers": "N/A",
                 "PlayingTime": "N/A",
                 "MinAge": "N/A",
                 "Mechanics": [],
                 "Designers": [],
                 "Artists": [],
                 "Publishers": []}

    for item in tree_root.find("item"):
        if item.attrib["type"] == "boardgame" or item.attrib["type"] == "boardgameexpansion":
            game_info['id'] = item.attrib["value"]
        if item.attrib["type"] == "boardgameexpansion":
            game_info['Name'] = "- Expansion"
        if item.attrib["type"] == "":
            game_info[''] = ""
        if item.attrib["type"] == "":
            game_info[''] = ""
        if item.attrib["type"] == "":
            game_info[''] = ""
        if item.attrib["type"] == "":
            game_info[''] = ""
        if item.attrib["type"] == "":
            game_info[''] = ""
        if item.attrib["type"] == "":
            game_info[''] = ""
        if item.attrib["type"] == "":
            game_info[''] = ""
        if item.attrib["type"] == "":
            game_info[''] = ""
        if item.attrib["type"] == "":
            game_info[''] = ""
        if item.attrib["type"] == "":
            game_info[''] = ""
        if item.attrib["type"] == "":
            game_info[''] = ""
        if item.attrib["type"] == "":
            game_info[''] = ""

    return game_info

