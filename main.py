from src.category import Category
from src.products import Product


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 1)
    product4 = Product("Xiaomi Redmi Note 1133", "1024GB, Черный", 31000.0, 1)

    category1 = Category(
        "Смартфоны",
        (
            "Смартфоны, как средство не только коммуникации, но и получения "
            "дополнительных функций для удобства жизни"
        ),
        [product1, product2, product3],
    )

    print(category1.list_products)
    category1.add_product(product4)
    print(category1.list_products)
    print(product1 + product4)
