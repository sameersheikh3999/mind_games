import time 
import asyncio

async def fetch_bone():
    print("My pet is fetching the bone....")
    await asyncio.sleep(4)
    print("The bone is fetched")

async def fetch_money():
    print("He is fetching the money...")
    await asyncio.sleep(2)
    print("The money is fetched")

async def main():

    

    start_time=time.time()
    await asyncio.gather(fetch_bone(),fetch_money())


    end_time=time.time()

    Total_time_taken=end_time-start_time

    print(f"Total time to run this program is {Total_time_taken:.2f}")


if __name__=="__main__":
    asyncio.run(main())