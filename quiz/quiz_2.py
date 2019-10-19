# Written by Chongshi Wang for COMP9021

def rule_encoded_by(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    values = [int(d) for d in f'{rule_nb:04b}']
    return {(p // 2, p % 2): values[p] for p in range(4)}

def describe_rule(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    rule = rule_encoded_by(rule_nb)
    print('The rule encoded by', rule_nb, 'is: ', rule)
    print()
    for key in rule:
        print('After '+str(key[0])+' followed by '+str(key[1])+', we draw '+str(rule[key]))
        
def draw_line(rule_nb, first, second, length):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    "first" and "second" are supposed to be the integer 0 or the integer 1.
    "length" is supposed to be a positive integer (possibly equal to 0).

    Draws a line of length "length" consisting of 0's and 1's,
    that starts with "first" if "length" is at least equal to 1,
    followed by "second" if "length" is at least equal to 2,
    and with the remaining "length" - 2 0's and 1's determined by "rule_nb".
    '''
    rule = rule_encoded_by(rule_nb)
    if length == 0:
        print('')
    elif length == 1:
        print(str(first))
    elif length == 2:
        print(str(first), str(second))
    elif length > 2:
        l = [first, second]
        for a in range(length - 2):
            l.append(rule[l[-2], l[-1]])
        print("".join(str(v) for v in l))

def uniquely_produced_by_rule(line):
    '''
    "line" is assumed to be a string consisting of nothing but 0's and 1's.

    Returns an integer n between 0 and 15 if the rule encoded by n is the
    UNIQUE rule that can produce "line"; otherwise, returns -1.
    '''
    l = [int(x) for x in line]
    false = -1
    if len(l) < 6:
        return false
    for v in l:
        if v != 0 and v != 1:
            return false
    dict_rule = {}
    addition_list = []
    for r in range(16):
        rule_list = [l[0], l[1]]
        dict_rule = rule_encoded_by(r)
        for i in range(len(l)-2):
            rule_list.insert(i+2,dict_rule[rule_list[-2], rule_list[-1]])
        if l == rule_list:
            addition_list.insert(i,r)
    if len(addition_list) == 1:
        return addition_list[0]
    else:
        return false