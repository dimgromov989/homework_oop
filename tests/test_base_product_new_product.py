from src.base_product import BaseProduct


def test_base_product_new_product_returns_none():
    assert BaseProduct.new_product() is None
