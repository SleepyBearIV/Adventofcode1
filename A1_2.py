import re

#opens the document
f = open('input_1A.txt', 'r').read()
#splits the teixt in to array
with open('input_1A.txt', 'r') as file:
    text = f.split("\n")

word_to_digits = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
word = text[0].split()
digits = [word_to_digits[x] for x in word]

print(text[0])
print(word)
print(digits)



inputArray = text


inputNumbers = []

def extract_nums(string):
    nums = []

    for char in string:
        if char.isnumeric():
            if len(nums) > 1:
                nums.pop()
                num = int(char)
                nums.append(num)
            else:
                num = int(char)
                nums.append(num)
                nums.append(num)
    s = [str(i) for i in nums]
    number = int("".join(s))
    return number

for x in inputArray:
    extract_nums(x)
    inputNumbers.append(extract_nums(x))

sum = 0

for i in inputNumbers:
    sum = sum + i
print(sum)





