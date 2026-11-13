import time 
import asyncio


async def do_something():
    print("doing something...")
    await asyncio.sleep(4)
    print("I have done somehting")

async def do_enjoy():
    print("enjoyed something...")
    await asyncio.sleep(2)
    print("I have enjoyed everything")


async def main():
    start_time=time.time()

    await asyncio.gather(do_something(),do_enjoy())

    end_time=time.time()

    print(f"The total time taken is {end_time - start_time:.2f}")


if __name__=="__main__":
    asyncio.run(main())

print("Yes, I did this......!!!")