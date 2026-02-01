from src.products import Product


class LawnGrass(Product):
    def __init__(
        self,
        name,
        description,
        price,
        quantity,
        country,
        germination_period,
        color,
    ):
        """Инициализация объекта LawnGrass"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Сложение объектов LawnGrass"""
        if type(other) is LawnGrass:
            return self.quantity + other.quantity
        raise TypeError("Ошибка: невозможно сложить два объекта разных типов")


if __name__ == "__main__":
    lawn_grass = LawnGrass(
        "Lawn Grass",
        "Lawn grass for lawn",
        10,
        100,
        "USA",
        30,
        "green",
    )
    lawn_grass_1 = LawnGrass(
        "Lawn Grass",
        "Lawn grass for lawn",
        10,
        100,
        "USA",
        30,
        "green",
    )
    print(lawn_grass + lawn_grass_1)
