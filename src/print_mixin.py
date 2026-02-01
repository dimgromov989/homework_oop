class PrintMixin:
    def __init__(self):
        """Инициализация объекта"""
        print(repr(self))

    def __repr__(self):
        """Стандартное строковое представление объекта"""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
