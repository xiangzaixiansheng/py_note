import random
import string


def is_viable_str(value=None):
    if isinstance(value, str) and len(value) > 0:
        return True
    else:
        return False


def is_viable_number_str(value=None):
    if isinstance(value, str) and len(value) > 0:
        try:
            number = int(value)
        except Exception as e:
            return False
        else:
            return True
    else:
        return False

def is_viable_number(value=None):
    if isinstance(value, int):
        return True
    else:
        return False

def is_viable_numbers(values=None):
    for value in values:
        if not isinstance(value, int):
            return False
    return True

def get_random_str(length=32):
    """
    随机声明一个字符串
    :param num: 字符串的长度
    :return:
    """
    salt = ''.join(random.sample(string.ascii_lowercase + string.digits, length))

    return salt


def is_viable_url_str(value=None):
    """
    判断字符串是否是一个合法的链接
    :param value: 需要判断的字符串
    :return:
    """
    is_viable_url = False
    if isinstance(value, str) and len(value) > 0:
        try:
            import re
            regex = re.compile(
                r'^(?:http|ftp)s?://'  # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
                r'localhost|'  # localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
                r'(?::\d+)?'  # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)
            if re.match(regex, value) is not None:
                is_viable_url = True
        except Exception as e:
            print(e)
    return is_viable_url

def get_MD5(value=None):
    #1、参数必须是utf8
    #2、python3所有字符都是unicode形式，已经不存在unicode关键字
    #3、python3 str 实质上就是unicode
    import hashlib
    if isinstance(value,str):
        # 如果是unicode先转utf-8
        parmStr=value.encode("utf-8")
        m = hashlib.md5()
        m.update(parmStr)
        return m.hexdigest()
    else:
        return ''

if __name__ == '__main__':
    print(is_viable_url_str("http://www.example.com"))
    print(is_viable_str("hello world"))
