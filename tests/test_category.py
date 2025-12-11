from src.category import Category
from src.products import Product


def test_add_new_product():
    category = Category("Овощи", "Свежие овощи", [])
    new_product = Product("Морковь", "Оранжевая", 5.0, 4)

    category.add_product(new_product)

    expected_output = "Морковь, 5.0 руб. Остаток: 4 шт"
    assert category.list_products.strip() == expected_output


def test_update_existing_product():
    initial_product = Product("Картошка", "Белая", 10.0, 5)
    category = Category("Овощи", "Свежие овощи", [initial_product])

    updated_product = Product("Картошка", "Белая", 12.0, 3)
    category.add_product(updated_product)

    expected_output = "Картошка, 12.0 руб. Остаток: 8 шт"
    assert category.list_products.strip() == expected_output

    total_quantity = sum(p.quantity for p in category._Category__list_products)
    assert total_quantity == 8
