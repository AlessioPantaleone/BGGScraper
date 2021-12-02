from lxml import etree
import pprint


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
                currentmax = 0
                for element in item.iter("rank"):
                    if int(element.attrib["value"]) > currentmax and element.attrib["type"] == "family":
                        currentmax = int(element.attrib["value"])
                        game_info['Category'] = element.attrib["name"]
            case "minplayers":
                game_info['MinPlayers'] = item.attrib["value"]
            case "maxplayers":
                game_info['MaxPlayers'] = item.attrib["value"]
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

