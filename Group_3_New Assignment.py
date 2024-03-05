#!/usr/bin/env python
# coding: utf-8

# ### Group members are: Collins Ugwuozor, Daudu Tobi, Ebunoluwa, and Daniel Macdinna

# No 3: Write a program to calculate the permutation and combination using the formula:
# - p(n,r) = n!/(n-r)!
# - c(n,r) = n!/(r! * (n-r)!) = p(n,r)/r! 
# - where n is the no of permutations/combinations taken at r time

# In[2]:


def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def permutation(n, r):
    """
    Calculate the permutation of n taken r at a time.
    """
    return factorial(n) // factorial(n - r)

def combination(n, r):
    """
    Calculate the combination of n taken r at a time.
    """
    return permutation(n, r) // factorial(r)


n = int(input("Enter value for n: "))
r = int(input("Enter value for r: "))

permutations = permutation(n, r)
combinations = combination(n, r)

print("Permutations of", n, "taken", r, "at a time:", permutations)
print("Combinations of", n, "taken", r, "at a time:", combinations)


# N0 4: Write a program that converts a decimal number to binary number.

# In[4]:


def decimal_to_binary(decimal_num):
    """
    Convert a decimal number to a binary number.
    """
    binary_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    return binary_num if binary_num else "0"


decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print("Binary Number:", binary_number)


#  No 6: Write a program function sumPdivisiors that finds the sum of proper divisors of a given number.
# - Proper divisors are those numbers which by which the number is divisible except the number itself. 
# - e.g. divisors of 10: 1,2,5

# In[13]:


def sumPdivisors(n):
    """
    Find the sum of proper divisors of a given number.
    """
    if n <= 1:
        return 0
    divisors_sum = 1  # 1 is always a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum


number = int(input("Enter a number: "))
print("Sum of proper divisors of", number, "is:", sumPdivisors(number))


# No 7: Write a program that filters odd numbers in a list. Hint: use lambda func

# In[17]:


# Define a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]
# Use filter with lambda function to filter odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Print the filtered list of odd numbers
print("Odd numbers in the list:", odd_numbers)

