import sys,traceback
import mal_readline


def READ(i):
    return i

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
            print(rep(line))
        except Exception as e:
            print("".join(traceback.format_exception(*sys.exc_info())))
main()
