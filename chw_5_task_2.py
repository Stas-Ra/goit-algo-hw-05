
import re

text = ("Загальний дохід працівника складається з декількох частин:"
        " 1000.01 як основний дохід, доповнений додатковими"
        " надходженнями 27.45 і 324.00 доларів.")
  

def generator_numbers(text):
    pattern = r"\d+\.\d+"
    for value in re.findall(pattern, text):
        yield float(value)

for value in generator_numbers(text):
    value

def sum_profit(text, func):
    result = sum(func)
    return result

total_income = sum_profit(text, generator_numbers(text))
print(f"Загальний дохід: {total_income}")

