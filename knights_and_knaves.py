//
// COMP9021 Project 1
//
// Authors:
// Chongshi Wang
//
// Written: 31/03/2019
//
import sys
import re    #引用正则
import string
from itertools import product  #引用笛卡尔集
#第一步：开始输入
file_name = input('Which text file do you want to use for the puzzle? ')
with open(file_name) as file:
    text = file.read()   #读取文件
    text = text.replace("\n"," ")  #把几行文字变成一整行
text = re.sub('[.]"','".',text)   #把引号里面的？。！换到引号外面
text = re.sub('[!]"','"!',text)
text = re.sub('[?]"','"?',text)
newtext = re.split('[.!?]',text)  #根据？！。分割句子
#第一步结束 第二步开始
names=[]
name1=[]
name2=[]
name3=[]
name4=[]
name5=[]
name6=[]
sirs=[]
for i in range(len(newtext)):
    name1 += re.findall("Sir (\w+)",newtext[i]) #把每句话 Sir 后面的 name提取出来
    name2 += re.findall("Sirs (\w*) and (\w*)",newtext[i]) #把每句话 Sirs A and B 中的 A 和 B 提取出来
    name3 += re.findall("Sirs (\w*)((, \w*)*) and (\w*)", newtext[i]) #把多于两个Sir的所有名字提取出来
name1 = [x for x in name1 if x != []]  # 把name1、name2、name3中的空元素删除
name2 = [x for x in name2 if x != []]
name3 = [x for x in name3 if x != []]
print(name1)
for item in name2:
    for i in range(len(item)):
        name6.append(item[i]) # 把name2中每个元素分别添加到name6列表中
for item in name3:
    if len(item)==4:  # 处理两个以上sir时正则搜寻姓名时的重复情况
        name4.append(item[0])
        name4.append(item[1])
        name4.append(item[3])
    else:
        for i in range(len(item)):
            name4.append(i)
for item in name4:
    if item=="": #把name4中空字符删除
        name4.remove(item)
for item in name4:
    if item[0]!=",":
        name5.append(item)
    else:
        name5.append(item[2:])
names = name6 + name5 #实际上相当于name2+name3
sirs = name1 + names #实际上相当于name1+name2+name3
sirs=list(set(sirs))  #利用set去除重复
new_sirs = []
for item in sirs: #把sir大于2情况里几个用一个括号装着的名字用"，"分割分别填到新列表里
    if ',' in item:
        new_sirs += item.split(', ')
    else:
        new_sirs.append(item)
new_sirs = list(set(new_sirs))
new_sirs.sort()
#第二步结束
talking_sir=[]  #说话的speaker
talkings=[]     #说的话 引号里面的内容
l1=[] #说话者在后面
l2=[] #说话者在前面
for item in newtext:
    if '"' in item:
        l1 += re.findall('Sir (\w+).*(".*")',item) #sir："  " 第一种情况
        l2 += re.findall('(".*").*Sir (\w*)',item) #"  " ： Sir  第二种情况
for item in l1:
    talking_sir.append(item[0])  #把Sir填到第一个列表
    talkings.append(item[1])     #把说的话填到第二个列表
for item in l2:
    talking_sir.append(item[1])
    talkings.append(item[0])
#第三、第四步结束
m_names=[] #话语中提及的人
for i in range(len(talkings)):
    l_i=[]
    l_i += re.findall('Sir +(\w*)',talkings[i])
    if re.search('I ',talkings[i]):
        l_i.append(talking_sir[i])
    elif re.search('us ', talkings[i]):
        l_i+=(new_sirs)
    m_names.append(l_i)
