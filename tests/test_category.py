from src.category import Category
from src.products import Product


def test_add_new_product():
    category = Category("Овощи", "Свежие овощи", [])
    new_product = Product("Морковь", "Оранжевая", 5.0, 4)

    category.add_product(new_product)

    expected_output = "Морковь, 5.0 руб. Остаток: 4 шт.\n"
    assert category.list_products == expected_output


def test_update_existing_product():
    initial_product = Product("Картошка", "Белая", 10.0, 5)
    category = Category("Овощи", "Свежие овощи", [initial_product])

    updated_product = Product("картошка", "Белая", 12.0, 3)
    category.add_product(updated_product)

    expected_output = "Картошка, 12.0 руб. Остаток: 8 шт.\n"
    assert category.list_products == expected_output

    total_quantity = sum(p.quantity for p in category._Category__list_products)
    assert total_quantity == 8

    stored_product = category._Category__list_products[0]
    assert stored_product.price == 12.0


def test_category_str_representation():
    product_1 = Product("Огурцы", "Свежие", 7.0, 2)
    product_2 = Product("Помидоры", "Сочные", 9.0, 3)
    category = Category("Овощи", "Свежие овощи", [product_1, product_2])

    assert str(category) == "Овощи, количество продуктов: 5 шт."
