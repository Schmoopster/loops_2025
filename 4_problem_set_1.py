
# # **Python Practice Problems (No Code Included)

# **Directions:** Solve each problem by writing your own Python code. Show outputs where required.


# ### **Problem 1: Print Numbers 1 to 10

# Write a program that prints the numbers from **1 to 10**, each on a new line.
list1to10 = list(range(1,11))
for number in list1to10:
    print(number)


# ### **Problem 2: Sum of Numbers

# Ask the user for a number **n**, then calculate and display the **sum of all numbers from 1 to n**.
# n = int(input("Enter a number:"))
# total_sum = 0
# for number in range(1, n+1):
#     total_sum += number
# print("The sum of number from 1 to" n, "is:", total_sum)


# ### **Problem 3: Factorial Calculator

# Ask the user for a number **n**, then calculate the **factorial** of that number.
def factorial(n):
    factorial=1
    for i in range(n):
        factorial*=i+1
    return factorial
print(factorial(67))
# *(Example: factorial of 5 is 120)


# ### **Problem 4: Count Vowels**

# Ask the user for a string. Count and print how many **vowels (a, e, i, o, u)** are in the string.


# ### **Problem 5: Print Even Numbers**

# Ask the user for a number **n**, then print all **even numbers** from 2 up to n.
n = int(input("Enter a number: "))
print("Even numbers from 2 to", n, ":")
for number in range(2, n+1, 2):
    print(number)
#Alternative method using if condition
list_even_numbers = list(range(1,45))
for number in list_even_numbers:
    #if number is not even, skip
    #check if number is odd
    if number % 2 == 0:
        print(number)
    else:
        print("odd number," number)



# ### **Problem 6: Reverse a String**

# Ask the user for a string, then print the string **backwards**.



# ### **Problem 7: Multiplication Table**

# Ask the user for a number **n**, then print the **multiplication table** for n from
# n × 1 up to n × 10.



# ### **Problem 8: Count Occurrences**

# Ask the user for **two strings**, a and b.
# Determine how many times **string b appears inside string a**.



# ### **Problem 9: Fibonacci Sequence**

# Ask the user for a number **n**, then print the first **n numbers** of the Fibonacci sequence.



# ### **Problem 10: Pattern Printing**

# Ask the user for a number **n**, then print a pattern of stars where the first row has 1 star, the second has 2, and so on until row n.

# *(Example for n = 4)*
# *
# **
# ***
# ****



# If you want, I can also turn this into a **Google Doc**, **worksheet**, **PDF**, or **Canvas/Schoology assignment format**.