#第五步结束
talkings_type=[] #讲说话的八种方式简化成6种
for i in range(len(talkings)):
    if re.search('least',talkings[i]): #at laest 是第一种
        talkings_type.append(1)
    elif re.search('[Ee]xactly',talkings[i]): #or 第一种
        talkings_type.append(3)
    elif re.search('most',talkings[i]): #most 第二种
        talkings_type.append(2)
    elif re.search('or ',talkings[i]): #exactly 第三种
        talkings_type.append(1)
    elif re.search('[Aa]ll', talkings[i]): #all 第四种
        talkings_type.append(4)
    elif re.search('I am', talkings[i]): # I am 第五种
        talkings_type.append(5)
    else:
        talkings_type.append(6)   #其他所有情况归类第六种
#第六步结束
judge_knights_and_knaves=[] #判断说的话是带有knight 还是 knave
for item in talkings:
    if re.search('Knights?',item): #如果是knight 添加knight
        judge_knights_and_knaves.append('Knight')
    elif re.search('Knaves?',item): #如果是knave  添加knave
        judge_knights_and_knaves.append('Knave')
#knight 和 knave 判断 结束
#print(new_sirs)
#print(talking_sir)
#print(talkings)
#print(m_names)
#print(talkings_type)
#print(judge_knights_and_knaves)
sirs_name_dict={}
for i in range(len(new_sirs )): #用一个集合把所有sir的名字在new_sirs列表中的位置表示出来
    sirs_name_dict[new_sirs[i]] = i
