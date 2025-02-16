'''Problem Statement:

You are given a 2D list (matrix) containing integers. Your task is to flatten the matrix 
into a single list and retain only the even numbers, squaring them in the process.
'''

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

output_list = [val**2 for row in matrix for val in row if val % 2 == 0]
print(output_list)


'''
Problem Statement:

Given a 2D list of words, flatten it into a single list while keeping only words with 
more than three letters. Convert them to uppercase.
'''

pythonCopyEditwords = [
    ["hi", "hello", "to"],
    ["apple", "go", "code"],
    ["yes", "python", "AI"]
]

output = [word.upper() for row in pythonCopyEditwords for word in row if len(word) > 3]

print(output)
