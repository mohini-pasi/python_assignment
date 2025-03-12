#TYPE CONVERSION
# str to int = a="abc" can't convert into int
a="123"
b=int(a)
print(b,type(b))

# int to str
a=10
b=str(a)
print(b,type(b))

#str handling
a="DCODETECH"
b="dcodetech"
print(a.lower()==b.lower())

a="DCODETECH"
print(a.lower())

a=" hello world "
print(a.strip())   # remove whitespace

b="hello, world!"
print(b[6])

#slicing
a="hello world"
print(a[2:7]) #output will llo w

a="hello world"
print(a[ :7])    #output will hello w

a="hello world"
print(a[1: ])    #output will ello world





