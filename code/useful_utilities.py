"""
Python 实用工具函数集合
包含各种常用的辅助函数和技巧
"""
from typing import Any, List, Dict, Union
import json
import csv
import random
import string
from pathlib import Path
from collections import defaultdict, Counter

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """展平嵌套列表"""
    flat_list = []
    for item in nested_list:
        if isinstance(item, (list, tuple)):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """将列表分割成固定大小的块"""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def generate_random_string(length: int = 10) -> str:
    """生成指定长度的随机字符串"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def safe_get(dictionary: Dict, keys: Union[str, List[str]], default: Any = None) -> Any:
    """安全地从嵌套字典中获取值"""
    if isinstance(keys, str):
        keys = keys.split('.')
    
    for key in keys:
        try:
            dictionary = dictionary[key]
        except (KeyError, TypeError):
            return default
    return dictionary

def merge_dicts(dict1: Dict, dict2: Dict, deep: bool = True) -> Dict:
    """合并两个字典，支持深度合并"""
    result = dict1.copy()
    
    for key, value in dict2.items():
        if deep and key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    
    return result

class DataValidator:
    """数据验证工具类"""
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """简单的电子邮件格式验证"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        """简单的电话号码格式验证（中国大陆手机号）"""
        import re
        pattern = r'^1[3-9]\d{9}$'
        return bool(re.match(pattern, phone))

class FileHandler:
    """文件处理工具类"""
    @staticmethod
    def save_json(data: Any, filepath: str, indent: int = 4) -> None:
        """保存数据为JSON文件"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)

    @staticmethod
    def load_json(filepath: str) -> Any:
        """从JSON文件加载数据"""
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def save_csv(data: List[Dict], filepath: str) -> None:
        """保存数据为CSV文件"""
        if not data:
            return
        
        fieldnames = data[0].keys()
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def load_csv(filepath: str) -> List[Dict]:
        """从CSV文件加载数据"""
        with open(filepath, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))

def count_elements(items: List[Any]) -> Dict[Any, int]:
    """计算列表中元素出现的次数"""
    return dict(Counter(items))

def group_by(items: List[Dict], key: str) -> Dict[Any, List[Dict]]:
    """根据指定的键对字典列表进行分组"""
    groups = defaultdict(list)
    for item in items:
        groups[item.get(key)].append(item)
    return dict(groups)

# 使用示例
def main():
    # 1. 列表操作
    print("=== 列表操作示例 ===")
    nested = [1, [2, 3, [4, 5]], 6]
    print("展平列表:", flatten_list(nested))
    
    numbers = list(range(10))
    print("分块后的列表:", chunk_list(numbers, 3))

    # 2. 随机字符串生成
    print("\n=== 随机字符串示例 ===")
    print("随机字符串:", generate_random_string())
    print("指定长度的随机字符串:", generate_random_string(5))

    # 3. 字典操作
    print("\n=== 字典操作示例 ===")
    nested_dict = {'a': {'b': {'c': 1}}}
    print("安全获取嵌套值:", safe_get(nested_dict, 'a.b.c'))
    print("安全获取不存在的值:", safe_get(nested_dict, 'a.b.d', default='未找到'))

    # 4. 数据验证
    print("\n=== 数据验证示例 ===")
    validator = DataValidator()
    print("邮箱验证:", validator.is_valid_email("example@email.com"))
    print("手机号验证:", validator.is_valid_phone("13812345678"))

    # 5. 文件操作
    print("\n=== 文件操作示例 ===")
    # 创建示例数据
    data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ]
    
    # 保存和加载JSON
    json_file = "example.json"
    FileHandler.save_json(data, json_file)
    loaded_json = FileHandler.load_json(json_file)
    print("从JSON加载的数据:", loaded_json)

    # 保存和加载CSV
    csv_file = "example.csv"
    FileHandler.save_csv(data, csv_file)
    loaded_csv = FileHandler.load_csv(csv_file)
    print("从CSV加载的数据:", loaded_csv)

    # 6. 数据统计和分组
    print("\n=== 数据统计和分组示例 ===")
    items = ['a', 'b', 'a', 'c', 'b', 'a']
    print("元素计数:", count_elements(items))

    people = [
        {"dept": "IT", "name": "Alice"},
        {"dept": "IT", "name": "Bob"},
        {"dept": "HR", "name": "Charlie"}
    ]
    print("按部门分组:", group_by(people, "dept"))

if __name__ == "__main__":
    main()
