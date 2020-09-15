from os import environ
def path():
    home = environ.get("HOME")
    dir = home + '/' + 'TerminalToDo'
    return dir

f = open(path() + "/list.txt","w+")
