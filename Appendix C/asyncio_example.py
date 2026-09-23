# C-0 asyncio

import asyncio
import time

async def wicked():
    print("Surrender,")
    await asyncio.sleep(2)
    print("Dorothy")

start_time = time.time()

asyncio.run(wicked())

end_time = time.time()

print('__________')
print(start_time)
print(end_time)
print(end_time - start_time)
print('__________')

async def say(phrase, seconds):
    print(phrase)
    await asyncio.sleep(seconds)
    print("now!")

async def wicked2():
    task_1 = asyncio.create_task(say("Surrender,", 2))
    task_2 = asyncio.create_task(say("Dorothy!", 0))
    await task_1
    await task_2

asyncio.run(wicked2())