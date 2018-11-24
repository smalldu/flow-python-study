
> 列表推导是构建列表（list）的快捷方式，生成器表达式则可以用来创建其他任何类型的序列

### 列表推导

```python
x = 'ABC'
dummy = [ord(x) for x in x] # [65, 66, 67]
```

列表推导、生成器表达式，以及其他很相似的集合（set）推导和字典（dict）推导，在 `Python3` 中都有自己的局部作用域。


#### 列表推导和 `filter` 、 `map` 比较 

```python
symbols = '$&^%'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 50]
print(beyond_ascii)

beyond_ascii1 = list( filter(lambda c: c > 50, map(ord,symbols)))
print(beyond_ascii1)
```
不知道是习惯还是什么原因 ，感觉列表推导很好理解，就像读一个句子。 `filter` 、 `map` 不好理解 


#### 笛卡尔积 

> 列表推导可以生成两个或两个以上可迭代类型的笛卡尔积。笛卡尔积是一个列表，列表里的元素是由输入的可迭代类型的元素对构成的元祖。因此笛卡尔积
列表的长度等于输入变量的长度的乘积

eg:

```python
colors = ['black','white']
sizes = ['S','M','L']
tshirts = [(color,size) for color in colors 
                        for size in sizes]
# [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
print(tshirts)
```

### 生成器表达式 

> 虽然也可以用列表推导来初始化元祖、数组或其他序列类型，但是生成器表达式是更好的选择，因为它背后遵守了迭代器协议，可以诸葛地
产出元素，而不是先建立一个完整的列表，更节省内存。

```python
symbols = '$&^%'
print(tuple(ord(s) for s in symbols))
import array
print(array.array('I',(ord(s) for s in symbols))) # 第一个参数指定数组中数字的存储方式
```

一个笛卡尔积示例，不会再内存中留下一个6个组合的列表

```python
colors = ['black','white']
sizes = ['S','M','L']
for tshirt in ( '%s %s' % (c,s) for c in colors for s in sizes ):
    print(tshirt)
```


### 元祖 

元祖拆包

```python
city,year,pop,chg,area = ('Tokyo',2003,32450,0.66,8014)
print(city) # Tokyo
city,_,_,_,_ = ('Tokyo',2003,32450,0.66,8014)
print(city) # Tokyo
city,*rest = ('Tokyo',2003,32450,0.66,8014)
print(city) # Tokyo
print(rest) # [2003, 32450, 0.66, 8014]
city,*rest,area = ('Tokyo',2003,32450,0.66,8014)
print(city,rest,area) # Tokyo [2003, 32450, 0.66] 8014 
```

嵌套元祖的拆包

> string.format 有着丰富的的“格式限定符”（语法是{}中带:号），比如： 
填充常跟对齐一起使用 
^、<、>分别是居中、左对齐、右对齐，后面带宽度
:号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
还有一些精度和进制转换的方法。 


```python
metro_areas = [
    ('Tokyo','JP',36.993,(35.689722,139.691667)) ,
    ('Delhi NCR','IN',36.993,(35.689722,139.691667)) ,
    ('Mexico City','MX',36.993,(35.689722,139.691667)) ,
    ('New York','US',36.993,(35.689722,139.691667)) ,
    ('Sao Paulo','BR',-36.993,(35.689722,139.691667)) ,
]

print('{:15} | {:^9} | {:^9}'.format('','lat.','long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name,cc,pop,(lat,lng) in metro_areas:
    print(fmt.format(name,lat,lng))
    
#                 |   lat.    |   long.  
# Tokyo           |   35.6897 |  139.6917
# Delhi NCR       |   35.6897 |  139.6917
# Mexico City     |   35.6897 |  139.6917
# New York        |   35.6897 |  139.6917
# Sao Paulo       |   35.6897 |  139.6917
```

具名元祖 

`collections.namedtuple` 是一个工厂函数，它可以用来构建一个带字段名的元祖和一个有名字的类。 

```python
from collections import namedtuple
# 字段名可以使空格隔开的字符串 也可以是字符串组成的可迭代对象
City = namedtuple('City','name country population coordinates')
tokyo = City(name='Tokyo',country='JP',population=66.63,coordinates=(35.689722,139.691667))
print(tokyo.name , tokyo.country , tokyo.population , tokyo.coordinates)
# Tokyo JP 66.63 (35.689722, 139.691667)

# 除了从普通元祖集成来的属性之外，具名元祖还有一些自己专有的属性 
print(City._fields)
print(tokyo._asdict())
delhi_data = ('Delhi NCR','IN',21.66,(28.36,135.66))
delhi = City._make(delhi_data)
print(delhi)

# ('name', 'country', 'population', 'coordinates')
# OrderedDict([('name', 'Tokyo'), ('country', 'JP'), ('population', 66.63), ('coordinates', (35.689722, 139.691667))])
# City(name='Delhi NCR', country='IN', population=21.66, coordinates=(28.36, 135.66))
```

