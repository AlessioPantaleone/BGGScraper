import requests
import time
import LoggerHelper
import XMLParser

"""
https://boardgamegeek.com/wiki/page/BGG_XML_API2
EXAMPLE: https://www.boardgamegeek.com/xmlapi2/thing?type=boardgame&stats=1&id=45
"""

# Returns a list that contains XML objects for the queried games
# Multiple attempts at getting the items

Logger = LoggerHelper.get_complete_logger("ScraperLog")
Logger.info("Logging started")

# idToQuery = TODO
idToQuery = [45]
gameData = []
for identifier in idToQuery:
    boardgameurl = 'http://www.boardgamegeek.com/xmlapi2/thing?type=boardgame&stats=1&id=' + str(identifier)
    Logger.info(f"Requesting game with id: {identifier}")
    r = requests.get(boardgameurl)
    for i in range(5):
        r = requests.get(boardgameurl)
        if r.status_code == 200:
            Logger.info(f"Request Successful")
            gameData.append(r.content)
            break
        else:
            Logger.error(f"Failed to retrieve game with id: {identifier}")
            time.sleep(5)
            i += 1
            continue

time.sleep(0.5)

XMLParser.boardgame_parse((gameData[0]))
