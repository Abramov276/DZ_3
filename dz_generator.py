import re
from typing import Callable


def generator_numbers(text: str):
    # Створюємо регулярний вираз для пошуку дійсних чисел в тексті
    pattern = r'\b-?\d+(?:\.\d+)?\b'

# Шукаємо співпадіння чисел в тексті, перетворюємо їх в тип float, та повертаємо
    for match in re.findall(pattern, text):
        yield float(match)

# Створюємо функцію яка рахує сумму чисел з тексту


def sum_profit(text: str, func: Callable):
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_profit = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_profit}")
