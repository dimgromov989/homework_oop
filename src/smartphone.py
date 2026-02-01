from src.products import Product


class Smartphone(Product):
    def __init__(
        self,
        name,
        description,
        price,
        quantity,
        efficiency,
        model,
        memory,
        color,
    ):
        """Инициализация объекта Smartphone"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Сложение двух объектов Smartphone, с учетом типа объекта"""
        if type(other) is Smartphone:
            return self.quantity + other.quantity
        raise TypeError("Ошибка: невозможно сложить два объекта разных типов")


if __name__ == "__main__":
    product1 = Product("Товар1", "Описание", 100, 5)
    product2 = Product("Товар2", "Описание", 200, 3)
    smartphone = Smartphone(
        "iPhone",
        "Описание",
        1000,
        1,
        "A15",
        "13",
        128,
        "black",
    )

    print(product1 + product2)
    print(product1 + smartphone)
