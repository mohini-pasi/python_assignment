```pythondef default_argument(a,b,c,d=1,e=1):
    sum=a+b+c+d+e
    return sum
data = default_argument(a=10,b=20,c=30,d=40,e=50)
print(data)          #output 150


def default_argument2(a,b,c,d=1,e=1):
    sum=a+b+c+d+e
    return sum
data2 = default_argument2(a=10,b=20,c=30,d=40)
print(data2)    
```
#output 101
