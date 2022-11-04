# pip3 install aiohttp
import aiohttp
import asyncio
import time


async def dl_coroutine(session, url):
    print('开始下载图片%s' + url)
    async with session.get(url, verify_ssl=False) as res:
        content = await res.content.read()
        t = time.time()
        filename = './img/{}.jpg'.format(int(round(t*1000)))
        with open(filename, mode='wb') as f:
            f.write(content)
        print('下载完成')


async def main():
    async with aiohttp.ClientSession() as session:
        imglist=['https://img2.baidu.com/it/u=2240230198,3231648811&fm=253&fmt=auto&app=120&f=JPEG?w=1422&h=800.jpg'] * 20
       
        tasks = [asyncio.create_task(dl_coroutine(session, img))
                 for img in imglist]

        await asyncio.wait(tasks)

if __name__ == '__main__':
    t1 = int(round(time.time()*1000))
    asyncio.run(main())
    t2 = int(round(time.time()*1000))
    print('执行了{} 毫秒'.format(t2-t1))