### 切片 

> Python 中 `list` 、 `tuple` 、 `str` 这类序列类型都支持切片操作。 

```python
l = [10,20,30,40,50,60]
print(l[:2]) # [10, 20]
print(l[2:]) # [30, 40, 50, 60]
```

我们还可以使用 `s[a:b:c]` 的形式对s在a和b之间以c为间隔取值 , c 的值还可以为负，意味着反向取值 

```python
s = 'bicycle'
print(s[::3]) # bye
print(s[::-1]) # elcycib
print(s[::-2]) # eccb
```

我们也可以提前定义好切片然后使用

```python
infos = """
Tokyo       35.6897 139.6917 
Delhi NCR   35.6897 139.6917
Mexico City 35.6897 139.6917
New York    35.6897 139.6917
Sao Paulo   35.6897 139.6917"""
city = slice(0,12)
lat = slice(12,20)
lng = slice(20,28)

line_items = infos.split("\n")[1:]
print(line_items)
for item in line_items:
    print(item[city],item[lat] ,item[lng])
    
# ['Tokyo       35.6897 139.6917 ', 'Delhi NCR   35.6897 139.6917', 'Mexico City 35.6897 139.6917', 'New York    35.6897 139.6917', 'Sao Paulo   35.6897 139.6917']
# Tokyo        35.6897  139.6917
# Delhi NCR    35.6897  139.6917
# Mexico City  35.6897  139.6917
# New York     35.6897  139.6917
# Sao Paulo    35.6897  139.6917
```

为切片赋值 

```python
l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [20,30]
print(l)
# [0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]
print(l)
# [0, 1, 20, 30, 5, 8, 9]
l[2:5] = 100 # TypeError: can only assign an iterable
```

### 对序列使用 `+` 和 `*` 

```python
l = [1,2,3]
print(l * 5)

# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

print(5 * 'abc')

# abcabcabcabcabc
```

`+` 和 `*` 都遵守不修改原有的操作对象，构建一个全新的序列的规律 

用 `*` 初始化一个由列表组成的列表

```python
# 列表推导的方式
board = [ [''] * 3 for i in range(3) ]
print(board)

# [['', '', ''], ['', '', ''], ['', '', '']]
board[1][2] = 'X'
print(board)
# [['', '', ''], ['', '', 'X'], ['', '', '']]
# 含有3个指向同一个对象的引用列表是毫无用处的
weird_board = [[''] * 3] * 3
print(weird_board)

# [['', '', ''], ['', '', ''], ['', '', '']]
weird_board[1][2] = 'X'
print(weird_board)
# [['', '', 'X'], ['', '', 'X'], ['', '', 'X']]
# 3个都指向同一个引用

board = []
for i in range(3):
    # 这里每次都新建一个列表
    row = [''] * 3
    board.append(row)
print(board)

# [['', '', ''], ['', '', ''], ['', '', '']]
board[1][2] = 'X'
print(board)
# [['', '', ''], ['', '', 'X'], ['', '', '']]
``` 

### `list.sort` 和内置 `sorted` 

> `list.sort` 方法会就地排序列表，也就是说不会把原列表复制一份，所以它返回`None` 。
`sorted` 会新建一个列表作为返回值，这个方法可以接受任何形式的可迭代对象作为参数。包括不可变序列和生成器。不管接受什么参数，它都返回一个列表
它们都有两个可选参数 `reverse` , `key` 一个只有一个参数的函数，它会被用在每个元素上产生的结果将是排序算法依赖对比的关键字。 

```python
fruits = ['grape','raspberry','apple','banana']
print(sorted(fruits))
# ['apple', 'banana', 'grape', 'raspberry']

print(sorted(fruits,reverse=True))
# ['raspberry', 'grape', 'banana', 'apple']
fruits.sort(key=len)
print(fruits)
# ['grape', 'apple', 'banana', 'raspberry']
```

### `bisect` 管理已排序的序列 

