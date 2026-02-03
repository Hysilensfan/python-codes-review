#Code Comparison(just using define function)
add = lambda i,j:print(" ".join(f"{i}*{j}={i*j}"),end="  ")
print(f"there are the multiplication table: ")
for index in range(81):
    i, j = index // 9 + 1 ,index % 9 + 1;add(i, j)
    while j == 9:print();break


#Code Comparison(using class)
#ex1:
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


#ex2:
class Archer:
    def __init__(self):
        self.bone = "sword"
        self.body = "steel"
        self.blood = "fire"
        self.blades_created = 1000
        self.alive = False
        self.dead = False

    def unlimited_blade_works(self):
        print(f"I am the bone of my {self.bone}.")
        print(f"{self.body} is my body, and {self.blood} is my blood.")
        print(f"I have created over {self.blades_created} blades, "
        print(f"Unknown to Death, Nor known to Life"if not self.alive and not self.dead)
        print("As I pray...")
        print("Unlimited Blade Works!")
archer = Archer()
archer.unlimited_blade_works()
