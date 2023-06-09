#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argvL = len(sys.argv) - 1
    if argvL == 0:
        print("{} arguments.".format(argvL))
    elif argvL > 1:
        print("{:d} arguments:".format(argvL))
        for i in range(argvL):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
    elif argvL == 1:
        print("{} argument:".format(argvL))
        print("{}: {}".format(argvL, sys.argv[argvL]))

