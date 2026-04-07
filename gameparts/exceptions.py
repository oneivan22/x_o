# gameparts/exceptions.py

class FieldIndexError(IndexError):
    """Исключение для выхода за границы игрового поля."""
    
    def __str__(self):
        return 'Введено значение за границами игрового поля'


class InvalidMoveException(Exception):
    """Выбрасывается, когда ход невозможен (клетка занята)."""
    
    def __str__(self):
        return 'Эта клетка уже занята!'