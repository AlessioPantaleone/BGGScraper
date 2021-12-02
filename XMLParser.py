from lxml import etree

"""

parsed = etree.fromstring(coll)

for i in parsed:
    print i.items()

ids = [x.items()[1][1] for x in parsed]

[rating.attrib for rating in parsed.iter('rating')]

# try parsed.get('rating')?
"""


def boardgame_parse(game):

    print(game)
    tree_root = etree.XML(game)
    game_info = {}

    for attribute in tree_root:
        match (str(attribute.tag)):
            case "item":
                game_info['ID'] = attribute.attrib["id"]
                break
            case _:
                print(f"{attribute.tag} not interesting")
                break

        # match attribute["type"]
        # TODO Voto ID
        # TODO Voto Name
        # TODO Anno di pubblicazione
        # TODO Voto online
        # TODO Min giocatori
        # TODO Max giocatori
        # TODO Reccommended age
        # TODO Theme
        # TODO Mechanics
        # TODO Designers
        # TODO Artists
        # TODO Publishers

    print(game_info)


"""
    for item in tree_root.iter('item'):
        if item.attrib["type"] == "boardgame":
            game_info['ID'] = item.attrib["id"]

    for name in tree_root.iter('name'):
        if name.attrib["type"] == "primary":
            game_info['Name'] = name.attrib["value"]
"""