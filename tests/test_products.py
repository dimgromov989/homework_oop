from unittest.mock import patch

import pytest

from src.products import Product


@pytest.fixture
def sample_product():
    """Фикстура: стандартный продукт для тестов."""
    return Product("Телефон", "Смартфон", 1000.0, 5)


@pytest.fixture
def sample_product_data():
    """Фикстура: данные продукта в виде словаря."""
    return {
        "name": "Наушники",
        "description": "Беспроводные",
        "price": 500.0,
        "quantity": 10,
    }


def test_product_initialization(sample_product):
    """Тест инициализации продукта."""
    assert sample_product.name == "Телефон"
    assert sample_product.description == "Смартфон"
    assert sample_product.price == 1000.0
    assert sample_product.quantity == 5


def test_new_product_creation(sample_product_data):
    """Тест создания продукта через класс-метод new_product."""
    product = Product.new_product(sample_product_data)
    assert product.name == "Наушники"
    assert product.description == "Беспроводные"
    assert product.price == 500.0
    assert product.quantity == 10


@pytest.mark.parametrize(
    "new_price, expected_price, input_response",
    [
        (1200.0, 1200.0, None),
        (1000.0, 1000.0, None),
        (800.0, 800.0, "y"),
        (600.0, 1000.0, "n"),
        (600.0, 1000.0, "no"),
    ],
)
def test_price_setter_with_confirmation(
    sample_product, new_price, expected_price, input_response
):
    """Параметризованный тест сеттера цены с подтверждением понижения."""
    if input_response is not None:
        with patch("builtins.input", return_value=input_response):
            sample_product.price = new_price
    else:
        sample_product.price = new_price

    assert sample_product.price == expected_price


def test_price_setter_negative_or_zero_price(sample_product, capsys):
    """Тест установки недопустимой (≤0) цены."""
    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 1000.0

    sample_product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 1000.0


def test_new_product_with_missing_quantity():
    """Тест: если quantity отсутствует или None — должно быть 0."""
    data = {
        "name": "Часы",
        "description": "Механические",
        "price": 2000.0,
        "quantity": None,
    }
    product = Product.new_product(data)
    assert product.quantity == 0

    data2 = {
        "name": "Часы",
        "description": "Механические",
        "price": 2000.0,
    }
    product2 = Product.new_product(data2)
    assert product2.quantity == 0


def test_product_addition_returns_total_value():
    product_1 = Product("Плеер", "MP3", 100.0, 2)
    product_2 = Product("Колонки", "Стерео", 50.0, 1)

    result = product_1 + product_2

    assert result == "Сумма с учетом количества товаров на складе: 250.0 руб."


def test_product_addition_with_different_types_raises():
    product = Product("Плеер", "MP3", 100.0, 2)
    with pytest.raises(TypeError, match="невозможно сложить два объекта разных типов"):
        _ = product + "not a product"
