import os , sys, readline as pyreadline
history_file = os.path.expanduser("~/.mal-history")
history_loaded = False

def readline(prompt="user> "):
    global history_loaded
    #检验history是否载入，若没有，先载入
    if not history_loaded:
        history_loaded=True
        try:
            with open(history_file,'r') as f:
                for line in f.readlines():
                    pyreadline.add_history(line.rstrip("\r\n"))
                pass
        except IOError:
            #
            pass
    #读用户输入行
    try :
        line = input(prompt)
        pyreadline.add_history(line)

        with open(history_file,'a') as f:
            f.write(line+'\n')
    except IOError:
        pass
    except EOFError:
        return None
    return line
