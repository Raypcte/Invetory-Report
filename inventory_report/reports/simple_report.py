from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate_old_date(list):
        date_list_fabrication = [
            d["data_de_fabricacao"]
            for d in list
        ]
        return min(date_list_fabrication)

    @staticmethod
    def generate_next_date(list):
        date_now = datetime.today().isoformat()
        date_list_validation = [
            d["data_de_validade"]
            for d in list
            if d["data_de_validade"] >= date_now
        ]
        return min(date_list_validation)

    @staticmethod
    def generate_max_products(list):
        contador_de_empresas = {}

        for produto in list:
            empresa = produto["nome_da_empresa"]
            if empresa in contador_de_empresas:
                contador_de_empresas[empresa] += 1
            else:
                contador_de_empresas[empresa] = 1

        return contador_de_empresas

    @staticmethod
    def generate(list):
        old_date_fabrication = SimpleReport.generate_old_date(list)
        next_date_validate = SimpleReport.generate_next_date(list)
        contador_de_empresas = SimpleReport.generate_max_products(list)
        company_max_products = max(
            contador_de_empresas, key=contador_de_empresas.get
        )

        return (
            f"Data de fabricação mais antiga: {old_date_fabrication}\n"
            f"Data de validade mais próxima: {next_date_validate}\n"
            f"Empresa com mais produtos: {company_max_products}"
        )
