Example 1: 

For num() function we are applying 2 decorator functions. Firstly the inner decorator will work and then the outer decorator.


# code for testing decorator chaining
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
Output:

400


     

        