>`bisect` 模块包含两个主要函数，`bisect` 和 `insort`， 两个函数都利用二分查找算法来再有序序列中查找插入元素 

```python
import bisect
HAYSTACK = [1,3,4,5,6,7,8,9,11,22,45,56,69]
position = bisect.bisect_left(HAYSTACK,2)
print(position) # 1

position = bisect.bisect(HAYSTACK,2)
print(position) # 1
```

bisect 可以用来建立一个用数字作为索引的查询表格，比如说把分数和成绩对应起来。 

```python
def grade(score, breakpoints=[60,70,80,90],grades='FDCBA'):
    i = bisect.bisect(breakpoints,score)
    return grades[i]

print([ grade(score) for score in [33,99,77,70,89,90,100] ])

# ['F', 'A', 'C', 'C', 'B', 'A', 'A']
```

用 `bisect.insort`插入新元素,总能保证`seq`的升序顺序

```python

import random

SIZE = 7

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list,new_item)
    print('{:2d} -> {}'.format(new_item,my_list))

#  5 -> [5]
#  1 -> [1, 5]
#  0 -> [0, 1, 5]
#  3 -> [0, 1, 3, 5]
# 13 -> [0, 1, 3, 5, 13]
#  7 -> [0, 1, 3, 5, 7, 13]
#  9 -> [0, 1, 3, 5, 7, 9, 13]
```

### 当列表不再是首选

> 当我们要存放1000万个浮点数时，数组(`array`)的效率要高很多，因为数组在背后存的并不是 `float` 对象，而是数字的机器翻译
也就是字节表述。如果要频繁对队列进行先进先出的操作，`deque` （双端队列）的速度应该更快。

#### 数组 

创建数组需要一个类型码，这个类型码用来表示在底层 C 语言应该存放怎样的数据类型，如 `b` 类型码代表的是有符号的字符 （signed char）
Python 不允许你在数组存放指定类型之外的数据 


下面代码展示将1000wan个随机浮点数的数组存到文件再读取出来 


```python

from array import array
from random import random

floats = array('d',(random() for i in range(10**7)))

fp = open('floats.bin','wb')
floats.tofile(fp)
fp.close()
print(floats[-1])

floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp,10**7)
fp.close()
print(floats2[-1])
print(floats2 == floats)

# 0.6205547382661204
# 0.6205547382661204
# True

``` 

#### 内存试图 `memoryview` 

`memoryview` 是一个内置类，它能让用户在不复制内容的情况下操作同一个数组的不同切片。 

```python
from array import array
numbers = array('h' ,[-2,-1,0,1,2])
memv = memoryview(numbers)
print(len(memv)) # 5
print(memv[0])  # -2
memv_oct = memv.cast('B') # 转换为 `B` 类型 无符号字符
print(memv_oct.tolist()) # 以列表的形式看 memv_oct
# [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
memv_oct[5] = 4 # 把位置5的字节赋值成4
# 因为我们把占2个字节的证书的高位字节改成了4所以这个有符号的整数的值变成了 1024 (没看懂 ~~~)
print(numbers)
# array('h', [-2, -1, 1024, 1, 2])
```

#### 双向队列和其他形式的队列

利用 `.append` 和 `.pop` 方法我们可以把列表当做栈和队列来用。但是删除列表第一个元素或者第一个元素之前添加一个元素是很
耗时的，因为这些操作会牵扯到移动列表里的所有元素。 

`collections.deque` 类（双向队列）是一个线程安全的可以快速从两端添加或者删除元素的数据类型，而且如果想要有一种数据类型来
存放"最近用到的几个元素"，`deque` 也是一个很好的选择。这是因为在新建一个双向队列的时候你可以指定这个队列的大小。如果这个队列
满员了，还可以从反向端删除过期的元素，然后再尾端添加新的元素。 

```python
from collections import deque

# maxlen 是一个可选参数，代表这个队列可以容纳的元素数量，一旦设定，这个属性就不能修改
dq = deque(range(10),maxlen=10)
print(dq)
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

# 队列的旋转操作接收一个参数n
# n>0时 最右边的n个元素会被移动到左边，n<0，最左边n个元素移动到右边
dq.rotate(3)
print(dq)
# deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
dq.rotate(-4)
print(dq)
# deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
dq.appendleft(-1)
print(dq)
# deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.extend([11,12,13])
print(dq)
# deque([3, 4, 5, 6, 7, 8, 9, 11, 12, 13], maxlen=10)
dq.extendleft([10,20,30,40])
print(dq)
# deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)
```




































 




