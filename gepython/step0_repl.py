import sys,traceback
import mal_readline
express_over = False
#规则，1.去最外层括号 2.如果是word不处理，3.如果是括号，取出带有这对括号的表达式
       #分割，填入q_list
def to_list(parenthesis_exp):
    q_list=[]
    first_parenthesis=0
    isword = 0
    word = ''
    exp  = ''
    for letter in parenthesis_exp:
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
    for i in q_list:

        if i[0] != '(' :
            pass
        elif i[0] == '(':
            tem_list = to_list(i)
            q_list[index] = tem_list
        index += 1
    return q_list



def continue_read (line):
#判断第一组括号是否完成
            #完成则将所有输出给rep，未完成则等待完成
    done = exp_done(line)
    if not done:
        str_exp = ''
        str_exp = line.rstrip("\r\n")
        put_in_done=False
        while  not  put_in_done:
            line_sub = mal_readline.readline("> ")
            str_exp +=' '+line_sub.rstrip("\r\n")
            put_in_done=exp_done(str_exp)
        lines = str_exp
    else :
        lines = line
    return lines
def exp_done(lines):
    num = 0
    for word in lines:
        if word == '(' :
            num +=1
        elif word == ')' :
            num -=1
        else :
            pass
    if num == 0 :
        return True
    else :
        return False



def READ(line):

    #提取 oprand 与 express


    return line

def EVAL(i,env):
    return i

def PRINT(i):
    return i

def rep(i):
    return PRINT(EVAL(READ(i),{}))


def main():
    while True:
        try:
            line = mal_readline.readline("user> ")
            if line == None:
                break
            if line == '':
                continue
            lines=continue_read(line)
            print(rep(lines))
        except Exception as e:
            print("".join(traceback.format_exception(*sys.exc_info())))
main()
