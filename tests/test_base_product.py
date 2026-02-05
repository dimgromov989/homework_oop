import pytest

from src.base_product import BaseProduct


def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        BaseProduct()
