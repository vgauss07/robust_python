from typing import Iterable
def print_items(items: Iterable):
    """
    Duck Typing:
        objects and entities
        adhering to some interface
    """
    for item in items:
        print(item)

# printing only items that are iterable
print_items([1, 2, 3])
print_items({4, 5, 6})
print_items({'A':1, "B":2, "C":3})