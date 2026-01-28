class Product:
    name: str
    description: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity if quantity else 0

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            total_quantity = (self.quantity * self.__price) + (
                other.quantity * other.__price
            )
            return f"Сумма с учетом количества товаров на складе: {float(total_quantity)} руб."

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            product_data.get("name"),
            product_data.get("description"),
            product_data.get("price"),
            product_data.get("quantity"),
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if value < self.__price:
            user_input = (
                input("Вы действительно хотите понизить цену? (y/n): ").strip().lower()
            )
            if user_input != "y":
                print("Изменение цены отменено")
                return
        self.__price = value
