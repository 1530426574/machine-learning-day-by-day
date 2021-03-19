# import asyncio
# from pyppeteer import launch
#
# async def main():
#     await launch(headless=False)
#     await asyncio.sleep(10)
#
# asyncio.get_event_loop().run_until_complete(main())
# import asyncio
# from pyppeteer import launch
#
# async def main():
#     browser = await launch(devtools=True)
#     page = await browser.newPage()
#     await page.goto('https://www.baidu.com')
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://www.taobao.com')
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())
