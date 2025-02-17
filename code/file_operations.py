"""
Python 文件操作示例
展示常见的文件读写操作
"""
import os

# 文件写入
def write_example():
    # 写入文本文件
    with open('example.txt', 'w', encoding='utf-8') as f:
        f.write('Hello, World!\n')
        f.write('这是第二行\n')
        
    # 使用print写入
    with open('example.txt', 'a', encoding='utf-8') as f:
        print('这是第三行', file=f)
        
# 文件读取
def read_example():
    # 读取整个文件
    with open('example.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print("整个文件内容:", content)
        
    # 逐行读取
    with open('example.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print("行内容:", line.strip())
            
    # 读取所有行到列表
    with open('example.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print("所有行:", lines)

# 文件和目录操作
def file_dir_operations():
    # 检查文件是否存在
    print("文件是否存在:", os.path.exists('example.txt'))
    
    # 获取文件大小
    if os.path.exists('example.txt'):
        print("文件大小:", os.path.getsize('example.txt'), "字节")
    
    # 创建目录
    os.makedirs('test_dir', exist_ok=True)
    
    # 列出目录内容
    print("当前目录内容:", os.listdir('.'))
    
    # 删除文件
    if os.path.exists('example.txt'):
        os.remove('example.txt')
    
    # 删除目录
    if os.path.exists('test_dir'):
        os.rmdir('test_dir')

if __name__ == '__main__':
    # 执行示例
    write_example()
    read_example()
    file_dir_operations()
