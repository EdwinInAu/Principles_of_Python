# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and determines the size of the largest
# isosceles triangle, consisting of nothing but 1s and whose base can be either
# vertical or horizontal, pointing either left or right or up or down.
#
# Written by Chongshi Wang and Eric Martin for COMP9021

from random import seed, randint
import sys

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def size_of_largest_isosceles_triangle():
    l=[] 
    def south(): #三角形顶点方向向南
        l1=[0]
        for item in grid:  #对grid进行操作 变成10个子列表 当子列表中的元素不为0时 元素变为1
            for i in range(len(item)):
                if item[i] != 0:
                    item[i] = 1
        g = grid #让g列表等于grid
        for i in range(6): #从上往下六行
                for j in range(8): #每行内从0到8检索
                    if g[i][j] == 1  and g[i][j+1] == 1 and g[i][j+2] == 1 and g[i+1][j+1] != 0: #如果连续三个1并且中间元素下面一行对应的元素不是0 则变为2
                        g[i+1][j+1] = 2
                        l1.append(2)
                for j in range(8):
                    if g[i+1][j] == 2 and g[i+1][j+1] == 2 and g[i+1][j+2] == 2 and g[i+2][j+1] != 0: #如果连续三个2并且中间元素下面一行对应的元素不是0 则变为3
                        g[i+2][j+1] = 3
                        l1.append(3)
                for j in range(8):
                    if g[i+2][j] == 3 and g[i+2][j+1] == 3 and g[i+2][j+2] == 3 and g[i+3][j+1] != 0: #如果连续三个3并且中间元素下面一行对应的元素不是0 则变为4
                        g[i+3][j+1] = 4
                        l1.append(4)
                for j in range(8):
                    if g[i+3][j] == 4 and g[i+3][j+1] == 4 and g[i+3][j+2] == 4 and g[i+4][j+1] != 0: #如果连续三个4并且中间元素下面一行对应的元素不是0 则变为5
                        g[i+4][j+1] = 5
                        l1.append(5)
                for item in g:  #每次更新g列表变为初始状态
                    for a in range(len(item)):
                        if item[a] != 0:
                            item[a] = 1
        l1.sort()
        return(l1[-1]) #return列表中最大值

    def north(): #三角形顶点方向向北
       l2 = [0] 
       for item in grid: #对grid进行操作 变成10个子列表 当子列表中的元素不为0时 元素变为1
           for i in range(len(item)):
               if item[i] != 0:
                   item[i] = 1
       h = grid #让h列表等于grid
       for i in range(9,3,-1): #从第10行开始往上检索到第5行停止
            for j in range(8): #每行内从0到8检索
                if h[i][j] == 1  and h[i][j+1] == 1 and h[i][j+2] == 1 and h[i-1][j+1] != 0: #如果连续三个1并且中间元素上面一行对应的元素不是0 则变为2
                    h[i-1][j+1] = 2
                    l2.append(2)
            for j in range(8):
                if h[i-1][j] == 2 and h[i-1][j+1] == 2 and h[i-1][j+2] == 2 and h[i-2][j+1] != 0: #如果连续三个2并且中间元素上面一行对应的元素不是0 则变为3
                    h[i-2][j+1] = 3
                    l2.append(3)
            for j in range(8):
                if h[i-2][j] == 3 and h[i-2][j+1] == 3 and h[i-2][j+2] == 3 and h[i-3][j+1] != 0: #如果连续三个3并且中间元素上面一行对应的元素不是0 则变为4
                    h[i-3][j+1] = 4
                    l2.append(4)
            for j in range(8):
                if h[i-3][j] == 4 and h[i-3][j+1] == 4 and h[i-3][j+2] == 4 and h[i-4][j+1] != 0: #如果连续三个4并且中间元素上面一行对应的元素不是0 则变为5
                    h[i-4][j+1] = 5
                    l2.append(5)
            for item in h: #每次更新h列表变为初始状态
                for y in range(len(item)):
                    if item[y]!= 0:
                        item[y] = 1
       l2.sort()
       return(l2[-1]) #return列表中最大值

    def east(): #三角形顶点方向向东
        l3 = [0]
        for item in grid: #对grid进行操作 变成10个子列表 当子列表中的元素不为0时 元素变为1
            for i in range(len(item)):
                if item[i] != 0:
                    item[i] = 1
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        g=[]
        h=[]
        i=[]
        j=[]
        k=[]
        for item in grid: #把grid中每个item的第1-10位元素分别放到10个列表中
            a.append(item[0])
            b.append(item[1])
            c.append(item[2])
            d.append(item[3])
            e.append(item[4])
            f.append(item[5])
            g.append(item[6])
            h.append(item[7])
            i.append(item[8])
            j.append(item[9])
        k.append(a) #把10个子列表按照0-10顺序分别添加到k列表中
        k.append(b)
        k.append(c)
        k.append(d)
        k.append(e)
        k.append(f)
        k.append(g)
        k.append(h)
        k.append(i)
        k.append(j)
        for i in range(6): #从上往下六行
                for j in range(8): #每行内从0到8检索
                    if k[i][j] == 1  and k[i][j+1] == 1 and k[i][j+2] == 1 and k[i+1][j+1] != 0: #如果连续三个1并且中间元素上面一行对应的元素不是0 则变为2
                        k[i+1][j+1] = 2
                        l3.append(2)
                for j in range(8):
                    if k[i+1][j] == 2 and k[i+1][j+1] == 2 and k[i+1][j+2] == 2 and k[i+2][j+1] != 0: #如果连续三个2并且中间元素上面一行对应的元素不是0 则变为3
                        k[i+2][j+1] = 3
                        l3.append(3)
                for j in range(8):
                    if k[i+2][j] == 3 and k[i+2][j+1] == 3 and k[i+2][j+2] == 3 and k[i+3][j+1] != 0: #如果连续三个3并且中间元素上面一行对应的元素不是0 则变为4
                        k[i+3][j+1] = 4
                        l3.append(4)
                for j in range(8):
                    if k[i+3][j] == 4 and k[i+3][j+1] == 4 and k[i+3][j+2] == 4 and k[i+4][j+1] != 0: #如果连续三个4并且中间元素上面一行对应的元素不是0 则变为5
                        k[i+4][j+1] = 5
                        l3.append(5)
                for item in k: #每次更新k列表变为初始状态
                    for a in range(len(item)):
                        if item[a] != 0:
                            item[a] = 1
        l3.sort()
        return(l3[-1]) #return列表中最大值

    def west(): #三角形顶点方向向西
        l4 = [0]
        for item in grid: #对grid进行操作 变成10个子列表 当子列表中的元素不为0时 元素变为1
            for i in range(len(item)):
                if item[i] != 0:
                    item[i] = 1
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        g=[]
        h=[]
        i=[]
        j=[]
        k=[]
        for item in grid: #把grid中每个item的第1-10位元素分别放到10个列表中
            a.append(item[0])
            b.append(item[1])
            c.append(item[2])
            d.append(item[3])
            e.append(item[4])
            f.append(item[5])
            g.append(item[6])
            h.append(item[7])
            i.append(item[8])
            j.append(item[9])
        k.append(j) #把10个子列表按照10-0顺序分别添加到k列表中
        k.append(i)
        k.append(h)
        k.append(g)
        k.append(f)
        k.append(e)
        k.append(d)
        k.append(c)
        k.append(b)
        k.append(a)
        for i in range(6): #从上往下六行
                for j in range(8): #每行内从0到8检索
                    if k[i][j] == 1  and k[i][j+1] == 1 and k[i][j+2] == 1 and k[i+1][j+1] != 0: #如果连续三个1并且中间元素上面一行对应的元素不是0 则变为2
                        k[i+1][j+1] = 2
                        l4.append(2)
                for j in range(8):
                    if k[i+1][j] == 2 and k[i+1][j+1] == 2 and k[i+1][j+2] == 2 and k[i+2][j+1] != 0: #如果连续三个2并且中间元素上面一行对应的元素不是0 则变为3
                        k[i+2][j+1] = 3
                        l4.append(3)
                for j in range(8):
                    if k[i+2][j] == 3 and k[i+2][j+1] == 3 and k[i+2][j+2] == 3 and k[i+3][j+1] != 0: #如果连续三个3并且中间元素上面一行对应的元素不是0 则变为4
                        k[i+3][j+1] = 4
                        l4.append(4)
                for j in range(8):
                    if k[i+3][j] == 4 and k[i+3][j+1] == 4 and k[i+3][j+2] == 4 and k[i+4][j+1] != 0: #如果连续三个4并且中间元素上面一行对应的元素不是0 则变为5
                        k[i+4][j+1] = 5
                        l4.append(5)
                for item in k: #每次更新k列表变为初始状态
                    for a in range(len(item)):
                        if item[a] != 0:
                            item[a] = 1
        l4.sort()
        return(l4[-1]) #return列表中最大值
    l.append(south()) #把south,north,west and east 四个功能运行的结果添加到l列表中
    l.append(north())
    l.append(east())
    l.append(west())
    l.sort()
    return l[-1] #return列表中最大值
try:
    arg_for_seed, density = (abs(int(x)) for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
print('The largest isosceles triangle has a size of',
      size_of_largest_isosceles_triangle()
      )