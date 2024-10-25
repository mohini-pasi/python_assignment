#python-assingment(Dcodetech)
#here are some python question'

**1.write a program to find given number is even or odd**
```python
number = int(input("enter a number:"))
if(number % 2 == 0):
    print("it is even number")
else: 
    print("it is odd number")
```
with function
```python
def evenodd(num):
    if(num%2)==0:
        print("it is even number")
    else:
        print("it is odd number")
evenodd(23)
evenodd(34)
evenodd(0)
```

**2. write a program to find given number is positive or negative**
```python
number = int(input("ENTER YOUR NUMBER:"))

if(number>=0):
    print("IT'S A POSITIVE NUMBER")
else:
    print("IT'S A NEGATIVE NUMBER")
```
with function
```python
def positivenegative(num):
    if(num>=0):
        print("it is positive number")
    else:
        print("it is negative number")
positivenegative(23)
```

**3.write a program to find a sum of two number**
```python
a=10
b=20
c=a+b
print("c=",c)
```
with function
```python
def sum(a,b):
    c=a+b
    print(c)
sum(20,23)
```

**4.write a program to check given number is palindrome**
```python
string=input("enter string")
if(string==string[::-1]):
    print("the string is palindrome")
else:
    print("the string is not palindrome")
```
with function
```python
def palindorme(string):
    if(string==string[::-1]):
        print("the string is palindrome")
    else:
        print("the string is not palindrome")
palindorme("moim")
```

**5.write a prgram to check given string is palindrome and ignore special character and space**
```python
def palindorme(string):
    a=[]
    print(string)
    for i in string:
        if i == "%" or i == " " or i == "$" or i=="&":
            continue
        a.append(i)
    print(a)

    if(a==a[::-1]):
            print("the string is palindrome")
    else:
            print("the string is not palindrome")
 
palindorme("moh%%om l")
```

**6.write a program to check armstrong number**
```python
num=int(input("enter your number"))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
```
with function
```python
def armstrong():

   num=int(input("enter your number"))   
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
      digit = temp % 10
      sum += digit ** order
      temp //= 10
   if num == sum:
      print(num,"is an Armstrong number")
   else:
      print(num,"is not an Armstrong number")
armstrong()
```

**7.write a program to check given string is anagram or not**
```python
a="silent"
b="listen"
c=list(a)
d=list(b)

if (sorted(c) == sorted(d)):
    print("its a anagram")
else:
    print("its not a anagram")
```
with function
```python
def armstrong():

   num=int(input("enter your number"))   
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
      digit = temp % 10
      sum += digit ** order
      temp //= 10
   if num == sum:
      print(num,"is an Armstrong number")
   else:
      print(num,"is not an Armstrong number")
armstrong()
```

**8.write a program to find max of two number**
```python
number = max(12,34,45,56)
print(number)
```
with if-elif
```python
a= int(input("enter a value of a"))
b= int(input("enter a value of b"))
if(a>b):
    print("a is max")
elif(b>a):
    print("b is max")
else:
    print("both are equal")
```

**9.write a program to find factorial of a number**
```python
n = int(input("ENTER THE NUMBER:"))
sum=1
for i in range(1,n+1):
    sum = sum*i
    print(sum)
```
with function
```python
def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum= sum*i
        print(sum)
factorial(5)    
```

**10.write a program to find fibonacci series**

a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
The simplest is the series 1, 1, 2, 3, 5, 8, etc.

FIRST 0 1 IS BY DEFAULT

0 + 1 = 1
    1 + 1 = 2
        1 + 2 = 3
            2 + 3 = 5
                3 + 5 = 8
                    5 + 8 = 13
                        8 + 13 = 21
                            13 + 21 = 34
                                 21 + 34 = 55 
