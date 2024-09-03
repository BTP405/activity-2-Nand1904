def is_prime(num):
    """
    Helper function to check if a number is prime.
    """
    # A prime number is a special kind of number that is only divisible by 1 and itself.
    # This function helps us find out if a number is a prime number or not.
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def getPrimeNumbers(n):
    """
    Function to generate a list of prime numbers between 2 and n.
    """
    # Let's create a list of prime numbers! A list is like a group of friends, 
    # and we only want the special numbers that are prime to be our friends.
    prime_numbers = [num for num in range(2, n + 1) if is_prime(num)]
    
    # We made a list of prime numbers, and now we want to share it with others.
    return prime_numbers

# Example usage:
n = 10
result = getPrimeNumbers(n)
print(f"Prime numbers between 2 and {n}: {result}")

'''
Explanation:

is_prime() is like a detective that helps us find out if a number is a prime number.
It looks at the number's friends (divisors) between 2 and the square root of the number,
and if it doesn't find any friends, then the number is a prime!

getPrimeNumbers() is like a magic box that gives us a list of special prime numbers.
It uses our detective (is_prime()) to decide who should be in the list.

The example usage at the end is like asking the magic box for a list of prime numbers
up to a certain number (in this case, up to 6). The magic box does the work, and we get
the list of prime numbers as a result!
'''
