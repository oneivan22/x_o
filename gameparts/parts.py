# gameparts/parts.py

from gameparts.exceptions import InvalidMoveException


class Board:
    """Класс, который описывает игровое поле."""
    
    field_size = 3
    
    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)] for _ in range(self.field_size)
        ]
    
    def make_move(self, row, col, player):
        """Размещает символ игрока на указанной клетке."""
        if self.board[row][col] != ' ':
            raise InvalidMoveException
        self.board[row][col] = player
    
    def display(self):
        """Отрисовывает игровое поле в терминале."""
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    
    def is_board_full(self):
        """Проверяет, заполнено ли поле полностью (ничья)."""
        for row in range(self.field_size):
            for col in range(self.field_size):
                if self.board[row][col] == ' ':
                    return False
        return True
    
    def check_win(self, player):
        """Проверяет, выиграл ли указанный игрок."""
        # Проверка по вертикали и горизонтали
        for i in range(self.field_size):
            if (all([self.board[i][j] == player for j in range(self.field_size)]) or
                    all([self.board[j][i] == player for j in range(self.field_size)])):
                return True
        # Проверка по диагонали
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True
        return False
    
    def __str__(self):
        """Возвращает строковое описание объекта игрового поля."""
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )