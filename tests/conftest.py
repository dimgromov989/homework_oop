import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def sample_product():
    return Product(name="Банан", description="жёлтый", price=15.0, quantity=10)


@pytest.fixture
def category_food():
    return Category(
        name="Еда",
        description="Продукты питания",
        products=[
            Product(
                name="Помидор", description="азербайджанский", price=3.0, quantity=10
            ),
            Product(name="Банан", description="жёлтый", price=15.0, quantity=3),
        ],
    )
