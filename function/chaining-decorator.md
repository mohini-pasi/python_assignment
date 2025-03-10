What is Decorator In Python?
A decorator is a function that can take a function as an argument and extend its functionality and return a modified function with extended functionality.


So, here in this post, we are going to learn about Decorator Chaining. Chaining decorators means applying more than one decorator inside a function. Python allows us to implement more than one decorator to a function. It makes decorators useful for reusable building blocks as it accumulates several effects together. It is also known as nested decorators in Python. we will also see Python decorator examples.

Syntax of decorator in python
@decor1
@decor
def num():
    statement(s)    
    Example 1: 

For num() function we are applying 2 decorator functions. Firstly the inner decorator will work and then the outer decorator.


# code for testing decorator chaining
  ```python
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor
def num():
    return 10

print(num())
```


Output:

400


     

        
