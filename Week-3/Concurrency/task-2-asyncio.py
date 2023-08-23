import aiohttp, aiofiles
import asyncio
import time
from bs4 import BeautifulSoup
import html5lib

# ----- build connection function -----
async def connection(url):
    async with aiohttp.ClientSession() as session:
        respone = session(url)


# ----- build file save function -----



# ----- build asyncio event loop function -----