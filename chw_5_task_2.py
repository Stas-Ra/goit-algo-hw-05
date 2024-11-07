
from typing import Callable
import re

  
def generator_numbers(text):
    pattern = r" \d+\.\d+\ "
    for value in re.findall(pattern, text):
        yield value

def sum_profit(text, funk):
    list_profit = []
    for value in generator_numbers(text):
        list_profit.append(float(value))
        result = sum(list_profit)
    return result

text_profit = ("Загальний дохід працівника складається з декількох частин:"
        "1. 1000.01 як основний дохід, доповнений додатковими"
        " надходженнями 2. 27.45 і 3. 324.00 доларів.")

total_income = sum_profit(text_profit, generator_numbers)
print(f"Загальний дохід: {total_income}")