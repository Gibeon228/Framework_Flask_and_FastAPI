import asyncio
from pathlib import Path
from random import randint
import time

arr = [randint(1, 100) for _ in range(10 ** 6)]

sum_ = 0
async def sum_numbers(num_list):
    global sum_
    for i in num_list:
        sum_ += i


async def main():
    tasks = []
    for i in range(10):
        start_index = i * 100_000
        end_index = start_index + 100_000
        task = asyncio.ensure_future(sum_numbers(arr[start_index:end_index]))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
