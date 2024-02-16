

with open('input_1A.txt', 'r') as file:
    inputArray = file.read().split("\n")

inputNumbers = []
inputArray_numbers = []

def text_to_numbers(string):
    # Define a dictionary to map text representations of numbers to their numerical values
    number_dict = {
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

    # Replace textual representations with numerical values
    for word, number in number_dict.items():
        string = string.replace(word, number)
    return string

inputArray_numbers = []

for i in inputArray:
    text_to_numbers(i)
    inputArray_numbers.append(text_to_numbers(i))

def extract_nums(string):
    nums = []

    for char in string:
        if char.isdigit():
            if len(nums) > 1:
                nums.pop()
                num = int(char)
                nums.append(num)
            else:
                num = int(char)
                nums.append(num)
                nums.append(num)
    number = int("".join(str(i) for i in nums))
    return number

for x in inputArray_numbers:
    extract_nums(x)
    inputNumbers.append(extract_nums(x))


sum = 0
print(inputNumbers)
for i in inputNumbers:
    sum = sum + i
print(sum)