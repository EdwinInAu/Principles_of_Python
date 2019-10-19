# Prompts the user for a positive integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived positive integer that codes the set of running sums
# ot the members of S when those are listed in increasing order.
#
# Written by Chongshi Wang and Eric Martin for COMP9021

from itertools import accumulate
import sys

try:
    encoded_set = int(input('Input a positive integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

def display_encoded_set(encoded_set):
    l1 = []
    l2 = []
    l3 = []
    number = bin(encoded_set)[2:]  #十进制转换二进制 并且去除'0b'
    for i in range(len(number)):
        l1.append(int(number[i]))  #把二进制数分解 依次添加到l1列表中
    l1.reverse() #调换位置
    for i in range(len(l1)):
        if l1[i] == 1:  #找到列表中数值为1的元素
            if i % 2 == 0:  #位置为偶数
                a = int(i / 2) #找到对应值
                l2.append(a)
            else:
                a = int(-((i + 1) / 2)) #位置为奇数 找到对应值
                l2.append(a)
    l2.sort() #从小到大排序
    for item in l2:
        l3.append(str(item)) #把各个元素字符化添加到l3列表中
    l3 = ", ".join(l3)   #join字符
    print('{' + l3 + '}') #打印最终结果

def code_derived_set(encoded_set):
    encoded_running_sum = 0
    l1 = []
    l2 = []
    l3 = []
    number = bin(encoded_set)[2:]  # 十进制转换二进制 并且去除'0b'
    for i in range(len(number)):
        l1.append(int(number[i]))  # 把二进制数分解 依次添加到l1列表中
    l1.reverse()  # 调换位置
    for i in range(len(l1)):
        if l1[i] == 1:  # 找到列表中数值为1的元素
            if i % 2 == 0:  # 位置为偶数
                a = int(i / 2)  # 找到对应值
                l2.append(a)
            else:
                a = int(-((i + 1) / 2))  # 位置为奇数 找到对应值
                l2.append(a)
    l2.sort()  # 从小到大排序
    l2.reverse() #调换位置
    la = []
    def mysum(l): #定义函数对列表里的元素进行递归相加
        la.append(sum(l))
        if not l:
            return 0
        else:
            return l[0] + mysum(l[1:])

    mysum(l2)
    la.remove(la[-1]) #移除最后的'0'元素
    lc = set(la)   #用set去重
    lb = []
    for item in lc:
        lb.append(item)
    lb.sort()
    lp = []
    for item in lb:
        if item < 0:  #求列表中每个元素所在的位置 比如-5 对应9
            lp.append(-(item * 2 + 1))
        else:
            lp.append(item * 2)
    lx = []
    if len(lp) == 0 : #空列表的情况
        return 0
    else:
        for i in range(max(lp)+1): #空列表里全部填0
            lx.append(0)
        for i in range(len(lx)):
            if i in lp: #在1的位置上改成1
                lx[i] = 1
        lx.reverse()
        lm = []
        for item in lx:
            lm.append(str(item)) #把每个数字变成str格式
        lm = ''.join(lm)   #用join函数连接各个字符
        q = int(lm, 2)  #把二进制整数化之后转换成十进制
        return q

print('The encoded set is: ', end = '')
display_encoded_set(encoded_set)
encoded_running_sum = code_derived_set(encoded_set)
print('The derived encoded set is: ', end = '')
display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)