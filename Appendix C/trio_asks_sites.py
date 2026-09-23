# C-1 webcrawler with trio, asks(deprecated), using httpx as alternative
#       Google AI suggests httpx instead of asks after book example barfed

import time

#import asks
import httpx    # modern alternative to asks
import trio

#asks.init("trio")

urls = [
    'https://boredomtherapy.com/bad-taxidermy/',
    'http://www.badtaxidermy.com/',
    'https://crappytaxidermy.com/',
    'https://www.ranker.com/list/bad-taxidermy-pictures/ashley-reign',
]

async def get_one(client, url, t1, start_idx):
    try:
        r = await client.get(url)   # changed asks to client
        t2 = time.time()
        print(f"{start_idx}\t{(t2-t1):.04}\t{len(r.content)}\t{url}")

    except Exception as e:
        t2 = time.time()
        print(f"{start_idx}\t{(t2-t1):.04}\t\tFAILED\t{url} ({type(e).__name__})")


async def get_sites(sites):
    t1 = time.time()
    async with httpx.AsyncClient() as client:       # Google AI says is more efficient
        async with trio.open_nursery() as nursery:
            for idx, url in enumerate(sites, start=1):
                # added in starting index, to see order of start and finish
                nursery.start_soon(get_one, client, url, t1, idx)

if __name__ == "__main__":
    print("start\tseconds\tbytes\turl")
    trio.run(get_sites, urls)