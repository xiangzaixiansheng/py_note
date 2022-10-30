
# 全局变量 使用
global x
x = 100


def get_global():
    return globals().get('x')


def strory(**params):
    return 'he name is {name}, age {age}'.format_map(params)


if __name__ == '__main__':
    print(get_global())
    print(strory(name="xiangzai", age=18))
    
    _params = {"name":"xiangzai", "age":18}
    print(strory(**_params))