"""
Program to display the Fibonacci sequence up to n-th term
```python
number = int(input("Enter the number? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if number <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif number == 1:
   print("Fibonacci sequence upto",number,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < number:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth   #nth meaning the last sum of number 
       count += 1
```

**11.write a program to print diamond pattern**
```python
h = int(input("please enter diamond's height:"))

for i in range(h):
    print(" "*(h-i), "*"*(i*2+1))
for i in range(h-2, -1, -1):
    print(" "*(h-i), "*"*(i*2+1))
```

**12.write a program for the function that take input as a list and find the even number from the list and return a new list with the even number data**
```python
def function(input_list : list)->list:
    even_numbers = []
    for num in input_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
print(function([12,23,22]))
```

**13.write a program to take num as a input and print the table from 1 to 10**
```python

def table():
    num = int(input("Enter a number: "))
    for i in range(1,11):
        print(num,'*',i,'=',num*i)
table()
```

**14.write a program that will take a list as an input and insdie that list convert in key value pair**
```python
def list_to_dict(input_list):

    output_dict = {}
    for i, element in enumerate(input_list):
        output_dict[i] = element
    return output_dict

# Example usage:
input_list = [1, 2, 3, 4, 5]
output_dict = list_to_dict(input_list)
print(output_dict)
```

**15.write a program that will take dict as an input and it will pick only that dict value which is of type string**
```python
def dict_data(input_dict):

    string_dict={ }
    for key,value in input_dict.items():
        if isinstance(value,str):
            string_dict[key]=value
    return string_dict
input_dict={1:2,1:"mohini"}
string_dict=dict_data(input_dict)
print(string_dict)
```

**16.write a program that taken list of int as input and return the 2nd largest number in the list if list have a single value or no value return none**
```python
def second_largest(numbers):
    # Check if the list has less than 2 elements
    if len(numbers) < 2:
        return None
    
    # Remove duplicates and sort the list in descending order
    unique_numbers = list(set(numbers))
    
    # Check again if there are at least 2 unique numbers
    if len(unique_numbers) < 2:
        return None
    
    # Sort the unique numbers in descending order
    unique_numbers.sort(reverse=True)
    
    # Return the second largest number
    return unique_numbers[1]

# Example usage
if __name__ == "__main__":
    # Input list of integers
    input_list = input("Enter a list of integers separated by spaces: ")
    
    # Convert input string to a list of integers
    input_numbers = list(map(int, input_list.split()))
    
    result = second_largest(input_numbers)
    
    print(result)
```

**17.write a program a function that will take input as an int and return the list of 1st n number fibonacci series(number input)**
```python
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]
data=fibonacci(9)
print(data)
```

**18.write a program to find the largest word in the given sentence**
```python
def longest_word(sentence):
    words = sentence.split()
    max_length = 0
    longest_word = ""
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    return longest_word
data=longest_word("hi i am mohini")
print(data)
```

**19. write a program function that take list of numbers and return the sum of all the even number**
```python
def sum(num : list)->list:
    add=0
    print(num)
    for i in num:
        if i % 2 ==0:           
            add+=i
    print(add)
sum(num=[1,2,3,4,5,6])
```

**20. write a function that accept 5 argument and return sum of all argument(int)**

**#positional argument**
```python
def positional_arg(a,b,c,d,e):
    sum=a+b+c+d+e
    return sum
data=positional_arg(1,2,3,4,5)
print(data)      #output 15
```
**#keyword argument**
```python
def keyword_argument(a,b,c,d,e):
    sum=a+b+c+d+e
    return sum
data = keyword_argument(a=1,b=2,c=3,d=4,e=5)
print(data)       #output 15
```
**#arbitrary argument**
```python
def arbitrary_agrument(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum
data=arbitrary_agrument(12,23,34,45,45)
print(data)          #output 159
```
**#keyword arbitrary argument**
```python
def keyword_arbitrary_agrument(**kargs):
    sum = 0
    for key,values in kargs.items():
        if isinstance (values,int):
            sum = sum + values
    return sum
data=keyword_arbitrary_agrument(a=100,b=200,c=300,d=400,e=500)
print(data)             #output 1500
```
**#default argument**
```python
def default_argument(a,b,c,d=1,e=1):
    sum=a+b+c+d+e
    return sum
data = default_argument(a=10,b=20,c=30,d=40,e=50)
print(data)          #output 150


def default_argument2(a,b,c,d=1,e=1):
    sum=a+b+c+d+e
    return sum
data2 = default_argument2(a=10,b=20,c=30,d=40)
print(data2)          #output 101
```




