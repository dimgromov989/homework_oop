from src.print_mixin import PrintMixin


class DummyProduct(PrintMixin):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()


def test_print_mixin_repr():
    obj = DummyProduct("Товар", "Описание", 10.0, 2)

    assert repr(obj) == "DummyProduct(Товар, Описание, 10.0, 2)"


def test_print_mixin_init_prints_repr(capsys):
    _ = DummyProduct("Товар", "Описание", 10.0, 2)

    captured = capsys.readouterr()
    assert "DummyProduct(Товар, Описание, 10.0, 2)" in captured.out
