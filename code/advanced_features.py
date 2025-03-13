"""
Python 高级特性示例
展示一些Python的高级用法和特性
"""
from functools import wraps
from typing import List, Dict, Optional
import time

# 装饰器示例
def timer_decorator(func):
    """计时装饰器：计算函数执行时间"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time:.4f} 秒")
        return result
    return wrapper

# 带参数的装饰器
def retry(times: int):
    """重试装饰器：函数失败时自动重试指定次数"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第 {i+1} 次尝试失败: {e}")
                    if i == times - 1:
                        raise
        return wrapper
    return decorator

# 上下文管理器
class Timer:
    """计时上下文管理器"""
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.duration = self.end - self.start

# 属性装饰器
class Person:
    def __init__(self, name: str):
        self._name = name
        self._age = 0

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("名字必须是字符串")
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int):
            raise TypeError("年龄必须是整数")
        if value < 0:
            raise ValueError("年龄不能为负数")
        self._age = value

# 生成器和迭代器进阶
class FibonacciSequence:
    """斐波那契数列迭代器"""
    def __init__(self, max_num: int):
        self.max_num = max_num
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_num:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

# 描述符示例
class Validator:
    """属性验证描述符"""
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f"值不能小于 {self.minvalue}")
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f"值不能大于 {self.maxvalue}")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

# 使用示例
@timer_decorator
def example_function():
    """装饰器示例函数"""
    time.sleep(1)
    return "完成"

@retry(times=3)
def might_fail():
    """重试装饰器示例"""
    import random
    if random.random() < 0.7:
        raise ValueError("随机失败")
    return "成功"

class Temperature:
    """使用描述符的类"""
    celsius = Validator(minvalue=-273.15)
    fahrenheit = Validator(minvalue=-459.67)

def main():
    # 1. 装饰器示例
    print("=== 装饰器示例 ===")
    example_function()

    # 2. 上下文管理器示例
    print("\n=== 上下文管理器示例 ===")
    with Timer() as timer:
        time.sleep(0.5)
    print(f"代码块执行时间: {timer.duration:.4f} 秒")

    # 3. 属性装饰器示例
    print("\n=== 属性装饰器示例 ===")
    person = Person("Alice")
    person.age = 25
    print(f"姓名: {person.name}, 年龄: {person.age}")

    # 4. 生成器和迭代器示例
    print("\n=== 斐波那契数列示例 ===")
    fib = FibonacciSequence(5)
    print("斐波那契数列前5个数:", list(fib))

    # 5. 描述符示例
    print("\n=== 描述符示例 ===")
    temp = Temperature()
    temp.celsius = 25
    print(f"摄氏度: {temp.celsius}")
    try:
        temp.celsius = -300  # 将引发ValueError
    except ValueError as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    main()
