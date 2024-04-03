# Модифицируйте программу таким образом, чтобы она сама определяла количество необходимых параллельных потоков.
import os
from concurrent.futures import ThreadPoolExecutor

def calculate_something(parameter):
    # Допустим, параметр - это список чисел, которые нужно сложить
    total = sum(parameter)
    return total

# Пример использования функции
parameters = [1, 2, 3, 4, 5]
result = calculate_something(parameters)
print(f"Результат сложения: {result}")

# Определение количества ядер процессора
num_cores = os.cpu_count()

# Создание пула потоков
with ThreadPoolExecutor(max_workers=num_cores) as executor:
    # Запуск задач в пуле потоков
    tasks = [executor.submit(calculate_something, param) for param in parameters]

# Ожидание завершения всех задач
for task in tasks:
    print(task.result())
