import pytest

from src.smartphone import Smartphone


def test_smartphone_initialization():
    smartphone = Smartphone(
        "iPhone",
        "Описание",
        1000.0,
        2,
        "A15",
        "13",
        128,
        "black",
    )

    assert smartphone.name == "iPhone"
    assert smartphone.description == "Описание"
    assert smartphone.price == 1000.0
    assert smartphone.quantity == 2
    assert smartphone.efficiency == "A15"
    assert smartphone.model == "13"
    assert smartphone.memory == 128
    assert smartphone.color == "black"


def test_smartphone_addition_returns_quantity_sum():
    smartphone_1 = Smartphone(
        "iPhone",
        "Описание",
        1000.0,
        2,
        "A15",
        "13",
        128,
        "black",
    )
    smartphone_2 = Smartphone(
        "iPhone",
        "Описание",
        1000.0,
        3,
        "A15",
        "13",
        128,
        "black",
    )

    assert smartphone_1 + smartphone_2 == 5


def test_smartphone_addition_different_type_raises():
    smartphone = Smartphone(
        "iPhone",
        "Описание",
        1000.0,
        2,
        "A15",
        "13",
        128,
        "black",
    )

    with pytest.raises(TypeError, match="невозможно сложить два объекта разных типов"):
        _ = smartphone + "not a smartphone"
