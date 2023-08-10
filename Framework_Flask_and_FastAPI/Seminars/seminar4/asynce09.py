import asyncio
import aiohttp
import time

urls = ['https://p4.wallpaperbetter.com/wallpaper/93/30/487/nature-jpg-format-download-1920x1200-wallpaper-preview.jpg',
        'https://jcup.ru/images/zakat-v-webm.jpg',
        'https://img.freepik.com/premium-photo/dcim-101media-dji-0067-jpg_665346-20571.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/1/10/Rubiks_cube.jpg',
        'https://mirimstudent25.files.wordpress.com/2013/10/movietalk-despicableme630-jpg_002144.jpg',
        ]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.content
            start_index = url.rfind("/") + 1
            filename = url[start_index:]
            with open(filename, "wb") as f:
                f.write(text.content)
            print(f"Download {url} in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
