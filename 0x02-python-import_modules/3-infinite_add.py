#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argvL = len(sys.argv) - 1
    sumResult = 0
    if argvL >= 1:
        for i in range(argvL):
            sumResult += int(sys.argv[i + 1])
        print(sumResult)
    else:
        print(argvL)
