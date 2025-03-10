'''python
def decorator(func):
    def wrapper():
        func()
    return wrapper

@decorator
def add():
    print("hello")
    return "hello"
data = decorator(add)
print(data())'''

'''python
def decorator(func):
    def wrapper(*args,**kw):
        result=func(*args,**kw)
        return result
    return wrapper

@decorator
def add(name,age):
    print(f"my name is {name},my age is {age}")
    return "done"

data=add("mohini",21)
print(data)'''


