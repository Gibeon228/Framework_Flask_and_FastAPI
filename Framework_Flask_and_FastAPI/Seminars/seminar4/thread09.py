# Написать программу, которая скачивает изображения с заданных URL-адресов и
# сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
# файле, название которого соответствует названию изображения в URL-адресе.
# � Например URL-адрес: https://example/images/image1.jpg -> файл на диске:
# image1.jpg
# � Программа должна использовать многопоточный, многопроцессорный и
# асинхронный подходы.
# � Программа должна иметь возможность задавать список URL-адресов через
# аргументы командной строки.
# � Программа должна выводить в консоль информацию о времени скачивания
# каждого изображения и общем времени выполнения программы.


import requests
import time
import threading

urls = ['https://p4.wallpaperbetter.com/wallpaper/93/30/487/nature-jpg-format-download-1920x1200-wallpaper-preview.jpg',
        'https://jcup.ru/images/zakat-v-webm.jpg',
        'https://img.freepik.com/premium-photo/dcim-101media-dji-0067-jpg_665346-20571.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/1/10/Rubiks_cube.jpg',
        'https://mirimstudent25.files.wordpress.com/2013/10/movietalk-despicableme630-jpg_002144.jpg',
        ]

def download(url):
    response = requests.get(url)
    start_index = url.rfind("/") + 1
    filename = url[start_index:]
    with open(filename, "wb") as f:
        f.write(response.content)
        f.close()
    print(f"Download {url} in {time.time() - start_time:.2f} seconds")

threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

