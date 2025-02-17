"""
Python 日期和时间操作示例
展示datetime模块的常用操作
"""
from datetime import datetime, date, timedelta
import time

# 获取当前日期和时间
now = datetime.now()
print("当前日期和时间:", now)
print("格式化日期时间:", now.strftime("%Y-%m-%d %H:%M:%S"))

# 创建日期
specific_date = date(2024, 1, 1)
print("指定日期:", specific_date)

# 日期运算
tomorrow = date.today() + timedelta(days=1)
print("明天:", tomorrow)
next_week = date.today() + timedelta(weeks=1)
print("下周:", next_week)

# 时间戳操作
current_timestamp = time.time()
print("当前时间戳:", current_timestamp)

# 时间戳转datetime
datetime_from_timestamp = datetime.fromtimestamp(current_timestamp)
print("时间戳转换为datetime:", datetime_from_timestamp)

# 字符串转日期
date_string = "2024-01-01 12:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("字符串转换为日期:", parsed_date)

# 计算时间差
date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 2, 1)
diff = date2 - date1
print("两个日期之间的天数:", diff.days)

# 获取日期的具体部分
print("年:", now.year)
print("月:", now.month)
print("日:", now.day)
print("时:", now.hour)
print("分:", now.minute)
print("秒:", now.second)

# 获取星期几
print("今天是星期:", now.weekday())  # 0-6, 0是星期一
print("今天是星期:", now.isoweekday())  # 1-7, 1是星期一
