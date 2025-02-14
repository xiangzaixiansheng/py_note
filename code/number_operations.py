#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
常用数字操作示例
"""

def number_operations_demo():
    # 1. 基本数学运算
    print("1. 基本数学运算:")
    a, b = 10, 3
    print(f"加法: {a} + {b} = {a + b}")
    print(f"减法: {a} - {b} = {a - b}")
    print(f"乘法: {a} * {b} = {a * b}")
    print(f"除法: {a} / {b} = {a / b}")  # 返回浮点数
    print(f"整除: {a} // {b} = {a // b}")  # 返回整数
    print(f"取余: {a} % {b} = {a % b}")
    print(f"幂运算: {a} ** {b} = {a ** b}")

    # 2. 数字类型转换
    print("\n2. 数字类型转换:")
    x = 3.14
    print(f"浮点数: {x}")
    print(f"转整数: {int(x)}")
    print(f"四舍五入: {round(x)}")
    print(f"向上取整: {import_ceil()}")
    print(f"向下取整: {import_floor()}")

    # 3. 数字的特殊方法
    print("\n3. 数字的特殊方法:")
    num = -42.789
    print(f"原始数字: {num}")
    print(f"绝对值: {abs(num)}")
    print(f"保留2位小数: {round(num, 2)}")

    # 4. 进制转换
    print("\n4. 进制转换:")
    n = 42
    print(f"十进制数: {n}")
    print(f"转二进制: {bin(n)}")
    print(f"转八进制: {oct(n)}")
    print(f"转十六进制: {hex(n)}")

    # 5. 复数运算
    print("\n5. 复数运算:")
    c1 = 3 + 4j
    c2 = 2 + 3j
    print(f"复数1: {c1}")
    print(f"复数2: {c2}")
    print(f"复数加法: {c1 + c2}")
    print(f"复数乘法: {c1 * c2}")
    print(f"复数1的实部: {c1.real}")
    print(f"复数1的虚部: {c1.imag}")

    # 6. 数学库函数
    print("\n6. 数学库函数:")
    import math
    x = 1.5
    print(f"正弦: {math.sin(x)}")
    print(f"余弦: {math.cos(x)}")
    print(f"正切: {math.tan(x)}")
    print(f"π值: {math.pi}")
    print(f"e值: {math.e}")
    print(f"平方根: {math.sqrt(16)}")

def import_ceil():
    import math
    return math.ceil(3.14)

def import_floor():
    import math
    return math.floor(3.14)

if __name__ == '__main__':
    number_operations_demo()
