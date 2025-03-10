def arbitrary_agrument(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum
data=arbitrary_agrument(12,23,34,45,45)
print(data)          #output 159