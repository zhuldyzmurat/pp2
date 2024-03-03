#ex1
from functools import reduce

def multiply(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

if __name__ == "__main__":
    numbers = [int(x) for x in input(). split()]
    product = multiply(numbers)
    print(product)
#ex2
def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

if __name__ == "__main__":
    input_string = input()
    upper, lower = count_upper_lower(input_string)
    print(upper)
    print(lower)
#ex3
def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

if __name__ == "__main__":
    input_string = input()
    if is_palindrome(input_string):
        print(f"'{input_string}' is a palindrome.")
    else:
        print(f"'{input_string}' is not a palindrome.")
#ex4
import time
import math

def square(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    print(result)

if __name__ == "__main__":
    number = int(input())
    milliseconds = int(input())

    square(number, milliseconds)
#ex5
def all_true(elements):
    return all(elements)

if __name__ == "__main__":
    my_tuple = input()
    if all_true(my_tuple):
        print("All elements of the tuple are True")
    else:
        print("Not all elements of the tuple are True")