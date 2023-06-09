#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for name in names:
        print("{}".format(name)) if name[:2] != "__" else None
