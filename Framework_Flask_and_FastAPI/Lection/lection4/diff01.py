import requests
import time

urls = ['https://t.me/python3k',
        'https://www.youtube.com/channel/UCQ1YbfMA6JeGamfA1RHMWHQ',
        'https://gitlab.com/dzhoker1/function-list-or-square-brackets',
        'https://docs.python.org/3/library/asyncio.html',
        'https://habr.com/ru/acticles/671602',
        ]

start_time = time.time()

for url in urls:
    response = requests.get(url)
    filename = 'sync_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Download {url} in {time.time() - start_time:.2f} seconds")