list_solution=list(product([0,1],repeat=int(len(new_sirs)))) #利用product功能生成笛卡尔集
for i in range(len(talkings)):
    if judge_knights_and_knaves[i] =='Knight': #如果说的话提及的是knight
        if talkings_type[i] ==1: #如果是第一种情况
            correct_solution = []
            for item in list_solution:
                sum = 0
                if item[sirs_name_dict[talking_sir[i]]] == 1: #if speaker is knight
                    for r in range(len(m_names[i])):
                        sum += item[sirs_name_dict[m_names[i][r]]]    #把每个涉及到的人所代表的数字加在一起
                    if sum >= 1:
                        correct_solution.append(item)
                if item[sirs_name_dict[talking_sir[i]]] == 0:  #if speaker is knave
                    for r in range(len(m_names[i])):
                        sum += item[sirs_name_dict[m_names[i][r]]] #把每个涉及到的人所代表的数字加在一起
                    if sum == 0:
                        correct_solution.append(item)
            list_solution = correct_solution #把经过处理的列表传递给笛卡尔集列表形成新的列表
        elif talkings_type[i] == 2: #如果是第二种情况
            correct_solution = []
            for item in list_solution:
                sum = 0
                if item[sirs_name_dict[talking_sir[i]]] == 1: #if speaker is knight
                    for r in range(len(m_names[i])):
                        sum += item[sirs_name_dict[m_names[i][r]]] #把每个涉及到的人所代表的数字加在一起
                    if sum <= 1:
                        correct_solution.append(item)
                if item[sirs_name_dict[talking_sir[i]]] == 0: #if speaker is knave
                    for r in range(len(m_names[i])):
                            sum += item[sirs_name_dict[m_names[i][r]]] #把每个涉及到的人所代表的数字加在一起
                    if sum > 1:
                            correct_solution.append(item)
            list_solution = correct_solution #把经过处理的列表传递给笛卡尔集列表形成新的列表
        elif talkings_type[i] == 3: #如果是第三种情况
            correct_solution = []
            for item in list_solution:
                sum = 0
                if item[sirs_name_dict[talking_sir[i]]] == 1: #if speaker is knight
                    for r in range(len(m_names[i])):
                        sum += item[sirs_name_dict[m_names[i][r]]] #把每个涉及到的人所代表的数字加在一起
                    if sum == 1:
                        correct_solution.append(item)
                if item[sirs_name_dict[talking_sir[i]]] == 0: #if speaker is knave
                    for r in range(len(m_names[i])):
                            sum += item[sirs_name_dict[m_names[i][r]]] #把每个涉及到的人所代表的数字加在一起
                    if sum != 1:
                        correct_solution.append(item)
            list_solution = correct_solution #把经过处理的列表传递给笛卡尔集列表形成新的列表
        elif talkings_type[i] == 4: #如果是第四种情况
            correct_solution = []
            for item in list_solution:
                sum = 0
                if item[sirs_name_dict[talking_sir[i]]] == 1: #if speaker is knight
                    for r in range(len(m_names[i])):
                        sum += item[sirs_name_dict[m_names[i][r]]] #把每个涉及到的人所代表的数字加在一起
                    if sum == len(new_sirs):
                        correct_solution.append(item)
                if item[sirs_name_dict[talking_sir[i]]] == 0: #if speaker is knave
                    for r in range(len(m_names[i])):
                            sum += item[sirs_name_dict[m_names[i][r]]] #把每个涉及到的人所代表的数字加在一起
                    if sum != len(new_sirs):
                        correct_solution.append(item)
            list_solution = correct_solution #把经过处理的列表传递给笛卡尔集列表形成新的列表
        elif talkings_type[i] == 5: #如果是第五种情况
            correct_solution = []
            for item in list_solution:
                sum = 0
                if item[sirs_name_dict[talking_sir[i]]] == 1: #if speaker is knight
                    for r in range(len(m_names[i])):
                        sum += item[sirs_name_dict[m_names[i][r]]] #把每个涉及到的人所代表的数字加在一起
                    if sum == 1:
                        correct_solution.append(item)
                if item[sirs_name_dict[talking_sir[i]]] == 0: #if speaker is knave
                    for r in range(len(m_names[i])):
                            sum += item[sirs_name_dict[m_names[i][r]]] #把每个涉及到的人所代表的数字加在一起
                    if sum ==0:
                        correct_solution.append(item)
            list_solution = correct_solution #把经过处理的列表传递给笛卡尔集列表形成新的列表
        elif talkings_type[i] == 6: #如果是第六种情况
            correct_solution = []
            for item in list_solution:
                sum = 0
                if item[sirs_name_dict[talking_sir[i]]] == 1: #if speaker is knight
                    for r in range(len(m_names[i])):
                        sum += item[sirs_name_dict[m_names[i][r]]] #把每个涉及到的人所代表的数字加在一起
                    if sum == len(m_names[i]):
                        correct_solution.append(item)
                if item[sirs_name_dict[talking_sir[i]]] == 0: #if speaker is knave
                    for r in range(len(m_names[i])):
                            sum += item[sirs_name_dict[m_names[i][r]]] #把每个涉及到的人所代表的数字加在一起
                    if sum != len(m_names[i]):
                        correct_solution.append(item)
            list_solution = correct_solution #把经过处理的列表传递给笛卡尔集列表形成新的列表
    if judge_knights_and_knaves[i] == 'Knave': #如果说的话提及的是knight
        if talkings_type[i] ==1: #如果是第一种情况
            correct_solution=[]
            for item in list_solution:
                sum = 0
                if item[sirs_name_dict[talking_sir[i]]] == 1: #if speaker is knight
                    for r in range(len(m_names[i])):
                        sum += item[sirs_name_dict[m_names[i][r]]]
                    if sum <= len(m_names[i])-1:
                        correct_solution.append(item)
                if item[sirs_name_dict[talking_sir[i]]] == 0: #if speaker is knave
                    for r in range(len(m_names[i])):
                        sum += item[sirs_name_dict[m_names[i][r]]]
                    if sum == len(m_names[i]):
                        correct_solution.append(item)
            list_solution = correct_solution #把经过处理的列表传递给笛卡尔集列表形成新的列表
        elif talkings_type[i] == 2: #如果是第二种情况
            correct_solution = []
            for item in list_solution:
                sum = 0
                if item[sirs_name_dict[talking_sir[i]]] == 1: #if speaker is knight
                    for r in range(len(m_names[i])):
                        sum += item[sirs_name_dict[m_names[i][r]]]
                    if sum >= len(m_names[i])-1:
                        correct_solution.append(item)
                if item[sirs_name_dict[talking_sir[i]]] == 0: #if speaker is knave
                    for r in range(len(m_names[i])):
                            sum += item[sirs_name_dict[m_names[i][r]]]
                    if sum < len(m_names[i])-1:
                            correct_solution.append(item)
            list_solution = correct_solution #把经过处理的列表传递给笛卡尔集列表形成新的列表
        elif talkings_type[i] == 3: #如果是第三种情况
            correct_solution = []
            for item in list_solution:
                sum = 0
                if item[sirs_name_dict[talking_sir[i]]] == 1: #if speaker is knight
                    for r in range(len(m_names[i])):
                        sum += item[sirs_name_dict[m_names[i][r]]]
                    if sum == len(m_names[i])-1:
                        correct_solution.append(item)
                if item[sirs_name_dict[talking_sir[i]]] == 0: #if speaker is knave
                    for r in range(len(m_names[i])):
                            sum += item[sirs_name_dict[m_names[i][r]]]
                    if sum != len(m_names[i])-1:
                        correct_solution.append(item)
            list_solution = correct_solution #把经过处理的列表传递给笛卡尔集列表形成新的列表
        elif talkings_type[i] == 4: #如果是第四种情况
            correct_solution = []
            wrong_solution=[]
            for item in list_solution:
                sum = 0
                if item[sirs_name_dict[talking_sir[i]]] == 1:
                    wrong_solution.append(item)
                if item[sirs_name_dict[talking_sir[i]]] == 0: #if speaker is knave
                    for r in range(len(m_names[i])):
                            sum += item[sirs_name_dict[m_names[i][r]]]
                    if sum > 0:
                        correct_solution.append(item)
            correct_solution = list(set(correct_solution) - set(wrong_solution))
            list_solution = correct_solution #
        elif talkings_type[i] == 5: #如果是第五种情况
            correct_solution = []
            for item in list_solution:
                if item[sirs_name_dict[talking_sir[i]]] == 1:
                    correct_solution.append(item)
                if item[sirs_name_dict[talking_sir[i]]] == 0:
                    correct_solution.append(item)
            list_solution = list(set(list_solution)-set(correct_solution))
        elif talkings_type[i] == 6: #如果是第六种情况
            correct_solution =[]
            for item in list_solution:
                sum = 0
                if item[sirs_name_dict[talking_sir[i]]] == 1: #if speaker is knight
                    for r in range(len(m_names[i])):
                        sum += item[sirs_name_dict[m_names[i][r]]]
                    if sum == 0:
                        correct_solution.append(item)
                if item[sirs_name_dict[talking_sir[i]]] == 0: #if speaker is knave
                    for r in range(len(m_names[i])):
                            sum += item[sirs_name_dict[m_names[i][r]]]
                    if sum > 0:
                        correct_solution.append(item)
            list_solution = correct_solution  #把经过处理的列表传递给笛卡尔集列表形成新的列表
print(f"The Sirs are: {' '.join(item for item in new_sirs)}") #print 所有sirs的姓名
if len(list_solution) == 0: #没有solution的情况
    print(f"There is no solution.")
if len(list_solution) > 1: #solution大于1的情况
    print(f"There are {len(list_solution)} solutions.")
if len(list_solution) == 1 :#solution等于1的情况
    print(f"There is a unique solution:")
    l_kight_knave=[] #用列表把0，1转化成 "knave" and "knight"
    for i in range(len(list_solution[0])):
        if list_solution[0][i] == 0:
            l_kight_knave .append('Knave')
        elif list_solution[0][i] == 1:
            l_kight_knave.append('Knight')
    for i in range(len(new_sirs)):
        print(f"Sir {new_sirs[i]} is a {l_kight_knave[i]}.")
