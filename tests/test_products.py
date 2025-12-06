def test_product(sample_product):
    assert sample_product.name == "Банан"
    assert sample_product.description == "жёлтый"
    assert sample_product.price == 15.0
    assert sample_product.quantity == 10


def test_category_creation(category_food):
    assert category_food.name == "Еда"
    assert category_food.description == "Продукты питания"
    assert len(category_food.list_products) == 2
    assert category_food.list_products[0].name == "Помидор"
    assert category_food.list_products[1].name == "Банан"
