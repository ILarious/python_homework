from random import choice
from types import function
from typing import List


battle_field: List[int] = list(range(1, 10))
total: List[int] = [0, 0]


# start_game - функция начало игры
def start_game() -> None:
    print(f'\n{"-" * 34} TIC_TAC_TOE {"-" * 33}')
    print('Бро, ты словил попадос на мега-супер игру - KRESTιKι N0LιKI\n')
    print('Одна из игр, в которые играют два игрока на квадратной сетке 3 x 3.\n'
          'Каждый игрок заселяет клетку в свои ходы, стараясь поставить три \n'
          'одинаковых метки по вертикали, горизонтали или диагонали. \n'
          'Один игрок использует Крестик (X), а другой использует Ноль (0).')
    print(f'{"-" * 80}')

    global player_1
    global player_2

    player_1: str = input('Введите имя игрока №1:\n'
                 '--> ')

    player_2: str = input('Введите имя игрока №2:\n'
                 '--> ')

    print(f'{"-"*80}')


# giving_X0 - функция рандомно присваивает игрокам Х и 0
def giving_X0(player_1: str, player_2: str) -> tuple:
    global chr_1
    global chr_2
    chr_1: str = choice('X0')
    print(f'{player_1}, тебе присвоен {chr_1}')

    if 'X' in chr_1:
        chr_2: str = '0'
        print(f'{player_2}, а тебе присвоен {chr_2}')

    else:
        chr_2: str = 'X'
        print(f'{player_2}, а тебе присвоен {chr_2}')

    return chr_1, chr_2


# show_battle_field - функция показывает поле сражение
def show_battle_field(field: list) -> None:
    print(f'{"-" * 80}')
    for i in range(3):
        print(f'  {field[0+i*3]} | {field[1+i*3]} | {field[2+i*3]}  ')
        if i < 2:
            print(f'----+---+----')
    print()


# data_handler - функция обрабатывает данные на валидность и
# заполняет клетку ходом игрока
def data_handler(player: str, chr_: str) -> None:
    while True:
        try:
            print(f'{player}, выбери позицию для {chr_}')
            choice: int = int(input('--> '))

        except:
            print('Это не число')
            continue

        if 1 <= choice <= 9:

            if not battle_field[choice - 1] in ['X', '0']:
                battle_field[choice - 1] = chr_
                break
            else:
                print('Эта позиция уже занята!')

        else:
            print('Бро, введи число от 1 до 9.')


# check_win - функция проверят, выиграл игрок или нет
def check_win(field: list) -> bool:
    win_true: List[tuple[int, ...]] = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    for i in win_true:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]
    return False


# end_game - функция завершает или возобновляет игру
def end_game() -> None:
    try:
        print(f'{"-" * 80}')
        choice: int = int(input('Продолжить игру - 1\n'
                           'Нет - 2\n--> '))
        print(f'{"-" * 80}')

        if choice == 1:
            global battle_field
            battle_field = list(range(1, 10))
            game(battle_field)

        elif choice == 2:
            print(f'Окончательный счет - {total[0]}:{total[1]}\n'
                  f'{" " * 31} END GAME {" " * 31}')
        else:
            print('Неверный ввод')
            end_game()
    except:
        print('Неверный ввод')
        end_game()


# cnt_win - функция - счетчик счета выигрышей
def cnt_win(player: str) -> None:

    if player == player_1:
        total[0] += 1
    else:
        total[1] += 1

    print(f'Счет: {total[0]}:{total[1]}')


# game - функция, в которой записан основной алгоритм игры
def game(field: list) -> None:
    giving_X0(player_1, player_2)

    counter: int = 0
    while True:

        show_battle_field(field)

        if counter % 2 == 0:
            data_handler(player_1, chr_1)
        else:
            data_handler(player_2, chr_2)

        counter += 1

        if counter > 4:
            who_win: function = check_win(field)
            if who_win:
                if who_win == chr_1:
                    print(f'\n{player_1}, выиграл(а)!')
                    cnt_win(player_1)
                    show_battle_field(field)
                    end_game()
                    break
                else:
                    print(f'\n{player_2}, выиграл(а)!')
                    cnt_win(player_2)
                    show_battle_field(field)
                    end_game()
                    break

        if counter == 9:
            print('Ничья!')
            show_battle_field(field)
            end_game()
            break


# main_def - основная функция в которой собраны фунцкии игры
def main_def(field: list) -> None:
    start_game()
    game(field)


main_def(battle_field)