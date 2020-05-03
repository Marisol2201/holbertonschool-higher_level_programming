#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for hiddenfile in dir(hidden_4):
        if hiddenfile[0] != '_':
            print(hiddenfile)
