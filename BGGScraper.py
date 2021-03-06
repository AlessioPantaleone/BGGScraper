import sys
import traceback

import requests
import time

import FileHelper
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

idToQuery = FileHelper.get_input_from_file("Input.txt")
#idToQuery = [45,199025]   #TO TEST ONLY

gamesData = []
skippedIDs = []

for identifier in idToQuery:
    boardgameurl = 'http://www.boardgamegeek.com/xmlapi2/thing?type=boardgame&stats=1&id=' + str(identifier)
    Logger.info(f"Requesting game with id: {identifier}")
    r = requests.get(boardgameurl)
    for i in range(5):
        r = requests.get(boardgameurl)
        if r.status_code == 200:
            Logger.info(f"HTTP Get Request Successful")
            try:
                parsedDictionary = XMLParser.boardgame_parse2(r.content)
                if parsedDictionary["Name"] == "N/A":
                    raise Exception
                gamesData.append(parsedDictionary)
                Logger.info(f"Game {identifier} parsed successfully")
                break
            except Exception as e:
                Logger.debug(f"Critical Failure for parsing game {identifier}, trying again as an expansion")
                boardgameurl = 'http://www.boardgamegeek.com/xmlapi2/thing?type=boardgameexpansion&stats=1&id='\
                               + str(identifier)
                if i == 4:
                    Logger.error(traceback.format_exc())
                    skippedIDs.append(identifier)
        else:
            Logger.error(f"Failed to retrieve game with id: {identifier}")
            time.sleep(5)
            i += 1
            continue

time.sleep(0.5)

Logger.info(f"Finished Downloading and parsing {len(gamesData)} games")
if len(skippedIDs) != 0:
    Logger.critical(f"Skipped {len(skippedIDs)} identifiers")
    for item in skippedIDs:
        Logger.critical(f"Skipped the game with id: {item}")

FileHelper.export_data_to_excel(gamesData, "NuoviGiochiPLD.xlsx")



