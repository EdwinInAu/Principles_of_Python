# Written by Chongshi Wang for COMP9021

import sys
from random import seed, randint, randrange

try:
    arg_for_seed, upper_bound, length =\
            (int(x) for x in input('Enter three integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

def length_of_longest_increasing_sequence(L):
    if len(L) == 0:
        return 0
    if len(set(L)) == 1:
        return len(L)
    l = L * 2
    x = 1
    list = []
    for i in range(len(L)*2-1):
        if l[i] <= l[i+1]:
            x = x + 1
            list.append(x)
        else:
            x = 1
    list.sort()
    return list[-1]

def max_int_jumping_in(L):
    if len(L) == 0:
        return None
    list2=[]
    for i in range(len(L)):
        list1 = []
        list3 = []
        while i not in list3 and i < len(L):
            list3.append(i)
            list1.append(L[i])
            i = L[i]
        b = "".join(str(v) for v in list1)
        list2.append(int(b))
    list2.sort()
    return list2[-1]

seed(arg_for_seed)
L_1 = [randint(0, upper_bound) for _ in range(length)]
print('L_1 is:', L_1)
print('The length of the longest increasing sequence\n'
      '  of members of L_1, possibly wrapping around, is:',
      length_of_longest_increasing_sequence(L_1), end = '.\n\n'
     )
L_2 = [randrange(length) for _ in range(length)]
print('L_2 is:', L_2)
print('The maximum integer built from L_2 by jumping\n'
      '  as directed by its members, from some starting member\n'
      '  and not using any member more than once, is:',
      max_int_jumping_in(L_2)
     )



