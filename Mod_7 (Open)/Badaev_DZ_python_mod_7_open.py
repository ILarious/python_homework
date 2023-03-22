import pickle
from string import ascii_letters
from typing import List, Dict, TextIO, Tuple

# =============================================================================
# =============================================================================

# /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\========/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{ TASK 1 }~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# | Во входном файле numbers.txt записано N целых чисел, которые могут быть   |
# | разделены пробелами и концами строк. Напишите программу, которая выводит  |
# | сумму чисел во выходной файл answer.txt.                                  |
# \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/========\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/

# try:
#     file_numbers: TextIO = open('numbers.txt', 'r')
#     file_answer: TextIO = open('answer.txt', 'w')
#
#     try:
#         def cnt_num_in_file(file: TextIO) -> int:
#             # List comprehension итерируется по файлу и если
#             # символ преобразуется в целое число int(chr_) то добавляет это
#             # число в список. Функцию sum() суммирует значения списка.
#             cnt: int = sum([int(chr_) for chr_ in file if int(chr_)])
#
#             return cnt
#
#         # Записывает результат функции в файл answer.txt, преобразуя его в str
#         file_answer.write(str(cnt_num_in_file(file_numbers)))
#
#     finally:
#         file_numbers.close()
#         file_answer.close()
#
# except FileNotFoundError:
#     print('Невозможно открыть файл')


# /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\========/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{ TASK 2 }~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# | В файле zen.txt хранится так называемый Дзен Пайтона — текст философии    |
# | программирования на языке Python. Напишите программу, которая выводит на  |
# | экран все строки этого файла в обратном порядке.                          |
# \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/========\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/

# try:
#     file_zen = open('zen.txt', 'r')
#     try:
#         file_zen: TextIO
#         # readlines() считывает все строки из файла и возвращает список.
#         # reversed() возвращает список в обратном порядке.
#         # join возвращает строку из списка.
#         res: str = ''.join(reversed(file_zen.readlines()))
#
#         print(res)
#
#     finally:
#         file_zen.close()
#
#
# except FileNotFoundError:
#     print('Невозможно открыть файл')


# /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\========/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{ TASK 3 }~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# | В файле first_tour.txt записано число K и данные об участниках турнира    |
# | по настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных|
# | в первом туре. Во второй тур проходят участники, которые набрали более    |
# | K баллов в первом туре.                                                   |
# | Напишите программу, которая выводит в файл second_tour.txt данные всех    |
# | участников, прошедших во второй тур, с нумерацией.                        |
# \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/========\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/

# try:
#     f_in: TextIO = open('first_tour.txt', 'r')
#     f_out: TextIO = open('second_tour.txt', 'w')
#
#     try:
#         k: int = int(f_in.readline())
#         participants: List[Tuple[str, str, int]] = []
#
#         for line in f_in:
#             surname: str
#             name: str
#             score: int
#             surname, name, score = line.split()
#
#             # Проверяет, набрал ли участник нужный минимум баллов
#             if int(score) > k:
#                 # Добавляет данные об участнике в список
#                 participants.append((surname, name[0], int(score)))
#
#         # Сортирует список по убыванию набранных баллов
#         participants.sort(key=lambda x: x[2], reverse=True)
#
#         # Выводит количество участников второго тура
#         f_out.write(str(len(participants)) + '\n')
#
#         # Выводит данные об участниках
#         for i, participant in enumerate(participants):
#             f_out.write(
#             f'{i + 1}. {participant[0]} {participant[1]}. {participant[2]}\n')
#
#     finally:
#         f_in.close()
#         f_out.close()
# except:
#     print('Невозможно открыть файл')


# /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\========/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{ TASK 4 }~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# | Есть файл text.txt, который содержит текст. Напишите программу, которая   |
# | выполняет частотный анализ, определяя долю каждой буквы английского       |
# | алфавита в общем количестве английских букв в тексте, и выводит результат |
# | в файл analysis.txt. Символы, не являющиеся буквами английского алфавита, |
# | учитывать не нужно. В файл analysis.txt выводится доля каждой буквы,      |
# | встречающейся в тексте, с тремя знаками в дробной части. Буквы должны быть|
# | отсортированы по убыванию их доли.                                        |
# | Буквы с равной долей должны следовать в алфавитном порядке.               |
# \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/========\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/

try:
    f_text: TextIO = open('text.txt', 'r')
    f_analysis: TextIO = open('analysis.txt', 'w')

    try:
        text: str = f_text.read().lower()
        letters: Dict[str, int] = {}

        for letter in text:
            letter: str

            if letter in ascii_letters:
                if letter not in letters:
                    letters[letter] = 1
                else:
                    letters[letter] += 1

        total: int = sum(letters.values())
        frequencies: Dict[str, float] = {
            letter: round(count/total, 3) for letter, count in letters.items()}

        for letter in sorted(frequencies.keys(), key=lambda x: (-frequencies[x], x)):
            f_analysis.write(f'{letter}: {frequencies[letter]}\n')

    finally:
        f_text.close()
        f_analysis.close()

except FileNotFoundError:
    print('Невозможно открыть файл')

