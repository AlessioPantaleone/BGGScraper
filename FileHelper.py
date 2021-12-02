import csv
import re
from openpyxl import Workbook


def get_input_from_file(filename: str):
    with open(filename, 'r') as fd:
        reader = csv.reader(fd)
        data = []
        for row in reader:
            data.append(re.findall(r'\d+', str(row))[0])
    return data


def export_data_to_excel(data, filename: str):
    workbook = Workbook()

    sheet = workbook.create_sheet("Cipolla")
    for i, array in enumerate(data):
        for j, cell in enumerate(array):
            if cell == "Mechanics" or cell == "Designers" or cell == "Artists" or cell == "Publishers":
                new_value = ""
                for name in array[cell]:
                    new_value += f"{name}\n"
                sheet.cell(row=i + 1, column=j + 1).value = new_value
            else:
                sheet.cell(row=i + 1, column=j + 1).value = str(array[cell])

    sheet = workbook.create_sheet("Peperone")

    for i, array in enumerate(data):
        sheet.cell(row=i + 1, column=1).value = array["Name"]
        sheet.cell(row=i + 1, column=2).value = f"https://boardgamegeek.com/boardgame/{array['id']}"
        sheet.cell(row=i + 1, column=6).value = array["PublicationYear"]
        sheet.cell(row=i + 1, column=10).value = array["BGG_Score"]
        sheet.cell(row=i + 1, column=11).value = array["MinPlayers"]
        sheet.cell(row=i + 1, column=12).value = array["MaxPlayers"]
        sheet.cell(row=i + 1, column=13).value = array["MinAge"]
        sheet.cell(row=i + 1, column=14).value = array["PlayingTime"]

        try:
            sheet.cell(row=i + 1, column=15).value = array["Category"]
        except KeyError:
            sheet.cell(row=i + 1, column=15).value = "Not Categorized"

        new_value = ""
        for j, name in enumerate(array["Mechanics"]):
            if j < 3:
                new_value += f"{name}\n"
        sheet.cell(row=i + 1, column=16).value = new_value

        new_value = ""
        for j, name in enumerate(array["Designers"]):
            if j < 3:
                new_value += f"{name}\n"
        sheet.cell(row=i + 1, column=17).value = new_value

        new_value = ""
        for j, name in enumerate(array["Artists"]):
            if j < 3:
                new_value += f"{name}\n"
        sheet.cell(row=i + 1, column=18).value = new_value

        new_value = ""
        for j, name in enumerate(array["Publishers"]):
            if j < 3:
                new_value += f"{name}\n"
        sheet.cell(row=i + 1, column=19).value = new_value

    workbook.save(filename=filename)
