
x = 'ABC'
dummy = [ord(x) for x in x]
print(dummy)

symbols = '$&^%'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 50]
print(beyond_ascii)

beyond_ascii1 = list( filter(lambda c: c > 50, map(ord,symbols)))
print(beyond_ascii1)


colors = ['black','white']
sizes = ['S','M','L']
tshirts = [(color,size) for color in colors
                        for size in sizes]
print(tshirts)

# 生成器表达式
print(tuple(ord(s) for s in symbols))
import array
print(array.array('I',(ord(s) for s in symbols))) # 第一个参数指定数组中数字的存储方式


for tshirt in ( '%s %s' % (c,s) for c in colors for s in sizes ):
    print(tshirt)


city,year,pop,chg,area = ('Tokyo',2003,32450,0.66,8014)
print(city)
city,_,_,_,_ = ('Tokyo',2003,32450,0.66,8014)
print(city)
city,*rest = ('Tokyo',2003,32450,0.66,8014)
print(city)
print(rest)
city,*rest,area = ('Tokyo',2003,32450,0.66,8014)
print(city,rest,area)



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


from collections import namedtuple

# 字段名可以使空格隔开的字符串 也可以是字符串组成的可迭代对象
City = namedtuple('City','name country population coordinates')
tokyo = City(name='Tokyo',country='JP',population=66.63,coordinates=(35.689722,139.691667))
print(tokyo.name , tokyo.country , tokyo.population , tokyo.coordinates)


print(City._fields)
print(tokyo._asdict())
delhi_data = ('Delhi NCR','IN',21.66,(28.36,135.66))
delhi = City._make(delhi_data)
print(delhi)


l = [10,20,30,40,50,60]
print(l[:2]) # [10, 20]
print(l[2:]) # [30, 40, 50, 60]

s = 'bicycle'
print(s[::3]) # bye
print(s[::-1]) # elcycib
print(s[::-2]) # eccb

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

l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [20,30]
print(l)
# [0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]
print(l)
# [0, 1, 20, 30, 5, 8, 9]
# l[2:5] = 100 # TypeError: can only assign an iterable


l = [1,2,3]
print(l * 5)

# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

print(5 * 'abc')

# abcabcabcabcabc

# 用 `*` 初始化一个由列表组成的列表


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

fruits = ['grape','raspberry','apple','banana']
print(sorted(fruits))
# ['apple', 'banana', 'grape', 'raspberry']

print(sorted(fruits,reverse=True))
# ['raspberry', 'grape', 'banana', 'apple']
fruits.sort(key=len)
print(fruits)
# ['grape', 'apple', 'banana', 'raspberry']


