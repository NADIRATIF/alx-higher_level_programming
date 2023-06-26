def safe_print_list(my_list=[], x=0):
    c = 0

    try:
        for e in my_list:
            if c < x:
                print(e, end=" ")
                c += 1
            else:
                break
        print()
    except:
        pass

    return c
