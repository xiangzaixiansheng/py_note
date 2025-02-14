#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
常用字典操作示例
"""

def dict_operations_demo():
    # 1. 创建字典
    print("1. 创建字典:")
    # 直接创建
    dict1 = {'name': 'Alice', 'age': 25}
    # 使用dict()构造函数
    dict2 = dict(name='Bob', age=30)
    print(f"字典1: {dict1}")
    print(f"字典2: {dict2}")

    # 2. 访问和修改字典
    print("\n2. 访问和修改字典:")
    person = {'name': 'Charlie', 'age': 35, 'city': 'Beijing'}
    print(f"原始字典: {person}")
    # 访问元素
    print(f"获取name: {person['name']}")
    print(f"安全获取age: {person.get('age')}")
    print(f"获取不存在的键(带默认值): {person.get('country', 'Unknown')}")
    # 修改元素
    person['age'] = 36
    person['country'] = 'China'  # 添加新键值对
    print(f"修改后的字典: {person}")

    # 3. 字典方法
    print("\n3. 字典方法:")
    # 获取所有键
    print(f"所有键: {list(person.keys())}")
    # 获取所有值
    print(f"所有值: {list(person.values())}")
    # 获取所有键值对
    print(f"所有键值对: {list(person.items())}")
    # 删除并返回元素
    removed_item = person.pop('country')
    print(f"删除的值: {removed_item}")
    print(f"删除后的字典: {person}")

    # 4. 字典合并
    print("\n4. 字典合并:")
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    # 使用update方法
    dict1.update(dict2)
    print(f"合并后的字典: {dict1}")
    # 使用 | 运算符 (Python 3.9+)
    dict3 = {'a': 1, 'b': 2}
    dict4 = {'b': 3, 'c': 4}
    merged_dict = dict3 | dict4
    print(f"使用|运算符合并: {merged_dict}")

    # 5. 字典推导式
    print("\n5. 字典推导式:")
    # 创建平方字典
    squares = {x: x**2 for x in range(5)}
    print(f"平方字典: {squares}")
    # 过滤字典
    filtered_dict = {k: v for k, v in squares.items() if v > 5}
    print(f"过滤后的字典: {filtered_dict}")

    # 6. 嵌套字典
    print("\n6. 嵌套字典:")
    users = {
        'user1': {'name': 'Alice', 'age': 25},
        'user2': {'name': 'Bob', 'age': 30}
    }
    print(f"嵌套字典: {users}")
    print(f"访问嵌套值: {users['user1']['name']}")

    # 7. 字典的复制
    print("\n7. 字典的复制:")
    original = {'a': 1, 'b': [1, 2, 3]}
    # 浅复制
    shallow_copy = original.copy()
    # 深复制
    import copy
    deep_copy = copy.deepcopy(original)
    print(f"原始字典: {original}")
    print(f"浅复制: {shallow_copy}")
    print(f"深复制: {deep_copy}")

if __name__ == '__main__':
    dict_operations_demo()
