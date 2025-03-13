"""
Python 类和继承示例
展示类的定义、继承、多态等面向对象编程概念
"""
from typing import List, Optional
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

# 基本类定义
class Person:
    """人员基本类"""
    
    # 类变量（所有实例共享）
    species = "Homo Sapiens"
    
    def __init__(self, name: str, age: int):
        # 实例变量（每个实例独有）
        self.name = name
        self.age = age
        self._secret = None  # 约定私有（单下划线）
        self.__very_secret = None  # 真正的私有（双下划线）

    # 实例方法
    def introduce(self) -> str:
        return f"我是 {self.name}，今年 {self.age} 岁"
    
    # 类方法
    @classmethod
    def create_anonymous(cls) -> 'Person':
        return cls("Anonymous", 0)
    
    # 静态方法
    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18
    
    # 属性装饰器
    @property
    def secret(self) -> Optional[str]:
        return self._secret
    
    @secret.setter
    def secret(self, value: str):
        self._secret = value

# 继承示例
class Employee(Person):
    """员工类，继承自Person"""
    
    def __init__(self, name: str, age: int, employee_id: str):
        # 调用父类的初始化方法
        super().__init__(name, age)
        self.employee_id = employee_id
        self.tasks: List[str] = []
    
    # 方法重写
    def introduce(self) -> str:
        base_intro = super().introduce()  # 调用父类方法
        return f"{base_intro}，工号是 {self.employee_id}"
    
    def add_task(self, task: str):
        self.tasks.append(task)
    
    def list_tasks(self) -> List[str]:
        return self.tasks

# 多重继承
class Swimmer:
    def swim(self):
        return "我会游泳"

class Runner:
    def run(self):
        return "我会跑步"

class Athlete(Person, Swimmer, Runner):
    """运动员类，多重继承示例"""
    def __init__(self, name: str, age: int, sport: str):
        super().__init__(name, age)
        self.sport = sport
    
    def introduce(self) -> str:
        return f"{super().introduce()}，我是一名{self.sport}运动员"

# 抽象类
class Animal(ABC):
    """抽象基类示例"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def make_sound(self) -> str:
        """必须被子类实现的抽象方法"""
        pass
    
    def introduce(self) -> str:
        return f"我是{self.name}"

class Dog(Animal):
    """具体类必须实现抽象类的所有抽象方法"""
    def make_sound(self) -> str:
        return "汪汪!"

# 使用dataclass装饰器
@dataclass
class Point:
    """使用dataclass的示例"""
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

# 接口示例（Python中使用抽象类实现接口的概念）
class Drawable(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass

class Circle(Drawable):
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> str:
        return f"画一个半径为{self.radius}的圆"

# 混入类（Mixin）示例
class TimestampMixin:
    def get_created_time(self) -> datetime:
        return getattr(self, '_created_time', datetime.now())
    
    def set_created_time(self):
        self._created_time = datetime.now()

class Task(TimestampMixin):
    def __init__(self, title: str):
        self.title = title
        self.set_created_time()

def main():
    # 1. 基本类使用
    print("=== 基本类使用 ===")
    person = Person("张三", 25)
    print(person.introduce())
    print(f"是否成年: {Person.is_adult(person.age)}")

    # 方式1：通过类名调用
    anonymous1 = Person.create_anonymous()

    # 方式2：通过实例调用
    person = Person("张三", 25)
    anonymous2 = person.create_anonymous()

    # 方式3：在子类中使用
    anonymous_employee = Employee.create_anonymous()  # 返回Employee实例

    # 2. 继承示例
    print("\n=== 继承示例 ===")
    employee = Employee("李四", 30, "E001")
    print(employee.introduce())
    employee.add_task("完成报告")
    print(f"任务列表: {employee.list_tasks()}")
    
    # 3. 多重继承
    print("\n=== 多重继承示例 ===")
    athlete = Athlete("王五", 20, "游泳")
    print(athlete.introduce())
    print(athlete.swim())
    print(athlete.run())
    
    # 4. 抽象类和具体实现
    print("\n=== 抽象类示例 ===")
    dog = Dog("小黑")
    print(f"{dog.introduce()} {dog.make_sound()}")
    
    # 5. 数据类
    print("\n=== 数据类示例 ===")
    point = Point(3, 4)
    print(f"点 ({point.x}, {point.y}) 到原点的距离: {point.distance_from_origin()}")
    
    # 6. 接口实现
    print("\n=== 接口实现示例 ===")
    circle = Circle(5)
    print(circle.draw())
    
    # 7. Mixin使用
    print("\n=== Mixin示例 ===")
    task = Task("学习Python")
    print(f"任务创建时间: {task.get_created_time()}")

if __name__ == "__main__":
    main()
