from src.products import Product


class Category:
    name: str
    description: str
    quantity_categories = 0
    quantity_products = 0

    def __init__(self, name, description, list_products: list):
        self.name = name
        self.description = description
        self.__list_products = list_products if list_products else []
        Category.quantity_categories += 1
        Category.quantity_products += sum(
            product.quantity for product in self.__list_products
        )

    def add_product(self, product: Product):
        for item in self.__list_products:
            if item.name.lower() == product.name.lower():
                item.quantity += product.quantity
                item.price = max(item.price, product.price)
                return
        self.__list_products.append(product)
        Category.quantity_products += product.quantity

    @property
    def list_products(self):
        """Геттер для безопасного чтения списка товаров (только для чтения)."""
        str_for_list = ""
        for product in self.__list_products:
            str_for_list += (
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт\n"
            )
        return str_for_list
