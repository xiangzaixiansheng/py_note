#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
常用字符串操作示例
"""

def string_operations_demo():
    # 1. 字符串基本操作
    print("1. 基本字符串操作:")
    text = "Hello, Python!"
    print(f"原始字符串: {text}")
    print(f"长度: {len(text)}")
    print(f"大写: {text.upper()}")
    print(f"小写: {text.lower()}")
    print(f"首字母大写: {'hello world'.capitalize()}")
    print(f"每个单词首字母大写: {'hello world'.title()}")
    
    # 2. 字符串查找和替换
    print("\n2. 查找和替换:")
    text = "Python is awesome, Python is great"
    print(f"查找'Python'第一次出现的位置: {text.find('Python')}")
    print(f"查找'Python'最后一次出现的位置: {text.rfind('Python')}")
    print(f"替换第一个'Python': {text.replace('Python', 'Java', 1)}")
    print(f"替换所有'Python': {text.replace('Python', 'Java')}")
    
    # 3. 字符串分割和连接
    print("\n3. 分割和连接:")
    words = "apple,banana,orange"
    word_list = words.split(',')
    print(f"分割字符串: {word_list}")
    print(f"用'-'连接列表: {'-'.join(word_list)}")
    
    # 4. 字符串去除空白
    print("\n4. 去除空白字符:")
    text = "   Hello World   "
    print(f"原始字符串: '{text}'")
    print(f"去除两端空白: '{text.strip()}'")
    print(f"去除左边空白: '{text.lstrip()}'")
    print(f"去除右边空白: '{text.rstrip()}'")
    
    # 5. 字符串判断方法
    print("\n5. 字符串判断:")
    print(f"是否全是字母: {'Hello123'.isalpha()}")
    print(f"是否全是数字: {'123'.isdigit()}")
    print(f"是否全是字母或数字: {'Hello123'.isalnum()}")
    print(f"是否全是小写: {'hello'.islower()}")
    print(f"是否全是大写: {'HELLO'.isupper()}")
    print(f"是否是空白字符: {'   '.isspace()}")
    
    # 6. 字符串格式化
    print("\n6. 字符串格式化:")
    name = "Alice"
    age = 25
    # 使用format()方法
    print("使用format(): {}今年{}岁".format(name, age))
    # 使用f-string (Python 3.6+)
    print(f"使用f-string: {name}今年{age}岁")
    # 使用%操作符
    print("使用%%操作符: %s今年%d岁" % (name, age))
    
    # 7. 字符串对齐
    print("\n7. 字符串对齐:")
    text = "Python"
    print(f"居中对齐: '{text.center(20, '*')}'")
    print(f"左对齐: '{text.ljust(20, '*')}'")
    print(f"右对齐: '{text.rjust(20, '*')}'")
    print(f"数字补零: '{str(42).zfill(5)}'")

if __name__ == '__main__':
    string_operations_demo()