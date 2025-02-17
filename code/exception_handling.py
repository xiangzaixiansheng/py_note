"""
Python 异常处理示例
展示各种异常处理方式和自定义异常
"""

# 基本的try-except结构
def basic_exception_handling():
    try:
        x = 1 / 0  # 会触发 ZeroDivisionError
    except ZeroDivisionError as e:
        print(f"捕获到除零错误: {e}")
    
    try:
        num = int("abc")  # 会触发 ValueError
    except ValueError as e:
        print(f"捕获到值错误: {e}")

# 多个异常的处理
def multiple_exceptions():
    try:
        # 尝试打开一个不存在的文件
        with open("nonexistent.txt") as f:
            content = f.read()
    except FileNotFoundError as e:
        print(f"文件不存在: {e}")
    except PermissionError as e:
        print(f"没有权限访问文件: {e}")
    except Exception as e:
        print(f"捕获到其他异常: {e}")

# 使用else和finally
def else_finally_example():
    try:
        number = int(input("请输入一个数字: "))
    except ValueError:
        print("输入无效，不是一个数字")
    else:
        # 只有当try块中的代码成功执行时，才会执行else块
        print(f"你输入的数字是: {number}")
    finally:
        # 无论是否发生异常，finally块都会执行
        print("这里的代码总是会执行")

# 自定义异常
class CustomError(Exception):
    """自定义异常类"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# 使用自定义异常
def validate_age(age):
    if age < 0:
        raise CustomError("年龄不能为负数")
    if age > 150:
        raise CustomError("年龄超出正常范围")
    return f"年龄 {age} 是有效的"

# 异常的传播和重新抛出
def propagate_exception():
    try:
        result = validate_age(200)
    except CustomError as e:
        print(f"捕获到自定义异常: {e}")
        # 可以选择重新抛出异常
        raise

# 使用with语句进行上下文管理
def context_manager_example():
    try:
        with open("example.txt") as f:
            content = f.read()
    except FileNotFoundError:
        print("文件不存在")
    except Exception as e:
        print(f"发生其他错误: {e}")

# 展示assert的使用
def assert_example(x):
    try:
        assert x > 0, "x必须大于0"
        print(f"x的值是: {x}")
    except AssertionError as e:
        print(f"断言错误: {e}")

if __name__ == "__main__":
    print("基本异常处理示例:")
    basic_exception_handling()
    
    print("\n多个异常处理示例:")
    multiple_exceptions()
    
    print("\n带else和finally的示例:")
    try:
        else_finally_example()
    except Exception as e:
        print(f"发生错误: {e}")
    
    print("\n自定义异常示例:")
    try:
        print(validate_age(25))  # 正常情况
        print(validate_age(-5))  # 会抛出异常
    except CustomError as e:
        print(f"验证年龄时发生错误: {e}")
    
    print("\n断言示例:")
    assert_example(5)   # 正常情况
    assert_example(-1)  # 会触发断言错误
