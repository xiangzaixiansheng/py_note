"""
Python 遍历操作示例
展示各种常见的遍历方法和技巧
"""

def list_iterations():
    """列表遍历的各种方式"""
    print("\n=== 列表遍历示例 ===")
    fruits = ['apple', 'banana', 'orange', 'grape']
    
    # 1. 基本for循环
    print("基本for循环:")
    for fruit in fruits:
        print(fruit)
    
    # 2. 带索引的遍历 (enumerate)
    print("\n使用enumerate:")
    for index, fruit in enumerate(fruits):
        print(f"索引 {index}: {fruit}")
    
    # 3. 带索引的遍历（指定起始索引）
    print("\n使用enumerate并指定起始索引:")
    for index, fruit in enumerate(fruits, start=1):
        print(f"第 {index} 个水果是: {fruit}")
    
    # 4. 使用range和len
    print("\n使用range和len:")
    for i in range(len(fruits)):
        print(f"位置 {i}: {fruits[i]}")
    
    # 5. 反向遍历
    print("\n反向遍历:")
    for fruit in reversed(fruits):
        print(fruit)

def dict_iterations():
    """字典遍历的各种方式"""
    print("\n=== 字典遍历示例 ===")
    person = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    
    # 1. 遍历键
    print("遍历键:")
    for key in person:  # 或使用 person.keys()
        print(key)
    
    # 2. 遍历值
    print("\n遍历值:")
    for value in person.values():
        print(value)
    
    # 3. 遍历键值对
    print("\n遍历键值对:")
    for key, value in person.items():
        print(f"{key}: {value}")

def advanced_iterations():
    """高级遍历技巧"""
    print("\n=== 高级遍历示例 ===")
    
    # 1. zip函数用法
    names = ['Alice', 'Bob', 'Charlie']
    ages = [24, 30, 35]
    cities = ['Paris', 'London', 'Tokyo']
    
    print("使用zip同时遍历多个列表:")
    for name, age, city in zip(names, ages, cities):
        print(f"{name} is {age} years old and lives in {city}")
    
    # 2. 列表推导式
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print("\n列表推导式:", squares)
    
    # 3. 字典推导式
    square_dict = {x: x**2 for x in numbers}
    print("\n字典推导式:", square_dict)
    
    # 4. 集合推导式
    even_squares = {x**2 for x in numbers if x % 2 == 0}
    print("\n集合推导式:", even_squares)

def generator_examples():
    """生成器和迭代器示例"""
    print("\n=== 生成器示例 ===")
    
    # 1. 简单生成器函数
    def count_up_to(n):
        i = 1
        while i <= n:
            yield i
            i += 1
    
    print("使用生成器函数:")
    for num in count_up_to(5):
        print(num)
    
    # 2. 生成器表达式
    squares_gen = (x**2 for x in range(1, 6))
    print("\n使用生成器表达式:")
    for square in squares_gen:
        print(square)

def nested_iterations():
    """嵌套遍历示例"""
    print("\n=== 嵌套遍历示例 ===")
    
    # 1. 嵌套列表遍历
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("遍历矩阵:")
    for row in matrix:
        for num in row:
            print(num, end=' ')
        print()  # 换行
    
    # 2. 使用列表推导式展平嵌套列表
    flattened = [num for row in matrix for num in row]
    print("\n展平后的列表:", flattened)

if __name__ == "__main__":
    # 运行所有示例
    list_iterations()
    dict_iterations()
    advanced_iterations()
    generator_examples()
    nested_iterations()
