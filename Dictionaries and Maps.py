# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
d={}

for i in range(n):
    name,number=input().split()
    d[name]=int(number)


while True:
    try:
        name=input()
        if name in d:
            print(f'{name}={d[name]}')
        else:
            print("Not found")
    except EOFError:
        break
