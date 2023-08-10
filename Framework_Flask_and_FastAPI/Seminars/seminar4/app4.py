# Создать программу, которая будет производить подсчёт количества слов в каждом файле
# в указанной директории и выводить результаты в консоль.
# Используйте потоки

import threading
import os

def count_words(file):
    with open(file, 'r') as f:
        text = f.read()
        count = len(text.split())
    print(count)

threads =[]
files = os.walk('../seminar4/1')

for file in files:
    thread = threading.Thread(target=count_words, args=(file,))
    threads.append(thread)


for item in threads:
    item.start()

for item in threads:
    item.join()