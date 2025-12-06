import pytest

from src.category import Category
from src.products import Product


@pytest.fixture(autouse=True)
def reset_counters():
    """Сбрасывает статические счётчики перед каждым тестом."""
    Category.quantity_categories = 0
    Category.quantity_products = 0


def test_category_initialization():
    """Проверка корректной инициализации атрибутов категории."""
    p1 = Product(name="Банан", description="жёлтый", price=15.0, quantity=3)
    p2 = Product(name="Помидор", description="азербайджанский", price=3.0, quantity=10)
    category = Category(
        name="Еда", description="Продукты питания", list_products=[p1, p2]
    )

    assert category.name == "Еда"
    assert category.description == "Продукты питания"
    assert category.list_products == [p1, p2]


def test_category_counters_with_products():
    """Проверка счётчиков при передаче непустого списка продуктов."""
    p1 = Product(name="Банан", description="жёлтый", price=15.0, quantity=3)
    p2 = Product(name="Помидор", description="азербайджанский", price=3.0, quantity=10)
    Category(name="Еда", description="Продукты", list_products=[p1, p2])

    assert Category.quantity_categories == 1
    assert Category.quantity_products == 2


def test_category_counters_empty_list():
    """Счётчики при пустом списке продуктов."""
    Category(name="Пусто", description="Нет товаров", list_products=[])

    assert Category.quantity_categories == 1
    assert Category.quantity_products == 0


def test_category_counters_none_list():
    """Счётчики при list_products=None."""
    Category(name="Нет списка", description="Список не задан", list_products=None)

    assert Category.quantity_categories == 1
    assert Category.quantity_products == 0


def test_multiple_categories():
    """Проверка накопления счётчиков при создании нескольких категорий."""
    p1 = Product("Хлеб", "Белый", 50.0, 5)
    p2 = Product("Сыр", "Твёрдый", 300.0, 2)
    p3 = Product("Чай", "Зелёный", 200.0, 10)
    cat1 = Category("Бакалея", "Сухие товары", [p1, p2])
    cat2 = Category("Напитки", "Чай и кофе", [p3])
    assert Category.quantity_categories == 2
    assert Category.quantity_products == 3


def test_access_class_counters_via_instance():
    """Проверка, что экземпляр видит классовые счётчики."""
    p = Product("Молоко", "1л", 70.0, 4)
    cat = Category("Молочка", "Молочные продукты", [p])
    assert cat.quantity_categories == 1
    assert cat.quantity_products == 1
