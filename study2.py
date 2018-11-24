import bisect
import sys

HAYSTACK = [1,3,4,5,6,7,8,9,11,22,45,56,69]
position = bisect.bisect_left(HAYSTACK,2)
print(position) # 1

position = bisect.bisect(HAYSTACK,2)
print(position) # 1


def grade(score, breakpoints=[60,70,80,90],grades='FDCBA'):
    i = bisect.bisect(breakpoints,score)
    return grades[i]

print([ grade(score) for score in [33,99,77,70,89,90,100] ])

# ['F', 'A', 'C', 'C', 'B', 'A', 'A']


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


# from random import random
#
# floats = array('d',(random() for i in range(10**7)))
#
# fp = open('floats.bin','wb')
# floats.tofile(fp)
# fp.close()
# print(floats[-1])
#
# floats2 = array('d')
# fp = open('floats.bin','rb')
# floats2.fromfile(fp,10**7)
# fp.close()
# print(floats2[-1])
# print(floats2 == floats)

from array import array
numbers = array('h' ,[-2,-1,0,1,2])
memv = memoryview(numbers)
print(len(memv)) # 5
print(memv[0])  # -2
memv_oct = memv.cast('B') # 转换为 `B` 类型 无符号字符
print(memv_oct.tolist()) # 以列表的形式看 memv_oct
# [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
memv_oct[5] = 4 # 把位置5的字节赋值成4
# 因为我们把占2个字节的证书的高位字节改成了4所以这个有符号的整数的值变成了 1024
print(numbers)
# array('h', [-2, -1, 1024, 1, 2])

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







