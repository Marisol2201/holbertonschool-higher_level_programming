#!/usr/bin/python3
"""inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        list_sort = sorted(self)
        print(list_sort)
