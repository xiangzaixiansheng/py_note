#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
常用列表操作示例
"""

def list_operations_demo():
    # 1. 创建列表
    print("1. 创建列表:")
    # 直接创建
    list1 = [1, 2, 3, 4, 5]
    # 使用list()函数
    list2 = list('Hello')
    # 列表推导式
    list3 = [x**2 for x in range(5)]
    print(f"普通列表: {list1}")
    print(f"字符串转列表: {list2}")
    print(f"列表推导式: {list3}")

    # 2. 访问和修改列表
    print("\n2. 访问和修改列表:")
    fruits = ['apple', 'banana', 'orange', 'grape']
    print(f"原始列表: {fruits}")
    # 索引访问
    print(f"第一个元素: {fruits[0]}")
    print(f"最后一个元素: {fruits[-1]}")
    # 切片
    print(f"前两个元素: {fruits[:2]}")
    print(f"后两个元素: {fruits[-2:]}")
    # 修改元素
    fruits[1] = 'pear'
    print(f"修改后的列表: {fruits}")

    # 3. 列表方法
    print("\n3. 列表方法:")
    numbers = [1, 2, 3]
    print(f"原始列表: {numbers}")
    # 添加元素
    numbers.append(4)
    print(f"append后: {numbers}")
    numbers.insert(0, 0)
    print(f"insert后: {numbers}")
    # 扩展列表
    numbers.extend([5, 6])
    print(f"extend后: {numbers}")
    # 删除元素
    numbers.remove(3)  # 删除指定值
    print(f"remove后: {numbers}")
    popped = numbers.pop()  # 删除并返回最后一个元素
    print(f"pop后: {numbers}, 弹出的元素: {popped}")

    # 4. 列表排序
    print("\n4. 列表排序:")
    nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"原始列表: {nums}")
    # 排序方法
    sorted_nums = sorted(nums)  # 返回新列表
    print(f"sorted()后: {sorted_nums}")
    nums.sort()  # 原地排序
    print(f"sort()后: {nums}")
    # 反转
    nums.reverse()
    print(f"reverse()后: {nums}")

    # 5. 列表操作
    print("\n5. 列表操作:")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    # 连接
    concatenated = list1 + list2
    print(f"连接后的列表: {concatenated}")
    # 重复
    repeated = list1 * 2
    print(f"重复后的列表: {repeated}")
    # 成员检测
    print(f"2在list1中: {2 in list1}")
    print(f"5在list1中: {5 in list1}")

    # 6. 列表推导式和过滤
    print("\n6. 列表推导式和过滤:")
    # 带条件的列表推导式
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"偶数的平方: {even_squares}")
    # 使用map和filter
    doubles = list(map(lambda x: x*2, range(5)))
    print(f"使用map加倍: {doubles}")
    odds = list(filter(lambda x: x % 2 == 1, range(10)))
    print(f"使用filter过滤奇数: {odds}")

    # 7. 多维列表
    print("\n7. 多维列表:")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"矩阵: {matrix}")
    print(f"访问元素[1][1]: {matrix[1][1]}")
    # 列表展平
    flattened = [item for sublist in matrix for item in sublist]
    print(f"展平后的列表: {flattened}")

    # 8. 列表去重
    print("\n8. 列表去重:")
    # 原始列表（包含重复元素）
    duplicate_list = [1, 2, 2, 3, 3, 3, 4, 4, 5, 1, 2, 3]
    print(f"原始列表: {duplicate_list}")
    
    # 方法1：使用set()去重（最简单的方法，但会打乱顺序）
    unique_list1 = list(set(duplicate_list))
    print(f"使用set()去重: {unique_list1}")
    
    # 方法2：使用dict.fromkeys()去重（保持顺序，Python 3.7+）
    unique_list2 = list(dict.fromkeys(duplicate_list))
    print(f"使用dict.fromkeys()去重（保持顺序）: {unique_list2}")
    
    # 方法3：使用列表推导式去重（保持顺序）
    unique_list3 = []
    [unique_list3.append(x) for x in duplicate_list if x not in unique_list3]
    print(f"使用列表推导式去重（保持顺序）: {unique_list3}")
    
    # 对包含字典的列表去重
    dict_list = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 1, 'name': 'Alice'},  # 重复项
        {'id': 3, 'name': 'Charlie'}
    ]
    print(f"\n包含字典的列表: {dict_list}")
    
    # 使用元组转换去重
    unique_dict_list = list({tuple(d.items()): d for d in dict_list}.values())
    print(f"字典列表去重后: {unique_dict_list}")

if __name__ == '__main__':
    list_operations_demo()
