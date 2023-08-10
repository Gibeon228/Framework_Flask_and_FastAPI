import requests
import time
from multiprocessing import Process

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
