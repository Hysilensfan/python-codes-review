# we don’t create any functions ourselves ,so import can load from function library to introduce function that already established
# import (function library)
import random
n = input()
if n == "I want to play this":
    print(random.randint(1,87))
else:
    pass


# import (function library) as (Customize name)
import random as x
n = input()
if n == "I want to play this"and n != "?":
    print(x.randint(1,87))
else:
    if n == "?":
        print("don't be confuse😒")
    pass


# from (function library) import (function/class /variable)
from random import randint
n = input()
if n == "I want to play this"and n != "?":
    print(randint(1,87))
else:
    if n == "?":
        print("don't be confuse😒")
    pass


# from (function library) import (function/class /variable) as (Customize name)
from random import randint as x
n = input()
if n == "I want to play this"and n != "?":
    print(x(1,87))
else:
    if n == "?":
        print("don't be confuse😒")
    pass
