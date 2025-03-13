"""
Python 异步编程示例
展示 async/await 的使用方法和常见模式
"""
import asyncio
import aiohttp
import time
from typing import List, Dict
import random

# 基础异步函数示例
async def hello_world():
    """简单的异步函数示例"""
    await asyncio.sleep(1)  # 模拟异步操作
    return "Hello, World!"

# 多个异步任务
async def count_down(name: str, seconds: int):
    """倒计时异步函数"""
    for i in range(seconds, 0, -1):
        print(f"{name}: {i} 秒")
        await asyncio.sleep(1)
    print(f"{name}: 完成!")
    return name

# 并发运行多个任务
async def run_multiple_tasks():
    """同时运行多个异步任务"""
    # 创建多个任务
    tasks = [
        count_down("计时器A", 3),
        count_down("计时器B", 2),
        count_down("计时器C", 4)
    ]
    # 等待所有任务完成
    results = await asyncio.gather(*tasks)
    print("所有计时器完成:", results)

# 异步上下文管理器
class AsyncResource:
    """异步上下文管理器示例"""
    async def __aenter__(self):
        print("获取资源")
        await asyncio.sleep(1)  # 模拟资源获取
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("释放资源")
        await asyncio.sleep(0.5)  # 模拟资源释放

    async def do_something(self):
        print("使用资源")
        await asyncio.sleep(0.5)

# 异步迭代器
class AsyncNumberGenerator:
    """异步迭代器示例"""
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.current = start

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current > self.end:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)  # 模拟异步操作
        self.current += 1
        return self.current - 1

# 实际应用示例：异步网络请求
async def fetch_url(session: aiohttp.ClientSession, url: str) -> Dict:
    """异步获取URL内容"""
    async with session.get(url) as response:
        return {
            'url': url,
            'status': response.status,
            'content_length': len(await response.text())
        }

async def fetch_multiple_urls(urls: List[str]):
    """并发获取多个URL的内容"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

# 异步生产者-消费者模式
async def producer(queue: asyncio.Queue):
    """生产者：生成数据并放入队列"""
    for i in range(5):
        item = random.randint(1, 100)
        await queue.put(item)
        print(f"生产: {item}")
        await asyncio.sleep(random.random())
    await queue.put(None)  # 发送结束信号

async def consumer(queue: asyncio.Queue):
    """消费者：从队列中获取并处理数据"""
    while True:
        item = await queue.get()
        if item is None:  # 检查结束信号
            break
        print(f"消费: {item}")
        await asyncio.sleep(random.random())
        queue.task_done()

# 异步事件示例
async def waiter(event: asyncio.Event):
    """等待事件"""
    print("等待事件...")
    await event.wait()
    print("事件已触发!")

async def trigger(event: asyncio.Event):
    """触发事件"""
    await asyncio.sleep(2)
    print("触发事件")
    event.set()

# 主函数：运行所有示例
async def main():
    print("=== 基础异步函数示例 ===")
    result = await hello_world()
    print(result)

    print("\n=== 多任务并发示例 ===")
    await run_multiple_tasks()

    print("\n=== 异步上下文管理器示例 ===")
    async with AsyncResource() as resource:
        await resource.do_something()

    print("\n=== 异步迭代器示例 ===")
    async for num in AsyncNumberGenerator(1, 5):
        print(f"生成数字: {num}")

    print("\n=== 异步网络请求示例 ===")
    urls = [
        'http://example.com',
        'http://python.org',
        'http://github.com'
    ]
    try:
        results = await fetch_multiple_urls(urls)
        for result in results:
            if isinstance(result, Exception):
                print(f"Error: {result}")
            else:
                print(f"URL: {result['url']}, Status: {result['status']}")
    except Exception as e:
        print(f"网络请求出错: {e}")

    print("\n=== 生产者-消费者示例 ===")
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

    print("\n=== 事件示例 ===")
    event = asyncio.Event()
    await asyncio.gather(waiter(event), trigger(event))

# 运行示例
if __name__ == "__main__":
    # 在Python 3.7+中，可以直接使用asyncio.run()
    asyncio.run(main())
