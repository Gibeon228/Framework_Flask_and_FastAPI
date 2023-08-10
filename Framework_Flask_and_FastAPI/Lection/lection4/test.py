import img
import requests
import time
import threading
import urllib





urls = ['https://p4.wallpaperbetter.com/wallpaper/93/30/487/nature-jpg-format-download-1920x1200-wallpaper-preview.jpg',
        'https://jcup.ru/images/zakat-v-webm.jpg',
        'https://img.freepik.com/premium-photo/dcim-101media-dji-0067-jpg_665346-20571.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/1/10/Rubiks_cube.jpg',
        'https://mirimstudent25.files.wordpress.com/2013/10/movietalk-despicableme630-jpg_002144.jpg',
        ]

url = 'https://jcup.ru/images/zakat-v-webm.jpg'
index = url.rfind("/") + 1
filename = 'thread_' + url[index:]

print(filename)
# def download(url):
#     response = requests.get(img)
#     out = open(url, "wb")
#     out.write(response.content)
#     out.close()
#
# download('https://jcup.ru/imresponseages/zakat-v-webm.jpg')