import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type) -> list[dict]:
        with open(path, mode='r') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            lista_dict = []
            for linha in leitor_csv:
                lista_dict.append(linha)
            if type == "simples":
                return SimpleReport.generate(lista_dict)
            elif type == "completo":
                return CompleteReport.generate(lista_dict)
