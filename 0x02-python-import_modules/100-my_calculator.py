#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) < 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)


    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == "+":
        r = add(a, b)
    elif operator == "-":
        r = sub(a, b)
    elif operator == "*":
        r = mul(a, b)
    elif operator == "/":
        r = div(a, b)
    else:
        print("Unknown opertaor. Available operator: +, -, * and /")
        sys.exit(1)


    print("{} {} {} = {}".format(a, operator, b, r))
