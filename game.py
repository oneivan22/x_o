# game.py - самая простая графическая версия

import pygame
from gameparts.parts import Board

# Настройки
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 200

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Запуск pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-нолики')
screen.fill(WHITE)

# Рисуем сетку
for i in range(1, 3):
    pygame.draw.line(screen, BLACK, (CELL_SIZE * i, 0), (CELL_SIZE * i, HEIGHT), 5)
    pygame.draw.line(screen, BLACK, (0, CELL_SIZE * i), (WIDTH, CELL_SIZE * i), 5)

pygame.display.update()

# Игровые переменные
game = Board()
current_player = 'X'
running = True
game_over = False

# Главный цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # Получаем координаты клика
            x, y = pygame.mouse.get_pos()
            row = y // CELL_SIZE
            col = x // CELL_SIZE
            
            # Проверяем, можно ли сходить
            if game.board[row][col] == ' ':
                # Делаем ход
                game.make_move(row, col, current_player)
                
                # Рисуем X или O
                if current_player == 'X':
                    # Рисуем крестик
                    x1 = col * CELL_SIZE + 30
                    y1 = row * CELL_SIZE + 30
                    x2 = (col + 1) * CELL_SIZE - 30
                    y2 = (row + 1) * CELL_SIZE - 30
                    pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 8)
                    pygame.draw.line(screen, RED, (x2, y1), (x1, y2), 8)
                else:
                    # Рисуем нолик
                    center = (col * CELL_SIZE + 100, row * CELL_SIZE + 100)
                    pygame.draw.circle(screen, BLUE, center, 70, 8)
                
                pygame.display.update()
                
                # Проверка победы
                if game.check_win(current_player):
                    print(f'Победил {current_player}!')
                    game_over = True
                
                # Проверка ничьи
                elif game.is_board_full():
                    print('Ничья!')
                    game_over = True
                
                # Меняем игрока
                current_player = 'O' if current_player == 'X' else 'X'

pygame.quit()
