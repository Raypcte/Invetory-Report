from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data: list[dict]) -> str:
        simple_result = SimpleReport.generate(data)
        contador_de_empresas = SimpleReport.generate_max_products(data)
        complex_result = ""
        for key in contador_de_empresas.keys():
            complex_result += f"- {key}: {contador_de_empresas[key]}\n"

        return (
            f"{simple_result}\n"
            "Produtos estocados por empresa:\n"
            f"{complex_result}")
