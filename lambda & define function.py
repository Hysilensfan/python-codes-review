#define function
def add(i,j):
    result=i*j;print(" ".join(f"{i}*{j}={result}"),end="  ")
print(f"there are the multiplication table: ")
for index in range(81):
    i, j = index // 9 + 1 ,index % 9 + 1;add(i, j)
    while j == 9:print();break
