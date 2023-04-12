from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Baton",
        "Doce Sabor Ltda",
        "01-10-2021",
        "01-10-2023",
        "123",
        "em local fresco e seco"
    )

    assert str(product) == (
        'O produto Baton'
        ' fabricado em 01-10-2021'
        ' por Doce Sabor Ltda com validade'
        ' até 01-10-2023'
        ' precisa ser armazenado em local fresco e seco.'
    )
