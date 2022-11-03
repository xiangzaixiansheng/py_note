### 字典

#### 1.1、创建字典

```python
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
```

可使用函数dict从其他映射（如其他字典）或键值对序列创建字典。

```python
>>> items = [('name', 'Gumby'), ('age', 42)] 
>>> d = dict(items) 
>>> d 
{'age': 42, 'name': 'Gumby'} 
>>> d['name'] 
'Gumby'
```

#### 1.2、字典的基本操作方法

 len(d)返回字典d包含的项（键值对）数。

d[k]返回与键k相关联的值。

d[k] = v将值v关联到键k。 

del d[k]删除键为k的项。

k in d检查字典d是否包含键为k的项。

```python
>>> x = [] 
>>> x[42] = 'Foobar' 
Traceback (most recent call last): 
 File "<stdin>", line 1, in ? 
IndexError: list assignment index out of range 
>>> x = {} 
>>> x[42] = 'Foobar' 
>>> x 
{42: 'Foobar'}
```

​		首先，我尝试将字符串'Foobar'赋给一个空列表中索引为42的元素。这显然不可能，因为

没有这样的元素。要让这种操作可行，初始化x时，**必须使用[None] * 43之类的代码**，而不能使

用[]。然而，接下来的尝试完全可行。这次我将'Foobar'赋给一个空字典的键42；如你所见，这

样做一点问题都没有：在这个字典中添加了一个新项，我得逞了。

#### 1.3、将字符串格式设置功能用于字典

​	可在字典中包含各种信息，这样只需在格式字符串中提取所需的信息即可。为此，

必须使用format_map来指出你将通过一个映射来提供所需的信息

```python
>>> phonebook 
{'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'} 
>>> "Cecil's phone number is {Cecil}.".format_map(phonebook) 
"Cecil's phone number is 3258."
```

#### 1.4、字典的方法

**clear** 方法clear删除所有的字典项

**copy** 方法copy返回一个新字典，其包含的键值对与原来的字典相同（这个方法执行的是浅复制，

因为值本身是原件，而非副本）

```python
>>> x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']} 
>>> y = x.copy() 
>>> y['username'] = 'mlh' 
>>> y['machines'].remove('bar') 
>>> y 
{'username': 'mlh', 'machines': ['foo', 'baz']} 
>>> x 
{'username': 'admin', 'machines': ['foo', 'baz']}
```

为避免这种问题，一种办法是执行深复制，即同时复制值及其包含的所有值，等等。为此，

可使用模块copy中的函数deepcopy。

```python
>>> from copy import deepcopy 
>>> d = {} 
>>> d['names'] = ['Alfred', 'Bertrand'] 
>>> c = d.copy() 
>>> dc = deepcopy(d) 
>>> d['names'].append('Clive') 
>>> c 
{'names': ['Alfred', 'Bertrand', 'Clive']} 
>>> dc 
{'names': ['Alfred', 'Bertrand']}
```

**fromkeys** 方法fromkeys创建一个新字典，其中包含指定的键，且每个键对应的值都是None。

```python
>>> {}.fromkeys(['name', 'age']) 
{'age': None, 'name': None}

这个示例首先创建了一个空字典，再对其调用方法fromkeys来创建另一个字典，这显得有点
多余。你可以不这样做，而是直接对dict（前面说过，dict是所有字典所属的类型。类和类型将
在第7章详细讨论）调用方法fromkeys。
>>> dict.fromkeys(['name', 'age']) 
{'age': None, 'name': None}
如果你不想使用默认值None，可提供特定的值。
>>> dict.fromkeys(['name', 'age'], '(unknown)') 
{'age': '(unknown)', 'name': '(unknown)'}
```

**get** 方法get为访问字典项提供了宽松的环境

如你所见，使用get来访问不存在的键时，没有引发异常，而是返回None。你可指定“默认”

值，这样将返回你指定的值而不是None。

```python
>>> d.get('name', 'N/A') 

'N/A' 
```

**items** 方法items返回一个包含所有字典项的列表，其中每个元素都为(key, value)的形式。字典项

在列表中的排列顺序不确定。

```python
>>> d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0} 
>>> d.items() 
dict_items([('url', 'http://www.python.org'), ('spam', 0), ('title', 'Python Web Site')])
返回值属于一种名为字典视图的特殊类型。字典视图可用于迭代
```

**keys** 方法keys返回一个字典视图，其中包含指定字典中的键

**pop** 方法pop可用于获取与指定键相关联的值，并将该键值对从字典中删除

```python
>>> d = {'x': 1, 'y': 2} 
>>> d.pop('x') 
1 
>>> d 
{'y': 2}
```

**popitem** 方法popitem类似于list.pop，但list.pop弹出列表中的最后一个元素，而popitem随机地弹出一个字典项，因为字典项的顺序是不确定的，没有“最后一个元素”的概念。

```python
>>> d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'} 
>>> d.popitem() 
('url', 'http://www.python.org') 
>>> d 
{'spam': 0, 'title': 'Python Web Site'}
```

**setdefault** 方法setdefault有点像get，因为它也获取与指定键相关联的值，但除此之外，setdefault

还在字典不包含指定的键时，在字典中添加指定的键值对

```
>>> d = {} 
>>> d.setdefault('name', 'N/A') 
'N/A' 
>>> d 
{'name': 'N/A'} 
>>> d['name'] = 'Gumby' 
>>> d.setdefault('name', 'N/A') 
'Gumby' 
>>> d 
{'name': 'Gumby'}
```

**update** 方法update使用一个字典中的项来更新另一个字典

```python
>>> d = { 
... 'title': 'Python Web Site', 
... 'url': 'http://www.python.org', 
... 'changed': 'Mar 14 22:09:15 MET 2016' 
... }
>>> x = {'title': 'Python Language Website'} 
>>> d.update(x) 
>>> d 
{'url': 'http://www.python.org', 'changed': 
'Mar 14 22:09:15 MET 2016', 'title': 'Python Language Website'}
```

**values** 方法values返回一个由字典中的值组成的字典视图。不同于方法keys，方法values返回的视

图可能包含重复的值。

```python
>>> d = {} 
>>> d[1] = 1 
>>> d[2] = 2 
>>> d[3] = 3 
>>> d[4] = 1 
>>> d.values() 
dict_values([1, 2, 3, 1])
```



#### 1.5、合并两个字点

**使用两次update方法向字典中添加元素**

```python
d1 = {'name': 'revotu', 'age': 99}
d2 = {'age': 24, 'sex': 'male'}
 
d = {}
d.update(d1) 
d.update(d2)
print(d)
 
#输出：
{'name': 'revotu', 'age': 24, 'sex': 'male'}
```

**字典构造器**

```python
d1 = {'name': 'revotu', 'age': 99}
d2 = {'age': 24, 'sex': 'male'}
d1 = {'name': 'revotu', 'age': 99}
d2 = {'age': 24, 'sex': 'male'}
d = dict(d1)             
d.update(d2)
print(d)
 
#输出：
{'name': 'revotu', 'age': 24, 'sex': 'male'}
```

在Python3.5+中，可以使用一种全新的字典合并方式

```python
d1 = {'name': 'revotu', 'age': 99}
d2 = {'age': 24, 'sex': 'male'}
d = {**d1, **d2}        
print(d)     
 
#输出：
{'name': 'revotu', 'age': 24, 'sex': 'male'} 
```

