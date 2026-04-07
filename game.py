# game.py

from gameparts.parts import Board
from gameparts.exceptions import FieldIndexError, InvalidMoveException


def save_result(result):
    """Сохраняет результат игры в файл results.txt."""
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:
        print(f'\nХод делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки (0, 1, 2): '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                
                column = int(input('Введите номер столбца (0, 1, 2): '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                
                # Попытка сделать ход
                game.make_move(row, column, current_player)
                
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.\n')
                continue
            
            except InvalidMoveException:
                print('Ячейка занята!')
                print('Введите другие координаты.\n')
                continue
            
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.\n')
                continue
            
            except Exception as e:
                print(f'Возникла ошибка: {e}\n')
            
            else:
                break

        game.display()
        
        # Проверка победы
        if game.check_win(current_player):
            result = f'Победили {current_player}.'
            print(f'\n🎉 {result} 🎉\n')
            save_result(result)
            running = False
        
        # Проверка ничьи
        elif game.is_board_full():
            result = 'Ничья!'
            print(f'\n🤝 {result} 🤝\n')
            save_result(result)
            running = False
        
        # Смена игрока
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()