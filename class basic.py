#Code Comparison(just using define function)
add = lambda i,j:print(" ".join(f"{i}*{j}={i*j}"),end="  ")
print(f"there are the multiplication table: ")
for index in range(81):
    i, j = index // 9 + 1 ,index % 9 + 1;add(i, j)
    while j == 9:print();break
#Code Comparison(using class)
class Multiplicationtable(object):
    def __init__(self):
        self.staringvalueI=1;self.staringvalueII=1;self.result=0
    def add(self):
        self.result=self.staringvalueI * self.staringvalueII;print(" ".join(f"{self.staringvalueI}*{self.staringvalueII}={self.result}"),end="  ")
mt = Multiplicationtable();print(f"there are the multiplication table: ")
for _ in range(9):
    for _ in range(9):
        mt.add();mt.staringvalueII +=1
    print();mt.staringvalueII = 1;mt.staringvalueI+=1
