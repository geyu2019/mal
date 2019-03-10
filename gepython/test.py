#!/home/geyu/anaconda3/bin/python
import sys
def to_list(parenthesis_exp):
    q_list=[]
    first_parenthesis=0
    isword = 0
    word = ''
    exp  = ''
    for letter in parenthesis_exp:
        print(letter)
        if letter=='(' :
            first_parenthesis += 1
            if first_parenthesis != 1:
                exp = '('
            continue
        elif  letter == ')' :
            first_parenthesis -= 1
            if first_parenthesis != 0:
                exp += ')'
                q_list.append(exp)
                exp = ''
            continue
        if first_parenthesis == 1 and not word  and (letter != ' ' or letter != '\t' ):
            word += letter
        elif first_parenthesis == 1 and word  and (letter != ' ' or letter != '\t' ):
            word += letter
        elif first_parenthesis == 1 and word  and (letter == ' ' or letter == '\t' ):
            q_list.append(word)
            word = ''
        elif first_parenthesis != 1 :
            exp += letter
    index = 0
    tem_list = []
    print(q_list)
    for i in q_list:

        if i[0] != '(' :
            pass
        elif i[0] == '(':
            tem_list = to_list(i)
            q_list[index] = tem_list
        index += 1
    return q_list
print(sys.argv[1])
list=to_list(sys.argv[1])
print(list)
