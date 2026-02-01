import pytest

from src.lawngrass import LawnGrass


def test_lawngrass_initialization():
    grass = LawnGrass(
        "Lawn Grass",
        "Lawn grass for lawn",
        10.0,
        100,
        "USA",
        30,
        "green",
    )

    assert grass.name == "Lawn Grass"
    assert grass.description == "Lawn grass for lawn"
    assert grass.price == 10.0
    assert grass.quantity == 100
    assert grass.country == "USA"
    assert grass.germination_period == 30
    assert grass.color == "green"


def test_lawngrass_addition_returns_quantity_sum():
    grass_1 = LawnGrass(
        "Lawn Grass",
        "Lawn grass for lawn",
        10.0,
        100,
        "USA",
        30,
        "green",
    )
    grass_2 = LawnGrass(
        "Lawn Grass",
        "Lawn grass for lawn",
        10.0,
        50,
        "USA",
        30,
        "green",
    )

    assert grass_1 + grass_2 == 150


def test_lawngrass_addition_different_type_raises():
    grass = LawnGrass(
        "Lawn Grass",
        "Lawn grass for lawn",
        10.0,
        100,
        "USA",
        30,
        "green",
    )

    with pytest.raises(TypeError, match="невозможно сложить два объекта разных типов"):
        _ = grass + 1
