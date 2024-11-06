
from typing import Callable
import re

  
text_profit = ("Загальний дохід працівника складається з декількох частин:"
        " 1000.01 як основний дохід, доповнений додатковими"
        " надходженнями 27.45 і 324.00 доларів.")
def generator_numbers(text):
    pattern = r"\d+\.\d+"
    for value in re.findall(pattern, text):
        yield value

def sum_profit(text, func: Callable):
    list_profit = []
    for value in generator_numbers(text):
        list_profit.append(float(value))
        result = sum(list_profit)
    return result

text_profit = ("Загальний дохід працівника складається з декількох частин:"
        " 1000.01 як основний дохід, доповнений додатковими"
        " надходженнями 27.45 і 324.00 доларів.")

total_income = sum_profit(text_profit, generator_numbers)
print(f"Загальний дохід: {total_income}")