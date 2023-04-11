import csv
import json
import xmltodict
from pathlib import Path
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def read_csv(path) -> list[dict]:
        with open(path, mode='r') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            lista_dict = []
            for linha in leitor_csv:
                lista_dict.append(linha)
            return lista_dict

    @staticmethod
    def read_json(path) -> list[dict]:
        with open(path) as arquivo_json:
            leitor_json = json.load(arquivo_json)
            lista_dict = [dict(item) for item in leitor_json]
            return lista_dict

    @staticmethod
    def read_xml(path) -> list[dict]:
        with open(path) as file:
            return xmltodict.parse(file.read())['dataset']['record']

    @staticmethod
    def validate_file(path) -> list[dict]:
        extensao = Path(path).suffix
        lista_dict = list()
        if extensao == ".json":
            lista_dict = Inventory.read_json(path)
        elif extensao == ".csv":
            lista_dict = Inventory.read_csv(path)
        elif extensao == ".xml":
            lista_dict = Inventory.read_xml(path)
        return lista_dict

    @staticmethod
    def import_data(path, type) -> list[dict]:
        lista_dict = Inventory.validate_file(path)
        if type == "simples":
            return SimpleReport.generate(lista_dict)
        elif type == "completo":
            return CompleteReport.generate(lista_dict)
