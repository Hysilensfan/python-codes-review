# define multiplication table function
def add(i,j):
    result=i*j;print(" ".join(f"{i}*{j}={result}"),end="  ")
print(f"there are the multiplication table: ")
for index in range(81):
    i, j = index // 9 + 1 ,index % 9 + 1;add(i, j)
    while j == 9:print();break
# using a lambda function to print the multiplication table
add = lambda i,j:print(" ".join(f"{i}*{j}={i*j}"),end="  ")
print(f"there are the multiplication table: ")
for index in range(81):
    i, j = index // 9 + 1 ,index % 9 + 1;add(i, j)
    while j == 9:print();break
|
|
|
|
|
#Usage:
c=lambda d:d-4 # Here c is a lambda function, which is like a tiny function we write in one line. It returns d minus 4
d=int(input());print(c(d))
def c(d): # Here c is a normal function. It does the same thing: subtract 4. But it’s written in multiple lines and has a name r inside
    r = d-4;return r
d=int(input());print(c(d))
c=lambda a,b:a*b # Lambda can take more than one input. Here a and b are multiplied and returned
a,b=map(int,input().split());print(c(a,b))
d=lambda a,b,c:b**2-4*a*c # Here lambda returns b² - 4ac
a,b,c=map(int,input().split());print(d(a,b,c))
