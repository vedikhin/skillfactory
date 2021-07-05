import numpy as np

MIN_VALUE = 1
MAX_VALUE = 100


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    if number < MIN_VALUE or number > MAX_VALUE:
        print(f"ОШИБКА! Число должно быть в диапазоне [{MIN_VALUE} .. {MAX_VALUE}]")
        return 0

    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, MAX_VALUE + 1)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного. Функция принимает загаданное число и возвращает число попыток """
    if number < MIN_VALUE or number > MAX_VALUE:
        print(f"ОШИБКА! Число должно быть в диапазоне [{MIN_VALUE} .. {MAX_VALUE}]")
        return 0

    count = 1
    predict = np.random.randint(1, MAX_VALUE + 1)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    """Алгоритм двоичного поиска (без рекурсии).
       Функция принимает загаданное число и возвращает число попыток"""
    low, high, count = MIN_VALUE, MAX_VALUE, 1

    if number < MIN_VALUE or number > MAX_VALUE:
        print(f"ОШИБКА! Число должно быть в диапазоне [{MIN_VALUE} .. {MAX_VALUE}]")
        return 0

    while True:
        mid = (low + high) // 2  # в питоне числа безразмерные, поэтому не делаем так: mid = low + (high - low) // 2
        if mid == number:
            return count  # угадали - выход из цикла
        elif mid < number:
            low = mid + 1  # ищем в промежутке mid+1 .. high
        else:
            high = mid - 1  # ищем в промежутке low .. mid-1
        count += 1


def game_core_v4(number, low=MIN_VALUE, high=MAX_VALUE, count=1):
    """Алгоритм двоичного поиска (с рекурсией).
       Функция принимает загаданное число и возвращает число попыток"""
    if number < MIN_VALUE or number > MAX_VALUE:
        print(f"ОШИБКА! Число должно быть в диапазоне [{MIN_VALUE} .. {MAX_VALUE}]")
        return 0

    mid = (low + high) // 2  # в питоне числа безразмерные, поэтому не делаем так: mid = low + (high - low) // 2
    if mid == number:
        return count
    elif mid < number:
        return game_core_v4(number, mid + 1, high, count + 1)  # ищем в промежутке mid+1 .. high
    else:
        return game_core_v4(number, low, mid - 1, count + 1)  # ищем в промежутке low .. mid-1


def game_core_v5(number):
    """Экспоненциальный поиск (https://en.m.wikipedia.org/wiki/Exponential_search).
       Функция принимает загаданное число и возвращает число попыток"""
    if number < MIN_VALUE or number > MAX_VALUE:
        print(f"ОШИБКА! Число должно быть в диапазоне [{MIN_VALUE} .. {MAX_VALUE}]")
        return 0

    bound, count = 1, 0
    while True:
        count += 1
        if bound == number:
            return count  # угадали
        elif bound < number:
            bound *= 2
        else:
            return game_core_v4(number, bound // 2, min(bound, MAX_VALUE), count + 1)  # делаем бинарный поиск


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    scores = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!

    random_numbers = np.random.randint(1, MAX_VALUE + 1, size=1000)
    for number in random_numbers:
        scores.append(game_core(number))

    score = int(np.mean(scores))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


print("Алгоритм 1:")
score_game(game_core_v1)

print("\nАлгоритм 2:")
score_game(game_core_v2)

print("\nАлгоритм 3 (мой):")
score_game(game_core_v3)

print("\nАлгоритм 4 (мой):")
score_game(game_core_v4)

print("\nАлгоритм 5 (мой):")
score_game(game_core_v5)

