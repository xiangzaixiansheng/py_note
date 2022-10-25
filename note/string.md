## 1、字符串的替换

推荐使用format

```
>>> format = "Hello, s. s enough for ya?" % %
>>> values = ('world', 'Hot') 
>>> format values %
'Hello, world. Hot enough for ya?'

>>> "{}, {} and {}".format("first", "second", "third") 
'first, second and third' 
>>> "{0}, {1} and {2}".format("first", "second", "third") 
'first, second and third' 
然而，索引无需像上面这样按顺序排列。
>>> "{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to") 
'to be or not to be' 

命名字段的工作原理与你预期的完全相同。
>>> from math import pi 
>>> "{name} is approximately {value:.2f}.".format(value=pi, name="π") 
'π is approximately 3.14.' 
当然，关键字参数的排列顺序无关紧要。在这里，我还指定了格式


>>> fullname = ["Alfred", "Smoketoomuch"] 
>>> "Mr {name[1]}".format(name=fullname) 
'Mr Smoketoomuch'

```

推荐使用下面的方法

```
>>> "The number is {num}".format(num=42) 
'The number is 42' 
>>> "The number is {num:f}".format(num=42) 
'The number is 42.000000' 
你也可以将其作为二进制数进行处理。
>>> "The number is {num:b}".format(num=42) 
'The number is 101010'
```

b  将整数表示为二进制数

c 将整数解读为Unicode码点

d 将整数视为十进制数进行处理，这是整数默认使用的说明符

e 使用科学表示法来表示小数（用e来表示指数）

E 与e相同，但使用E来表示指数

f 将小数表示为定点数

F 与f相同，但对于特殊值（nan和inf），使用大写表示

g 自动在定点表示法和科学表示法之间做出选择。这是默认用于小数的说明符，但在默认情况下至少有1位小数

G 与g相同，但使用大写来表示指数和特殊值

n 与g相同，但插入随区域而异的数字分隔符

o 将整数表示为八进制数

s 保持字符串的格式不变，这是默认用于字符串的说明符

x 将整数表示为十六进制数并使用小写字母

X 与x相同，但使用大写字母

% 将数表示为百分比值（乘以100，按说明符f设置格式，再在后面加上%）



## 2、字符串方法

2.1  **find**

方法find在字符串中查找子串。如果找到，就返回子串的第一个字符的索引，否则返回-1。

```
>>> 'With a moo-moo here, and a moo-moo there'.find('moo') 
7 
>>> title = "Monty Python's Flying Circus" 
>>> title.find('Monty') 
0 
>>> title.find('Python')
6
```

2.2  **join** 

```
>>> seq = ['1', '2', '3', '4', '5'] 
>>> sep.join(seq) # 合并一个字符串列表
'1+2+3+4+5'
```

2.3  **replace**

```
>>> 'This is a test'.replace('is', 'eez') 
'Theez eez a test'
```

2.4  **strip**

方法strip将字符串开头和末尾的空白（但不包括中间的空白）删除，并返回删除后的结果。

```
>>> ' internal whitespace is kept '.strip() 
'internal whitespace is kept'
```

2.5 **lower**

方法lower返回字符串的小写版本。

