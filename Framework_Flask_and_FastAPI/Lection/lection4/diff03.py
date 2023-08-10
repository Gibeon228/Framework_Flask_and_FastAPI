#     Написать программу, которая считывает список из 10 URL-адресов
# и одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте процессы.

import requests
import time
from multiprocessing import Process

urls = ['https://t.me/python3k',
        'https://www.youtube.com/channel/UCQ1YbfMA6JeGamfA1RHMWHQ',
        'https://gitlab.com/dzhoker1/function-list-or-square-brackets',
        'https://docs.python.org/3/library/asyncio.html',
        'https://habr.com/ru/acticles/671602',
        ]


def download(url):
    response = requests.get(url)
    filename = 'multiproc_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Download {url} in {time.time() - start_time:.2f} seconds")


processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=[url])
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
