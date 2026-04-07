import pygame
from gameparts.parts import Board

# Инициализировать библиотеку Pygame.
pygame.init()

# Создать окно размером 600x600.
screen = pygame.display.set_mode((600, 600))
# Задать окну заголовок.
pygame.display.set_caption('Крестики-нолики')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Заливаем фон белым
screen.fill(WHITE)

# Рисуем линии сетки
pygame.draw.line(screen, BLACK, (200, 0), (200, 600), 5)
pygame.draw.line(screen, BLACK, (400, 0), (400, 600), 5)
pygame.draw.line(screen, BLACK, (0, 200), (600, 200), 5)
pygame.draw.line(screen, BLACK, (0, 400), (600, 400), 5)

# Отобразить сетку
pygame.display.update()

# Игровые переменные
game = Board()
current_player = 'X'
running = True
game_over = False

# Функция для рисования крестика
def draw_x(row, col):
    x = col * 200
    y = row * 200
    pygame.draw.line(screen, RED, (x + 30, y + 30), (x + 170, y + 170), 8)
    pygame.draw.line(screen, RED, (x + 170, y + 30), (x + 30, y + 170), 8)

# Функция для рисования нолика
def draw_o(row, col):
    x = col * 200 + 100
    y = row * 200 + 100
    pygame.draw.circle(screen, BLUE, (x, y), 70, 8)

# Главный цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Клик мыши
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # Получаем координаты
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // 200
            col = mouse_x // 200
            
            # Проверяем пустая ли клетка
            if game.board[row][col] == ' ':
                # Делаем ход
                game.make_move(row, col, current_player)
                
                # Рисуем символ
                if current_player == 'X':
                    draw_x(row, col)
                else:
                    draw_o(row, col)
                
                pygame.display.update()
                
                # Проверяем победу
                if game.check_win(current_player):
                    # Рисуем сообщение о победе
                    font = pygame.font.Font(None, 74)
                    text = font.render(f'{current_player} WIN!', True, BLACK)
                    text_rect = text.get_rect(center=(300, 300))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    game_over = True
                
                # Проверяем ничью
                elif game.is_board_full():
                    font = pygame.font.Font(None, 74)
                    text = font.render('DRAW!', True, BLACK)
                    text_rect = text.get_rect(center=(300, 300))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    game_over = True
                
                # Меняем игрока
                current_player = 'O' if current_player == 'X' else 'X'

# Деинициализирует все модули pygame
pygame.quit()
