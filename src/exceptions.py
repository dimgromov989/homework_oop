class MyValueError(Exception):
    def __init__(self, *args, **kwargs):
        """Инициализация для *args"""
        self.message = (
            args[0] if args else "Товар с нулевым количеством не может быть добавлен"
        )

    def __str__(self):
        """Вызов метода, для вывода сообщения"""
        return self.message
