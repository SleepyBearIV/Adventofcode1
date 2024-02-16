

with open('input_1A.txt', 'r') as file:
    inputArray = file.read().split("\n")


def text_to_numbers(text):
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
        text = text.replace(word, number)
    return text

for i in inputArray:
    text_to_numbers(i)
    inputArray_numbers.append(text_to_numbers(i))

print(inputArray_numbers)
