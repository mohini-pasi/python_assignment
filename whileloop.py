"""
The while Loop
With the while loop we can execute a set of statements as long as a condition is true.

Print i as long as i is less than 6:"""
i = 1
while i < 6:
  print(i)
  i += 1

"""
The break Statement
With the break statement we can stop the loop even if the while condition is true:

Example
Exit the loop when i is 3:"""
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

"""
The continue Statement
With the continue statement we can stop the current iteration, and continue with the next:

Example
Continue to the next iteration if i is 3:"""
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

"""
The else Statement
With the else statement we can run a block of code once when the condition no longer is true:

Example
Print a message once the condition is false:"""
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#10 different patterns printed using while loops in Python:

#Pattern 1: Increasing asterisks
i = 1
while i <= 5:
    print("* " * i)
    i += 1
"""
Output:
* 
* * 
* * * 
* * * * 
* * * * * 
"""

#Pattern 2: Decreasing asterisks
i = 5
while i >= 1:
    print("* " * i)
    i -= 1
"""
Output:
* * * * * 
* * * * 
* * * 
* * 
* 
"""

#Pattern 3: Right-angled triangle
i = 1
while i <= 5:
    print(" " * (5 - i) + "* " * i)
    i += 1
"""
Output:
    * 
   * * 
  * * * 
 * * * * 
* * * * *
"""

#Pattern 4: Inverted right-angled triangle
i = 5
while i >= 1:
    print(" " * (5 - i) + "* " * i)
    i -= 1
"""
Output:
* * * * * 
 * * * * 
  * * * 
   * * 
    *
"""
 

#Pattern 5: Hourglass
i = 1
while i <= 5:
    print(" " * (5 - i) + "* " * i)
    i += 1
i = 4
while i >= 1:
    print(" " * (5 - i) + "* " * i)
    i -= 1
"""
Output:
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    *
"""

#Pattern 6: Diamond shape
i = 1
while i <= 5:
    print(" " * (5 - i) + "* " * (2 * i - 1))
    i += 1
i = 4
while i >= 1:
    print(" " * (5 - i) + "* " * (2 * i - 1))
    i -= 1
"""
Output:
    * 
   * * * 
  * * * * * 
 * * * * * * * 
* * * * * * * * * 
 * * * * * * * 
  * * * * * 
   * * * 
    *
"""

#Pattern 7: Alternating asterisks and spaces
i = 1
while i <= 5:
    for j in range(i):
        if j % 2 == 0:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
    i += 1
"""
Output:
* 
*   
* * 
*   * 
* * * 
"""

#Pattern 8: Increasing number
i = 1
while i <= 5:
    for j in range(i):
        print(j + 1, end=" ")
    print()
    i += 1
"""
Output:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""

#Pattern 9: Decreasing numbers
i = 5
while i >= 1:
    for j in range(i):
        print(j + 1, end=" ")
    print()
    i -= 1
"""
Output:
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
"""

# Pattern 10: Pyramid
i = 1
while i <= 5:
    print(" " * (5 - i) + "* " * i)
    i += 1
print(" " * 4 + "|")
i = 4
while i >= 1:
    print(" " * (5 - i) + "* " * i)
    i -= 1
"""
Output:
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
    | 
 * * * * 
  * * * 
   * * 
    *
    """