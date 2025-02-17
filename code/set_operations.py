"""
Python Set（集合）操作示例
集合是一个无序的不重复元素序列
"""

# 创建集合
fruits = {'apple', 'banana', 'orange'}
numbers = set([1, 2, 3, 4, 5])
empty_set = set()  # 创建空集合

# 添加元素
fruits.add('grape')
print("添加元素后的集合:", fruits)

# 更新集合
fruits.update(['pear', 'melon'])
print("更新后的集合:", fruits)

# 删除元素
fruits.remove('apple')  # 如果元素不存在会报错
fruits.discard('banana')  # 如果元素不存在不会报错
popped_item = fruits.pop()  # 随机移除一个元素
print("删除元素后的集合:", fruits)

# 集合运算
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 交集
intersection = set1 & set2  # 或使用 set1.intersection(set2)
print("交集:", intersection)

# 并集
union = set1 | set2  # 或使用 set1.union(set2)
print("并集:", union)

# 差集
difference = set1 - set2  # 或使用 set1.difference(set2)
print("差集:", difference)

# 对称差集
symmetric_difference = set1 ^ set2  # 或使用 set1.symmetric_difference(set2)
print("对称差集:", symmetric_difference)

# 子集和超集判断
subset = {1, 2}
print("subset是set1的子集吗?", subset.issubset(set1))
print("set1是subset的超集吗?", set1.issuperset(subset))

# 判断是否有交集
print("set1和set2是否有交集?", set1.isdisjoint({9, 10}))  # False表示有交集
