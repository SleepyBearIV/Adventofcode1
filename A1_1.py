f = open('input_1A.txt', 'r').read()

with open('input_1A.txt', 'r') as file:
    text = f.split("\n")


CodeString = text
print(CodeString)

def extract_nums(string):
    nums = []

    for char in string:
        if char.isnumeric():
            num = int(char)
            nums.append(num)
    print(nums)
    return nums


for x in CodeString:
    extract_nums(x)




