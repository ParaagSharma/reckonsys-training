'''
1. Fibonacci Sequence Generator: 
'''
# def fibonacci(n):
#     x, y = 0, 1
#     for i in range(n):
#         yield x
#         x, y = y, x+y
    
# n = int(input('Enter num of fibonacci elements: '))
# output = fibonacci(n)

# for i in range(n):
#     print(next(output))
    
    
'''
2. Custom Range Generator: for example input 5. Output will be 1,2,3,4,5
'''
# def range_generator(n):
#     count = 0
#     while count < n:
#         yield count
#         count += 1

# n = int(input('Enter num: '))    
# output = range_generator(n)

# for _ in range(n):
#     print(next(output))
    
    
'''
Prime Number Generator
'''
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def prime_nums_generator():
#     n = 2
#     while True:
#         if is_prime(n):
#             yield n
#         n += 1

# primes = prime_nums_generator()

# n = int(input("Input num of prime numbers: "))

# for _ in range(n):
#     print(next(primes))
    

'''
Write a generator function called char_counter(text) that yields 
each unique character in a string along with the count of 
how many times it appears in the text.
'''
def char_counter(text):
    seen = {}
    for character in text:
        if character not in seen:
            seen[character] = text.count(character)
            yield character, seen[character]
            
text = input('Enter a string: ')
for char, count in char_counter(text):
    print(f"{char}: {count}")
