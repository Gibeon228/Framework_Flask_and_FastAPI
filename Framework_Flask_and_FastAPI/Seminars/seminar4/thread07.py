# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6..]
# Массив должен быть заполнен случайными числамиот 1 до 100.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.

import threading
import time
from random import randint

arr = [randint(1, 100) for _ in range(10 ** 6)]
sum_ = 0

start_time = time.time()

def sum_numbers(num_list):
    global sum_
    for i in num_list:
        sum_ += i


threads = []
for i in range(10):
    start_index = i * 100_000
    end_index = start_index + 100_000
    thread = threading.Thread(target=sum_numbers, args=(arr[start_index:end_index],))
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()

print(f"Время выполнения программы: {time.time() - start_time} seconds\n")
print(sum_)