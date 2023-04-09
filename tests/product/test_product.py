from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "action figure",
        "Yuyu Empresa",
        "09/04/2023",
        "09/04/2024",
        "4277",
        "Armazém de colecionáveis")

    assert produto.id == 1
    assert produto.nome_do_produto == "action figure"
    assert produto.nome_da_empresa == "Yuyu Empresa"
    assert produto.data_de_fabricacao == "09/04/2023"
    assert produto.data_de_validade == "09/04/2024"
    assert produto.numero_de_serie == "4277"
    assert produto.instrucoes_de_armazenamento == "Armazém de colecionáveis"
